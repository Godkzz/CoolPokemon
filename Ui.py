import pygame
import SET_STATE
import Player
import Battle
import Event
import Pokmen
import Enemy
import Controller
import Skill
import Bag
import ItemFactory
#设置字体
pygame.font.init()
tip_text = pygame.font.SysFont("SimHei",50) #战斗对话框字体
say_text =  pygame.font.SysFont("SimHei",38) #剧情对话框字体
battile_text = pygame.font.SysFont("SimHei",30) #战斗Ui字体
skill_text = pygame.font.SysFont("SimHei",40) #战斗技能Ui字体
skillNumber_text = pygame.font.SysFont("SimHei",60) #战斗技能数量Ui字体
info_name_text =  pygame.font.SysFont("SimHei",38) #个人信息名字字体
info_level_text =  pygame.font.SysFont("SimHei",40) #个人信息等级字体
info_hp_text =  pygame.font.SysFont("SimHei",37) #个人信息hp字体
bag_text =  pygame.font.SysFont("SimHei",41) #背包字体
battile_text.set_italic(True)
info_level_text.set_italic(True)
info_level_text.set_bold(True)
#背包字体RENDER
bag_fmt = {}
bag_fmt[0] = bag_text.render("测试物品×1",1,(0,0,0))
#剧情对话文字 最多显示三行 每行最多22个字符
global say_fmt1
global say_fmt2
global say_fmt3
say_fmt1 = say_text.render("1",1,(0,0,0))
say_fmt2 = say_text.render("2",1,(0,0,0))
say_fmt3 = say_text.render("3",1,(0,0,0))
#最多显示三行 每行最多22个字符
global text_fmt1
global text_fmt2
global text_fmt3
text_fmt1 = tip_text.render("1",1,(255,255,255))
text_fmt2 = tip_text.render("2",1,(255,255,255))
text_fmt3 = tip_text.render("3",1,(255,255,255))
#人物信息配置
global info_fmt_level
global info_fmt_name
global info_fmt_hp
global info_fmt_attack
global info_fmt_defense
global info_fmt_exp
global info_fmt_skill_name1
global info_fmt_skill_name2
global info_fmt_skill_name3
global info_fmt_skill_name4
global info_fmt_skill_pp1
global info_fmt_skill_pp2
global info_fmt_skill_pp3
global info_fmt_skill_pp4
global info_fmt_money
info_fmt_level = tip_text.render("Lv1",1,(255,255,255))
info_fmt_name = tip_text.render("小松",1,(255,255,255))
info_fmt_hp = tip_text.render("100/100",1,(255,255,255))
info_fmt_attack = tip_text.render("10",1,(255,255,255))
info_fmt_defense = tip_text.render("10",1,(255,255,255))
info_fmt_exp = tip_text.render("1/10",1,(255,255,255))
info_fmt_money = tip_text.render("1￥",1,(255,255,255))
#对话框配置
UiSayIsShow = False #是否显示对话框
UiSayImage = pygame.image.load('res/ui/ui4.png')  # 加载战斗对话框
UiSayImage2 = pygame.image.load('res/ui/ui14.png')  # 加载剧情对话框
UiSelect = pygame.image.load('res/ui/ui15.png')  # 加载是否框
UiMenu = pygame.image.load('res/ui/ui16.png')  # 加载菜单框
UiInfoHuman = pygame.image.load('res/ui/ui17.png')  # 加载个人信息人物图
UiBag = pygame.image.load('res/ui/ui18.png')  # 加载背包图
UiSayImageRect = UiSayImage.get_rect()
UiSayImageRect.y = 470
def Tip(tip):
    print(tip)
    global text_fmt1
    global text_fmt2
    global text_fmt3
    text_fmt1 = tip_text.render(tip[0:22], 1, (255, 255, 255))
    text_fmt2 = tip_text.render(tip[22:44], 1, (255, 255, 255))
    text_fmt3 = tip_text.render(tip[44:66], 1, (255, 255, 255))
def Say(say):
    global say_fmt1
    global say_fmt2
    global say_fmt3
    say_fmt1 = say_text.render(say[0:22], 1, (0, 0, 0))
    say_fmt2 = say_text.render(say[22:44], 1, (0, 0, 0))
    say_fmt3 = say_text.render(say[44:66], 1, (0, 0, 0))
    SET_STATE.isAllowMove = False
    SET_STATE.isInSaying = True
def Say_update():#更新对话
    if SET_STATE.say_id == -2:
        Say_close()
    if SET_STATE.say_id == -1:
        Say_close()
        SET_STATE.isAllowMove = True
    if SET_STATE.say_id == 0:
        pass
    elif SET_STATE.say_id == 1:
        Say("大木博士：想要去野外，必须拥有一只小精灵作为你忠实的伙伴")
        SET_STATE.say_id = 2
    elif SET_STATE.say_id == 2:
        Event.trigger(2)
    elif SET_STATE.say_id == 3:
        Say("大木博士：你们是...？")
        SET_STATE.say_id = 4
    elif SET_STATE.say_id == 4:
        Say("小轩：我人傻了，居然连我们也不认识")
        SET_STATE.say_id = 5
    elif SET_STATE.say_id == 5:
        Say("小豪：有眼无珠的老东西，我们是四大家族的三大护法")
        SET_STATE.say_id = 6
    elif SET_STATE.say_id == 6:
        Say("小英：不用和他们多废话，干就完了")
        SET_STATE.say_id = 7
    elif SET_STATE.say_id == 7:
        Say_close()
        #创建精灵
        pkq = Pokmen.Pokmen(1, 1, 5, 5, 5)
        #添加技能
        pkq.addSkill(2)
        pkq.addSkill(1)
        #训练师配置
        ying = Enemy.Enemy("小英", 100, "难道我不配吗？")
        ying.addPokmen(pkq)
        Battle.OpenBattle(3, ying)
        SET_STATE.battle_end_eventid = 4
    elif SET_STATE.say_id == 8:
        Say("小英：刚刚和你打的很尽兴，不过你也只是个没有精灵的废物罢了，相信我，迟早我们会再次相遇")
        SET_STATE.say_id = 9
    elif SET_STATE.say_id == 9:
        Say_close()
        Event.trigger(5)
    elif SET_STATE.say_id == 10:
        Say_close()
        Event.trigger(6)
    elif SET_STATE.say_id == 11:
        Say_close()
        Controller.colliderDoorController()
        SET_STATE.isAllowMove = True
    elif SET_STATE.say_id == 12:
        Say("生命值和所有技能的PP值都恢复了！")
        SET_STATE.say_id = -1
        Player.hp = Player.hp_max
        Player.skill_pp_1 = Skill.getSkillMaxPP(Player.skill_1)
        Player.skill_pp_2 = Skill.getSkillMaxPP(Player.skill_2)
        Player.skill_pp_3 = Skill.getSkillMaxPP(Player.skill_3)
        Player.skill_pp_4 = Skill.getSkillMaxPP(Player.skill_4)
    elif SET_STATE.say_id == 13:
        Say("大木博士：你现在实力不够，我不能让你去冒这个险，等你七级之后再来找我吧")
        SET_STATE.say_id = -1
    elif SET_STATE.say_id == 13:
        Say("大木博士：我通过最近的研究发现，这些石头的关键所在就在迷幻森林！")
        SET_STATE.say_id = 14
    elif SET_STATE.say_id == 14:
        Say("大木博士：拜托你前往迷幻森林帮我调查！")
        SET_STATE.main_id = 3
        SET_STATE.say_id = -1
    elif SET_STATE.say_id == 15:
        pygame.mixer.Sound("res/music/sound/s12.wav").play()
        Say("获得伤药")
        Bag.addBag(1, 5)
        SET_STATE.main_id = 3.5
        SET_STATE.say_id = -1
    elif SET_STATE.say_id == 16:
        Say("小豪：什么？！你想硬闯？找死！")
        SET_STATE.say_id = 17
    elif SET_STATE.say_id == 17:
        Say_close()
        #创建精灵
        hkl = Pokmen.Pokmen(4, 32, 12, 8, 12)
        #添加技能
        hkl.addSkill(2)
        hkl.addSkill(1)
        #创建精灵
        yd = Pokmen.Pokmen(25, 80, 35, 16, 20)
        #添加技能
        yd.addSkill(2)
        yd.addSkill(1)
        #训练师配置
        hao = Enemy.Enemy("小豪", 200, "四大家族，要没落了吗？")
        hao.addPokmen(hkl)
        hao.addPokmen(yd)
        Battle.OpenBattle(2, hao)
        SET_STATE.battle_end_eventid = 13
def Say_close():#关闭对话
    SET_STATE.isInSaying = False

def Select(select_id):#开启上下选择
    SET_STATE.isAllowMove = False
    SET_STATE.isInSelect = True
    SET_STATE.select_id = select_id

def Select_close():#关闭上下选择
    SET_STATE.isAllowMove = True
    SET_STATE.isInSelect = False
    SET_STATE.isInSaying = False
def Info():
    global info_fmt_level
    global info_fmt_name
    global info_fmt_hp
    global info_fmt_attack
    global info_fmt_defense
    global info_fmt_exp
    global info_fmt_skill_name1
    global info_fmt_skill_name2
    global info_fmt_skill_name3
    global info_fmt_skill_name4
    global info_fmt_skill_pp1
    global info_fmt_skill_pp2
    global info_fmt_skill_pp3
    global info_fmt_skill_pp4

    info_fmt_level = info_level_text.render("Lv"+str(Player.level), 1, (255, 255, 255))
    info_fmt_name = info_name_text.render(Player.name, 1, (255, 255, 255))
    info_fmt_hp = info_hp_text.render(str(Player.hp) + "/" + str(Player.hp_max), 1, (0, 0, 0))
    info_fmt_attack = info_hp_text.render(str(Player.attack), 1, (0, 0, 0))
    info_fmt_defense = info_hp_text.render(str(Player.defense), 1, (0, 0, 0))
    info_fmt_exp = info_hp_text.render(str(Player.exp) + "/" + str(Player.exp_max), 1, (0, 0, 0))
    info_fmt_skill_name1 = info_hp_text.render(Skill.getSkillName(Player.skill_1), 1, (255, 255, 255))
    info_fmt_skill_name2 = info_hp_text.render(Skill.getSkillName(Player.skill_2), 1, (255, 255, 255))
    info_fmt_skill_name3 = info_hp_text.render(Skill.getSkillName(Player.skill_3), 1, (255, 255, 255))
    info_fmt_skill_name4 = info_hp_text.render(Skill.getSkillName(Player.skill_4), 1, (255, 255, 255))
    info_fmt_skill_pp1 = info_hp_text.render(str(Player.skill_pp_1), 1, (0, 0, 0))
    info_fmt_skill_pp2 = info_hp_text.render(str(Player.skill_pp_2), 1, (0, 0, 0))
    info_fmt_skill_pp3 = info_hp_text.render(str(Player.skill_pp_3), 1, (0, 0, 0))
    info_fmt_skill_pp4 = info_hp_text.render(str(Player.skill_pp_4), 1, (0, 0, 0))

    SET_STATE.isInInfo = True

def Info_close():
    SET_STATE.isInInfo = False


def OpenBag():#开启背包
    global info_fmt_money
    Bag.bag_fix = 0 #恢复背包偏移
    SET_STATE.isInBag = True
    bag_count = len(Bag.bag_list)
    print("背包物品数："+str(bag_count))
    for i in range(len(Bag.bag_list)):
        bag_fmt[i] = bag_text.render(ItemFactory.getItemName(Bag.bag_list[i].tid) + "×" + str(Bag.bag_list[i].number),1, (0, 0, 0))
    #金钱
    info_fmt_money = info_hp_text.render(str(Player.money)+"元", 1, (0, 0, 0))

def UpdateBag():#刷新背包
    #刷新物品信息
    if len(Bag.bag_list) > 8:
        for i in range(9):
            bag_fmt[i] = bag_text.render(ItemFactory.getItemName(Bag.bag_list[i + Bag.bag_fix].tid) + "×" + str(
                Bag.bag_list[i + Bag.bag_fix].number), 1, (0, 0, 0))
    else:
        for i in range(len(Bag.bag_list)):
            bag_fmt[i] = bag_text.render(
                ItemFactory.getItemName(Bag.bag_list[i].tid) + "×" + str(Bag.bag_list[i].number), 1, (0, 0, 0))
    #刷新光标
    #如果光标索引大于 物品总数则等于最大物品索引
    if SET_STATE.bag_select_id > len(Bag.bag_list) - 1:
        SET_STATE.bag_select_id = len(Bag.bag_list) - 1
def Bag_close():
    SET_STATE.isInBag = False




#战斗场景配置
UiBattleBackgroundImage = pygame.image.load('res/ui/bk'+str(Battle.background_type)+'.png')  # 加载战斗背景
UiBattleArrowImage = pygame.image.load('res/ui/ui1.png')  # 加载敌人战斗箭头
UiBattleMyArrowImage = pygame.image.load('res/ui/ui12.png')  # 加载我方战斗箭头
UiBattleEmptyBallImage = pygame.image.load('res/ui/ui2.png')  # 加载空精灵球图标
UiBattleBallImage = pygame.image.load('res/ui/ui3.png')  # 加载精灵球图标
UiBattleHumanImage = pygame.image.load('res/ui/ui13.png')  # 加载我方战斗背景
UiHpImage = pygame.image.load('res/ui/ui5.png')  # 加载敌人血条
UiMyHpImage = pygame.image.load('res/ui/ui6.png')  # 加载我血条
UiChooseImage = pygame.image.load('res/ui/ui7.png')  # 加载战斗选择框
UiChooseBtnImage = pygame.image.load('res/ui/ui8.png')  # 加载战斗选择框按钮
UiattackBoxImage = pygame.image.load('res/ui/ui9.png')  # 加载战斗攻击选择框按钮
#敌人信息
text_pokmen_name = battile_text.render("皮卡丘",1,(62,50,55))
text_pokmen_level = battile_text.render("Lv99",1,(62,50,55))
#我的信息
text_my_name = battile_text.render(Player.name,1,(62,50,55))
text_my_level = battile_text.render("Lv99",1,(62,50,55))
text_my_hp = battile_text.render("3600",1,(62,50,55))
text_my_maxhp = battile_text.render("3600",1,(62,50,55))
#技能名字显示
UiSkillName1 = skill_text.render("摇尾巴",1,(74,73,74))
UiSkillName2 = skill_text.render("拍打",1,(74,73,74))
UiSkillName3 = skill_text.render("大文字",1,(74,73,74))
UiSkillName4 = skill_text.render(" -",1,(74,73,74))
#技能数量显示
UiSkillNumber = skillNumber_text.render("PP     30/30",1,(74,73,74))