import pygame
import SET_STATE

#基础属性
name = "小松"
global hp
global hp_max
global exp
global exp_max
global level
global attack
global defense
hp = 10
hp_max = 10
exp = 6
exp_max = 100 #所需升级经验
level = 1
attack = 3 #初始值3
defense = 3 #防御
money = 0 #金钱
hp_per = 0 #血量百分比
exp_per = 0  #经验百分比
skill_1 = 4 #技能对应技能ID 0 = 无
skill_2 = 3 #技能对应技能ID 0 = 无
skill_3 = 8 #技能对应技能ID 0 = 无
skill_4 = 9 #技能对应技能ID 0 = 无
skill_pp_1 = 10 #对应技能剩下的PP数值
skill_pp_2 = 10 #对应技能剩下的PP数值
skill_pp_3 = 10 #对应技能剩下的PP数值
skill_pp_4 = 10 #对应技能剩下的PP数值
#移动
global face
global DX
global DY
global moveSpeed
DX = 0
DY = 0
face = 0  # 人物面3向 0=下 1=左 2=右 3=上
moveSpeed = 20 #移动速度 默认20
class Human(pygame.sprite.Sprite):
    humanRes = []

    moveflag = 0 #移动的状态

    def __init__(self, hid):
        super().__init__()
        self.hid = hid
        self.spiltHuman()
        self.image = self.humanRes[0 + self.moveflag]
    def spiltHuman(self):
        #单个人物模块的宽度和高度
        HUMAN_W = 39
        HUMAN_H = 52
        #记录分割时的行索引和列索引
        w_index = 0
        h_index = 0
        HUMAN_IMAGE = pygame.image.load('res/human/h'+str(self.hid)+'.png')# 加载人物资源图片
        # 设置角色矩阵坐标
        self.rect = HUMAN_IMAGE.get_rect()
        self.rect.x = 600
        self.rect.y = 350
        self.rect.w = HUMAN_W
        self.rect.h = HUMAN_H

        for (h_index) in (0,1,2,3):
            for (w_index) in (0, 1, 2, 3):
                spilt_rect = pygame.Rect(HUMAN_W * w_index, HUMAN_H * h_index, HUMAN_W, HUMAN_H)  # 分割矩阵
                spilt_human = HUMAN_IMAGE.subsurface(spilt_rect)
                self.humanRes.append(spilt_human)
    def update(self):
        global face
        if face == 0:
            self.image = self.humanRes[0 + self.moveflag]
        if face == 1:
            self.image = self.humanRes[4 + self.moveflag]
        if face == 2:
            self.image = self.humanRes[8 + self.moveflag]
        if face == 3:
            self.image = self.humanRes[12 + self.moveflag]

    def move(self, myface):
        global face
        global DX
        global DY
        SET_STATE.isMoving =True
        face = myface
        if face == 0:
            DY -= moveSpeed
        if face == 3:
            DY += moveSpeed
        if face == 1:
            DX += moveSpeed
        if face == 2:
            DX -= moveSpeed
        if self.moveflag >= 3:
            self.moveflag = 0
        else:
            self.moveflag += 1

def ExpUpdate():
    global hp
    global hp_max
    global exp
    global exp_max
    global level
    global attack
    global defense
    if exp >= exp_max:  # 升级
        exp_max *= 2  # 每级经验是之前的两倍
        exp = 0  # 升级后经验值归0
        level += 1
        hp += 10
        hp_max += 10
        attack += 1
        defense += 1










