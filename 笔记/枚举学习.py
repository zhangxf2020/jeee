from enum import Enum
from datetime import datetime

class Week(Enum):
    Monday = 0
    Tuesday = 1
    Wednesday = 2
    Thursday = 3
    Friday = 4
    Saturday = 5
    Sunday = 6

class Students():

    def kecheng(self):
        if Week(datetime.now().weekday()) == Week.Friday:
            print('语文')


Students().kecheng()



