import pygame
import time
import threading
import Player
import SET_SPRITES
import random
class Human(pygame.sprite.Sprite):

    def __init__(self, hid ,name, evenid):
        super().__init__()
        self.hid = hid
        self.humanRes = []
        self.face = 0  # 人物面向 0=下 1=左 2=右 3=上
        self.moveflag = 0  # 移动的状态
        self.moveSpeed = 10  # 移动速度 默认10
        self.name = name
        self.evenid = evenid
        self.spiltHuman()
        self.DX = 0
        self.DY = 0
        self.random_face = False #控制是否随机面向
        self.rd_face_number = 0 #随机面向间隔索引
        self.image = self.humanRes[0 + self.moveflag]
        SET_SPRITES.npc_sprites.add(self)
    def spiltHuman(self):
        # 单个人物模块的宽度和高度
        HUMAN_W = 39
        HUMAN_H = 52
        # 记录分割时的行索引和列索引
        w_index = 0
        h_index = 0
        HUMAN_IMAGE = pygame.image.load('res/human/h' + str(self.hid) + '.png')  # 加载人物资源图片
        # 设置角色矩阵坐标
        self.rect = HUMAN_IMAGE.get_rect()
        self.rect.x = 600
        self.rect.y = 350
        self.rect.w = HUMAN_W
        self.rect.h = HUMAN_H

        for (h_index) in (0, 1, 2, 3):
            for (w_index) in (0, 1, 2, 3):
                spilt_rect = pygame.Rect(HUMAN_W * w_index, HUMAN_H * h_index, HUMAN_W, HUMAN_H)  # 分割矩阵
                spilt_human = HUMAN_IMAGE.subsurface(spilt_rect)
                self.humanRes.append(spilt_human)
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

        if self.random_face == True:
            self.rd_face_number += 1
            if self.rd_face_number >= 100: #随机面向的速度
                self.face = random.randint(0, 3)
                self.rd_face_number = 0



        if self.face == 0:
            self.image = self.humanRes[0 + self.moveflag]
        if self.face == 1:
            self.image = self.humanRes[4 + self.moveflag]
        if self.face == 2:
            self.image = self.humanRes[8 + self.moveflag]
        if self.face == 3:
            self.image = self.humanRes[12 + self.moveflag]

    def move(self, face, distance):
        self.face = face
        delay = 0.04 #触发移动间隔
        if distance > 0:
            if(self.face == 2):
                self.rect.x += self.moveSpeed
            if (self.face == 1):
                self.rect.x -= self.moveSpeed
            if(self.face == 0):
                self.rect.y += self.moveSpeed
            if (self.face == 3):
                self.rect.y -= self.moveSpeed
            distance -= self.moveSpeed
            if self.moveflag >= 3:
                self.moveflag = 0
            else:
                self.moveflag += 1
            timethread = threading.Timer(delay, self.move,[face,distance])  # npc移动回调线程
            timethread.start()
        else:
            self.moveflag = 0 #变成静止动作

