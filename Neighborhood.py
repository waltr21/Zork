from Home import Home

class Neighborhood:
    """
	Constuctor for the Neighborhood class. Creates a 3x3 grid for the houses to be layed across.
	"""
    def __init__(self):
        self.max = 3
        self.grid = [None]*self.max
        for i in range(self.max):
            self.grid[i] = []
            for x in range(self.max):
                tempHome = Home()
                self.grid[i].append(tempHome)

    """
	Returns a house at a specific index.
	"""
    def getHouse(self, i, j):
        return self.grid[i][j]

    """
	Gets the size of the grid the houses are on.
	"""
    def getMax(self):
        return self.max

    """
    Returns true if there are no more monsters left to kill.
    """
    def gameWon(self):
        for i in range(self.max):
            for j in range(self.max):
                if self.grid[i][j].isEmpty() == False:
                    return False
        return True

    # def printGrid(self):
    #     for i in range(len(self.max)):
    #         for j in range(le)
