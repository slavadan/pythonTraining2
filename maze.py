import cell
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

        self.breakWall(0, 0)





    def generateStartedMaze(self):

        for i in range(0, self.sizeY):

            self.maze.append([])
            self.maze[i] = [None] * self.sizeX

            for m in range(0, self.sizeX):

                if i % 2 != 0 and m % 2 != 0 and i < self.sizeY - 1 and m < self.sizeX - 1:

                    self.maze[i][m] = 0
                    self.notVisitedCells.append(self.maze[i][m])

                else:

                    self.maze[i][m] = 1


    def breakWall(self, startX, startY):

        chooseDirection = random.randint(1, 4)

        if len(self.notVisitedCells) == 0:
            return

        if chooseDirection == 1 and self.checkRightNeighbour(startX, startY): #go to right

            self.fieldWithoutBorders[startY][startX + 1] = 0
            self.notVisitedCells.pop(-1)
            self.breakWall(startX + 1, startY)


        if chooseDirection == 2 and self.checkLeftNeighbour(startX, startY): #go to left

            self.fieldWithoutBorders[startY][startX - 1] = 0
            self.notVisitedCells.pop(-1)
            self.breakWall(startX - 1, startY)


        if chooseDirection == 3 and self.checkTopNeighbour(startX, startY):#go to top

            self.fieldWithoutBorders[startY - 1][startX] = 0
            self.notVisitedCells.pop(-1)
            self.breakWall(startX, startY - 1)

        if chooseDirection == 4 and self.checkDownstairsNeighbor(startX, startY):

            self.fieldWithoutBorders[startY + 1][startX] = 0
            self.notVisitedCells.pop(-1)
            self.breakWall(startX, startY + 1)






    def checkTopNeighbour(self, x, y):

        if y - 1 >= 0 and self.fieldWithoutBorders[y - 1][x] == 1:
            return True #neighbour not visited
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