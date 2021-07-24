import pygame
import sys
import os
import Player
import Map
import time
import threading
import SET_SPRITES
import SET_STATE
import Controller
import Ui
import Battle
import Enemy
import Pokmen
import Skill
import Effect
import PokmenFactory
import Event
import ItemFactory
import Bag
# 初始化pygame
pygame.init()
SCREEN_SIZE = (width, height) = (1200, 700)  # 设置窗口大小
os.environ['SDL_VIDEO_CENTERED'] = '1' #居中显示
screen = pygame.display.set_mode(SCREEN_SIZE)  # 显示窗口

PokmenFactory.init()
ItemFactory.init()
Controller.init()
Skill.init()
Effect.init()
#加载地图
Player.level = 1
SET_STATE.main_id = 0
Map.MapGroup(1)

for i in range(11):
    Bag.addBag(i+1, 3)
while True:  # 死循环确保窗口一直显示
    screen.fill((0, 0, 0))  # 清空背景
    if SET_STATE.isInMaping == True:#绘制更新地图
        SET_SPRITES.door_sprites.update()
        SET_SPRITES.build_sprites.update()
        SET_SPRITES.tile_sprites.update()
        SET_SPRITES.npc_sprites.update()
        SET_SPRITES.player_sprites.update()
        SET_SPRITES.tile_sprites.draw(screen)
        SET_SPRITES.build_sprites.draw(screen)
        SET_SPRITES.npc_sprites.draw(screen)
        SET_SPRITES.player_sprites.draw(screen)

    #黑色块可视化
    #for item in SET_SPRITES.door_sprites:
        #pygame.draw.rect(screen,(0,0,0),item.rect)
    if SET_STATE.isInMenu == True:#菜单栏
        screen.blit(Ui.UiMenu, (900, 30))
        if SET_STATE.menu == 1:
            screen.blit(Ui.UiChooseBtnImage, (935, 65))
        if SET_STATE.menu == 2:
            screen.blit(Ui.UiChooseBtnImage, (935, 130))
        if SET_STATE.menu == 3:
            screen.blit(Ui.UiChooseBtnImage, (935, 195))
        if SET_STATE.menu == 4:
            screen.blit(Ui.UiChooseBtnImage, (935, 260))
    if SET_STATE.isInBag == True:
        screen.blit(Ui.UiBag, (0, 0))
        screen.blit(Ui.info_fmt_money, (180, 540))
        for i in range(len(Bag.bag_list)):
            if i < 9:#最多显示八个
                screen.blit(Ui.bag_fmt[i], (650, 90 + 60 * i))
        if SET_STATE.bag_select_id >=0:
            screen.blit(Ui.UiChooseBtnImage, (600, 85 + 60 * SET_STATE.bag_select_id))  # 选择光标


    if SET_STATE.isInInfo == True:
        screen.blit(Ui.UiInfoHuman, (0, 0))
        screen.blit(Ui.info_fmt_level, (80, 460))
        screen.blit(Ui.info_fmt_name, (210, 462))
        screen.blit(Ui.info_fmt_hp, (680, 262))
        screen.blit(Ui.info_fmt_attack, (680, 332))
        screen.blit(Ui.info_fmt_defense, (680, 402))
        screen.blit(Ui.info_fmt_exp, (920, 530))
        screen.blit(Ui.info_fmt_skill_name1, (910, 250))
        screen.blit(Ui.info_fmt_skill_name2, (910, 300))
        screen.blit(Ui.info_fmt_skill_name3, (910, 350))
        screen.blit(Ui.info_fmt_skill_name4, (910, 400))
        screen.blit(Ui.info_fmt_skill_pp1, (1050, 250))
        screen.blit(Ui.info_fmt_skill_pp2, (1050, 300))
        screen.blit(Ui.info_fmt_skill_pp3, (1050, 350))
        screen.blit(Ui.info_fmt_skill_pp4, (1050, 400))

    if SET_STATE.isInSaying == True:#剧情对话中
        screen.blit(Ui.UiSayImage2, (90, 485))
        screen.blit(Ui.say_fmt1, (180, 510))
        screen.blit(Ui.say_fmt2, (180, 560))
        screen.blit(Ui.say_fmt3, (180, 610))

    if SET_STATE.isInSelect == True:
        screen.blit(Ui.UiSelect, (860, 155))
        if SET_STATE.select == True:
            screen.blit(Ui.UiChooseBtnImage, (915, 187))
        else:
            screen.blit(Ui.UiChooseBtnImage, (915, 247))

    if SET_STATE.isInBattle == True:
        # 绘制背景
        screen.blit(Ui.UiBattleBackgroundImage, (0, 0))
        if Battle.my_x < 300: #修正晃动的坐标
            Battle.my_x += 1
        screen.blit(Ui.UiBattleHumanImage, (Battle.my_x, 200))  # 我方人物
        if Battle.enemy_x < 850: #修正敌人晃动的坐标
            Battle.enemy_x += 1
        screen.blit(Battle.enemy_list[Battle.enemy_index].image, (Battle.enemy_x, Battle.enemy_y))  # 敌人 初始位置850
        Battle.enemy_list[Battle.enemy_index].update() #更新精灵出场动作
    #展示精灵球状态
    if SET_STATE.isInBattleShowBall == True:
        screen.blit(Ui.UiBattleArrowImage, (5, 100))  # 敌人箭头
        # 绘制敌人精灵球
        for i in range(6):
            if i < Battle.enemy_number:
                screen.blit(Ui.UiBattleBallImage, (335 - i * 45, 70))
            else:
                screen.blit(Ui.UiBattleEmptyBallImage, (335 - i * 45, 70))
        # 我方箭头
        screen.blit(Ui.UiBattleMyArrowImage, (735, 400))
        # 绘制我方精灵球
        screen.blit(Ui.UiBattleEmptyBallImage, (825, 370))
        screen.blit(Ui.UiBattleEmptyBallImage, (870, 370))
        screen.blit(Ui.UiBattleEmptyBallImage, (915, 370))
        screen.blit(Ui.UiBattleEmptyBallImage, (960, 370))
        screen.blit(Ui.UiBattleEmptyBallImage, (1005, 370))
        screen.blit(Ui.UiBattleEmptyBallImage, (1050, 370))
    #战斗中状态
    if SET_STATE.isInBattling == True:
        screen.blit(Ui.UiHpImage, (60, 40))  # 敌人血条框
        screen.blit(Ui.UiMyHpImage, (700, 310))  # 我方血条框
        screen.blit(Ui.text_pokmen_name, (100, 65))  # 敌人名字
        screen.blit(Ui.text_pokmen_level, (370, 65))  # 敌人等级
        pygame.draw.rect(screen, [110, 250, 119], (228, 113, 211 * Battle.enemy_list[Battle.enemy_index].hp_per, 14))  # 敌人血条 宽度 211 = 满血
        screen.blit(Ui.text_my_name, (790, 335))  # 我名字
        screen.blit(Ui.text_my_level, (1060, 335))  # 我等级
        screen.blit(Ui.text_my_hp, (960, 410))  # 我HP
        screen.blit(Ui.text_my_maxhp, (1060, 410))  # 我最大HP
        pygame.draw.rect(screen, [110, 250, 119], (906, 384, 211 * Player.hp_per, 14))  # 我血条
        pygame.draw.rect(screen, [67, 197, 244], (836, 453, 280 * Player.exp_per, 9))  # 我经验条 宽度280=满经验
    #战斗中的提示对话框
    if SET_STATE.isInBattle == True and SET_STATE.isChoseSkill == False:
        screen.blit(Ui.UiSayImage, Ui.UiSayImageRect)
        screen.blit(Ui.text_fmt1, (50, 500))
        screen.blit(Ui.text_fmt2, (50, 560))
        screen.blit(Ui.text_fmt3, (50, 620))
        if SET_STATE.isBattleMask == False and SET_STATE.isEnemyHandle == False:
            # 战斗选择框
            screen.blit(Ui.UiChooseImage, (693, 470))
            # 战斗选择框按钮箭头
            if SET_STATE.chose_mode == 1:
                screen.blit(Ui.UiChooseBtnImage, (723, 517))
            if SET_STATE.chose_mode == 2:
                screen.blit(Ui.UiChooseBtnImage, (960, 517))
            if SET_STATE.chose_mode == 3:
                screen.blit(Ui.UiChooseBtnImage, (723, 600))
            if SET_STATE.chose_mode == 4:
                screen.blit(Ui.UiChooseBtnImage, (960, 600))

    if SET_STATE.isChoseSkill == True:
        #绘制技能框
        screen.blit(Ui.UiattackBoxImage, (0, 470))
        #绘制技能名字
        screen.blit(Ui.UiSkillName1, (100, 530))
        screen.blit(Ui.UiSkillName2, (400, 530))
        screen.blit(Ui.UiSkillName3, (100, 610))
        screen.blit(Ui.UiSkillName4, (400, 610))
        #绘制技能数量
        screen.blit(Ui.UiSkillNumber, (780, 560))
        #绘制选择箭头
        if SET_STATE.chose_skill == 1:
            screen.blit(Ui.UiChooseBtnImage, (59, 519))
            # 刷新PP
            Ui.UiSkillNumber = Ui.skillNumber_text.render("PP     "+str(Player.skill_pp_1)+"/"+str(Skill.getSkillMaxPP(Player.skill_1)), 1, (74, 73, 74))
        if SET_STATE.chose_skill == 2:
            screen.blit(Ui.UiChooseBtnImage, (359, 519))
            # 刷新PP
            Ui.UiSkillNumber = Ui.skillNumber_text.render("PP     "+str(Player.skill_pp_2)+"/"+str(Skill.getSkillMaxPP(Player.skill_2)), 1, (74, 73, 74))
        if SET_STATE.chose_skill == 3:
            screen.blit(Ui.UiChooseBtnImage, (59, 605))
            # 刷新PP
            Ui.UiSkillNumber = Ui.skillNumber_text.render("PP     "+str(Player.skill_pp_3)+"/"+str(Skill.getSkillMaxPP(Player.skill_3)), 1, (74, 73, 74))
        if SET_STATE.chose_skill == 4:
            screen.blit(Ui.UiChooseBtnImage, (359, 605))
            # 刷新PP
            Ui.UiSkillNumber = Ui.skillNumber_text.render("PP     "+str(Player.skill_pp_4)+"/"+str(Skill.getSkillMaxPP(Player.skill_4)), 1, (74, 73, 74))

    for sprite in SET_SPRITES.effect_sprites: #遍历所有特效
        sprite.update()
        screen.blit(sprite.image, sprite.rect)
    #战斗前的遮罩层
    if SET_STATE.isBattleMask == True:
        pygame.draw.rect(screen, [0, 0, 0], (0, Battle.mask_topy, 1200, 350))
        pygame.draw.rect(screen, [0, 0, 0], (0, Battle.mask_bottomy, 1200, 350))

    pygame.display.flip()  # 更新全部显示

    for event in pygame.event.get():  # 遍历所有事件
        if event.type == pygame.QUIT:  # 如果单击关闭窗口，则退出
            sys.exit()
        if event.type == pygame.KEYUP:
            SET_SPRITES.player.moveflag = 0 #当键盘弹起，移动恢复静止状态
            SET_STATE.isMoving = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_z: #确认键
            if SET_STATE.isInSelect == True:#确认上下选择
                if SET_STATE.select == True:#是
                    Ui.Select_close()
                    Event.trigger(SET_STATE.select_id)
                else:#否
                    if SET_STATE.isInBag == True:
                        SET_STATE.isInSelect = False#在背包中上下选择
                        SET_STATE.isInSaying = False
                    else:
                        Ui.Select_close()
            elif SET_STATE.isInSaying == True:#对话
                Ui.Say_update()#显示下一个对话
            elif SET_STATE.isCollNpc == True and SET_STATE.isInMenu == False:#触发NPC碰撞
                if SET_STATE.collNpcId != 0:
                    Event.trigger(SET_STATE.collNpcId)
            elif SET_STATE.isChoseSkill == True:#使用技能
                if SET_STATE.chose_skill == 1: #使用第一个技能
                    if Player.skill_pp_1 > 0:#查看技能剩余够不够
                        Player.skill_pp_1 -= 1
                        Battle.useSkill(Player.skill_1)
                if SET_STATE.chose_skill == 2: #使用第2个技能
                    if Player.skill_pp_2 > 0:#查看技能剩余够不够
                        Player.skill_pp_2 -= 1
                        Battle.useSkill(Player.skill_2)
                if SET_STATE.chose_skill == 3: #使用第3个技能
                    if Player.skill_pp_3 > 0:#查看技能剩余够不够
                        Player.skill_pp_3 -= 1
                        Battle.useSkill(Player.skill_3)
                if SET_STATE.chose_skill == 4: #使用第4个技能
                    if Player.skill_pp_4 > 0:#查看技能剩余够不够
                        Player.skill_pp_4 -= 1
                        Battle.useSkill(Player.skill_4)
            elif SET_STATE.isInMenu == True and SET_STATE.isInBag == False: #菜单选择
                if SET_STATE.menu == 4: #关闭菜单栏
                    SET_STATE.isInMenu = False
                    SET_STATE.isAllowMove = True
                if SET_STATE.menu == 1: #个人信息
                    Ui.Info()
                if SET_STATE.menu == 2: #背包
                    Ui.OpenBag()
            elif SET_STATE.isInBag == True and SET_STATE.isInSelect == False and SET_STATE.isInSaying == False and SET_STATE.bag_select_id >=0:#物品使用
                Ui.Say("确定要使用"+ItemFactory.getItemName(Bag.bag_list[SET_STATE.bag_select_id+Bag.bag_fix].tid)+"吗？")
                Ui.Select(-2)
            elif SET_STATE.isInBattling == True and SET_STATE.isChoseSkill == False and SET_STATE.isEnemyHandle == False:#选择对战状态
                if SET_STATE.chose_mode == 1:#选择进入攻击状态
                    pygame.mixer.Sound("res/music/sound/s3.wav").play()
                    SET_STATE.isChoseSkill = True
                if SET_STATE.chose_mode == 3:#选择精灵
                    Ui.Tip("没有可以召唤的精灵！")
                    pygame.mixer.Sound("res/music/sound/s4.wav").play()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_x: #取消键
            if SET_STATE.isInInfo == True or SET_STATE.isInBag == True and SET_STATE.isInSaying == False:
                Ui.Info_close()
                Ui.Bag_close()
            if SET_STATE.isInBattling == True:
                if SET_STATE.chose_mode == 1:#取消选择进入攻击状态
                    SET_STATE.isChoseSkill = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_c: #召唤菜单
            if SET_STATE.isInMaping == True and SET_STATE.isInSaying == False:
                SET_STATE.isInMenu = True
                SET_STATE.isAllowMove = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_a:#测试按钮
            pkq = Pokmen.Pokmen(27,1,1 ,1,99)
            pkq.addSkill(7)
            jng = Pokmen.Pokmen(4, 1, 1, 1, 1)
            jng.addSkill(2)
            xhl = Pokmen.Pokmen(4,10,10,10,10)
            xhl.addSkill(2)
            ying = Enemy.Enemy("野怪",3000,"可恶，四大家族要开始没落了吗？")
            ying.addPokmen(pkq)
            #ying.addPokmen(xhl)
            #ying.addPokmen(jng)
            Battle.OpenBattle(4,ying)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_s:#测试按钮
            SET_STATE.isAllowWildBattle = False


        if event.type == pygame.KEYDOWN:
            if SET_STATE.isInBattling == True and SET_STATE.isChoseSkill == False: #战斗选项按键
                if event.key == pygame.K_LEFT:
                    pygame.mixer.Sound("res/music/sound/s3.wav").play()
                    if SET_STATE.chose_mode == 2:
                        SET_STATE.chose_mode = 1
                    if SET_STATE.chose_mode == 4:
                        SET_STATE.chose_mode = 3
                if event.key == pygame.K_RIGHT:
                    pygame.mixer.Sound("res/music/sound/s3.wav").play()
                    if SET_STATE.chose_mode == 1:
                        SET_STATE.chose_mode = 2
                    if SET_STATE.chose_mode == 3:
                        SET_STATE.chose_mode = 4
                if event.key == pygame.K_DOWN:
                    pygame.mixer.Sound("res/music/sound/s3.wav").play()
                    if SET_STATE.chose_mode == 1:
                        SET_STATE.chose_mode = 3
                    if SET_STATE.chose_mode == 2:
                        SET_STATE.chose_mode = 4
                if event.key == pygame.K_UP:
                    pygame.mixer.Sound("res/music/sound/s3.wav").play()
                    if SET_STATE.chose_mode == 3:
                        SET_STATE.chose_mode = 1
                    if SET_STATE.chose_mode == 4:
                        SET_STATE.chose_mode = 2
            elif SET_STATE.isInSelect == True and SET_STATE.isAllowMove == False:#上下选择
                if event.key == pygame.K_UP:
                    pygame.mixer.Sound("res/music/sound/s3.wav").play()
                    SET_STATE.select = True
                elif event.key == pygame.K_DOWN:
                    pygame.mixer.Sound("res/music/sound/s3.wav").play()
                    SET_STATE.select = False
            elif SET_STATE.isInBag == True and SET_STATE.isInSaying == False:#背包选择
                if event.key == pygame.K_UP:
                    if SET_STATE.bag_select_id > 0:
                        pygame.mixer.Sound("res/music/sound/s3.wav").play()
                        SET_STATE.bag_select_id -= 1
                    elif len(Bag.bag_list) > 8 and SET_STATE.bag_select_id == 0:  # 在背包最上一格往上拉
                        if SET_STATE.bag_select_id + Bag.bag_fix > 0:
                            pygame.mixer.Sound("res/music/sound/s3.wav").play()
                            Bag.bag_fix -= 1
                            Ui.UpdateBag()
                elif event.key == pygame.K_DOWN:
                    if SET_STATE.bag_select_id < len(Bag.bag_list) - 1:
                        if SET_STATE.bag_select_id < 8:#最多八个
                            pygame.mixer.Sound("res/music/sound/s3.wav").play()
                            SET_STATE.bag_select_id += 1
                        elif len(Bag.bag_list) > 8 and SET_STATE.bag_select_id == 8:#在背包最下一格往下拉
                            if SET_STATE.bag_select_id + Bag.bag_fix < len(Bag.bag_list) - 1:
                                pygame.mixer.Sound("res/music/sound/s3.wav").play()
                                Bag.bag_fix += 1
                                Ui.UpdateBag()
            elif SET_STATE.isInMenu == True:
                if event.key == pygame.K_UP:
                    if SET_STATE.menu > 1:
                        pygame.mixer.Sound("res/music/sound/s3.wav").play()
                        SET_STATE.menu -= 1
                elif event.key == pygame.K_DOWN:
                    if SET_STATE.menu < 4:
                        pygame.mixer.Sound("res/music/sound/s3.wav").play()
                        SET_STATE.menu += 1
            elif SET_STATE.isChoseSkill == True: #技能选项按键
                if event.key == pygame.K_LEFT:
                    pygame.mixer.Sound("res/music/sound/s3.wav").play()
                    if SET_STATE.chose_skill == 2:
                        SET_STATE.chose_skill = 1
                    if SET_STATE.chose_skill == 4:
                        SET_STATE.chose_skill = 3
                if event.key == pygame.K_RIGHT:
                    pygame.mixer.Sound("res/music/sound/s3.wav").play()
                    if SET_STATE.chose_skill == 1:
                        SET_STATE.chose_skill = 2
                    if SET_STATE.chose_skill == 3:
                        SET_STATE.chose_skill = 4
                if event.key == pygame.K_DOWN:
                    pygame.mixer.Sound("res/music/sound/s3.wav").play()
                    if SET_STATE.chose_skill == 1:
                        SET_STATE.chose_skill = 3
                    if SET_STATE.chose_skill == 2:
                        SET_STATE.chose_skill = 4
                if event.key == pygame.K_UP:
                    pygame.mixer.Sound("res/music/sound/s3.wav").play()
                    if SET_STATE.chose_skill == 3:
                        SET_STATE.chose_skill = 1
                    if SET_STATE.chose_skill == 4:
                        SET_STATE.chose_skill = 2

pygame.quit()  # 退出pygame



