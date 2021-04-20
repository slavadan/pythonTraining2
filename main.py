import random

class Unit():
    def __init__(self):
        self.lvl: int = 1
        self.team: int = random.randint(1, 2)
        self.id: int = random.randint(0, 10000)


class Hero(Unit):
    def __init__(self):
        Unit.__init__(self)
        self.army = list()



    def lvlup(self):
        self.lvl += 1

class Solder(Unit):
    def follow(self, general: Hero):
        print(general.id, self.id)



hero1 = Hero()
hero1.team = 1

hero2 = Hero()
hero1.team = 2


for x in range(0, 10):
    solder = Solder()

    if solder.team == hero1.team:
        hero1.army.append(solder)
    else:
        hero2.army.append(solder)



if len(hero1.army) > len(hero2.army):
    hero1.lvlup()
    print("hero1 lvlup")
elif len(hero1.army) < len(hero2.army):
    hero2.lvlup()

hero1.army[0].follow(hero1)