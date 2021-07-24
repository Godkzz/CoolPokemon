import ItemFactory
global bag_list
global bag_max
bag_list = []
bag_max = 50#最多五十格
global bag_fix
bag_fix = 0#背包下拉偏移
class Bag():#物品ID 数量
    def __init__(self,tid,number):
        self.tid = tid
        self.number = number

def addBag(tid,number):
    global bag_list
    global bag_max
    if len(bag_list) < bag_max:
        already = False
        for bag in bag_list:#归并物品
            if bag.tid == tid:
                bag.number += number
                already = True
                break
        if already == False:
            bag_list.append(Bag(tid, number))


    else:
        print("背包已满，无法添加")

def use(index):
    global bag_list
    global bag_max
    global bag_fix
    if bag_list[index].number > 0:
        bag_list[index].number -= 1
        ItemFactory.useItem(bag_list[index].tid)
        if(bag_list[index].number <= 0):
            OutBag(index)
            if bag_fix > 0:
                bag_fix -= 1


def OutBag(index):
    global bag_list
    global bag_max
    if index <= 50:
        bag_list.pop(index)