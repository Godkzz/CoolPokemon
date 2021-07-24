
PokmenInfo_KV = {} #存储精灵信息的键值对



class PokmenInfo():
    def __init__(self, name):
        self.name = name


def init():
    addPokmenInfo(1, PokmenInfo("皮卡丘"))
    addPokmenInfo(2, PokmenInfo("小火龙"))
    addPokmenInfo(3, PokmenInfo("杰尼龟"))
    addPokmenInfo(4, PokmenInfo("火恐龙"))
    addPokmenInfo(5, PokmenInfo("妙蛙花"))
    addPokmenInfo(6, PokmenInfo("裂空座"))
    addPokmenInfo(7, PokmenInfo("伊布"))
    addPokmenInfo(8, PokmenInfo("皮可西"))
    addPokmenInfo(9, PokmenInfo("喵喵"))
    addPokmenInfo(10, PokmenInfo("长翅鸥"))
    addPokmenInfo(11, PokmenInfo("海皇牙"))
    addPokmenInfo(12, PokmenInfo("蛇纹熊"))
    addPokmenInfo(13, PokmenInfo("古拉顿"))
    addPokmenInfo(14, PokmenInfo("快龙"))
    addPokmenInfo(15, PokmenInfo("超梦"))
    addPokmenInfo(16, PokmenInfo("大岩蛇"))
    addPokmenInfo(17, PokmenInfo("帝牙卢卡"))
    addPokmenInfo(18, PokmenInfo("卡比兽"))
    addPokmenInfo(19, PokmenInfo("腕力"))
    addPokmenInfo(20, PokmenInfo("怪力"))
    addPokmenInfo(21, PokmenInfo("帕路奇亚"))
    addPokmenInfo(22, PokmenInfo("海星星"))
    addPokmenInfo(23, PokmenInfo("宝石海星"))
    addPokmenInfo(24, PokmenInfo("梦幻"))
    addPokmenInfo(25, PokmenInfo("炎帝"))
    addPokmenInfo(26, PokmenInfo("路卡利欧"))
    addPokmenInfo(27, PokmenInfo("黑暗裂空座"))
    addPokmenInfo(28, PokmenInfo("黑暗喷火龙"))
def addPokmenInfo(pid,pokmenInfo):
    PokmenInfo_KV[pid] = pokmenInfo
def getPokmenInfo(pid):
    return PokmenInfo_KV[pid]