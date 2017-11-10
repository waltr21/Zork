class Monster:
    def __init__(self, h):
        self.helth = h

    def takeDamage(self, damage):
        self.helth -= damage

    def performAttack(self, attack=0):
        print (attack)
        return attack

    def getHealth(self):
        return self.helth

    def setHealth(self, num):
        self.health = num
