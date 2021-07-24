import pygame
#记录游戏状态
isAllowMove = False#是否允许移动
isAllowWildBattle = True #是否遇到野怪
isMoving = False #是否正在移动中
isInMaping = False #是否在地图中
isInBattle = False #是否在战斗中
isCollNpc = True #是否碰撞NPC
collNpcId = 0
isInBag = False#是否在背包中
bag_select_id = 0 #背包正在选择索引
isInSelect = False#是否上下选择中
isInMenu = False #是否在菜单中
isInInfo = False #是否在人物信息中
menu = 1 # 1 2 3 4 从上往下
select = True #选中中的状态
select_id = -1 #正在选择的事件ID
isInSaying = False #是否在对话中
isInBalck = False #黑屏状态
#战斗中的状态 在isinbattle为True下
isBattleMask = False
isInBattleShowBall = False
isInBattling = False
isChoseSkill = False #正在选择技能
isEnemyHandle = False #敌人回合中
battle_end_eventid = -1#对战结束后触发的事件ID
#战斗选择状态
chose_mode = 1 #战斗停留选项 1=战斗 2=背包 3=怪兽 4=逃
chose_skill = 1 #选择技能停留
#对话
say_id = 0 #记录下一个对话的ID
#剧情
main_id = 0 #主线剧情ID
#地图 所在地图ID
map_id = 0
#一次性物品
homeStone = True