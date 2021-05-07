import maze

chooseSizeX = int(input("Input sizeX:"))
chooseSizeY = int(input("Input sizeY:"))

lab = maze.Maze(chooseSizeX, chooseSizeY)

for i in lab.maze:
    print(i)

for i in lab.fieldWithoutBorders:
    print(i)