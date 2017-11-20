from random import randint
from Monster import Zombie
from Monster import Vampire
from Monster import Ghoul
from Monster import Werewolves
from Monster import Person
from Observer import Observer
from Observer import Observable

class Home(Observer):
    def __init__(self):
        tempNum = randint(1,10)
        self.homeList = [None] * tempNum
        self.setList()

    def update(self, monster):
        monster = Person()
        print ("Moster updated!")


    def getMonsters(self):
        return self.homeList

    def setList(self):
        for i in range(len(self.homeList)):
            tempList = [Zombie(), Vampire(), Ghoul(), Werewolves()]
            self.homeList[i] = tempList[randint(0,3)]
            #self.homeList[i].add_observer(self)

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
