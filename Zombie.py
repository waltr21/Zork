from Monster import Monster
from random import randint

class Zombie(Monster):
    def __init__(self):
        self.health = randint(50,100)
        super().__init__(self.health)

    def takeDamage(self, weapon):
        if weapon.getType() == 1:
            super().takeDamage(weapon.getAttack()*2)
        else:
            super().takeDamage(weapon.getAttack())

    def performAttack(self, attack=0):
        tempAttack = randint(0,10)
        super().performAttack(tempAttack)

z = Zombie()
print (z.getHealth())
print(z.getHealth())
