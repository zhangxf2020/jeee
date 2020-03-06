import random,time
class Ore:
    def __init__(self,tm):
        self.tm = tm
        self.gold = [i for i in range(256)]
        self.gold_1 = [100 for i in range(256)]
        self.gold_1[0] = 5
        self.goldnum = 0
        self.tm_start = time.perf_counter()
    def begin(self):
        while True:
            tm_end = time.perf_counter()
            if self.tm <= tm_end - self.tm_start:
                break
            x = random.choices(self.gold,weights=self.gold_1,k=1)

            if x[0] == 0:
                print(x[0])
                self.goldnum +=1





s = Ore(10)
s.begin()
print(s.goldnum)
