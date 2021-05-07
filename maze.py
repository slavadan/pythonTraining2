import cell

class Maze:

    def __init__(self, sizeX, sizeY):

        self.sizeX = sizeX
        self.sizeY = sizeY

        self.maze: [[cell.Cell]] = []
        self.fieldWithoutBorders: [[cell.Cell]] = []

        self.generateStartedMaze()

        for i in range(1, len(self.maze) - 1):

            self.fieldWithoutBorders.append(self.maze[i][1:-1])

        for i in range(len(self.fieldWithoutBorders)):
            for m in self.fieldWithoutBorders[i]:
                m.neighbors = self.findТ(m.x, m.y)





    def generateStartedMaze(self):

        for i in range(0, self.sizeY):

            self.maze.append([])
            self.maze[i] = [None] * self.sizeX

            for m in range(0, self.sizeX):

                newCell = cell.Cell(m, i)

                if i % 2 != 0 and m % 2 != 0 and i < self.sizeY - 1 and m < self.sizeX - 1:

                    self.maze[i][m] = newCell

                else:

                    newCell.type = 1

                    self.maze[i][m] = newCell

    def breakWall(self, startX, startY):
        pass

    def findТ(self, x, y):

        res: [cell.Cell] = []

        if x + 1 < len(self.fieldWithoutBorders[0]) and self.fieldWithoutBorders[y][x + 1].type == 1:

            res.append(self.fieldWithoutBorders[y][x + 1])

        if x - 1 >= 0 and self.fieldWithoutBorders[y][x - 1].type == 1:

            res.append(self.fieldWithoutBorders[y][x - 1])

        # if y + 1 < len(self.fieldWithoutBorders) and self.fieldWithoutBorders[y + 1][x].type == 1:
        #
        #     res.append(self.fieldWithoutBorders[y + 1][x])
        #
        # if y - 1 >= 0 and self.fieldWithoutBorders[y - 1][x].type == 1:
        #
        #     res.append(self.fieldWithoutBorders[y - 1][x])

        return res