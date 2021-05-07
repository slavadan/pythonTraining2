import maze

chooseSizeX = int(input("Input sizeX:"))
chooseSizeY = int(input("Input sizeY:"))

lab = maze.Maze(chooseSizeX, chooseSizeY)

print(lab.fieldWithoutBorders[0][0].x)