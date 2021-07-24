import pygame
import SET_SPRITES
import SET_STATE
import Player
import Npc
import time
import os
import Controller
import Event
image_build_list = []
image_build_length = len(os.listdir('res/map/build/')) #资源数量
image_tile_list = []
image_tile_length = len(os.listdir('res/map/tile/')) #资源数量
#把资源读取到内存
for i in range(image_build_length):  # file 表示的是文件名
    image_build_list.append(pygame.image.load('res/map/build/b' +str(i+1)+'.png'))  # 加载所有帧
for i in range(image_tile_length):  # file 表示的是文件名
    image_tile_list.append(pygame.image.load('res/map/tile/t' +str(i+1)+'.png'))  # 加载所有帧
class Map(pygame.sprite.Sprite):
    visible = True #可视
    def __init__(self):
        super().__init__()
#地图物件、房子类 静态图片
class Build(Map):
    def __init__(self, bid, x, y,name=""):
        super().__init__()
        self.bid = bid
        #加载物件资源
        self.image = image_build_list[self.bid - 1] # 加载建筑资源图片
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.name = name
        self.DX = 0
        self.DY = 0
    def update(self):
        if self.DX > Player.DX:
            self.DX -= Player.moveSpeed
            self.rect.x -= Player.moveSpeed
        elif self.DX < Player.DX:
            self.DX += Player.moveSpeed
            self.rect.x += Player.moveSpeed
        if self.DY < Player.DY:
            self.DY += Player.moveSpeed
            self.rect.y += Player.moveSpeed
        elif self.DY > Player.DY:
            self.DY -= Player.moveSpeed
            self.rect.y -= Player.moveSpeed
#地图纹理
class Tile(Map):
    def __init__(self, tid, x, y):
        super().__init__()
        self.tid = tid
        # 加载物件资源
        self.image = image_tile_list[tid - 1]  # 加载资源图片
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.DX = 0
        self.DY = 0
    def update(self):
        if self.DX > Player.DX:
            self.DX -= Player.moveSpeed
            self.rect.x -= Player.moveSpeed
        elif self.DX < Player.DX:
            self.DX += Player.moveSpeed
            self.rect.x += Player.moveSpeed
        if self.DY < Player.DY:
            self.DY += Player.moveSpeed
            self.rect.y += Player.moveSpeed
        elif self.DY > Player.DY:
            self.DY -= Player.moveSpeed
            self.rect.y -= Player.moveSpeed
#房子 继承BUILD 特有房门可进入
class House(Build):
    def __init__(self, bid, x, y,mid): #mid 房子的门进入的地图ID
        super().__init__(bid, x, y)
        if bid == 1:
            self.door = HouseDoor(mid,pygame.Rect(0, 0, 50, 60))
        if bid == 21:
            self.door = HouseDoor(mid, pygame.Rect(0, 0, 65, 75))
        if bid == 22:
            self.door = HouseDoor(mid, pygame.Rect(0, 0, 60, 60))
        if bid == 24:
            self.door = HouseDoor(mid, pygame.Rect(0, 0, 50, 75))
        if bid == 25:
            self.door = HouseDoor(mid, pygame.Rect(0, 0, 60, 60))
    def setDoor(self,rect_x,rect_y):
        self.door.set(rect_x,rect_y)
    def update(self):
        if self.DX > Player.DX:
            self.DX -= Player.moveSpeed
            self.rect.x -= Player.moveSpeed
        elif self.DX < Player.DX:
            self.DX += Player.moveSpeed
            self.rect.x += Player.moveSpeed
        if self.DY < Player.DY:
            self.DY += Player.moveSpeed
            self.rect.y += Player.moveSpeed
        elif self.DY > Player.DY:
            self.DY -= Player.moveSpeed
            self.rect.y -= Player.moveSpeed
        if self.bid == 1:
            self.setDoor(self.rect.x + 45, self.rect.y + 120)  # 设置门口矩阵
        if self.bid == 21:
            self.setDoor(self.rect.x + 55, self.rect.y + 150)  # 设置门口矩阵
        if self.bid == 22:
            self.setDoor(self.rect.x + 55, self.rect.y + 180)  # 设置门口矩阵
        if self.bid == 24:
            self.setDoor(self.rect.x + 55, self.rect.y + 150)  # 设置门口矩阵
        if self.bid == 25:
            self.setDoor(self.rect.x + 95, self.rect.y + 170)  # 设置门口矩阵
class HouseDoor(pygame.sprite.Sprite):
    def __init__(self,mid,rect):
        super().__init__()
        self.mid = mid #记录进入地图的ID
        self.rect = rect
        SET_SPRITES.door_sprites.add(self)
    def set(self,x,y):
        self.rect.x = x
        self.rect.y = y
    def open(self): #触发门 进入地图
        MapGroup(self.mid)
#出口点
class OutPonint(pygame.sprite.Sprite):
    def __init__(self, mid,x,y,wild=False):
        super().__init__()
        self.mid = mid
        self.image = image_build_list[17]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.wild = wild
        self.DX = 0
        self.DY = 0
        SET_SPRITES.door_sprites.add(self)
    def update(self):
        if self.DX > Player.DX:
            self.DX -= Player.moveSpeed
            self.rect.x -= Player.moveSpeed
        elif self.DX < Player.DX:
            self.DX += Player.moveSpeed
            self.rect.x += Player.moveSpeed
        if self.DY < Player.DY:
            self.DY += Player.moveSpeed
            self.rect.y += Player.moveSpeed
        elif self.DY > Player.DY:
            self.DY -= Player.moveSpeed
            self.rect.y -= Player.moveSpeed
    def open(self):  # 触发点 进入地图
        pre_map_id = SET_STATE.map_id #记录上一张地图ID
        MapGroup(self.mid)
        if self.mid == 1 and pre_map_id == 3: #从3进入1
            FixMap(-340, 1150)
            Player.face = 2
        if self.mid == 3 and pre_map_id == 4:
            FixMap(-550, 1550)
            Player.face = 0
        if self.mid == 3 and pre_map_id == 5:
            FixMap(390, 1430)
            Player.face = 0
        if self.mid == 3 and pre_map_id == 6:
            FixMap(390, 1920)
            Player.face = 0
        if self.mid == 3 and pre_map_id == 7:
            FixMap(-500, 2130)
            Player.face = 0
        if self.mid == 3 and pre_map_id == 8:
            FixMap(-80, 3350)
            Player.face = 0
#触发事件的点
class EventPoint(pygame.sprite.Sprite):
    def __init__(self, eid,x,y,wild=False):
        super().__init__()
        self.eid = eid
        self.image = image_build_list[17]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.DX = 0
        self.DY = 0
        self.wild = wild #是否为野怪草丛
        SET_SPRITES.door_sprites.add(self)
    def update(self):
        if self.DX > Player.DX:
            self.DX -= Player.moveSpeed
            self.rect.x -= Player.moveSpeed
        elif self.DX < Player.DX:
            self.DX += Player.moveSpeed
            self.rect.x += Player.moveSpeed
        if self.DY < Player.DY:
            self.DY += Player.moveSpeed
            self.rect.y += Player.moveSpeed
        elif self.DY > Player.DY:
            self.DY -= Player.moveSpeed
            self.rect.y -= Player.moveSpeed
    def open(self):  # 触发点 触发事件
        Event.trigger(self.eid)



        #触发事件
    #地图组 一个场景
class MapGroup(Map):
    def __init__(self, mid):
        super().__init__()
        self.mid = mid
        # 加载地图
        self.clear()#清除地图所有
        self.load(mid)
    def clear(self):
        SET_SPRITES.build_sprites = pygame.sprite.Group()
        SET_SPRITES.door_sprites = pygame.sprite.Group()
        SET_SPRITES.tile_sprites = pygame.sprite.Group()
        SET_SPRITES.npc_sprites = pygame.sprite.Group()
        SET_SPRITES.player_sprites = pygame.sprite.Group()
    def load(self, mid):
        print('load_mapGroup:'+str(mid))
        SET_STATE.map_id = mid
        #重新开启门触发器
        Controller.colliderDoorController()
        #初始化偏移
        Player.DX = 0
        Player.DY = 0
        if mid == 1:#主角家外
            # 加载音乐
            pygame.mixer.music.load("res/music/bgm/m3.mp3")
            pygame.mixer.music.play(-1, 0.0)
            #房子区纹理
            for i in range(15):
                for j in range(10):
                    SET_SPRITES.tile_sprites.add(Tile(7, i * 50+200, j * 70-130))
            for i in range(20):
                for j in range(10):
                    SET_SPRITES.tile_sprites.add(Tile(7, i * 95+200, -95 - j * 90-130))
            for i in range(20):
                for j in range(10):
                    SET_SPRITES.tile_sprites.add(Tile(7, -90-i * 95+200, -95 - j * 90-130))
            for i in range(30):
                SET_SPRITES.tile_sprites.add(Tile(7, i * 60+200, 680-130))
            for i in range(15):
                SET_SPRITES.tile_sprites.add(Tile(7, -i * 60+200, 0-130))
            SET_SPRITES.tile_sprites.add(Tile(1, 380+200, 470-130))
            #结束树
            SET_SPRITES.build_sprites.add(Build(6, 1955 - 15 * 75, -1090 + 350))
            SET_SPRITES.build_sprites.add(Build(6, 1955 - 15 * 75, -1090 + 400))
            #树前纹理
            SET_SPRITES.tile_sprites.add(Tile(3, 1985 - 15 * 75, -955 + 70*2))
            SET_SPRITES.tile_sprites.add(Tile(3, 1985 - 15 * 75+92, -955 + 70 * 2))
            SET_SPRITES.tile_sprites.add(Tile(3, 1985 - 15 * 75 + 92*2, -955 + 70 * 2))
            #草
            for i in range(10):
                for j in range(4):
                    SET_SPRITES.tile_sprites.add(Tile(9, 800+i * 38+200, -170 + j * 38-130))
                    # 剧情触发点
                    EventPoint(1, 800 + i * 38 + 200, -160 + j * 10 - 130,True)

            for i in range(10):
                for j in range(4):
                    SET_SPRITES.tile_sprites.add(Tile(9, 1360+i * 38, -915+ j * 38))
                    EventPoint(7, 1363 + i * 33, -925 + j * 5,True)#遇怪触发点
            OutPonint(3, 803, -825)#出口点
            SET_SPRITES.player = Player.Human(2)  # 创建玩家角色
            #树木
            for i in range(20):
                SET_SPRITES.build_sprites.add(Build(6, -100+i*80+200, -480-130))
                SET_SPRITES.build_sprites.add(Build(6, -100+i*80+200, -380-130))
                SET_SPRITES.build_sprites.add(Build(6, -100+i*80+200, -280-130))
                SET_SPRITES.build_sprites.add(Build(6, -100+200, -180-130))
                SET_SPRITES.build_sprites.add(Build(6, -100+200, -100-130))
                SET_SPRITES.build_sprites.add(Build(6, 2030, -1090 + i * 70))#右上角向下树木
            for i in range(30):  # 右上角向左树木
                SET_SPRITES.build_sprites.add(Build(6, 1955 - i * 75, -1090))
                SET_SPRITES.build_sprites.add(Build(6, 1955 - i * 75, -1090+70))
            #结束树
            SET_SPRITES.build_sprites.add(Build(6, 1955 - 15 * 75, -1090 + 110))
            SET_SPRITES.build_sprites.add(Build(6, 1955 - 15 * 75, -1090 + 150))
            #水槽
            SET_SPRITES.build_sprites.add(Build(7, 200+200, 500-130))
            #围栏
            SET_SPRITES.build_sprites.add(Build(5, 500+200, 500-130))
            SET_SPRITES.build_sprites.add(Build(5, 532+200, 500-130))
            SET_SPRITES.build_sprites.add(Build(5, 564+200, 500-130))
            SET_SPRITES.build_sprites.add(Build(3, 580+200, 450-130))
            SET_SPRITES.build_sprites.add(Build(3, 580+200, 378-130))
            SET_SPRITES.build_sprites.add(Build(3, 580+200, 306-130))
            #花
            SET_SPRITES.tile_sprites.add(Tile(10, 700+200, 500-130))
            SET_SPRITES.tile_sprites.add(Tile(10, 400+200, 200-130))
            #房子
            SET_SPRITES.build_sprites.add(House(1, 350+200, 300-130,2))
            #树木
            for i in range(15):
                for j in range(10):
                    SET_SPRITES.build_sprites.add(Build(6, 780 + i * 75+200, -31+j * 69-130))
            for i in range(15):
                for j in range(10):
                    SET_SPRITES.build_sprites.add(Build(6, -70- i * 75+200, j * 70-130))
            for i in range(30):
                for j in range(10):
                    SET_SPRITES.build_sprites.add(Build(6, -600+i * 75+200, 700+j * 70-130))

        if mid == 2:#主角家
            #地板
            for i in range(20):
                for j in range(15):
                    SET_SPRITES.tile_sprites.add(Tile(11, 280+i * 32, -80+j * 32))
            #墙
            for i in range(13):
                SET_SPRITES.build_sprites.add(Build(10, 280 + 46 * i, -80 - 95))
            SET_SPRITES.build_sprites.add(Build(10, 275 + 46 * 13, -80 - 95))
            #地毯
            SET_SPRITES.tile_sprites.add(Tile(15, 560, 350))
            SET_SPRITES.player = Player.Human(2)  # 创建玩家角色
            #墙挂饰
            SET_SPRITES.build_sprites.add(Build(11, 350, -150))
            SET_SPRITES.build_sprites.add(Build(12, 750, -145))
            #桌子
            SET_SPRITES.build_sprites.add(Build(14, 370, 10))
            #凳子
            SET_SPRITES.build_sprites.add(Build(15, 310, 10))
            #黑色阻挡物
            for i in range(9):
                if i == 4:
                    # 出口
                    OutPonint(1, 250 + i * 81, 410)
                else:
                    SET_SPRITES.build_sprites.add(Build(16, 250 + i * 81, 410))
            for i in range(7):
                SET_SPRITES.build_sprites.add(Build(16, 180, -100+i*78))
                SET_SPRITES.build_sprites.add(Build(16, 930, -100 + i * 78))
            #柜子
            SET_SPRITES.build_sprites.add(Build(17, 500, -120))
            #床
            SET_SPRITES.build_sprites.add(Build(18, 730, -100))
            #花盆
            SET_SPRITES.build_sprites.add(Build(19, 830, -100))
            SET_SPRITES.build_sprites.add(Build(19, 870, -100))
            #力量之石
            if SET_STATE.homeStone == True:
                SET_SPRITES.build_sprites.add(Build(2, 870, 200,"攻击之石-家"))
            Player.face = 3
        if mid == 3:#狮山镇
            Player.face = 3
            #纹理
            for i in range(30):
                for j in range(50):
                    SET_SPRITES.tile_sprites.add(Tile(7, i * 50-80, j * 70-3050))
            SET_SPRITES.tile_sprites.add(Tile(3, 510, 360))
            SET_SPRITES.tile_sprites.add(Tile(3, 610, 360))
            SET_SPRITES.tile_sprites.add(Tile(3, 710, 360))
            SET_SPRITES.tile_sprites.add(Tile(10, 710, -100))
            SET_SPRITES.tile_sprites.add(Tile(10, 630, -300))
            #城镇前纹理
            for i in range(4):
                for j in range(25):
                    SET_SPRITES.tile_sprites.add(Tile(2, 510 + i * 85, -800 - j * 80))
            #花坛
            SET_SPRITES.build_sprites.add(Build(23, 610, -1600))
            # 迷幻树木
            for i in range(13):
                if i == 5 or i == 6 or i == 7:#出口
                    SET_SPRITES.tile_sprites.add(Tile(23, 120 + 90 * i, -3050))
                    OutPonint(8, 120 + 90 * i, -3150)
                else:
                    SET_SPRITES.build_sprites.add(Build(29, 70 + 100 * i, -3100))


            #下面树木
            for i in range(10):
                if i == 4 or i == 5:
                    pass#入口点
                else:
                    SET_SPRITES.build_sprites.add(Build(20, -100 + i * 150, 300))
            OutPonint(1, 500, 500)
            OutPonint(1, 600, 500)
            OutPonint(1, 700, 500)
            # 围栏
            for j in range(31):
                SET_SPRITES.build_sprites.add(Build(3, 20, -810 - j * 75))
                SET_SPRITES.build_sprites.add(Build(3, 1400, -810 - j * 75))
            #房子
            SET_SPRITES.build_sprites.add(House(21, 150, -1310,5))
            SET_SPRITES.build_sprites.add(House(22, 150, -1810,6))
            SET_SPRITES.build_sprites.add(House(25, 1050, -1430,4))
            SET_SPRITES.build_sprites.add(House(24, 1050, -2010,7))
            #指示牌
            tip = Build(4, 1000, -1050)
            tip.name = "狮山指示牌"
            SET_SPRITES.build_sprites.add(tip)
            #房子底下纹理
            for i in range(5):
                for j in range(25):
                    SET_SPRITES.tile_sprites.add(Tile(4, 50 + i * 86 , -850 - j * 86))
                    SET_SPRITES.tile_sprites.add(Tile(4, 920 + i * 86, -850 - j * 86))
            #两侧树木
            for i in range(4):
                for j in range(7):
                    SET_SPRITES.build_sprites.add(Build(20, -100 + i * 150, -800 + j * 150))
                    SET_SPRITES.build_sprites.add(Build(20, 800 + i * 150, -800 + j * 150))
        if mid == 4:#小精灵治疗房
            Player.face = 3
            SET_SPRITES.tile_sprites.add(Tile(17, 260, 0))
            #阻挡物
            #电梯
            SET_SPRITES.build_sprites.add(Build(16, 270, 250))
            #左上
            SET_SPRITES.build_sprites.add(Build(16, 294, 10))
            SET_SPRITES.build_sprites.add(Build(16, 375, 10))
            #右上
            SET_SPRITES.build_sprites.add(Build(16, 774, 10))
            SET_SPRITES.build_sprites.add(Build(16, 855, 10))
            #左边
            for i in range(5):
                SET_SPRITES.build_sprites.add(Build(16, 203, 10 + i*78))
            SET_SPRITES.build_sprites.add(Build(16, 223, 382))
            #右边
            for i in range(5):
                SET_SPRITES.build_sprites.add(Build(16, 943, 10 + i*78))
            #下面
            for i in range(8):
                if i == 3 or i == 4:
                    OutPonint(3,283 + i * 81, 410)#出口
                else:
                    SET_SPRITES.build_sprites.add(Build(16, 283 + i * 81, 410))
            SET_SPRITES.build_sprites.add(Build(16, 775, 280))
            #前台
            SET_SPRITES.build_sprites.add(Build(16, 470, 70))
            talk = Build(16, 551, 70)
            talk.name = "精灵所治疗"
            SET_SPRITES.build_sprites.add(talk)
            SET_SPRITES.build_sprites.add(Build(16, 632, 70))
            SET_SPRITES.build_sprites.add(Build(16, 673, 70))
            #NPC
            n1 = Npc.Human(14,"小遥",8)
            n1.rect.x = 850
            n1.rect.y = 100
        if mid == 5:#按摩馆
            #地板
            for i in range(20):
                for j in range(15):
                    SET_SPRITES.tile_sprites.add(Tile(11, 280+i * 32, -80+j * 32))
            #墙
            for i in range(13):
                SET_SPRITES.build_sprites.add(Build(10, 280 + 46 * i, -80 - 95))
            SET_SPRITES.build_sprites.add(Build(10, 275 + 46 * 13, -80 - 95))
            #地毯
            SET_SPRITES.tile_sprites.add(Tile(18, 560, 350))
            SET_SPRITES.player = Player.Human(2)  # 创建玩家角色
            #墙挂饰
            SET_SPRITES.build_sprites.add(Build(11, 550, -150))
            #黑色阻挡物
            for i in range(9):
                if i == 4:
                    # 出口
                    OutPonint(3, 250 + i * 81, 410)
                else:
                    SET_SPRITES.build_sprites.add(Build(16, 250 + i * 81, 410))
            for i in range(7):
                SET_SPRITES.build_sprites.add(Build(16, 180, -100+i*78))
                SET_SPRITES.build_sprites.add(Build(16, 930, -100 + i * 78))
            #货物
            SET_SPRITES.build_sprites.add(Build(26, 730, -120))
            SET_SPRITES.build_sprites.add(Build(26, 780, -120))
            SET_SPRITES.build_sprites.add(Build(26, 830, -120))
            #凳子
            SET_SPRITES.build_sprites.add(Build(27, 830, 40))
            #洗手池
            SET_SPRITES.build_sprites.add(Build(28, 330, -130))
            n1 = Npc.Human(15,"老中医",9)
            n1.rect.x = 760
            n1.rect.y = 40
            Player.face = 3
        if mid == 6:#博士研究所
            Player.face = 3
            SET_SPRITES.tile_sprites.add(Tile(19, 320, -185))
            #NPC
            n1 = Npc.Human(13,"大木博士",10)
            n1.rect.x = 550
            n1.rect.y = -50
            n2 = Npc.Human(10, "博士助手", 11)
            n2.random_face = True
            n2.rect.x = 800
            n2.rect.y = 240
            #阻挡物
            #左边
            SET_SPRITES.build_sprites.add(Build(16, 270, 330))
            for i in range(6):
                SET_SPRITES.build_sprites.add(Build(16, 230, 330-i*78))
            #右边
            SET_SPRITES.build_sprites.add(Build(16, 880, 330))
            for i in range(6):
                SET_SPRITES.build_sprites.add(Build(16, 920, 330-i*78))
            #上面
            for i in range(8):
                SET_SPRITES.build_sprites.add(Build(16, 300 + i*81, -200))
            #左柜子
            SET_SPRITES.build_sprites.add(Build(16, 300, 160))
            SET_SPRITES.build_sprites.add(Build(16, 381, 160))
            SET_SPRITES.build_sprites.add(Build(16, 462, 160))
            #右柜子
            SET_SPRITES.build_sprites.add(Build(16, 685, 160))
            SET_SPRITES.build_sprites.add(Build(16, 766, 160))
            SET_SPRITES.build_sprites.add(Build(16, 847, 160))
            #桌子
            SET_SPRITES.build_sprites.add(Build(16, 685, 0))
            SET_SPRITES.build_sprites.add(Build(16, 730, 0))
            #左边物品
            SET_SPRITES.build_sprites.add(Build(16, 380, 0))
            SET_SPRITES.build_sprites.add(Build(16, 280, -20))
            SET_SPRITES.build_sprites.add(Build(16, 280, -80))
            #下面
            for i in range(9):
                if i == 4 or i == 5:#出口
                    OutPonint(3,230 + i*81, 420)
                else:
                    SET_SPRITES.build_sprites.add(Build(16, 230 + i * 81, 420))
        if mid == 7:#基地
            #地板
            for i in range(20):
                for j in range(15):
                    SET_SPRITES.tile_sprites.add(Tile(20, 280+i * 32, -80+j * 32))
            #墙
            for i in range(13):
                SET_SPRITES.build_sprites.add(Build(30, 280 + 46 * i, -80 - 95))
            SET_SPRITES.build_sprites.add(Build(30, 275 + 46 * 13, -80 - 95))
            #地毯
            SET_SPRITES.tile_sprites.add(Tile(21, 560, 350))
            SET_SPRITES.player = Player.Human(2)  # 创建玩家角色
            #墙挂饰
            SET_SPRITES.build_sprites.add(Build(11, 800, -150))
            #黑色阻挡物
            for i in range(9):
                if i == 4:
                    # 出口
                    OutPonint(3, 250 + i * 81, 410)
                else:
                    SET_SPRITES.build_sprites.add(Build(16, 250 + i * 81, 410))
            for i in range(7):
                SET_SPRITES.build_sprites.add(Build(16, 180, -100+i*78))
                SET_SPRITES.build_sprites.add(Build(16, 930, -100 + i * 78))
            for i in range(14):
                for j in range(6):
                    n1 = Npc.Human(8, "保安", -1)
                    n1.rect.x = 280 + i * 46
                    n1.rect.y = -110 + j * 55
                    Player.face = 3
        if mid == 8:#迷幻森林
            Player.face = 2
            #剧情挡路树木
            if SET_STATE.main_id < 3:
                SET_SPRITES.build_sprites.add(Build(29, 770, 330))
            #入口
            OutPonint(3, 485, 350)
            #树木
            for i in range(12):
                SET_SPRITES.build_sprites.add(Build(29, 570 + 77 * i, 240))
                SET_SPRITES.build_sprites.add(Build(29, 570+ 77 * i, 430))
            SET_SPRITES.build_sprites.add(Build(29, 1648, 337))
            SET_SPRITES.build_sprites.add(Build(29, 1571, 337))
            SET_SPRITES.build_sprites.add(Build(29, 1499, 404))
            for i in range(16):
                SET_SPRITES.build_sprites.add(Build(29, 1418, 140 - 107 * i))
                SET_SPRITES.build_sprites.add(Build(29, 1648, 240- 107*i))
            #纹理
            for i in range(20):
                if i < 10:
                    SET_SPRITES.tile_sprites.add(Tile(23, 560 + i * 96, 350 - 96))
                    SET_SPRITES.tile_sprites.add(Tile(23, 560 + i * 96, 350))
                    SET_SPRITES.tile_sprites.add(Tile(23, 560 + i * 96, 350 + 96))
                if i < 20:
                    SET_SPRITES.tile_sprites.add(Tile(23, 560+ 9 * 96, 350- 96* i))
                    SET_SPRITES.tile_sprites.add(Tile(23, 560 + 10 * 96, 350- 96* i))
                    SET_SPRITES.tile_sprites.add(Tile(23, 560 + 11 * 96, 350- 96* i))
            #草
            for i in range(7):
                SET_SPRITES.tile_sprites.add(Tile(24, 1060 + 38 * i, 360))
                SET_SPRITES.tile_sprites.add(Tile(24, 1060+ 38 * i, 360 + 38))
            for i in range(6):
                for j in range(9):
                    SET_SPRITES.tile_sprites.add(Tile(24, 1448 + 38 * i, -202 + j * 38))
            #血
            SET_SPRITES.tile_sprites.add(Tile(22, 1548, -402))

            #属性石头
            ball1 = Build(2, 1448, 380)
            ball1.name = "防御之石"
            SET_SPRITES.build_sprites.add(ball1)
            ball2 = Build(2, 1548, -180)
            ball2.name = "攻击之石"
            SET_SPRITES.build_sprites.add(ball2)
            #剧情触发点
            if SET_STATE.main_id == 3 or SET_STATE.main_id == 3.5:
                EventPoint(12, 1528, -400)  # 触发点
                # NPC
                hao = Npc.Human(3, "小豪", -1)
                hao.rect.x = 1548
                hao.rect.y = -492
            #树木
            SET_SPRITES.build_sprites.add(Build(29, 1498, -1480))
            SET_SPRITES.build_sprites.add(Build(29, 1566, -1480))
            skillball = Build(2, 1566, -1350)
            skillball.name = "与鬼同行-球"
            SET_SPRITES.build_sprites.add(skillball)
            SET_SPRITES.build_sprites.add(Build(29, 1644, -1480))
        #存入精灵集合
        SET_SPRITES.player_sprites.add(SET_SPRITES.player)  # 主角必须最后一个加载 在图层最上方
        SET_STATE.isInMaping = True
        SET_STATE.isAllowMove = True


def FixMap(x,y):
    for item in SET_SPRITES.build_sprites:
        item.rect.x += x
        item.rect.y += y
    for item in SET_SPRITES.tile_sprites:
        item.rect.x += x
        item.rect.y += y
    for item in SET_SPRITES.door_sprites:
        item.rect.x += x
        item.rect.y += y
    for item in SET_SPRITES.npc_sprites:
        item.rect.x += x
        item.rect.y += y