class ris:
    def __init__(self, loc, y=0):
        self.location = loc
        self.x = loc
        self.y = y
    
    def get_location(self):
        return self.location
    def get_location_2d(self):
        return self.x, self.y