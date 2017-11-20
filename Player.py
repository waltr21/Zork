from random import randint
from Weapon import HersheyKisses
from Weapon import ChocolateBar
from Weapon import SourStraw
from Weapon import NerdBomb

class Player:
    def __init__(self):
        self.health = 200
        self.attackLevel = randint(30, 40)
        self.inventory = [None] * 10
        self.setInventory()
        self.bubble_sort()

    def takeDamage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
        elif self.health > 200:
            self.health = 200

    def setInventory(self):
        self.inventory[0] = HersheyKisses()
        self.inventory[0].setAttackModifier(round(self.inventory[0].getAttack() * self.attackLevel, 2))
        for i in range (1, len(self.inventory)):
            temp = [ChocolateBar(), SourStraw(), NerdBomb()]
            self.inventory[i] = temp[randint(0,2)]
            self.inventory[i].setAttackModifier(round(self.inventory[i].getAttack() * self.attackLevel, 2))

    def getHealth(self):
        return self.health

    def attackHouse(self, house, weapon):
        if weapon == None:
            print ("You don't have this weapon!")
            return False

        else:
            print ("\n************ Attack ************")
            for i in house.getMonsters():
                i.checkAndHit(weapon)
            print ("************ Attack ************\n")
            weapon.decreaseAmount()
            self.removeInventory()
            return True

    def removeInventory(self):
        for i in range(len(self.inventory)):
            if self.inventory[i].getAmount() < 1:
                del self.inventory[i]
                return

    def getAttack(self):
        return self.attackLevel

    def getInventory(self):
        return self.inventory

    def printInventory(self):
        print ("\n************ Inventory ************")
        for i in self.inventory:
            print (i.toString())
        print ("************ Inventory ************\n")

    def bubble_sort(self):
        length = len(self.inventory)
        for i in range(length-1, -1, -1):
            for j in range(i):
                if self.inventory[j].getType() > self.inventory[j+1].getType():
                    self.inventory[j], self.inventory[j+1] = self.inventory[j+1], self.inventory[j]
