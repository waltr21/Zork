from random import randint
class Player:
    def __init__(self):
        self.health = randint(100, 125)
        self.attackLevel = randint(10, 20)
        self.inventory = [None] * 10
        print ("Player created!")

    def takeDamage(self, damage):
        self.health -= damage

    def setInventory(self):
        #Make a list of weapons
        for i in self.inventory:
            #Choose a random weapon and set it equal to i
            #This is a temp thing cause Python is annoying
            i = None

    def getHealth(self):
        return self.health

    def getAttack(self):
        return self.attackLevel
