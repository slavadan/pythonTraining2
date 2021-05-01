import random

def neighbourhood(list, x, y):

        res = []

        if y-1 >= 0:
            res.append(list[y-1][x])
        if y+1 < len(list):
            res.append(list[y+1][x])

        if x-1 >= 0:
            res.append(list[y][x-1])
        if x+1 < len(list[y]):
            res.append(list[y][x+1])

        return res

x: int = int(input())
y: int = int(input())

list = []

for i in range(y):
    list.append([])
    for m in range(x):
        list[i].append(random.randint(0, 100))

#output order top bottom left right
for i in range(len(list)):
    print(list[i])



chooseX = int(input("Choose X coord: "))
chooseY = int(input("Choose Y coord: "))
print(neighbourhood(list, chooseX, chooseY))