import math
import sys
sys.path.append("C:/Users/ekans/OneDrive/Desktop/OUR/ris")


def freq_to_wavelength(frequency):
    """This function converts frequency provided in MHz to wavelength in meters"""
    wavelength = 3e8 / (frequency * 1e6)
    return wavelength


def calc_power_in_dbm(power):
    """
    This function calculates the transmitted power of the base station in dBm given the value in mW
    :param power: Transmitted power in mW
    """
    return 10 * math.log10(power)


def gigahertz_to_megahertz(frequency):
    """This function converts frequency provided in GHz to MHz"""
    frequency = frequency * 1e3
    return frequency


def calc_dist(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)
