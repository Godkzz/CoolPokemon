import Battle
global all_skill_kv
import Player
import Ui
import Effect
import pygame
import time
import random
all_skill_kv = {}#键=技能ID 数值=技能
class Skill():
    def __init__(self,name,pp_max,event):
        super().__init__()
        self.name = name
        self.pp_max = pp_max
        self.event = event

def pushSkill(sid,skill):
    global all_skill_kv
    all_skill_kv[sid] = skill

def getSkillName(sid):
    return all_skill_kv[sid].name

def getSkillMaxPP(sid):
    return all_skill_kv[sid].pp_max

def skillEvent(sid): #触发技能事件
    return all_skill_kv[sid].event()

def init(): #初始化所有技能
    global all_skill_kv
    pushSkill(0, Skill(" -", 0, skillEvent1)) #空技能
    pushSkill(1,Skill("叫声",10,skillEvent2))
    pushSkill(2, Skill("电击", 10, skillEvent3))
    pushSkill(3, Skill("资本攻击", 10, skillEvent8))
    pushSkill(4, Skill("拍打", 10, skillEvent4)) #主角技能
    pushSkill(5, Skill("头槌", 10, skillEvent5))
    pushSkill(6, Skill("冲击", 10, skillEvent6))
    pushSkill(7, Skill("翅膀攻击", 10, skillEvent7))
    pushSkill(8, Skill("紫色基情", 10, skillEvent9))  # 主角技能
    pushSkill(9, Skill("与鬼同行", 5, skillEvent10))  # 主角技能
def skillEvent1():
    print('empty skill')
def skillEvent2():
    pygame.mixer.Sound("res/music/sound/s10.wav").play()
    Battle.enemy_list[Battle.enemy_index].attack +=1
    Ui.Tip(Battle.enemy_list[Battle.enemy_index].name + "发出了叫声，"+Battle.enemy_list[Battle.enemy_index].name+"的攻击增加了！")
    Effect.Effect(5, 830, 100)
    time.sleep(2)
def skillEvent3():
    global damage
    damage = Battle.enemy_list[Battle.enemy_index].attack - Player.defense
    if damage <= 0:
        damage = 1
    Player.hp -= Battle.enemy_list[Battle.enemy_index].attack
    Effect.Effect(4, 270, 270)
    Ui.Tip(Battle.enemy_list[Battle.enemy_index].name + "使用电击，"+Player.name+"在电闪雷鸣中交加")
    Battle.my_x = 290  # 我方晃动效果
    pygame.mixer.Sound("res/music/sound/s2.wav").play()
    time.sleep(1)
def skillEvent4():
    global damage
    damage = Player.attack - Battle.enemy_list[Battle.enemy_index].defense
    if damage <= 0:
        damage = 1
    Battle.enemy_list[Battle.enemy_index].hp -= damage
    Effect.Effect(1,850,150)
    Ui.Tip(Player.name+"使出了浑身解数，拍打了对方")
    Battle.enemy_x = 840 #怪物晃动效果
    pygame.mixer.Sound("res/music/sound/s1.wav").play()
def skillEvent5():
    global damage
    damage = Battle.enemy_list[Battle.enemy_index].attack - Player.defense
    if damage <= 0:
        damage = 1
    Player.hp -= damage
    Effect.Effect(1, 310, 270)
    Ui.Tip(Battle.enemy_list[Battle.enemy_index].name + "使用头槌")
    Battle.my_x = 290  # 我方晃动效果
    pygame.mixer.Sound("res/music/sound/s1.wav").play()

def skillEvent6():
    global damage
    damage = Battle.enemy_list[Battle.enemy_index].attack - Player.defense
    if damage <= 0:
        damage = 1
    Player.hp -= damage
    Effect.Effect(1, 310, 270)
    Ui.Tip(Battle.enemy_list[Battle.enemy_index].name + "使用冲击")
    Battle.my_x = 290  # 我方晃动效果
    pygame.mixer.Sound("res/music/sound/s1.wav").play()

def skillEvent7():
    global damage
    damage = Battle.enemy_list[Battle.enemy_index].attack - Player.defense
    if damage <= 0:
        damage = 1
    Player.hp -= (damage + random.randint(1, 3))
    Effect.Effect(2, 310, 270)
    Ui.Tip(Battle.enemy_list[Battle.enemy_index].name + "展翅高飞，使用了翅膀攻击")
    Battle.my_x = 290  # 我方晃动效果
    pygame.mixer.Sound("res/music/sound/s11.wav").play()
def skillEvent8():
    global damage
    damage = Player.attack - Battle.enemy_list[Battle.enemy_index].defense
    if damage <= 0:
        damage = 1
    Battle.enemy_list[Battle.enemy_index].hp -= damage
    #扣钱
    Player.money -= 10
    Effect.Effect(7,850,150)
    Ui.Tip(Player.name+"用金钱砸向对方，使出资本攻击！")
    Battle.enemy_x = 840 #怪物晃动效果
    pygame.mixer.Sound("res/music/sound/s1.wav").play()
def skillEvent9():
    global damage
    damage = Player.attack * 2 - Battle.enemy_list[Battle.enemy_index].defense
    if damage <= 0:
        damage = 1
    Battle.enemy_list[Battle.enemy_index].hp -= damage
    Effect.Effect(8,850,110)
    Ui.Tip(Player.name+"使出了紫色基情，嘴巴里缓缓吐吞出紫色的烟雾！")
    Battle.enemy_x = 840 #怪物晃动效果
    pygame.mixer.Sound("res/music/sound/s1.wav").play()
def skillEvent10():
    global damage
    damage = Player.attack * 5 - Battle.enemy_list[Battle.enemy_index].defense
    if damage <= 0:
        damage = 1
    Battle.enemy_list[Battle.enemy_index].hp -= damage
    Effect.Effect(9,850,110)
    Ui.Tip(Player.name+"使出了与鬼同行，两仪生四象，四象生八卦！")
    Battle.enemy_x = 840 #怪物晃动效果
    pygame.mixer.Sound("res/music/sound/s1.wav").play()