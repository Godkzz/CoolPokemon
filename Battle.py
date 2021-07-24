import pygame
import SET_STATE
import threading
import Ui
import Player
import Controller
import Skill
import random
import time
import Event
#控制战斗开始的黑色遮罩层的Y坐标
global mask_topy
global mask_bottomy
mask_topy = 0
mask_bottomy = 350
global background_type
background_type = 1
global enemy_number
global enemy_list
global enemy_index
global this_enemy
this_enemy = 0 #记录战斗中的敌人信息
enemy_list = [] #记录敌人精灵列表
enemy_number = 0 #记录敌人一共有多少只精灵
enemy_index = 0 #敌人正在战斗的小精灵索引

enemy_x = 850 #敌人图标x坐标
global enemy_y
enemy_y = 70 #敌人图标Y坐标
my_x = 300#我方人物x坐标
global mask_speed
global mask_delay
mask_speed = 1  # 遮罩移动的速度
mask_delay = 0.07  # 遮罩移动触发时间间隔
def MaskMove():
    global mask_topy
    global mask_bottomy
    global mask_speed
    global mask_delay
    if mask_topy >=-1850:
        mask_topy -= mask_speed
        mask_bottomy += mask_speed
        mask_speed += 1
        timethread = threading.Timer(mask_delay, MaskMove)  # 回调线程
        timethread.start()
    else:
        #开始战斗
        SET_STATE.isBattleMask = False
        SET_STATE.isInBattleShowBall = False
        SET_STATE.isInBattling = True
        Ui.Tip(Player.name+"该如何应对？")



def OpenBattle(type,enemy):
    #加载音乐
    pygame.mixer.music.load("res/music/bgm/m1.mp3")
    pygame.mixer.music.play(-1, 0.0)
    #初始化敌人图坐标
    global enemy_y
    enemy_y = 70
    #同步敌人列表
    global enemy_list
    global this_enemy
    enemy_list = enemy.pokmen_list
    this_enemy = enemy
    #设置背景
    global background_type
    background_type = type
    Ui.UiBattleBackgroundImage = pygame.image.load('res/ui/bk' + str(type) + '.png')  # 加载战斗背景
    #获取敌人精灵总数
    global enemy_number
    enemy_number = len(enemy.pokmen_list)
    #改变状态
    SET_STATE.isInMaping = False  # 是否在地图中
    SET_STATE.isInBattle = True  # 是否在战斗中
    SET_STATE.isInSaying = False  # 是否在对话中
    #初始化遮罩层坐标
    global mask_topy
    global mask_bottomy
    mask_topy = 0
    mask_bottomy = 350
    #开始加载场景
    SET_STATE.isBattleMask = True
    SET_STATE.isInBattleShowBall = True
    #加载我属性
    Ui.text_my_name = Ui.battile_text.render(Player.name, 1, (62, 50, 55))
    Ui.text_my_level = Ui.battile_text.render("Lv"+str(Player.level), 1, (62, 50, 55))
    Ui.text_my_hp = Ui.battile_text.render(str(Player.hp), 1, (62, 50, 55))
    Ui.text_my_maxhp = Ui.battile_text.render(str(Player.hp_max), 1, (62, 50, 55))
    #加载技能
    Ui.UiSkillName1 = Ui.skill_text.render(Skill.getSkillName(Player.skill_1), 1, (74, 73, 74))
    Ui.UiSkillName2 = Ui.skill_text.render(Skill.getSkillName(Player.skill_2), 1, (74, 73, 74))
    Ui.UiSkillName3 = Ui.skill_text.render(Skill.getSkillName(Player.skill_3), 1, (74, 73, 74))
    Ui.UiSkillName4 = Ui.skill_text.render(Skill.getSkillName(Player.skill_4), 1, (74, 73, 74))
    #加载敌人属性
    Ui.text_pokmen_name = Ui.battile_text.render(enemy.pokmen_list[enemy_index].name, 1, (62, 50, 55))
    Ui.text_pokmen_level = Ui.battile_text.render("Lv"+str(enemy.pokmen_list[enemy_index].level), 1, (62, 50, 55))
    #计算我血条和经验值百分比
    Player.hp_per = Player.hp / Player.hp_max
    Player.exp_per = Player.exp / Player.exp_max
    #计算敌人血条
    enemy.pokmen_list[enemy_index].hp_per = enemy.pokmen_list[enemy_index].hp / enemy.pokmen_list[enemy_index].hp_max
    #开始移动遮罩层
    global mask_speed
    mask_speed = 3 #重置遮罩层速度
    MaskMove()
    #出现野怪的提示
    if enemy.name == "野怪":
        Ui.Tip("出现了一只野生的" + enemy.pokmen_list[enemy_index].name)
    else:
        Ui.Tip("训练师" + enemy.name +"向你发起了对决")


def useSkill(sid): #玩家使用技能
    Skill.skillEvent(sid)
    if sid >0:
        SET_STATE.isChoseSkill = False  # 正在选择技能
        SET_STATE.isEnemyHandle = True  # 敌人回合
        updateEnemy()  # 刷新敌人属性

global per_change_speed
per_change_speed = 0.03 #血条改变速度
def per_change(now_per,really_per,type):#循序改变敌人血条  really_per传入实际改变的变量 敌人的百分比或主角百分比
    global per_change_speed
    #type 0=敌人改变 1=主角改变
    if now_per < really_per: #扣血
        really_per -= per_change_speed
        # 防止溢出
        if now_per > really_per:
            really_per = now_per
        if really_per < 0:
            now_per = 0#跳出循环
            really_per = 0
        if type == 0:
            enemy_list[enemy_index].hp_per = really_per
        if type == 1:
            Player.hp_per = really_per
        timethread = threading.Timer(0.07, per_change,[now_per,really_per,type])  # 回调线程
        timethread.start()
    elif now_per > really_per and now_per <= 1 and really_per <= 1: #补血
        if now_per < really_per:  # 防止溢出
            really_per = now_per
        if really_per > 1:
            now_per = 1  # 跳出循环
            really_per = 1
        really_per += per_change_speed
        timethread = threading.Timer(0.07, per_change,[now_per,really_per,type])  # 回调线程
        timethread.start()
    else:
        if type == 0:
            Enemy_Handle()#敌人回合开始
        if type == 1:
            SET_STATE.isChoseSkill = False  # 正在选择技能
            SET_STATE.isEnemyHandle = False  # 敌人回合中
            Ui.Tip(Player.name + "该如何应对？")


def updateEnemy():#刷新战斗中的敌人数据
    #计算敌人血条
    now_per = enemy_list[enemy_index].hp / enemy_list[enemy_index].hp_max
    per_change(now_per,enemy_list[enemy_index].hp_per,0)#循序改变敌人血条

def updateMy():#刷新战斗中的我数据
    #计算我血条
    now_per = Player.hp / Player.hp_max
    per_change(now_per,Player.hp_per,1)#循序改变我血条
    #血量
    Ui.text_my_hp = Ui.battile_text.render(str(Player.hp), 1, (62, 50, 55))
    Ui.text_my_maxhp = Ui.battile_text.render(str(Player.hp_max), 1, (62, 50, 55))
    #判断是否死亡
    if Player.hp <=0: #直接关闭游戏
        sys.exit()

def Enemy_down():#精灵死亡倒下
    global enemy_list
    global enemy_index
    global enemy_y
    if enemy_y <400:
        enemy_y += 10
        timethread = threading.Timer(0.01, Enemy_down)  # 回调线程
        timethread.start()
    else:#游戏结束或敌人派出下一只精灵
        if len(enemy_list) > enemy_index + 1:
            time.sleep(1.5)
            enemy_index += 1
            print('敌人更换精灵:'+enemy_list[enemy_index].name)
            # 加载敌人属性
            Ui.text_pokmen_name = Ui.battile_text.render(enemy_list[enemy_index].name, 1, (62, 50, 55))
            Ui.text_pokmen_level = Ui.battile_text.render("Lv" + str(enemy_list[enemy_index].level), 1,(62, 50, 55))
            #初始化敌人图Y坐标
            pygame.mixer.Sound("res/music/sound/s5.wav").play() #派出新精灵的音效
            enemy_y = 70
            Ui.Tip("对手派出了"+enemy_list[enemy_index].name)
            time.sleep(1)
            SET_STATE.isInBattling = True #恢复战斗
            SET_STATE.isEnemyHandle = False
            Ui.Tip(Player.name + "该如何应对？")
        else:
            print("对战结束")
            # 加载音乐
            pygame.mixer.music.load("res/music/bgm/m2.mp3")
            pygame.mixer.music.play(-1, 0.0)
            if this_enemy.name != "野怪":
                time.sleep(2.5)
                Ui.Tip(this_enemy.name + ":" + this_enemy.say)
            time.sleep(3.5)
            Player.money += this_enemy.money
            Ui.Tip("获得胜利的奖金"+str(this_enemy.money)+"元")
            time.sleep(3.5)
            SET_STATE.isBattleMask = False
            SET_STATE.isInBattleShowBall = False
            SET_STATE.isInBattling = False
            SET_STATE.isInBattle = False
            SET_STATE.isChoseSkill = False  # 正在选择技能
            SET_STATE.isEnemyHandle = False  # 敌人回合中
            time.sleep(0.1)
            SET_STATE.isInMaping = True  # 是否在地图中
            Event.trigger(SET_STATE.battle_end_eventid)#触发剧情
            SET_STATE.battle_end_eventid = -1 #重置
            if SET_STATE.map_id == 1:
                pygame.mixer.music.load("res/music/bgm/m3.mp3")
                pygame.mixer.music.play(-1, 0.0)




def exp_per_change(now_per,really_per):
    per_change_speed = 0.03
    if now_per < really_per:
        now_per += per_change_speed
        Player.exp_per += per_change_speed
        if Player.exp_per >= 1:
            Player.exp_per = 0
        elif now_per >= really_per:
            pass #跳出回调线程
        else:
            timethread = threading.Timer(0.07, exp_per_change, [now_per, really_per])  # 回调线程
            timethread.start()


def Enemy_Handle():#敌人回合
    time.sleep(1)
    print('敌人回合开始')
    if enemy_list[enemy_index].hp > 0: #看看敌人这只精灵死了没
        all_skill = enemy_list[enemy_index].skill_list  # 这个精灵的所有技能
        skill_count = len(all_skill)  # 敌人技能总数
        rd = random.randint(0, skill_count - 1)  # 随机技能种子
        print('技能总数：' + str(skill_count) + ",[获得随机种子]" + str(rd) + ",[使用技能ID]" + str(all_skill[rd]))
        Skill.skillEvent(all_skill[rd])
        updateMy()
    else:
        print('敌人精灵死亡')
        Enemy_down()
        pygame.mixer.Sound("res/music/sound/s6.wav").play()  # 精灵死亡音效
        Ui.Tip(enemy_list[enemy_index].name+"倒下了！")
        time.sleep(1.5)
        exp = enemy_list[enemy_index].level * 20 #打败精灵后获得的经验
        Player.exp += exp #获取经验
        really_per = Player.exp / Player.exp_max    #计算真实的经验值百分比
        exp_per_change(Player.exp_per,really_per)
        Player.ExpUpdate()#刷新经验
        Ui.text_my_level = Ui.battile_text.render("Lv" + str(Player.level), 1, (62, 50, 55)) #刷新等级
        pygame.mixer.Sound("res/music/sound/s7.wav").play()
        Ui.Tip(Player.name + "获得了"+str(exp)+"点经验值")
