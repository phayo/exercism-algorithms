from datetime import time

class Clock(object):
    def __init__(self, hour, minute):
        init_m = minute // 60
        rem_m = (60 + (minute % 60)) % 60
        h = (24 + ((hour + init_m) % 24)) % 24
        self.time = time(h, rem_m)

    def __repr__(self):
        hour = self.time.strftime("%H")
        minute = self.time.strftime("%M")
        return f"{hour}:{minute}"

    def __eq__(self, other):
        return self.time == other

    def __add__(self, minutes):
        init_m = (self.time.minute + minutes) // 60
        rem_m = (60 + (self.time.minute + (minutes) % 60)) % 60
        h = (24 + ((self.time.hour + init_m) % 24)) % 24
        self.time = time(h, rem_m)
        return self.__repr__()

    def __sub__(self, minutes):
        init_m = (self.time.minute - minutes) // 60
        rem_m = (60 + ((self.time.minute - minutes) % 60)) % 60
        h = (24 + ((self.time.hour + init_m) % 24)) % 24
        self.time = time(h, rem_m)
        return self.__repr__()


print(str(Clock(10, 3) - 30))
# if Clock(10, 37).__eq__(Clock(10, 37)):
#     print("Yeaaaaa")
# else:
#     print("Urggghh")