


# def ile fire ve dusmen funksiyasi yaz her fire istifade edende dusmenin cani azalsin

class Soldier:
    health = 100
    power = 20

    def fire(self, other):
        other.health = other.health - self.power


soldier = Soldier()
soldier2 = Soldier()

soldier.fire(soldier2)
# print(soldier2.health)
# lambda ile factorial yaz``

f = lambda x: 1 if x == 0 else x * f(x-1)
print(f(5))



# bir geri sayim programi hazirla. programa bir deyer ver ve o deyerden 0-a qeder say

import time

num = int(input())

for i in range(num, 0, -1):
    time.sleep(1)
    print(i,"Saniye")
    
