import time

import pyautogui
import pyperclip
import xlrd

from fianlVersion.model.Task import Task
from fianlVersion.src.Commons import getMainOperations, getExcelPath, getSubOperations, getImgPath
from fianlVersion.src.LogOutput import SpiderLog
from fianlVersion.src.dataCheck import cmdExcelDataCheck, dataCheck

spiderLog = SpiderLog()


# 获取接下来的操作
def getOperationsByExcelNameAndSheetName(excelName, sheetName):
    # 设置文件名
    filePath = getExcelPath() + excelName
    spiderLog.info("获取Excel: " + filePath)
    # 打开文件
    wbs = xlrd.open_workbook(filename=filePath)
    # 从文件中读取所有的配置 根据sheetName 读取指定sheet
    spiderLog.info("获取sheet: " + sheetName)
    targetSheet = wbs.sheet_by_name(sheetName)

    # 对 targetSheet 的数据进行检查, 数据正常则进行操作
    checkResult = dataCheck(targetSheet)
    spiderLog.info("数据检查完成!")

    # print(checkResult)
    if checkResult:
        subtaskLists = []
        getSubOperations(subtaskLists, targetSheet)
        return subtaskLists
    else:
        spiderLog.error(excelName + excelName +
                        "数据有误" + "退出 getOperationsByExcelNameAndSheetName 方法")


# 获取 excel 主菜单
def getSubMenuSheetByExcelNameAndSheetName(excelName, sheetName):
    # 设置文件名
    filePath = getExcelPath() + excelName
    spiderLog.info("获取Excel: " + filePath)
    # 打开文件
    wbs = xlrd.open_workbook(filename=filePath)
    # 从文件中读取所有的配置 根据sheetName 读取指定sheet
    targetSheet = wbs.sheet_by_name(sheetName)
    spiderLog.info("获取sheet: " + sheetName)

    # 对 targetSheet 的数据进行检查, 数据正常则进行操作
    checkResult = cmdExcelDataCheck(targetSheet, filePath)
    spiderLog.info("数据检查完成!")

    # print(checkResult)
    if checkResult:
        subtaskLists = []
        getMainOperations(subtaskLists, targetSheet)
        return subtaskLists
    else:
        spiderLog.error(excelName + excelName +
                        "数据有误" + "退出 getSubMenuSheetByExcelNameAndSheetName 方法")


def doSubOperation(subAction):
    # 取本行指令的操作类型
    cmdType = subAction.cmdType
    if cmdType == 1.0:
        # 取图片名称
        img = getImgPath() + subAction.content
        reTry = 1
        if isinstance(subAction.retryTimes, int) and subAction.retryTimes != 0:
            reTry = subAction.retryTimes
        mouseClick(1, "left", img, reTry)
        spiderLog.info("单击左键" + img)
    # 2代表 双击左键
    elif cmdType == 2.0:
        # 取图片名称
        img = getImgPath() + subAction.content
        # 取重试次数
        reTry = 1
        if isinstance(subAction.retryTimes, int) and subAction.retryTimes != 0:
            reTry = subAction.retryTimes
        mouseClick(2, "left", img, reTry)
        spiderLog.info("双击左键" + img)
    # 3代表 右键
    elif cmdType == 3.0:
        # 取图片名称
        img = getImgPath() + subAction.content
        # 取重试次数
        reTry = 1
        if isinstance(subAction.retryTimes, int) and subAction.retryTimes != 0:
            reTry = subAction.retryTimes
        mouseClick(1, "right", img, reTry)
        spiderLog.info("右键" + img)
        # 4代表 输入
    elif cmdType == 4.0:
        inputValue = subAction.content
        pyperclip.copy(inputValue)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.5)
        spiderLog.info("输入" + inputValue)
        # 5代表 等待
    elif cmdType == 5.0:
        # 取图片名称
        waitTime = subAction.content
        spiderLog.info("等待" + str(waitTime) + "秒")
        time.sleep(waitTime)
    # 6代表 滚轮
    elif cmdType == 6.0:
        # 取图片名称
        scroll = subAction.content
        pyautogui.scroll(int(scroll))
        spiderLog.info("滚轮滑动" + str(scroll) + "距离")


def doOperations(subtaskLists):
    i = 0
    while i < len(subtaskLists):
        if isinstance(subtaskLists[i], Task):
            subTarget = subtaskLists[i]
            # 该任务是可以重复的
            if subTarget.isRepeat == 1 and subTarget.repeatTimes >= 1:
                j = 0
                subMenuSheetTaskLists = getOperationsByExcelNameAndSheetName(subTarget.excelName, subTarget.sheetName)
                while j < subTarget.repeatTimes:
                    doOperations(subMenuSheetTaskLists)
                    j += 1
            else:
                if subTarget.sheetType == 1:
                    subTargetTaskLists = getSubMenuSheetByExcelNameAndSheetName(subTarget.excelName, subTarget.sheetName)
                    doOperations(subTargetTaskLists)
                else:
                    subMenuSheetTaskLists = getOperationsByExcelNameAndSheetName(subTarget.excelName, subTarget.sheetName)
                    doOperations(subMenuSheetTaskLists)
        else:
            subOperation = subtaskLists[i]
            doSubOperation(subOperation)
        i += 1


# 定义鼠标事件
# pyautogui库其他用法 https://blog.csdn.net/qingfengxd1/article/details/108270159
def mouseClick(clickTimes, lOrR, img, reTry):
    if reTry == 1:
        while True:
            spiderLog.info("点击图片： " + img)
            location = pyautogui.locateCenterOnScreen(img, confidence=0.95)
            if location is not None:
                pyautogui.click(location.x, location.y, clicks=clickTimes, interval=0.2, duration=0.2, button=lOrR)
                break
            spiderLog.info("未找到匹配图片,0.3秒后重试" + img)
            time.sleep(0.3)
    elif reTry == -1:
        while True:
            location = pyautogui.locateCenterOnScreen(img, confidence=0.9)
            if location is not None:
                pyautogui.click(location.x, location.y, clicks=clickTimes, interval=0.2, duration=0.2, button=lOrR)
            time.sleep(0.1)
    elif reTry > 1:
        i = 1
        while i < reTry + 1:
            location = pyautogui.locateCenterOnScreen(img, confidence=0.9)
            if location is not None:
                pyautogui.click(location.x, location.y, clicks=clickTimes, interval=0.2, duration=0.2, button=lOrR)
                spiderLog.info("重复" + img)
                i += 1
            time.sleep(0.1)
