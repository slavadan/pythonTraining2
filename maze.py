import random

class Maze:

    def __init__(self, sizeX, sizeY):

        self.sizeX = sizeX
        self.sizeY = sizeY

        self.maze = []
        self.fieldWithoutBorders = []

        self.notVisitedCells = []

        self.generateStartedMaze()

        for i in range(1, len(self.maze) - 1):

            self.fieldWithoutBorders.append(self.maze[i][1:-1])

        self.findVisitedCells()


    def generateStartedMaze(self):

        for i in range(0, self.sizeY):

            self.maze.append([])
            self.maze[i] = [None] * self.sizeX

            for m in range(0, self.sizeX):

                if i % 2 != 0 and m % 2 != 0 and i < self.sizeY - 1 and m < self.sizeX - 1:

                    self.maze[i][m] = 0

                else:

                    self.maze[i][m] = 1

    def findVisitedCells(self):

        for i in range(len(self.fieldWithoutBorders)):
            for m in range(0, len(self.fieldWithoutBorders[i])):

                if self.fieldWithoutBorders[i][m] == 0:
                    self.notVisitedCells.append([m, i])

    def startBreakWalls(self, x, y):
        pass



    def checkTopNeighbour(self, x, y):

        if y - 1 >= 0 and self.fieldWithoutBorders[y - 1][x] == 1:
            return True # neighbour not visited
        else:
            return False

    def checkLeftNeighbour(self, x, y):

        if x - 1 >= 0 and self.fieldWithoutBorders[y][x - 1] == 1:
            return True  # neighbour not visited
        else:
            return False

    def checkRightNeighbour(self, x, y):

        if x + 1 < len(self.fieldWithoutBorders[y]) and self.fieldWithoutBorders[y][x + 1] == 1:
            return True  # neighbour not visited
        else:
            return False

    def checkDownstairsNeighbor(self, x, y):

        if y + 1 < len(self.fieldWithoutBorders) and self.fieldWithoutBorders[y + 1][x] == 1:
            return True  # neighbour not visited
        else:
            return False