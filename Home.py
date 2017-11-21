from random import randint
from Monster import Zombie
from Monster import Vampire
from Monster import Ghoul
from Monster import Werewolves
from Monster import Person
from Observer import Observer
from Observer import Observable


class Home(Observer, Observable):
    """
	Constructor for the home class.
    Randomly generates how many monsters each home will have.
	"""
    def __init__(self):
        tempNum = randint(1,10)
        self.homeList = [None] * tempNum
        self.setList()

    """
	Updates the monster to a person.
	"""
    def update(self, monster):
        monster = Person()
        print ("Moster updated!")


    """
	Returns the list of monsters in the house.
	"""
    def getMonsters(self):
        return self.homeList

    """
	Sets the house list to random monsters.
	"""
    def setList(self):
        for i in range(len(self.homeList)):
            tempList = [Zombie(), Vampire(), Ghoul(), Werewolves()]
            self.homeList[i] = tempList[randint(0,3)]
            #self.homeList[i].add_observer(self)

    """
	Attack the player one by one from the attack from each monster.
	"""
    def attackPlayer(self, player):
        total = 0
        for i in range(len(self.homeList)):
            if self.homeList[i].getHealth() <= 0:
                self.homeList[i] = Person()
            if self.homeList[i].getHealth() > 0:
                damage = self.homeList[i].setAndAttack()
                total += damage
                player.takeDamage(damage)


        print ("Player took ", total, " damage")

    """
    Returns true if there are no monsters in the house.
    """
    def isEmpty(self):
        for i in self.homeList:
            if i.getName() is not "Person":
                return False
        return True
