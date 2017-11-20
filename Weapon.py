import random

class Weapon:
    def __init__(self):
        self.name = None
        self.attackModifier = 0
        self.type = None
        self.amount = None

    def getName(self):
        return self.name

    def getAttack(self):
        return round(self.attackModifier,2)

    def getType(self):
        return self.type

    def getAmount(self):
        return self.amount

    def setAmount(self, a):
        self.amount = a

    def decreaseAmount(self):
        self.amount -= 1

    def setType(self, t):
        self.type = t

    def setName(self, n):
        self.name = n

    def setAttackModifier(self, a):
        self.attackModifier = a

    def toString(self):
        printable = (self.name + " Attack: " + str(self.attackModifier)
        + " Amount: " + str(self.amount))
        return printable

class HersheyKisses(Weapon):
    def __init__(self):
        super().setName("HersheyKiss")
        super().setAmount(9999)
        super().setType(0)
        self.initAttack()

    def initAttack(self):
        attack = 1
        super().setAttackModifier(attack)

class SourStraw(Weapon):
    def __init__(self):
        super().setName("SourStraw")
        super().setAmount(2)
        super().setType(1)
        self.initAttack()

    def initAttack(self):
        attack = random.uniform(1, 1.75)
        super().setAttackModifier(attack)

class ChocolateBar(Weapon):
    def __init__(self):
        super().setName("ChocolateBar")
        super().setAmount(4)
        super().setType(2)
        self.initAttack()

    def initAttack(self):
        attack = random.uniform(2, 2.4)
        super().setAttackModifier(attack)

class NerdBomb(Weapon):
    def __init__(self):
        super().setName("NerdBomb")
        super().setAmount(1)
        super().setType(3)
        self.initAttack()

    def initAttack(self):
        attack = random.uniform(3.5, 5)
        super().setAttackModifier(attack)
