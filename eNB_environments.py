import random
from ris import ris
from eNB_ris import eNB_ris
# from utils.grapher import graph_rsrp
# Mix Environment
def util():
    return random.randint(0,100)

'''
# NR Environment
# en1_1 = eNB_ris(1, random.randint(0, 15), util(), "nr")
# en1_2 = eNB_ris(2, random.randint(0, 15), util(), "nr")
# en1_3 = eNB_ris(5, random.randint(0, 15), util(), "nr")
# en1_4 = eNB_ris(15, random.randint(0, 15), util(), "nr")
# en1_5 = eNB_ris(25, random.randint(0, 15), util(), "nr")
# en1_6 = eNB_ris(20, random.randint(0, 15), util(), "nr")
# en1_7 = eNB_ris(16, random.randint(0, 15), util(), "nr")
# en1_8 = eNB_ris(45, random.randint(0, 15), util(), "nr")
# en1_9 = eNB_ris(10, random.randint(0, 15), util(), "nr")
# en1_10 = eNB_ris(12, random.randint(0, 15), util(), "nr")
eNBs_nr = ("NR", [en1_1, en1_2, en1_3, en1_4, en1_5, en1_6, en1_7, en1_8, en1_9, en1_10])
'''
en1_1 = eNB_ris(0, random.randint(0, 15), util(), "nr")
en1_2 = eNB_ris(2.5, random.randint(0, 15), util(), "nr")
en1_3 = eNB_ris(5, random.randint(0, 15), util(), "nr")
en1_4 = eNB_ris(7.5, random.randint(0, 15), util(), "nr")
en1_5 = eNB_ris(10, random.randint(0, 15), util(), "nr")
en1_6 = eNB_ris(12.5, random.randint(0, 15), util(), "nr")
en1_7 = eNB_ris(15, random.randint(0, 15), util(), "nr")
en1_8 = eNB_ris(17.5, random.randint(0, 15), util(), "nr")
en1_9 = eNB_ris(20, random.randint(0, 15), util(), "nr")
en1_10 = eNB_ris(22.5, random.randint(0, 15), util(), "nr")
en1_11 = eNB_ris(25, random.randint(0, 15), util(), "nr")
en1_12 = eNB_ris(27.5, random.randint(0, 15), util(), "nr")
en1_13 = eNB_ris(30, random.randint(0, 15), util(), "nr")
en1_14 = eNB_ris(32.5, random.randint(0, 15), util(), "nr")
en1_15 = eNB_ris(35, random.randint(0, 15), util(), "nr")
en1_16 = eNB_ris(37.5, random.randint(0, 15), util(), "nr")
en1_17 = eNB_ris(40, random.randint(0, 15), util(), "nr")
en1_18 = eNB_ris(42.5, random.randint(0, 15), util(), "nr")
en1_19 = eNB_ris(45, random.randint(0, 15), util(), "nr")
eNBs_nr = ("NR", [en1_1, en1_2, en1_3, en1_4, en1_5, en1_6, en1_7, en1_8, en1_9, en1_10, en1_11, en1_12, en1_13, en1_14, en1_15, en1_16, en1_17, en1_18, en1_19])


en2_1 = ris(2.5, random.randint(0,15))
en2_2 = ris(7.5, random.randint(0, 15))
en2_3 = ris(12.5, random.randint(0,15))
en2_4 = ris(17.5, random.randint(0, 15))
en2_5 = ris(22.5, random.randint(0,15))
en2_6 = ris(27.5, random.randint(0, 15))
en2_7 = ris(32.5, random.randint(0,15))
en2_8 = ris(37.5, random.randint(0, 15))
en2_9 = ris(42.5, random.randint(0,15))

# eNBs_mix1 = ("NR", [en1_1, en1_10])
ris = ("ris", [en2_1,  en2_2, en2_3, en2_4, en2_5, en2_6, en2_7, en2_8, en2_9])
# eNBs_mix1 = ("Ris", [en1_1, en1_2, en1_3, en1_4, en1_5, en1_6, en1_7, en1_8, en1_9])


en3_1 = eNB_ris(0, random.randint(0,15),util())
en3_2 = eNB_ris(5, random.randint(0,15), util())
en3_3 = eNB_ris(10, random.randint(0,15), util())
en3_4 = eNB_ris(15, random.randint(0,15), util())
en3_5 = eNB_ris(20, random.randint(0,15), util())
en3_6 = eNB_ris(25, random.randint(0,15), util())
en3_7 = eNB_ris(30, random.randint(0,15), util())
en3_8 = eNB_ris(35, random.randint(0,15), util())
en3_9 = eNB_ris(40, random.randint(0,15), util())
en3_10 = eNB_ris(45, random.randint(0,15), util())
eNBs_nr_ris = ("NR", [en3_1, en3_2, en3_3, en3_4, en3_5,
               en3_6, en3_7, en3_8, en3_9, en3_10])
# eNBs_nr = ("NR", [en2_1, en2_10])
# graph_rsrp(eNBs_nr)