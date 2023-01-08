# 本文件主要用于阴阳师的所有流程

import time

# 最重要的流程, 替换阵容预设
# 包括行为：
# 点击式神录
# 点击预设按钮
# 点击地域鬼王
# 点击默认分组
# 选中御魂交换(图片同时存在的情况下， 有确定情况的最后按照确定流程走)
# ********************************************
# 以下为参数可替换部分
# 点击指定的分组
# 查找阵容名
# 不存在的情况下， 滚动滑轮  （ 括号部分为 重复执行的行为）
# 再次查找  （括号部分为 重复执行的行为）
# 选中对应的阵容
# 以上为参数可替换部分
# ********************************************
# 点击对应阵容的坐标偏移处
# 点击确定按钮
# 退出式神录
import cv2

from latestVersion.src.common import Featurematcah, Functions
from latestVersion.src.mumuHuijuan import CtrInacWindow

chYuHunOperations = [
    # 点击式神录
    [['shishenlu'], 1, None, '点击式神录'],
    # 点击预设按钮
    [['shishenlu_yushe'], 1, None, '点击预设按钮'],
    # 点击地域鬼王
    [['shishenlu_yushe_diyuguiwang'], 1, None, '点击地域鬼王'],
    # 点击指定的分组
    [['shishenlu_yushe_morenfenzu'], 1, None, '点击指定的分组'],
    # 选中对应的阵容
    [['shishenlu_yushe_morenfenzu_yuhuanjiaohuan'], 1, None, '选中对应的阵容'],
    # 点击对应阵容的坐标偏移处
    [['shishenlu_yushe_morenfenzu_yuhuanjiaohuan'], 1, None, '点击对应阵容的坐标偏移处', True, True, (350, 0)],
    # 点击确定按钮
    [['shishenlu_yushe_quedinganniu'], 1, None, '点击确定按钮'],
    # 退出式神录
    [['shishenlu_fanhui'], 1, None, '退出式神录'],
]


# 总结： 可替换参数 分组/阵容名
def chYuHun(daily, groupName, lineupName):
    size = len(chYuHunOperations)
    for x in range(size):
        chYuHunActions = getChYuHunActions(x)
        doCoreOperations(daily, chYuHunActions)
    else:
        print("交换御魂流程结束")


# 核心操作
# 判断图的存在， 点击， 滑轮滚动
def doCoreOperations(daily, chYuHunActions):
    hwnd = daily.HWND
    images = daily.IMGS

    try:
        closeCollaborativeTask(daily)
        if len(chYuHunActions) > 0:
            image1 = None
            image2 = None
            image3 = None
            if chYuHunActions[0]:
                image1 = chYuHunActions[0].pic
            if chYuHunActions[1]:
                image2 = chYuHunActions[1].pic
            if chYuHunActions[2]:
                image3 = chYuHunActions[2].pic

            picNameList = [image2, image3]
            firstPicClick = False
            findPic = False
            while not findPic:
                for i in range(len(picNameList)):
                    for j in picNameList[i]:
                        screen = CtrInacWindow.capture_inactive_window(hwnd)
                        screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
                        want = images[j]
                        pts = Functions.locate_matchTemplate2(screen, want, 0)
                        if not len(pts) == 0 and i == 0 and not firstPicClick:
                            if chYuHunActions[1] and chYuHunActions[1].cmdType == 1 and chYuHunActions[1].precisely:
                                if chYuHunActions[1].needOffsetClick and chYuHunActions[1].offsetClickPoi:
                                    print('精确点击目标图片坐标偏移处：', j)
                                    clickOffsetScreenByPtsPrecisely(daily, pts, chYuHunActions[1].offsetClickPoi)
                                else:
                                    print('精确点击目标图片：', j)
                                    clickScreenByPtsPrecisely(daily, pts)
                                    time.sleep(1)
                                    firstPicClick = True
                            else:
                                print('非精确点击目标图片：', j)
                                clickScreenByPts(daily, pts)
                                time.sleep(1)
                                firstPicClick = True
                        if not len(pts) == 0 and i == 1:
                            print('找到图片：', j)
                            findPic = True
                            time.sleep(1)
        else:
            print("没有操作需要执行")
            raise Exception("没有操作需要执行")
    except Exception as e:
        # 如果查找图片或点击图片时出现异常，则休眠一段时间
        print(e)
        time.sleep(1)


# 协同任务关闭
def closeCollaborativeTask(daily):
    clickScreenPrecisely(daily, ['xiezuorenwu_jujue', 'xiezuorenwu_tongyi'])


# 创建行为
def getChYuHunActions(index):
    size = len(chYuHunOperations)
    if size > 1:
        if index == 1:
            return [None, getOperation(chYuHunOperations[index]), getOperation(chYuHunOperations[index + 1])]
        elif index == (size - 1):
            return [getOperation(chYuHunOperations[index - 1]), getOperation(chYuHunOperations[index]), None]
        else:
            return [getOperation(chYuHunOperations[index - 1]), getOperation(chYuHunOperations[index]),
                    getOperation(chYuHunOperations[index + 1])]
    elif size == 1:
        return [None, getOperation(chYuHunOperations[index]), None]
    else:
        return []


# 非精确点击屏幕
def clickScreenByPts(daily, pts):
    hwnd = daily.HWND
    bbox = daily.BBOX
    L_Boarder = daily.L_BOARDER
    U_Boarder = daily.U_BOARDER
    posi_1 = [pts[0] + bbox[0] - L_Boarder, pts[1] + bbox[1] - U_Boarder]
    poi_2 = Functions.cheat(posi_1, 20, 20)
    CtrInacWindow.click_inactive_window(hwnd, poi_2)
    time.sleep(1)


# 精确点击屏幕
def clickScreenByPtsPrecisely(daily, pts):
    hwnd = daily.HWND
    bbox = daily.BBOX
    L_Boarder = daily.L_BOARDER
    U_Boarder = daily.U_BOARDER
    posi_1 = [pts[0] + bbox[0] - L_Boarder, pts[1] + bbox[1] - U_Boarder]
    CtrInacWindow.click_inactive_window(hwnd, posi_1)
    time.sleep(1)

# 精确点击屏幕坐标偏移处
def clickOffsetScreenByPtsPrecisely(daily, pts, poi):
    hwnd = daily.HWND
    bbox = daily.BBOX
    L_Boarder = daily.L_BOARDER
    U_Boarder = daily.U_BOARDER
    posi_1 = [pts[0] + bbox[0] - L_Boarder, pts[1] + bbox[1] - U_Boarder]
    offsetPoi = Functions.getOffsetPoi(posi_1, poi)
    CtrInacWindow.click_inactive_window(hwnd, offsetPoi)
    time.sleep(1)

# 非精确点击屏幕
def clickScreen(daily, pictureName):
    hwnd = daily.HWND
    bbox = daily.BBOX
    images = daily.IMGS
    L_Boarder = daily.L_BOARDER
    U_Boarder = daily.U_BOARDER
    screen = CtrInacWindow.capture_inactive_window(hwnd)
    screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    for i in [pictureName]:
        posi_1 = []
        want = images[i]
        pts = Functions.locate_matchTemplate2(screen, want, 0)
        if not len(pts) == 0:
            posi_1.append(pts[0] + bbox[0] - L_Boarder)
            posi_1.append(pts[1] + bbox[1] - U_Boarder)
            poi_2 = Functions.cheat(posi_1, 20, 20)
            CtrInacWindow.click_inactive_window(hwnd, poi_2)
            time.sleep(1)
            print('点击目标图片：', pictureName)
        else:
            print('未找到目标图片：', pictureName)


# 精确点击屏幕
def clickScreenPrecisely(daily, pictureName):
    hwnd = daily.HWND
    bbox = daily.BBOX
    images = daily.IMGS
    L_Boarder = daily.L_BOARDER
    U_Boarder = daily.U_BOARDER
    screen = CtrInacWindow.capture_inactive_window(hwnd)
    screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    for i in pictureName:
        posi_1 = []
        want = images[i]
        pts = Functions.locate_matchTemplate2(screen, want, 0)
        if not len(pts) == 0:
            posi_1.append(pts[0] + bbox[0] - L_Boarder)
            posi_1.append(pts[1] + bbox[1] - U_Boarder)
            CtrInacWindow.click_inactive_window(hwnd, posi_1)
            time.sleep(1)
            print('点击目标图片：', i)
        else:
            print('未找到目标图片：', i)


# 创建操作对象
def getOperation(operation):
    size = len(operation)
    if size == 7:
        return Operation(operation[0], operation[1], operation[2], operation[3], operation[4], operation[5],
                         operation[6])
    elif size == 5:
        return Operation(operation[0], operation[1], operation[2], operation[3], operation[4])
    else:
        return Operation(operation[0], operation[1], operation[2], operation[3])


# 操作对象
class Operation(object):
    def __init__(self, pic=None, cmdType=None, poi=None, desc=None, precisely=False, needOffsetClick=False,
                 offsetClickPoi=None):
        # 操作类型 1.点击 2.判断存在 3.滑动滚轮
        self.pic = pic
        self.cmdType = cmdType
        # 坐标点击
        self.poi = poi
        # 描述
        self.desc = desc
        # 是否精确点击
        self.precisely = precisely
        # 是否需要 根据图片坐标偏移点击
        self.needOffsetClick = needOffsetClick
        # 偏移坐标
        self.offsetClickPoi = offsetClickPoi
