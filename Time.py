import time
class Time:
    startingTime = time.time()
    def getCurrentDay(self):
        return int(time.time() - Time.startingTime)/5
    def getCurrentSecond(self):
        return int(time.time() - Time.startingTime)
    ''' five seconds in real world per day in game
    '''
    def setTimerSeconds(self,t):
        start = self.getCurrentSecond()
        end = start + t
        while True:
            marker = self.getCurrentSecond()
            if marker == end:
                return False
    def setTimerDays(self,t):
        start = self.getCurrentDay()
        end = start + t
        while True:
            marker = self.getCurrentDay()
            if marker == end:
                return False
a = Time()
if not a.setTimerSeconds(5):
    print("Time up")
