import pygame
import Player
#记录精灵集合的模块
player = Player.Human(2)
player_sprites = pygame.sprite.Group()
build_sprites = pygame.sprite.Group() #地图物件
door_sprites = pygame.sprite.Group() #地图房子附属门 不在all之内
tile_sprites = pygame.sprite.Group() #地图纹理
map_sprites = pygame.sprite.Group() #地图集合
npc_sprites = pygame.sprite.Group() #npc集合
effect_sprites = pygame.sprite.Group() #特效集合 不在all之内