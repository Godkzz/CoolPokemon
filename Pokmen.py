import pygame
import PokmenFactory



class Pokmen(pygame.sprite.Sprite):
    def __init__(self, pid , hp, attack, defense, level):
        super().__init__()
        self.name = "pokmen"
        self.skill_list = []
        self.pid = pid
        self.hp = hp
        self.hp_max = hp
        self.hp_per = 1
        self.attack = attack
        self.defense = defense
        self.level = level
        self.image_real = pygame.image.load('res/pokmen/p' + str(self.pid) + '.png')  # 加载资源图片
        self.rect = self.image_real.get_rect()
        self.img_real_width = self.rect.width #正常显示时的的宽度，高度
        self.img_real_height = self.rect.height
        self.img_width = 0 #精灵弹出效果
        self.img_height = 0
        self.image = pygame.transform.scale(self.image_real,(self.img_width,self.img_height))
        self.name = PokmenFactory.getPokmenInfo(pid).name
    def addSkill(self,skill_id):
        if len(self.skill_list) < 4 :
            self.skill_list.append(skill_id)#存放技能 最多4个
        else:
            print(self.name+":宝可梦精灵已满4个，无法继续添加")
    def update(self):
        pokmen_show_speed = 8 #精灵出场动画的速度
        if self.img_width < self.img_real_width:
            self.img_width += pokmen_show_speed
        else:
            self.img_width = self.img_real_width
        if self.img_height < self.img_real_height:
            self.img_height += pokmen_show_speed
        else:
            self.img_height = self.img_real_height
        self.image = pygame.transform.scale(self.image_real, (self.img_width, self.img_height))

