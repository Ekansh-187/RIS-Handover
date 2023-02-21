import random
from ris import ris
from eNB_ris import eNB_ris
from utils.grapher import graph_rsrp
# Mix Environment
def util():
    return random.randint(0,100)


# NR Environment
en1_1 = eNB_ris(1, random.randint(0, 15), util(), "nr")
en1_2 = eNB_ris(2, random.randint(0, 15), util(), "nr")
en1_3 = eNB_ris(5, random.randint(0, 15), util(), "nr")
en1_4 = eNB_ris(15, random.randint(0, 15), util(), "nr")
en1_5 = eNB_ris(25, random.randint(0, 15), util(), "nr")
en1_6 = eNB_ris(20, random.randint(0, 15), util(), "nr")
en1_7 = eNB_ris(16, random.randint(0, 15), util(), "nr")
en1_8 = eNB_ris(45, random.randint(0, 15), util(), "nr")
en1_9 = eNB_ris(10, random.randint(0, 15), util(), "nr")
en1_10 = eNB_ris(12, random.randint(0, 15), util(), "nr")
eNBs_nr = ("NR", [en1_1, en1_2, en1_3, en1_4, en1_5, en1_6, en1_7, en1_8, en1_9, en1_10])


en1_1 = ris(3, random.randint(2, 10))
en1_2 = ris(8, random.randint(2, 10))
en1_3 = ris(17, random.randint(2, 10))

# eNBs_mix1 = ("NR", [en1_1, en1_10])
ris = ("ris", [en1_1,  en1_2, en1_3])
# eNBs_mix1 = ("Ris", [en1_1, en1_2, en1_3, en1_4, en1_5, en1_6, en1_7, en1_8, en1_9])


en3_1 = eNB_ris(1, random.randint(0,15),util())
en3_2 = eNB_ris(2, random.randint(0,15), util())
en3_3 = eNB_ris(5, random.randint(0,15), util())
en3_4 = eNB_ris(15, random.randint(0,15), util())
en3_5 = eNB_ris(25, random.randint(0,15), util())
en3_6 = eNB_ris(20, random.randint(0,15), util())
en3_7 = eNB_ris(16, random.randint(0,15), util())
en3_8 = eNB_ris(45, random.randint(0,15), util())
en3_9 = eNB_ris(10, random.randint(0,15), util())
en3_10 = eNB_ris(12, random.randint(0,15), util())
eNBs_nr_ris = ("NR", [en3_1, en3_2, en3_3, en3_4, en3_5,
               en3_6, en3_7, en3_8, en3_9, en3_10])
# eNBs_nr = ("NR", [en2_1, en2_10])
# graph_rsrp(eNBs_nr)