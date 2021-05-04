import random

def neighbourhood(list, x, y):

        res = []

        if y-1 >= 0 and x-1 >= 0:
            res.append(list[y-1][x-1])
        else:
            res.append(None)

        if y-1 >= 0:
            res.append(list[y-1][x])
        else:
            res.append(None)


        if y-1 >= 0 and x+1 < len(list[y-1]):
            res.append(list[y-1][x+1])
        else:
            res.append(None)

        if x-1 >= 0:
            res.append(list[y][x-1])
        else:
            res.append(None)




        if x+1 < len(list[y]):
            res.append(list[y][x+1])
        else:
            res.append(None)



        if y+1 < len(list) and x-1 >= 0:
            res.append(list[y+1][x-1])
        else:
            res.append(None)

        if y+1 < len(list):
            res.append(list[y+1][x])
        else:
            res.append(None)

        if y+1 < len(list) and x+1 < len(list[y+1]):
            res.append(list[y+1][x+1])
        else:
            res.append(None)



        return res

def foo(list):

    res = []

    for l in list:
        res.extend(l)
    return  res

def createList(x, y):
    list = []

    for i in range(y):
        list.append([])
        for m in range(x):
            list[i].append(random.randint(0, 100))

    return list

def createDList(list, x):

    res = []

    for i in range(0, len(list), x):
        res.append(list[i:i+x])

    return res


    # start = 0
    # end = x
    #
    # for i in res:
    #
    #     while start < end:
    #         i.append(list[start])
    #         start += 1
    #
    #     if end >= len(list):
    #         return res
    #     else:
    #         end += x


def printDList(list):
    for i in range(len(list)):
        print(list[i])

x: int = int(input())
y: int = int(input())

list = createList(x, y)

#output order top bottom left right
printDList(list)

line = foo(list)
print(line)

dline = createDList(line, x)
printDList(dline)


# chooseX = int(input("Choose X coord: "))
# chooseY = int(input("Choose Y coord: "))
#
# res = neighbourhood(list, chooseX, chooseY)
# print(res)
