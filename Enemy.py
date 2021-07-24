import pygame

class Enemy():
    def __init__(self, name,money,say="..."):#敌人的名字和战胜后获得的金钱
        super().__init__()
        self.name = name
        self.money = money
        self.say = say#战胜敌人后 敌人说的骚话
        self.pokmen_list = []  # 存储精灵
    def addPokmen(self,pokmen):  #最多6个精灵
        if len(self.pokmen_list) < 6:
            print(self.name+"add:pokmen"+pokmen.name)
            self.pokmen_list.append(pokmen)
        else:
            print(self.name + "的精灵已满6只，无法继续添加！")
