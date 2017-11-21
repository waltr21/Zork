from random import randint
from Observer import Observer
from Observer import Observable

class Monster(Observable):
    """
	Constuctor for the monster super class.
	"""
    def __init__(self):
        self.health = 0
        self.name = none

    """
	Subtracts the damage taken from the health.
	"""
    def takeDamage(self, damage):
        self.health -= damage

    """
	Returns the attack level of a monster.
	"""
    def performAttack(self, attack):
        return attack

    """
	Gets the healt of a monster.
	"""
    def getHealth(self):
        if self.health < 0:
            self.health = 0
        return round(self.health, 2)

    """
	Gets the name of a monster.
	"""
    def getName(self):
        return self.name

    """
	Sets the health of a monster.
	"""
    def setHealth(self, h):
        self.health = h

    """
	Sets the name of a monster.
	"""
    def setName(self, n):
        self.name = n

    """
	Turns the monster into a person.
	"""
    def setPerson(self):
        if (self.health <= 0):
            super().update()

    """
	Returns a printable string for the monster. (Used in the game class)
	"""
    def toString(self):
        temp = "Monster: " + self.name + " / " + str(self.health)
        return temp

"""
Child class of monster with the health between 100-200 and attack 10-20.
"""
class Vampire(Monster):
    def __init__(self):
        self.initHealth()
        self.initName()

    def checkAndHit(self, weapon):
        if weapon.getType() != 2:
            super().takeDamage(weapon.getAttack())
            print ("Vampire has taken damage! Current health: " + str(super().getHealth()))
        else:
            print ("Vampires are not harmed by chocolate bars! Current health: " + str(super().getHealth()))

        #super().setPerson()

    def setAndAttack(self):
        tempAttack = randint(10,20)
        return super().performAttack(tempAttack)

    def initHealth(self):
        health = randint(100,200)
        super().setHealth(health)

    def initName(self):
        super().setName("Vampire")

"""
Child class of monster with the health between 50-100 and attack 0-10.
"""
class Zombie(Monster):
    def __init__(self):
        self.initHealth()
        self.initName()

    def checkAndHit(self, weapon):
        if weapon.getType() == 1:
            super().takeDamage(weapon.getAttack()*2)
            print ("Sour straws are super effective against Zombies! Current health: " + str(super().getHealth()))
        else:
            super().takeDamage(weapon.getAttack())
            print ("Zombie has taken damage! Current health: " + str(super().getHealth()))

        #super().setPerson()

    def setAndAttack(self):
        tempAttack = randint(0,10)
        return super().performAttack(tempAttack)

    def initHealth(self):
        health = randint(50,100)
        super().setHealth(health)

    def initName(self):
        super().setName("Zombie")

"""
Child class of monster with the health between 40-80 and attack 15-30.
"""
class Ghoul(Monster):
    def __init__(self):
        self.initHealth()
        self.initName()

    def checkAndHit(self, weapon):
        if weapon.getType() == 3:
            super().takeDamage(weapon.getAttack()*5)
            print ("Nerd bombs are super super super effective! against Ghouls! Current health: " + str(super().getHealth()))
        else:
            super().takeDamage(weapon.getAttack())
            print ("Ghoul has taken damage! Current health: " + str(super().getHealth()))

        #super().setPerson()

    def setAndAttack(self):
        tempAttack = randint(15,30)
        return super().performAttack(tempAttack)

    def initHealth(self):
        health = randint(40,80)
        super().setHealth(health)

    def initName(self):
        super().setName("Ghoul")

"""
Child class of monster with the health of 200 and attack 0-40.
"""
class Werewolves(Monster):
    def __init__(self):
        self.initHealth()
        self.initName()

    def checkAndHit(self, weapon):
        if weapon.getType() == 2 or weapon.getType() == 1:
            print ("Werewolves are not effected by Chocolate bars or sour straws! Current health: " + str(super().getHealth()))
        else:
            super().takeDamage(weapon.getAttack())
            print ("Werewolf has taken damage! Current health: " + str(super().getHealth()))

        #super().setPerson()

    def setAndAttack(self):
        tempAttack = randint(0,40)
        return super().performAttack(tempAttack)

    def initHealth(self):
        super().setHealth(200)

    def initName(self):
        super().setName("Werewolf")

class Person(Monster):
    def __init__(self):
        self.initHealth()
        self.initName()

    def checkAndHit(self, weapon):
        print ("Don't worry, humans don't take damage from candy!")

    def setAndAttack(self):
        tempAttack = -5
        return super().performAttack(tempAttack)

    def initHealth(self):
        super().setHealth(100)

    def initName(self):
        super().setName("Person")
