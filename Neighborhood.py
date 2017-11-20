from Home import Home

class Neighborhood:
    def __init__(self):
        self.max = 3
        self.grid = [None]*self.max
        for i in range(self.max):
            self.grid[i] = []
            for x in range(self.max):
                tempHome = Home()
                self.grid[i].append(tempHome)

    def getHouse(self, i, j):
        return self.grid[i][j]

    def getMax(self):
        return self.max

    # def printGrid(self):
    #     for i in range(len(self.max)):
    #         for j in range(le)
