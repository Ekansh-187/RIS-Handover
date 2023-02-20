import math
from typing import List
import random
from eNB import eNB
import environment
import utils
import utils.misc
from ris import ris


class eNB_ris:
    """
    This class defines properties of a base station.
    It has a location, id, type and wavelength.
    """

    def __init__(self, x, y, ut, bs_type="ris"):
        self.util = ut
        self.x = x
        self.y = y
        self.ris = None
        self.free_elems = 10
        self.id = random.randint(0, 1000)
        self.location = x
        self.bs_type = bs_type
        self.wavelength = utils.misc.freq_to_wavelength(environment.FREQ_NR)
        self.ris = None

    def __str__(self):
        return "eNB located at %s of type: %s" % (self.location, self.bs_type)

    def get_location(self):
        return self.location
    
    def get_location_2d(self):
        return (self.x, self.y)

    def get_id(self):
        return self.id

    def get_type(self):
        return self.bs_type

    def set_location(self, x):
        self.location = x


    def set_ris(self, ris : ris):
        self.ris = ris
        





    

    def power_received(self, ueX, ueY):
        pt = utils.misc.calc_power_in_dbm(environment.PTX)
        pr_nr = pt
        dist = utils.misc.calc_dist(self.x, self.y, ueX, ueY)
        if (dist > 1):
            pr_nr /= dist
        return pr_nr

    def P_ris(self, ueX, ueY):
        if (self.bs_type == "nr"):
            return self.power_received(ueX, ueY)

        ris = self.ris
        if ris is None:
            return self.power_received(ueX, ueY)
        pt = utils.misc.calc_power_in_dbm(environment.PTX)
        pr_at_ris = pt
        dist = utils.misc.calc_dist(self.x, self.y, ueX, ueY)
        if (dist > 1):
            pr_at_ris /= dist

        pr_ris = 0.7*pr_at_ris

        return self.power_received(ueX, ueY) + pr_ris


