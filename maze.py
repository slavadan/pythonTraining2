import random


class Maze:

    def __init__(self, x, y):

        self.sizeX = x

        self.sizeY = y

        self.maze = []

        self.generateMaze()

        self.breakWall()

    def generateMaze(self):

        for i in range(0, self.sizeY):

            self.maze.append([])

            self.maze[i] = [None] * self.sizeX

            for m in range(0, self.sizeX):

                if i % 2 != 0 and m % 2 != 0 and i < self.sizeY - 1 and m < self.sizeX - 1:

                    self.maze[i][m] = 0

                else:

                    self.maze[i][m] = 1

    def breakWall(self):

        visited = list()

        self.breakWallHelper([1, 1], visited)

    def breakWallHelper(self, position, visited: []):

        row = position[0]#stroka(y)
        col = position[1]#stolb

        if row < 0 or col < 0 or row >= len(self.maze) or col >= len(self.maze[row]):
            return False

        direction = self.generateDirections(position)

        visited.append(position)

        while len(direction) != 0:

            it = random.randint(0, len(direction) - 1)

            choosedDirection = direction[it]

            nextMovePosition = [row + choosedDirection[0], col + choosedDirection[1]]

            nextWallPosition = [int(row + choosedDirection[0] / 2), int(col + choosedDirection[1] / 2)]

            res = False
            for i in visited:

                if i == nextMovePosition:
                    res = True

            if res == False:

                if self.breakWallHelper(nextMovePosition, visited):

                    self.maze[nextWallPosition[0]][nextWallPosition[1]] = 0

            direction.remove(choosedDirection)

        return True


    def generateDirections(self, position: []):

        row = position[0] - 1
        col = position[1] - 1

        res = []

        mazeWithOutBorders = []

        for i in range(1, len(self.maze) - 1):

            mazeWithOutBorders.append(self.maze[i][1:-1])

        if row - 1 >= 0 and mazeWithOutBorders[row - 1][col] == 1:

            res.append([-2, 0])

        if row + 1 < len(mazeWithOutBorders) and mazeWithOutBorders[row + 1][col] == 1:

            res.append([2, 0])

        if col - 1 >= 0 and mazeWithOutBorders[row][col - 1] == 1:

            res.append([0, -2])

        if col + 1 < len(mazeWithOutBorders) and mazeWithOutBorders[row][col + 1] == 1:

            res.append([0, 2])


        return res