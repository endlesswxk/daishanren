import time
import pyperclip
import pyautogui
from operateByContents import readAndCheckOperation

# 任务
def operaterBySheet(sheet):
    i = 1
    while i < sheet.nrows:
        # 取本行指令的操作类型
        cmdType = sheet.row(i)[0]
        if cmdType.value == 1.0:
            # 取图片名称
            img = sheet.row(i)[1].value
            reTry = 1
            if sheet.row(i)[2].ctype == 2 and sheet.row(i)[2].value != 0:
                reTry = sheet.row(i)[2].value
            mouseClick(1,"left",img,reTry)
            print("单击左键",img)
        # 2代表 双击左键
        elif cmdType.value == 2.0:
            # 取图片名称
            img = sheet.row(i)[1].value
            # 取重试次数
            reTry = 1
            if sheet.row(i)[2].ctype == 2 and sheet.row(i)[2].value != 0:
                reTry = sheet.row(i)[2].value
            mouseClick(2,"left",img,reTry)
            print("双击左键",img)
        # 3代表 右键
        elif cmdType.value == 3.0:
            # 取图片名称
            img = sheet.row(i)[1].value
            # 取重试次数
            reTry = 1
            if sheet.row(i)[2].ctype == 2 and sheet.row(i)[2].value != 0:
                reTry = sheet.row(i)[2].value
            mouseClick(1,"right",img,reTry)
            print("右键",img) 
        # 4代表 输入
        elif cmdType.value == 4.0:
            inputValue = sheet.row(i)[1].value
            pyperclip.copy(inputValue)
            pyautogui.hotkey('ctrl','v')
            time.sleep(0.5)
            print("输入:",inputValue)                                        
        # 5代表 等待
        elif cmdType.value == 5.0:
            #取图片名称
            waitTime = sheet.row(i)[1].value
            time.sleep(waitTime)
            print("等待",waitTime,"秒")
        # 6代表 滚轮
        elif cmdType.value == 6.0:
            #取图片名称
            scroll = sheet.row(i)[1].value
            pyautogui.scroll(int(scroll))
            print("滚轮滑动",int(scroll),"距离")
        # 7代表 读取数据
        elif cmdType.value == 7.0:
            # 读取数据
            # 数据类型类似： 1:日常，2:御魂，3:麒麟
            readAndCheckOperation(sheet, i)
        i += 1

# 定义鼠标事件
# pyautogui库其他用法 https://blog.csdn.net/qingfengxd1/article/details/108270159
def mouseClick(clickTimes,lOrR,img,reTry):
    if reTry == 1:
        while True:
            location=pyautogui.locateCenterOnScreen(img,confidence=0.95)
            if location is not None:
                pyautogui.click(location.x,location.y,clicks=clickTimes,interval=0.2,duration=0.2,button=lOrR)
                break
            print("未找到匹配图片,0.1秒后重试")
            time.sleep(0.1)
    elif reTry == -1:
        while True:
            location=pyautogui.locateCenterOnScreen(img,confidence=0.9)
            if location is not None:
                pyautogui.click(location.x,location.y,clicks=clickTimes,interval=0.2,duration=0.2,button=lOrR)
            time.sleep(0.1)
    elif reTry > 1:
        i = 1
        while i < reTry + 1:
            location=pyautogui.locateCenterOnScreen(img,confidence=0.9)
            if location is not None:
                pyautogui.click(location.x,location.y,clicks=clickTimes,interval=0.2,duration=0.2,button=lOrR)
                print("重复")
                i += 1
            time.sleep(0.1)


from asyncio.windows_events import NULL
import xlrd
from dataCheck import dataCheck
# from operateByExcel import operaterBySheet

# 读取到的数据有可能会有以下的操作
#
# 配置在 operateType.xls 中
#
# 1. 第二列 可能是一个文件名|sheet名
# 2. 第二列 可能是一个sheet名
# 3. 第二列 可能是一个操作选项，让你选择做什么
# 4. 第二列 枚举值，读取并返回

# 文件名情况下， 检查文件名是否正确
def contentsCheck(operateType, strList):
    checkCmd = True
    # 读取文件名
    if operateType == 1:
        fileNameFixs = strList.split('.')
        if len(fileNameFixs) != 2:
            print("文件名: ", strList, "不正确")
            checkCmd = False
    return checkCmd

# 根据文件名和sheet名 打开文件获取sheet
def openExcelAndGet(fileName, sheetName):
    # 打开文件
    wb = xlrd.open_workbook(filename=fileName)
    # 从文件中读取所有的配置 固定读取第一个sheet
    return wb

# 根据sheet名 获取sheet
def getSheetBySheetName(wb, sheetName):
    # 从文件中读取所有的配置 固定读取第一个sheet
    return wb.sheet_by_name(sheetName)


# 根据不同类型，执行不同操作
def doActionByOperateType(operateType, strList):
    
    wb: any
    
    if operateType == 1:
        # 1.文件名 2.sheet名
        fileNameFixs = strList.split('|')
        # 根据文件名,sheet名 获取sheet
        wb = openExcelAndGet(fileNameFixs[0], fileNameFixs[1])
        # 根据文件名,sheet名 获取sheet
        targetSheet = getSheetBySheetName(wb, fileNameFixs[1])
        # 对cmd.xls 的数据进行检查, 数据正常则进行操作
        checkCmd = dataCheck(targetSheet)
        if checkCmd: 
            operaterBySheet(targetSheet)

    if operateType == 2:
        # 1.文件名 2.sheet名
        fileNameFixs = strList.split('|')
        if wb is not NULL:
            # 根据文件名,sheet名 获取sheet
            targetSheet = getSheetBySheetName(wb, fileNameFixs[0])
            # 对cmd.xls 的数据进行检查, 数据正常则进行操作
            checkCmd = dataCheck(targetSheet)
            if checkCmd:
                operaterBySheet(targetSheet)
        else:
            print("对应的Excel未获取到")

    if operateType == 3:
        displayContent = '选择功能:' + strList + ' !\n'
        key = int(input(displayContent))
        








        # 1.文件名 2.sheet名
        # fileNameFixs = strList.split('|')
        # if wb is not NULL:
        #     # 根据文件名,sheet名 获取sheet
        #     targetSheet = getSheetBySheetName(wb, fileNameFixs[0])
        #     # 对cmd.xls 的数据进行检查, 数据正常则进行操作
        #     checkCmd = dataCheck(targetSheet)
        #     if checkCmd: 
        #         print("2")
        #         operaterBySheet(targetSheet)
        # else:
        #     print("对应的Excel未获取到")
        
# 读取操作并且执行
def readAndCheckOperation(sheet, i):

    # 第四列 操作类型
    operateType = int(sheet.row(i)[3].value)
    # 第二列 操作内容
    strList = sheet.row(i)[1].value

    if contentsCheck(operateType, strList):
        doActionByOperateType(operateType, strList)





