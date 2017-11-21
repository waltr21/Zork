import random

class Weapon:
    """
	Constuctor for the weapon class. Creates a name, attack, type, and amount for
    the weapon.
	"""
    def __init__(self):
        self.name = None
        self.attackModifier = 0
        self.type = None
        self.amount = None

    """
	Returns the name of the weapon.
	"""
    def getName(self):
        return self.name

    """
	Returns the attack of the weapon.
	"""
    def getAttack(self):
        return round(self.attackModifier,2)

    """
	Returns the type of the weapon. (This is just an integer used to quickly
    identify the weapons.)
	"""
    def getType(self):
        return self.type

    """
	Returns the amount of the weapon the user has left.
	"""
    def getAmount(self):
        return self.amount

    """
	Sets the amount of the weapon.
	"""
    def setAmount(self, a):
        self.amount = a

    """
	Decreases the amount of the weapon by one.
	"""
    def decreaseAmount(self):
        self.amount -= 1


    """
	Sets the type of the weapon.
	"""
    def setType(self, t):
        self.type = t

    """
	Sets the name of the weapon.
	"""
    def setName(self, n):
        self.name = n

    """
	Sets the attackModifier for the weapon.
	"""
    def setAttackModifier(self, a):
        self.attackModifier = a

    """
	Creates a printable string for the weapon. (Used in the game class.)
	"""
    def toString(self):
        printable = (self.name + " Attack: " + str(self.attackModifier)
        + " Amount: " + str(self.amount))
        return printable

"""
Child class of the weapon class. Given infinite amount and an attackModifier of 1.
"""
class HersheyKisses(Weapon):
    def __init__(self):
        super().setName("HersheyKiss")
        super().setAmount(9999)
        super().setType(0)
        self.initAttack()

    def initAttack(self):
        attack = 1
        super().setAttackModifier(attack)

"""
Child class of the weapon class. Given an amount of 2 and an attackModifier of 1-1.75.
"""
class SourStraw(Weapon):
    def __init__(self):
        super().setName("SourStraw")
        super().setAmount(2)
        super().setType(1)
        self.initAttack()

    def initAttack(self):
        attack = random.uniform(1, 1.75)
        super().setAttackModifier(attack)

"""
Child class of the weapon class. Given an amount of 4 and an attackModifier of 2-2.4.
"""
class ChocolateBar(Weapon):
    def __init__(self):
        super().setName("ChocolateBar")
        super().setAmount(4)
        super().setType(2)
        self.initAttack()

    def initAttack(self):
        attack = random.uniform(2, 2.4)
        super().setAttackModifier(attack)

"""
Child class of the weapon class. Given an amount of 1 and an attackModifier of 3.5-5.
"""
class NerdBomb(Weapon):
    def __init__(self):
        super().setName("NerdBomb")
        super().setAmount(1)
        super().setType(3)
        self.initAttack()

    def initAttack(self):
        attack = random.uniform(3.5, 5)
        super().setAttackModifier(attack)
