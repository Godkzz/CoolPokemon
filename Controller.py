import pygame
import threading
import time
import SET_SPRITES
import SET_STATE
import Player
import Ui
import Bag

def map_move(x, y):  # 移动整个地图块
    for item in SET_SPRITES.npc_sprites:  # 遍历所有npc
        item.rect.x += x
        item.rect.y += y
def moveController(): #移动线程
    if SET_STATE.isInMaping == True and SET_STATE.isAllowMove == True:
        key_pressed = pygame.key.get_pressed()
        # 键盘移动事件
        if key_pressed[pygame.K_LEFT]:
            SET_SPRITES.player.move(1)
        elif key_pressed[pygame.K_RIGHT]:
            SET_SPRITES.player.move(2)
        elif key_pressed[pygame.K_DOWN]:
            SET_SPRITES.player.move(0)
        elif key_pressed[pygame.K_UP]:
            SET_SPRITES.player.move(3)
    threading.Timer(0.07, moveController, ).start()



# 碰撞事件
def collideController():
    if SET_STATE.isInMaping == True:
        collide_list = pygame.sprite.spritecollide(SET_SPRITES.player, SET_SPRITES.build_sprites, False)  # 玩家与地图物件
        if collide_list != []:
            if collide_list[0].name == "小火龙精灵球":
                Ui.Select(3)
                Ui.Say("确定要选择小火龙吗？")
            if collide_list[0].name == "杰尼龟精灵球":
                Ui.Select(3)
                Ui.Say("确定要选择杰尼龟吗？")
            if collide_list[0].name == "皮卡丘精灵球":
                Ui.Select(3)
                Ui.Say("确定要选择皮卡丘吗？")
            if collide_list[0].name == "狮山指示牌":
                Ui.Say("狮山镇")
                SET_STATE.say_id = -1
            if collide_list[0].name == "精灵所治疗":
                Ui.Say("护士小姐：对不起，我们这里无法帮助人类治疗伤口疾病")
                SET_STATE.say_id = -1
            if collide_list[0].name == "攻击之石-家":
                pygame.mixer.Sound("res/music/sound/s12.wav").play()
                Ui.Say("获得攻击之石")
                SET_STATE.say_id = -1
                Bag.addBag(2,1)
                SET_STATE.homeStone = False
                temp_list = SET_SPRITES.build_sprites.copy()
                temp_list.remove(collide_list[0])
                SET_SPRITES.build_sprites = temp_list
            if collide_list[0].name == "攻击之石":
                pygame.mixer.Sound("res/music/sound/s12.wav").play()
                Ui.Say("获得攻击之石")
                SET_STATE.say_id = -1
                Bag.addBag(2,1)
                temp_list = SET_SPRITES.build_sprites.copy()
                temp_list.remove(collide_list[0])
                SET_SPRITES.build_sprites = temp_list
            if collide_list[0].name == "防御之石":
                pygame.mixer.Sound("res/music/sound/s12.wav").play()
                Ui.Say("获得防御之石")
                SET_STATE.say_id = -1
                Bag.addBag(3,1)
                temp_list = SET_SPRITES.build_sprites.copy()
                temp_list.remove(collide_list[0])
                SET_SPRITES.build_sprites = temp_list
            if collide_list[0].name == "与鬼同行-球":
                pygame.mixer.Sound("res/music/sound/s12.wav").play()
                Ui.Say("获得秘籍-与鬼同行！")
                SET_STATE.say_id = -1
                Bag.addBag(12,1)
                temp_list = SET_SPRITES.build_sprites.copy()
                temp_list.remove(collide_list[0])
                SET_SPRITES.build_sprites = temp_list

            if Player.face == 1:
                Player.DX -= Player.moveSpeed
            if Player.face == 2:
                Player.DX += Player.moveSpeed
            if Player.face == 0:
                Player.DY += Player.moveSpeed
            if Player.face == 3:
                Player.DY -= Player.moveSpeed
    threading.Timer(0.02, collideController, ).start()


#房屋门口碰撞事件
def colliderDoorController():# 开启房子门线程
    if SET_STATE.isInMaping == True:
        collide_list = pygame.sprite.spritecollide(SET_SPRITES.player, SET_SPRITES.door_sprites, False)  # 玩家与房子的门
        if collide_list != []:  # 与门碰撞
            collide_list[0].open()
            if collide_list[0].wild == False:
                temp_list = SET_SPRITES.door_sprites.copy()
                temp_list.remove(collide_list[0])
                SET_SPRITES.door_sprites = temp_list

        else:
            threading.Timer(0.07, colliderDoorController, ).start()
    else:
        threading.Timer(0.07, colliderDoorController, ).start()


#npc碰撞事件
def colliderNpcController():
    if SET_STATE.isInMaping == True:
        collide_list = pygame.sprite.spritecollide(SET_SPRITES.player, SET_SPRITES.npc_sprites, False)  # 玩家与房子的门
        if collide_list != []:
            SET_STATE.isCollNpc = True
            SET_STATE.collNpcId = collide_list[0].evenid
        else:
            SET_STATE.isCollNpc = False
            SET_STATE.collNpcId = 0
    threading.Timer(0.07, colliderNpcController, ).start()
def init():
    moveController()  # 开启碰撞线程
    collideController()  # 开启移动按键线程
    colliderNpcController()

