import Player
import Ui
import SET_STATE
import Bag
ItemInfo_KV = {} #存储物品信息的键值对



class ItemInfo():
    def __init__(self, name,price,event): #名字，价格，触发的事件
        self.name = name
        self.price = price
        self.event = event

def init():
    addItemInfo(1,ItemInfo("伤药",20,e1))
    addItemInfo(2, ItemInfo("攻击之石", 9999, e2))
    addItemInfo(3, ItemInfo("防御之石", 9999, e3))
    addItemInfo(4, ItemInfo("经验之石", 9999, e4))
    addItemInfo(5, ItemInfo("好伤药", 100, e5))
    addItemInfo(6, ItemInfo("创可贴", 5, e6))
    addItemInfo(7, ItemInfo("跌打酒", 35, e7))
    addItemInfo(8, ItemInfo("力量果实", 9999, e8))
    addItemInfo(9, ItemInfo("坚硬果实", 9999, e9))
    addItemInfo(10, ItemInfo("拌饭酱", 9999, e10))
    addItemInfo(11, ItemInfo("小英的砍刀", 9999, e11))
    addItemInfo(12, ItemInfo("秘籍-与鬼同行", 9999, e12))
def addItemInfo(tid,itemInfo):
    ItemInfo_KV[tid] = itemInfo

def getItemInfo(tid):
    return ItemInfo_KV[tid]

def useItem(tid):
    ItemInfo_KV[tid].event()

def getItemName(tid):
    return ItemInfo_KV[tid].name

def getItemPrice(tid):
    return ItemInfo_KV[tid].price

def e1():
    if SET_STATE.isInMaping == True:
        Ui.Say("妈妈曾经说过：饭可以乱吃，但是药不能！吃了精灵吃的药，血量减少了..")
        SET_STATE.say_id = -2
    Player.hp -= 1
    if Player.hp <= 0:
        Player.hp = 1
def e2():
    if SET_STATE.isInMaping == True:
        Ui.Say(f"{Player.name}的攻击力提升了1点")
        SET_STATE.say_id = -2
    Player.attack += 1
def e3():
    if SET_STATE.isInMaping == True:
        Ui.Say(Player.name+"的防御提升了1点")
        SET_STATE.say_id = -2
    Player.defense += 1
def e4():
    if SET_STATE.isInMaping == True:
        Ui.Say(Player.name+"的经验提升了100点")
        SET_STATE.say_id = -2
    Player.exp += 100
    Player.ExpUpdate()  # 刷新经验
def e5():
    if SET_STATE.isInMaping == True:
        Ui.Say("妈妈曾经说过：饭可以乱吃，但是药不能！吃了精灵吃的药，血量减少了..")
        SET_STATE.say_id = -2
    Player.hp -= 20
    if Player.hp <= 0:
        Player.hp = 1
def e6():
    if SET_STATE.isInMaping == True:
        Ui.Say(Player.name+"小心翼翼的贴上了创可贴，伤口被堵住了！")
        SET_STATE.say_id = -2
    Player.hp += 5
    if Player.hp > Player.hp_max:
        Player.hp = Player.hp_max
def e7():
    if SET_STATE.isInMaping == True:
        Ui.Say(Player.name+"把跌打酒在全身涂抹均匀，浑身散发出了一股药酒的味道")
        SET_STATE.say_id = -2
    Player.hp += 30
    if Player.hp > Player.hp_max:
        Player.hp = Player.hp_max
def e8():
    if SET_STATE.isInMaping == True:
        Ui.Say(Player.name+"感觉到力量从身体源源不断涌出，攻击增加10点！")
        SET_STATE.say_id = -2
    Player.attack += 10
def e9():
    if SET_STATE.isInMaping == True:
        Ui.Say(Player.name+"感觉到坚硬从身体源源不断涌出，防御增加10点！")
        SET_STATE.say_id = -2
    Player.defense += 10
def e10():
    if SET_STATE.isInMaping == True:
        Ui.Say(Player.name+"干捞拌饭酱，好吃不上火！恢复了60点生命值！")
        SET_STATE.say_id = -2
    Player.hp += 60
    if Player.hp > Player.hp_max:
        Player.hp = Player.hp_max
def e11():
    if SET_STATE.isInMaping == True:
        Ui.Say("和小英友谊的证明")
        SET_STATE.say_id = -2
        Bag.addBag(11,1)
def e12():
    if SET_STATE.isInMaping == True:
        Ui.Say("习得技能：与鬼同行！")
        SET_STATE.say_id = -2