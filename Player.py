from random import randint
from Weapon import HersheyKisses
from Weapon import ChocolateBar
from Weapon import SourStraw
from Weapon import NerdBomb

class Player:
    """
	Constuctor for the player. Given the health of 200 and an attack rate between 30 and 40.
    Inventory is also set to 10 random weapons.
	"""
    def __init__(self):
        self.health = 200
        self.attackLevel = randint(30, 40)
        self.inventory = [None] * 10
        self.setInventory()
        self.bubble_sort()

    """
	Subtracts and caps damage the player can take.
	"""
    def takeDamage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
        elif self.health > 200:
            self.health = 200

    """
	Set the first slot of the inventory equal to hersheykisses (becuase we have unlimited there
    is no point of having multuple), then choose random weapons for the rest of the slots.
	"""
    def setInventory(self):
        self.inventory[0] = HersheyKisses()
        self.inventory[0].setAttackModifier(round(self.inventory[0].getAttack() * self.attackLevel, 2))
        for i in range (1, len(self.inventory)):
            temp = [ChocolateBar(), SourStraw(), NerdBomb()]
            self.inventory[i] = temp[randint(0,2)]
            self.inventory[i].setAttackModifier(round(self.inventory[i].getAttack() * self.attackLevel, 2))

    """
	Returns the health of the player.
	"""
    def getHealth(self):
        return self.health

    """
	Method that allows the player to attack a house with a specific weapon.
	"""
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

    """
	Checks to see if an item in the users inventory is 0.
    Then that item is removed.
	"""
    def removeInventory(self):
        for i in range(len(self.inventory)):
            if self.inventory[i].getAmount() < 1:
                del self.inventory[i]
                return

    """
	Return the attack level of the player.
	"""
    def getAttack(self):
        return self.attackLevel

    """
	Returns the list of weapons the player has.
	"""
    def getInventory(self):
        return self.inventory

    """
	Prints the items in the users inventory.
	"""
    def printInventory(self):
        print ("\n************ Inventory ************")
        for i in self.inventory:
            print (i.toString())
        print ("************ Inventory ************\n")

    """
	Simple sorting algorithm used to organize the players inventory.
	"""
    def bubble_sort(self):
        length = len(self.inventory)
        for i in range(length-1, -1, -1):
            for j in range(i):
                if self.inventory[j].getType() > self.inventory[j+1].getType():
                    self.inventory[j], self.inventory[j+1] = self.inventory[j+1], self.inventory[j]
