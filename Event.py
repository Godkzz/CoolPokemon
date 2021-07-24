import SET_STATE
import SET_SPRITES
import Npc
import Player
import time
import Map
import Ui
import threading
import Controller
import pygame
import Enemy
import Pokmen
import Battle
import random
import ItemFactory
import Bag
#npc容器
npc_list = {}
#物件容器
item_list = {}
#事件模块

def trigger(event_id):
    print("trigge:"+str(event_id))
    print("main:" + str(SET_STATE.main_id))
    if event_id == -2:#使用物品
        SET_STATE.isInSaying = False
        if Bag.bag_list[SET_STATE.bag_select_id+Bag.bag_fix].number > 0:
            Bag.use(SET_STATE.bag_select_id + Bag.bag_fix)
            Ui.UpdateBag()

    if event_id == 1:#初遇博士
        if SET_STATE.main_id == 0:
            # 禁止移动
            SET_STATE.isAllowMove = False
            # 创建博士
            pygame.mixer.Sound("res/music/sound/s8.wav").play()
            npc_list[0] = Npc.Human(13, "博士", 0)
            npc_list[0].DX = Player.DX
            npc_list[0].DY = Player.DY
            npc_list[0].rect.x = 1
            npc_list[0].rect.y = 350
            npc_list[0].move(2, 350)
            SET_SPRITES.player.move(1)
            SET_SPRITES.player.move(1)
            Player.face = 1
            time.sleep(3.5)
            Ui.Say("大木博士：危险！随便进入草丛会遭遇精灵的袭击！")
            SET_STATE.say_id = 1
        elif SET_STATE.main_id == 1:
            Ui.Say("大木博士：危险！快过来挑选精灵！")
            SET_STATE.isAllowMove = False
            SET_SPRITES.player.move(1)
            SET_SPRITES.player.move(1)
            SET_STATE.say_id = 11
        else:#第一个草丛 遭遇怪物
            def f0():
                Controller.colliderDoorController()
            if SET_STATE.isMoving == True and SET_STATE.isAllowWildBattle == True:
                rd = random.randint(1, 10)  # 遇怪概率
                rdPK = random.randint(1, 2)  # 遇怪种类概率
                if rd == 1:  # 1/10概率遇怪
                    if rdPK == 1:
                        yb = Pokmen.Pokmen(7, 10, 3, 1, 5)
                        yb.addSkill(1)
                        yb.addSkill(6)
                        wild = Enemy.Enemy("野怪", 10)
                        wild.addPokmen(yb)
                    elif rdPK == 2:
                        zs = Pokmen.Pokmen(12, 15, 4, 1, 5)
                        zs.addSkill(1)
                        zs.addSkill(5)
                        wild = Enemy.Enemy("野怪", 10)
                        wild.addPokmen(zs)
                    Battle.OpenBattle(3, wild)
                    threading.Timer(0.1, f0, ).start()
                else:
                    threading.Timer(0.1, f0, ).start()
            else:
                threading.Timer(0.1, f0, ).start()

    if event_id == 2:#博士送精灵
        Ui.Say_close()
        item_list[0] = Map.Build(2, npc_list[0].rect.x + 30, npc_list[0].rect.y+20)
        item_list[0].DX = Player.DX
        item_list[0].DY = Player.DY
        item_list[0].name = "小火龙精灵球"
        pygame.mixer.Sound("res/music/sound/s8.wav").play()
        SET_SPRITES.build_sprites.add(item_list[0])
        def f0():
            npc_list[0].move(0, 80)
            threading.Timer(1, f1, ).start()
        threading.Timer(1, f0, ).start()
        def f1():
            npc_list[0].face = 2
            item_list[1] = Map.Build(2, npc_list[0].rect.x + 30, npc_list[0].rect.y + 20)
            item_list[1].DX = Player.DX
            item_list[1].DY = Player.DY
            item_list[1].name = "杰尼龟精灵球"
            pygame.mixer.Sound("res/music/sound/s8.wav").play()
            SET_SPRITES.build_sprites.add(item_list[1])
            threading.Timer(1, f2, ).start()
        def f2():
            npc_list[0].move(0, 80)
            threading.Timer(1, f3, ).start()
        def f3():
            npc_list[0].face = 2
            item_list[2] = Map.Build(2, npc_list[0].rect.x + 30, npc_list[0].rect.y + 20)
            item_list[2].DX = Player.DX
            item_list[2].DY = Player.DY
            item_list[2].name = "皮卡丘精灵球"
            pygame.mixer.Sound("res/music/sound/s8.wav").play()
            SET_SPRITES.build_sprites.add(item_list[2])
            threading.Timer(1, f4, ).start()
        def f4():
            npc_list[0].move(1, 150)
            threading.Timer(2, f5, ).start()
        def f5():
            npc_list[0].face = 2
            Ui.Say("大木博士：孩子，快过来选择一个陪伴你的精灵吧")
            Controller.colliderDoorController()
            SET_STATE.main_id = 1#禁止进入草丛
            SET_STATE.say_id = -1
    if event_id == 3:#选择完精灵球
        Ui.Say("大木博士：嗯..这是个很棒的精灵，相信你一定可以成为一个优秀的训练师")
        SET_STATE.say_id = 0
        def f0():
            # 加载音乐
            pygame.mixer.music.load("res/music/bgm/m4.mp3")
            pygame.mixer.music.play(-1, 0.0)
            Ui.Say_close()
            # 创建小轩
            npc_list[1] = Npc.Human(4, "小轩", 0)
            npc_list[1].DX = Player.DX
            npc_list[1].DY = Player.DY
            npc_list[1].rect.x = 1
            npc_list[1].rect.y = 350
            npc_list[1].move(2, 520)
            #创建小豪
            npc_list[2] = Npc.Human(3, "小豪", 0)
            npc_list[2].DX = Player.DX
            npc_list[2].DY = Player.DY
            npc_list[2].rect.x = 1
            npc_list[2].rect.y = 410
            npc_list[2].move(2, 510)
            #创建小英
            npc_list[3] = Npc.Human(5, "小英", 0)
            npc_list[3].DX = Player.DX
            npc_list[3].DY = Player.DY
            npc_list[3].rect.x = 1
            npc_list[3].rect.y = 480
            npc_list[3].move(2, 500)
            threading.Timer(3.5, f1, ).start() #3.5
        threading.Timer(1.5, f0, ).start()
        def f1():
            temp_list = SET_SPRITES.build_sprites.copy()
            temp_list.remove(item_list[0])
            temp_list.remove(item_list[1])
            temp_list.remove(item_list[2])
            SET_SPRITES.build_sprites = temp_list
            Ui.Say("小英：大木博士~~谢谢你的精灵球，我们不客气的收下了")
            SET_STATE.say_id = 3
    if event_id == 4:#初次胜利
        pygame.mixer.music.load("res/music/bgm/m4.mp3")
        pygame.mixer.music.play(-1, 0.0)
        Ui.Say("小轩：好了，到此为止了，我们的精灵还有很大的成长空间，没必要急于一时")
        SET_STATE.isAllowMove = False
        SET_STATE.say_id = 8
    if event_id == 5:#初次胜利2
        npc_list[1].move(1, 600)
        npc_list[2].move(1, 600)
        npc_list[3].move(1, 600)
        def f0():
            temp_list = SET_SPRITES.npc_sprites.copy()
            temp_list.remove(npc_list[1])
            temp_list.remove(npc_list[2])
            temp_list.remove(npc_list[3])
            SET_SPRITES.npc_sprites = temp_list
            npc_list[0].move(2, 150)
            threading.Timer(2, f1, ).start()
        threading.Timer(4.5, f0, ).start()
        def f1():
            Ui.Say("大木博士：你真的是个难得一遇的奇才，居然可以用人类的身躯战胜精灵，虽然那只是低级的精灵，如果你有兴趣开发潜力的话，可以来狮山镇找我")
            SET_STATE.say_id = 10
    if event_id == 6:#初次胜利3
        npc_list[0].move(1, 1200)
        def f0():
            temp_list = SET_SPRITES.npc_sprites.copy()
            temp_list.remove(npc_list[0])
            SET_SPRITES.npc_sprites = temp_list
            threading.Timer(2, f1, ).start()
        threading.Timer(5, f0, ).start()
        def f1():
            pygame.mixer.music.play(-1, 0.0)
            SET_STATE.isAllowMove = True
            SET_STATE.main_id = 2
            SET_STATE.say_id = -1
    if event_id == 7:#第二个草丛 遭遇怪物
        def f0():
            Controller.colliderDoorController()

        if SET_STATE.isMoving == True and SET_STATE.isAllowWildBattle == True:
            rd = random.randint(1, 10)  # 遇怪概率
            rdPK = random.randint(1,3)  # 遇怪种类概率
            if rd == 1:  # 1/10概率遇怪
                if rdPK == 1:
                    yb = Pokmen.Pokmen(7, 10, 3, 1, 5)
                    yb.addSkill(1)
                    yb.addSkill(6)
                    wild = Enemy.Enemy("野怪", 10)
                    wild.addPokmen(yb)
                elif rdPK == 2:
                    zs = Pokmen.Pokmen(12, 15, 4, 1, 5)
                    zs.addSkill(1)
                    zs.addSkill(5)
                    wild = Enemy.Enemy("野怪", 10)
                    wild.addPokmen(zs)
                elif rdPK == 3:
                    ho = Pokmen.Pokmen(10, 20, 3, 1, 7)
                    ho.addSkill(7)
                    wild = Enemy.Enemy("野怪", 15)
                    wild.addPokmen(ho)
                Battle.OpenBattle(3, wild)
                threading.Timer(0.1, f0, ).start()
            else:
                threading.Timer(0.1, f0, ).start()
        else:
            threading.Timer(0.1, f0, ).start()
    if event_id == 8:
        Ui.Say("小遥：你知道吗？四大家族最近正在举办一场比武招亲")
        SET_STATE.say_id = -1
    if event_id == 9:
        pygame.mixer.Sound("res/music/sound/s13.wav").play()
        Ui.Say("老中医：辛苦了孩子，老衲来帮你按摩放松肉体吧")
        SET_STATE.say_id = 12
    if event_id == 10:
        if SET_STATE.main_id == 2:
            if Player.level < 7:
                Ui.Say("大木博士：最近我们发现一种可以增强人体质的神奇石头，在使用这种石头之后人的体质可以极大的增强！")
                SET_STATE.say_id = 13
            else:
                Ui.Say("大木博士：最近我们发现一种可以增强人体质的神奇石头，在使用这种石头之后人的体质可以极大的增强！")
                SET_STATE.say_id = 14
        if SET_STATE.main_id == 3 or SET_STATE.main_id == 3.5:
            Ui.Say("大木博士：笔直穿过狮山镇就可以进入迷幻森林")
            SET_STATE.say_id = -1
    if event_id == 11:
        if SET_STATE.main_id == 2:
            Ui.Say("博士助手：让开让开，我忙得很！")
            SET_STATE.say_id = -1
        if SET_STATE.main_id == 3:
            Ui.Say("博士助手：这些药物给你，在迷幻森林里也许用得上！")
            SET_STATE.say_id = 15
        if SET_STATE.main_id == 3.5:
            Ui.Say("博士助手：据说迷幻森林里有人类可以学习秘籍")
            SET_STATE.say_id = -1
    if event_id == 12:#小豪初次战斗
        # 禁止移动
        SET_STATE.isAllowMove = False
        Ui.Say("小豪：这里是四大家族的领地，前方禁止通行！")
        SET_STATE.say_id = 16
    if event_id == 13:#战胜小豪
        Ui.Say("小豪：你是为数不多知道了秘密的人，在狮山镇的一个房子里，有一个秘密入口可以进入四大家族的领地，我在那里等着你！")
        SET_STATE.main_id = 4
        SET_STATE.isAllowMove = False
        SET_STATE.say_id = 11