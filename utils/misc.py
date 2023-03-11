import math, random
import sys
import numpy as np
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


def pause_probability_init(pause_low, pause_high, speed_low, speed_high, dimensions):
        alpha1 = ((pause_high+pause_low)*(speed_high-speed_low))/(2*np.log(speed_high/speed_low))
        delta1 = np.sqrt(np.sum(np.square(dimensions)))
        return alpha1/(alpha1+delta1)

def initial_speed(speed_mean, speed_delta, shape=(1,)):
    v0 = speed_mean - speed_delta
    v1 = speed_mean + speed_delta
    u = random(*shape)
    return pow(v1, u) / pow(v0, u - 1)

def residual_time(mean, delta, shape=(1,)):
    t1 = mean - delta
    t2 = mean + delta
    u = random(*shape)
    residual = np.zeros(shape)
    if delta != 0.0:
        case_1_u = u < (2.*t1/(t1+t2))
        residual[case_1_u] = u[case_1_u]*(t1+t2)/2.
        residual[np.logical_not(case_1_u)] = t2-np.sqrt((1.-u[np.logical_not(case_1_u)])*(t2*t2 - t1*t1))
    else:
        residual=u*mean  
    return residual
