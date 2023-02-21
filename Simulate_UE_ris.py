import math
from typing import List
from ris import ris
import environment
from UE_ris import UE_ris
from eNB_ris import eNB_ris
from utils.Result import Result
from utils.Ticker import Ticker
from utils.misc import calc_dist


class Simulate_UE_ris:
    """This class defines an environment for the simulator"""

    def __init__(self, ue: UE_ris, e_nbs: List[eNB_ris], ris: List[ris]):
        self.Ticker = Ticker()
        self.ue = ue
        self.ris = ris
        self.sorted_ris = []
        self.e_nbs = e_nbs
        self.ho_active = False
        self.ho_trigger_time = -1
        self.first = e_nbs[0]
        self.nearby_ris = None
        self.last = e_nbs[-1]

    def run(self, t: Ticker, time=10000):
        self.Ticker = t
        self.discover_bs()
        self.associate_ue_with_bs()
        result = self.trigger_motion(time)
        return Result(result[0], result[1], timeOfExecution=time) # <---

    def search_for_ris(self):
        nearby_ris = []
        associated_enb = self.ue.get_eNB()
        for ris in self.ris:
            dist = calc_dist(associated_enb.x, associated_enb.y, ris.x, ris.y)
            if dist <= 50000:
                nearby_ris.append(ris)
        return nearby_ris

    def search_for_bs(self):
        nearby_bs = []
        for e_nb in self.e_nbs:
            dist = calc_dist(e_nb.x, e_nb.y, self.ue.x, self.ue.y)
            if dist <= 50000:
                nearby_bs.append(e_nb)
        return nearby_bs

    def associate_bs_with_ris(self, enb):
        nearby_ris = self.search_for_ris()
        if(len(nearby_ris) == 0):
            return
        enb.set_ris(nearby_ris[0])
        
    def associate_ue_with_bs(self):
        """
        This function associates the UE with the base station, it also checks if the UE is in range of the base station,
        if it is then it keeps a record of the eNB in the list of eNBs
        """
        nearby_bs = self.search_for_bs()
        if len(nearby_bs) == 0:
            print("UE %s is out of range" % self.ue.get_location())
            return Exception("UE is out of range")
        sorted_nearby_bs = sorted(nearby_bs, key=lambda x: x.P_ris(self.ue.x, self.ue.y), reverse=True)
        self.ue.set_eNB(sorted_nearby_bs[0])
        self.associate_bs_with_ris(self.ue.get_eNB())
        self.ue.set_nearby_bs(nearby_bs)
        

    def trigger_motion(self, time=1000000):
        while self.Ticker.time < time:
            if self.ho_active is True:
                self.check_handover_completion()
            self.ue.update_UE_location(self.Ticker)
            self.check_for_handover()
        print("Successful HOs: %s" %
              self.ue.get_HO_success())
        print("Failed HOs: %s" %
              self.ue.get_HO_failure())
        
        
        environment.x.append(self.ue.get_HO_success()[0])
        
        return [self.ue.get_HO_success(), self.ue.get_HO_failure()] # <---

    def check_for_handover(self):
        """
        Handover occurs when the UE is in area of another base station with higher Pr for TTT
        """
        nearby_bs = self.ue.get_nearby_bs()
        if len(nearby_bs) == 0:
            self.ue.set_HO_failure()
            print("UE %s is out of range" % self.ue.get_location())
        else:
            for e_nb in nearby_bs:
                if e_nb.get_id() != self.ue.get_eNB().get_id():
                    curr_enb = self.ue.get_eNB()
                    self.associate_bs_with_ris(e_nb)
                    source_rsrp = curr_enb.P_ris(self.ue.x, self.ue.y)
                    target_rsrp = e_nb.P_ris(self.ue.x, self.ue.y)
                    
                    if target_rsrp > source_rsrp + environment.HYSTERESIS:
                        if self.ho_active is False:
                            self.ho_active = True
                            self.ho_trigger_time = self.Ticker.time
                            self.ue.set_upcoming_eNB(e_nb)

    def check_handover_completion(self):
        e_nb = self.ue.get_upcoming_eNB()
        self.associate_bs_with_ris(e_nb)

        if self.Ticker.time - self.ho_trigger_time >= environment.TTT:
            target_rsrp = e_nb.P_ris(self.ue.x, self.ue.y)
            source_rsrp = self.ue.get_eNB().P_ris(self.ue.x, self.ue.y)
            if target_rsrp > source_rsrp + environment.HYSTERESIS:
                self.ho_active = False
                self.ue.set_HO_success()
                self.ue.set_eNB(self.ue.get_upcoming_eNB())
                environment.no_of_ho += 1 
                
            else:
                self.ue.set_HO_failure()
                self.ho_active = False
            self.ue.set_upcoming_eNB(None)
            self.ho_trigger_time = -1
            self.associate_ue_with_bs()
        else:
            return


    def discover_bs(self):
        self.e_nbs.sort(key=lambda x: calc_dist(self.ue.x, self.ue.y, x.x, x.y))