import environment,  eNB_environments
import main, matplotlib.pyplot as plt
import random
from UE_ris import UE_ris
# TTT_range = [25, 50, 100, 200, 300, 400, 500]
# HYSTERESIS_range = [0, 3, 5, 7, 10, 12, 15, 17, 20]
# HYSTERESIS_range = [2*x*0.001 for x in range(10)]
TTT_range = [25]
HYSTERESIS_range = [5]

x = []
h = []
p = []
# plt.plot(environment.h1, environment.x)

# fig, ax1 = plt.subplots()
# ax1.plot(h, x)
# ax2 = ax1.twinx()
# ax2.plot(h,p)
# # plt.xlabel("Hysteresis")
# # plt.ylabel("Handover Rate")


fig = plt.plot()
plt.ylabel("HO rate")
plt.xlabel("Hysteresis")
for i in range(100):
    TTT = 2
    environment.x = []
    print(i)
    x = random.randint(5000, 15000)
    y = random.randint(1000,1500)
    print(f'UE at x, y', x,y)
    print("RIS less...")
    for HYSTERESIS in HYSTERESIS_range:
        
        environment.TTT = TTT
        environment.HYSTERESIS = HYSTERESIS
        main.run_threads_ris(
            eNB_environments.eNBs_nr[1], eNB_environments.ris[1], TTT, HYSTERESIS, UE_ris(x, y))
       
    

    environment.x = []
    print("\nwith RIS")
    for HYSTERESIS in HYSTERESIS_range:
        environment.TTT = TTT
        environment.HYSTERESIS = HYSTERESIS
        environment.no_of_ho = 0
        main.run_threads_ris(eNB_environments.eNBs_nr_ris[1], eNB_environments.ris[1], TTT, HYSTERESIS, UE_ris(x,y))




# # plt.plot(h, p)
# plt.show()

