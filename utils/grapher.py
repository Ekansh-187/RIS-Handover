from matplotlib import pyplot as plt

import sys
sys.path.append('C:/Users/ekans/OneDrive/Desktop/OUR/ris')
import eNB

def graph_rsrp(eNBs):
    """This function plots the received signal strength as a
    function of distance from the base station"""
    x = list(range(1, 50000))

    # Add y-axis labels at increments of 5
    # add guidelines at increments of 5
    plt.yticks(list(range(0, 110, 5)))
    for i in range(0, 110, 5):
        plt.axhline(y=i, color="lightgrey", linestyle="-")

    def get_line_color(bs_type):
        if bs_type == "ris":
            return "orange"
        if bs_type == "nr":
            return "deepskyblue"

    for e in eNBs:
        plt.plot(
            x,
            [e.calc_RSRP(a) for a in x],
            label=e.get_type() + str(e.get_id()),
            markersize=1,
            color=get_line_color(e.get_type()),
        )

    # plt.ylim(-120, -60)
    plt.xlabel("Distance from eNB")
    plt.ylabel("Estimated RSRP (dBm)")
    plt.legend()
    plt.show()
