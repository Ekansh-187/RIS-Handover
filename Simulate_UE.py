import math
from typing import List

import environment
from UE import UE
from eNB import eNB
from utils.Result import Result
from utils.Ticker import Ticker


class Simulate_UE:
    """This class defines an environment for the simulator"""

    def __init__(self, ue: UE, e_nbs: List[eNB]):
        self.Ticker = Ticker()
        self.ue = ue
        self.e_nbs = e_nbs
        self.ho_active = False
        self.ho_trigger_time = -1
        self.first = e_nbs[0]
        self.last = e_nbs[-1]

    def run(self, t: Ticker, time=10000):
        self.Ticker = t
        self.discover_bs()
        self.associate_ue_with_bs()
        result = self.trigger_motion(time)
        return Result(result[0], result[1], timeOfExecution=time) # <---

    def search_for_bs(self):
        nearby_bs = []
        for e_nb in self.e_nbs:
            dist = math.fabs(self.ue.get_location() - e_nb.get_location())
            if dist <= 20000:
                nearby_bs.append(e_nb)
        return nearby_bs

    def associate_ue_with_bs(self):
        """
        This function associates the UE with the base station, it also checks if the UE is in range of the base station,
        if it is then it keeps a record of the eNB in the list of eNBs
        """
        nearby_bs = self.search_for_bs()
        if len(nearby_bs) == 0:
            print("UE %s is out of range" % self.ue.get_location())
            return Exception("UE is out of range")
        sorted_nearby_bs = sorted(nearby_bs, key=lambda x: x.power_received(self.ue.get_location()), reverse=True)
        # TODO: add a minimum RSRP threshold to consider
        # print sorted_nearby_bs with their RSRP
        self.ue.set_eNB(sorted_nearby_bs[0])
        self.ue.set_nearby_bs(nearby_bs)

    def trigger_motion(self, time=1000000):
        while self.Ticker.time < time:
            if self.ho_active is True:
                self.check_handover_completion()
            self.ue.update_UE_location(self.Ticker)
            self.check_for_handover()
        print("Successful HOs [nr2nr]: %s" %
              self.ue.get_HO_success())
        print("Failed HOs [nr2nr]: %s" %
              self.ue.get_HO_failure())
        # if(self.ue.HO_total > 0):
        #     environment.x.append(self.ue.get_HO_success()[0]/self.ue.HO_total)
        # else:
        #     environment.x.append(0)
        
        environment.x.append(self.ue.get_HO_success()[0])
        
        return [self.ue.get_HO_success(), self.ue.get_HO_failure()] # <---

    def check_for_handover(self):
        """
        Handover occurs when the UE is in area of another base station with higher Pr for TTT
        """
        environment.pa.append(self.first.power_received(self.ue.get_location()))
        # environment.pb.append(self.)
        nearby_bs = self.ue.get_nearby_bs()
        if len(nearby_bs) == 0:
            self.ue.set_HO_failure()
            print("UE %s is out of range" % self.ue.get_location())
        else:
            for e_nb in nearby_bs:
                if e_nb.get_id() != self.ue.get_eNB().get_id():
                    source_rsrp = self.ue.get_eNB().power_received(self.ue.get_location())
                    target_rsrp = e_nb.power_received(self.ue.get_location())
                    if target_rsrp > source_rsrp + environment.HYSTERESIS:
                        if self.ho_active is False:
                            self.ho_active = True
                            self.ho_trigger_time = self.Ticker.time
                            self.ue.set_upcoming_eNB(e_nb)
                            # print("UE %s is in area of eNB %s" % (ue.get_id(), e_nb.get_id()))

    def check_handover_completion(self):
        target_rsrp = self.ue.get_upcoming_eNB().power_received(self.ue.get_location())
        if self.Ticker.time - self.ho_trigger_time >= environment.TTT:            
            source_rsrp = self.ue.get_eNB().power_received(self.ue.get_location())
            if  target_rsrp > source_rsrp + environment.HYSTERESIS + environment.A3_OFFSET:
                
                self.ho_active = False
                self.ue.set_HO_success(self.ue.get_handover_type())
                self.ue.set_eNB(self.ue.get_upcoming_eNB())
                environment.no_of_ho += 1 
                # print("UE %s is connected to eNB %s" % (self.ue.get_id(), self.ue.get_eNB().get_id()))
                
            else:
                # print("ho failure")
                self.ue.set_HO_failure()
                self.ho_active = False
            # if(self.ue.HO_total != 0):
                # environment.ho_status.append(self.ue.HO_success[0]/self.ue.HO_total)
            # else:
            #     environment.ho_status.append(0)
            # environment.rsrp.append(math.log10(target_rsrp))
            self.ue.set_upcoming_eNB(None)
            self.ho_trigger_time = -1
            self.associate_ue_with_bs()


    def discover_bs(self):
        self.e_nbs.sort(key=lambda x: x.get_location())