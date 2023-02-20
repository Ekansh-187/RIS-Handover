import os
import random
import threading
from typing import List
from UE_ris import UE_ris
import utils.Result
from Simulate_UE_ris import Simulate_UE_ris
from ris import ris
from eNB_ris import eNB_ris
from utils.Ticker import Ticker

# def main(enbs : List[eNB]) -> utils.Result.Result:
    
#     u1 = UE(0)
#     ticker = Ticker()
#     S = Simulate_UE(u1, enbs)
#     res = S.run(ticker, time=10000000)
#     file_name = "Results/results_corrected.xlsx"
#     file_name = os.path.join(os.path.dirname(__file__), file_name)
#     return res


# Define the number of threads to run

def main_ris(lock_mutex: threading.Lock, enbs : List[eNB_ris], ris : List[ris], ttt, hys, u1 : UE_ris) -> utils.Result.Result:
    
    ticker = Ticker()
    S = Simulate_UE_ris(u1, enbs, ris)
    res = S.run(ticker, time=10000000)
    lock_mutex.acquire()
    # try:
    #     file_name = "Results/results_corrected.xlsx"
    #     file_name = os.path.join(os.path.dirname(__file__), file_name)
    #     utils.Result.Result.save_to_file(res, file_name, "nr", ttt, hys, u1.get_eNB().location, bs)
    # finally:
    #     lock_mutex.release()
    return res


# # Define the number of threads to run
def run_threads_ris(enbs : List[eNB_ris], ris: List[ris], time_to_trigger: int, hysteresis: int, ue : UE_ris):
    """
    This function runs the main function in multiple threads
    """
    # Create a lock to synchronize access to the file
    lock = threading.Lock()

    # Create a list of threads
    num_threads = 1
    threads = []
    for i in range(num_threads):
        # Create a new UE and eNBs object for each thread
        thread = threading.Thread(target=main_ris, args=(lock, enbs, ris, time_to_trigger, hysteresis, ue))
        thread.start()
        threads.append(thread)

    # Wait for all threads to finish

    for thread in threads:
        thread.join()



