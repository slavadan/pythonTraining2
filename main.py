import maze

chooseSizeX = int(input("Input sizeX:"))
chooseSizeY = int(input("Input sizeY:"))

lab = maze.Maze(chooseSizeX, chooseSizeY)

a = 5

for i in lab.maze:
    print(i)