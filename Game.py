from Player import Player
from Neighborhood import Neighborhood

class Game:
    def __init__(self):
        self.myPlayer = Player()
        self.grid = Neighborhood()
        self.houseNums = [0,0]
        self.currentHouse = self.grid.getHouse(self.houseNums[0], self.houseNums[1])
        self.message = None
        self.playGame()

    def playGame(self):
        alive = True
        while alive:
            if self.myPlayer.getHealth() <= 0:
                print ("You are dead.")
                break
            print ("You are at house: " + str(self.houseNums[0]) + "," + str(self.houseNums[1]))
            s = input("What action would you like to take? ")
            self.getInput(s)

    def attackHouse(self):
        finished = False

        while finished is False:
            w = input("What weapon would you like to use? ")

            if w.lower() == "exit":
                return

            tempWeapon = self.checkWeaponInput(w)
            finished = self.myPlayer.attackHouse(self.currentHouse, tempWeapon)
        self.currentHouse.attackPlayer(self.myPlayer)
        print ("Current health: ", self.myPlayer.getHealth())


    def checkWeaponInput(self, w):
        w = w.lower()
        for i in self.myPlayer.getInventory():
            if i.getName().lower() == w:
                return i

        return None

    def checkMove(self):
        while True:
            m = input("What direction would you like to move? ")
            m = m.lower()
            if m == "left":
                if self.houseNums[0] <= 0:
                    print ("You are already touching the left edge of the grid!")
                else:
                    self.houseNums[0] -= 1
                    break

            elif m == "right":
                if self.houseNums[0] >= self.grid.getMax()-1:
                    print ("You are already touching the right edge of the grid!")
                else:
                    self.houseNums[0] += 1
                    break

            elif m == "up":
                if self.houseNums[1] <= 0:
                    print ("You are already touching the upper edge of the grid!")
                else:
                    self.houseNums[1] -= 1
                    break

            elif m == "down":
                if self.houseNums[1] >= self.grid.getMax()-1:
                    print ("You are already touching the bottom edge of the grid!")
                else:
                    self.houseNums[1] += 1
                    break

            else:
                print ("That wasn't a valid direction! Try up, down, left, right...")



    def getInput(self, n):
        n = n.lower()
        if n == "help":
            print ("Your available actions: list, attack, move")

        elif n == "list":
            self.myPlayer.printInventory()

        elif n == "attack":
            self.attackHouse()

        elif n == "move":
            self.checkMove()
            self.currentHouse = self.grid.getHouse(self.houseNums[0], self.houseNums[1])


        else:
            if (len(n) > 0):
                print ("Invalid thing!")

g = Game()
