from utils.misc import gigahertz_to_megahertz

# DEFINE constants for the environment
FREQ_NR = gigahertz_to_megahertz(25)  # MHz
TTT = 60  # ms
HYSTERESIS = 20  # dB
PTX = 10  # mW
TICKER_INTERVAL = 10  # ms
A3_OFFSET = 0  # dB
# MIN_SPEED = 0.01  # m/ms
# MAX_SPEED = 0.05  # m/ms
MIN_SPEED = 0.0001  # m/ms
MAX_SPEED = 0.0005  # m/ms
MIN_PAUSE = 10  # ms
MAX_PAUSE = 100  # ms
pow_diff = []



