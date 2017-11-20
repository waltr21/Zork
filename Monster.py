from random import randint
from Observer import Observer
from Observer import Observable

class Monster(Observable):
    def __init__(self):
        self.health = 0
        self.name = none

    def takeDamage(self, damage):
        self.health -= damage

    def performAttack(self, attack):
        return attack

    def getHealth(self):
        if self.health < 0:
            self.health = 0
        return round(self.health, 2)

    def getName(self):
        return self.name

    def setHealth(self, h):
        self.health = h

    def setName(self, n):
        self.name = n

    def setPerson(self):
        if (self.health <= 0):
            super().update()

    def toString(self):
        temp = "Monster: " + self.name + " / " + str(self.health)
        return temp

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
