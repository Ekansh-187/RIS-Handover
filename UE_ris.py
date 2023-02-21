import random
from math import fabs
from typing import List

import environment
from eNB_ris import eNB_ris
from utils.Ticker import Ticker


class UE_ris:
    """Defines user entity in the environment"""

    # def __init__(self, x, pause=1):
    #     self.direction = 1  # 0 - Towards 0, 1 - Away from
    #     self.nearby_bs = []
    #     self.HO_total = 0
    #     self.HO_success = [0]
    #     self.HO_failure = [0]
    #     self.associated_eNB = None
    #     self.upcoming_eNB = None
    #     self.velocity = 0
    #     self.time_at_destination = 0
    #     self.location = x
    #     self.id = random.randint(0, 10)
    #     self.pause_time = pause
    #     self.waypoint = x
    #     self.destinations = []

    def __init__(self, x, y=0, pause=1):
        self.direction = 1  # 0 - Towards 0, 1 - Away from
        self.nearby_bs = []
        self.nearby_ris = []
        self.HO_total = 0
        self.HO_success = [0]
        self.HO_failure = [0]
        self.associated_eNB = None
        self.upcoming_eNB = None
        self.time_at_destination = 0
        self.location = x
        self.x = x
        self.y = y
        self.dirx = 1
        self.diry = 1
        self.velocityX = 0
        self.velocityY = 0
        self.waypointX = x
        self.waypointY = y
        self.id = random.randint(0, 10)
        self.pause_time = pause
        self.waypoint = x
        self.ris = None
        self.destinations = []

    def set_eNB(self, associated_eNB):
        self.associated_eNB = associated_eNB
        associated_eNB.util += 1

    def get_eNB(self) -> eNB_ris:
        return self.associated_eNB

    def get_upcoming_eNB(self) -> eNB_ris:
        return self.upcoming_eNB

    def set_upcoming_eNB(self, upcoming_eNB):
        self.upcoming_eNB = upcoming_eNB

    def get_id(self):
        return self.id

    
    def get_location_2d(self):
        return self.x, self.y


    def set_nearby_ris(self, nearby_ris: List[eNB_ris]):
        self.nearby_ris = nearby_ris

    def set_nearby_bs(self, nearby_bs: List[eNB_ris]):
        self.nearby_bs = nearby_bs

    def get_nearby_ris(self):
        return self.nearby_ris

    def get_nearby_bs(self):
        return self.nearby_bs

    def set_direction(self, direction):
        self.direction = direction

    def get_direction(self):
        return self.direction

    def set_HO_success(self):
        # self.associated_eNB.num_ho += 1
        self.HO_total += 1
        self.HO_success[0] += 1

    def get_HO_success(self):
        return self.HO_success

    def get_HO_failure(self):
        return self.HO_failure

    def get_HO_total(self):
        return self.HO_total

    def set_HO_failure(self):
        self.HO_total += 1
        self.HO_failure[0] += 1

    def set_velocity(self, velocity):
        self.velocity = velocity

    def __str__(self):
        return "UE located at %s" % self.location

    def move(self, ticker: Ticker):  # Move the UE in the environment per millisecond(default)
        x = self.direction * self.velocity * ticker.ticker_duration
        self.location += x
        # if(x > 240 or x < 0)
        ticker.tick()

    
    def get_min_max_bounds(self):
        min_boundx = 0
        max_boundx=0
        min_boundy=0
        max_boundy=0
        if self.x < 10:
            min_boundx = 10
            max_boundx = self.x + 10
        elif self.x > 490:
            max_boundx = 5
            min_boundx = self.x - 10
        else:
            min_boundx = self.x - 10
            max_boundx = self.x + 10

        if self.y < 10:
            min_boundy = 0
            max_boundy = self.y + 10
        elif self.y > 49:
            max_boundy = 50
            min_boundy = self.y - 10
        else:
            min_boundy = self.y - 10
            max_boundy = self.y + 10

        return min_boundx, max_boundx, min_boundy, max_boundy

    def move_2d(self, ticker: Ticker):  # Move the UE in the environment per millisecond(default)
        self.x += (self.dirx * self.velocityX * ticker.ticker_duration)
        self.y += self.diry * self.velocityY * ticker.ticker_duration
        ticker.tick()



    def update_UE_location(self, ticker: Ticker):
        """
        This function is responsible for random motion of the UE using the random waypoint model
        """
        # If it is time for the UE to start moving to the next destination, choose a new destination
        flag1, flag2 = 0, 0
        if (fabs(self.x) >= fabs(self.waypointX) and self.dirx == 1) or \
                (fabs(self.x) <= fabs(self.waypointX) and self.dirx == -1):
            # Choose a new destination between 0 and 5 meters
            flag1 = 1                
            self.waypointX = random.uniform(self.get_min_max_bounds()[
                                            0], self.get_min_max_bounds()[1])
                
            self.velocityX = random.uniform(
                    environment.MIN_SPEED, environment.MAX_SPEED)
            if self.waypointX > self.x:
                self.dirx = 1  
            else:
                self.dirx = -1 

        if (fabs(self.y) >= fabs(self.waypointY) and self.diry == 1) or \
                (fabs(self.y) <= fabs(self.waypointY) and self.diry == -1):
            
            flag2 = 1
            self.waypointY = random.uniform(self.get_min_max_bounds()[
                                            2], self.get_min_max_bounds()[3])
              # Set the time at which the UE will start moving to the next destination

              # Choose a new random speed between 10 and 50 meters per second (m/s) equivalent to 0.01 and 0.05 m/ms
            self.velocityY = random.uniform(
                   environment.MIN_SPEED, environment.MAX_SPEED)
               # Choose a new direction of movement based on the relative positions of the current location and the
               # destination
            if self.waypointY > self.y:
                self.diry = 1  # Move forwards
            else:
                self.diry = -1  # Move backwards
                # Update the UE's location based on its speed, direction, and the elapsed time

        if(flag1 or flag2):
            self.pause_time = random.randint(
                    environment.MIN_PAUSE, environment.MAX_PAUSE)
            ticker.time = ticker.time + self.pause_time
        self.move_2d(ticker)

