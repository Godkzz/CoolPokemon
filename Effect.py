import pygame
import os
import SET_SPRITES
#技能特效类

skill_kv = {} #k=e? v=image_list

def init():
    for file in os.listdir('res/effect'):#技能特效根目录
        print(str(file))
        image_list = []  # 存储该技能所有帧
        for file2 in os.listdir('res/effect/'+str(file)):
            image_list.append(pygame.image.load('res/effect/' + str(file) + "/" + str(file2)))  # 加载该特效所有帧
            print(str(file2))
        skill_kv[file] = image_list


class Effect(pygame.sprite.Sprite):
    def __init__(self, eid ,x ,y):
        super().__init__()
        self.image_list = []# 存储所有帧
        self.image_index = 0  # 目前帧数
        self.eid = eid
        #for file in os.listdir('res/effect/e' + str(self.eid) + "/"):  # file 表示的是文件名
            #self.image_list.append(pygame.image.load('res/effect/e' + str(self.eid) + "/" + str(file)))  # 加载所有帧
            #self.image = self.image_list[0] #加载第一帧
        self.image_list = skill_kv["e"+str(self.eid)]
        self.image = self.image_list[0]  # 加载第一帧
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        SET_SPRITES.effect_sprites.add(self)
    def update(self):
        if self.image_index < len(self.image_list) - 1:
            self.image_index += 1
            self.image = self.image_list[self.image_index]  # 刷新帧
        else:
            self.kill()#删除特效

