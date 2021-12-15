import time

import pyautogui
import pyperclip
import xlrd

# 定义鼠标事件
# pyautogui库其他用法 https://blog.csdn.net/qingfengxd1/article/details/108270159
def mouseClick(clickTimes,lOrR,img,reTry):
    countTimes = 1
    if reTry == 1:
        while True:
            location=pyautogui.locateCenterOnScreen(img,confidence=0.95)
            if location is not None:
                pyautogui.click(location.x,location.y,clicks=clickTimes,interval=0.2,duration=0.2,button=lOrR)
                break
            print("未找到匹配图片,0.1秒后重试")
            time.sleep(0.1)
            countTimes += 1
            # 重试20次失败，则进入下一步 TODO: 待改进 区分情况判断
            if countTimes > 20:
                break
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

# 数据检查
# cmdType.value  1.0 左键单击    2.0 左键双击  3.0 右键单击  4.0 输入  5.0 等待  6.0 滚轮 7.0 读取数据
# ctype     空：0
#           字符串：1
#           数字：2
#           日期：3
#           布尔：4
#           error：5
def dataCheck(sheet1):
    checkCmd = True
    # 行数检查
    if sheet1.nrows<2:
        print("没数据啊哥")
        checkCmd = False
    # 每行数据检查
    i = 1
    while i < sheet1.nrows:
        # 第1列 操作类型检查
        cmdType = sheet1.row(i)[0]
        if cmdType.ctype != 2 or (cmdType.value != 1.0 and cmdType.value != 2.0 and cmdType.value != 3.0 
        and cmdType.value != 4.0 and cmdType.value != 5.0 and cmdType.value != 6.0 and cmdType.value != 7.0):
            print('第',i+1,"行,第1列数据有毛病")
            checkCmd = False
        # 第2列 内容检查
        cmdValue = sheet1.row(i)[1]
        # 读图点击类型指令，内容必须为字符串类型
        if cmdType.value ==1.0 or cmdType.value == 2.0 or cmdType.value == 3.0:
            if cmdValue.ctype != 1:
                print('第',i+1,"行,第2列数据有毛病")
                checkCmd = False
        # 输入类型，内容不能为空
        if cmdType.value == 4.0:
            if cmdValue.ctype == 0:
                print('第',i+1,"行,第2列数据有毛病")
                checkCmd = False
        # 等待类型，内容必须为数字
        if cmdType.value == 5.0:
            if cmdValue.ctype != 2:
                print('第',i+1,"行,第2列数据有毛病")
                checkCmd = False
        # 滚轮事件，内容必须为数字
        if cmdType.value == 6.0:
            if cmdValue.ctype != 2:
                print('第',i+1,"行,第2列数据有毛病")
                checkCmd = False
        # 读取数据，内容必须是str，自带默认值
        if cmdType.value == 7.0:
            if cmdValue.ctype != 1:
                print('第',i+1,"行,第2列数据有毛病")
                checkCmd = False
            if cmdValue is not None:
                print(cmdValue.value)
                sheetIndex, times = cmdValue.value.split(',', 1)
                # 读取对应的操作
                if sheetIndex is None:
                    print('第',i+1,"行,第2列第1条数据有毛病")
                    checkCmd = False                    
                if times is None:
                    print('第',i+1,"行,第2列第2条数据有毛病")
                    checkCmd = False
            else:
                print('第',i+1,"行,第2列数据有毛病")
                checkCmd = False
        i += 1
        # print("当前行:", i, "当前文件名:", sheet1) 
    return checkCmd

# 任务
def mainWork(sheet):
    i = 1
    while i < sheet.nrows:
        # 取本行指令的操作类型
        cmdType = sheet.row(i)[0]
        if cmdType.value == 1.0:
            # 取图片名称
            img = sheet.row(i)[1].value
            description = sheet.row(i)[3].value
            reTry = 1
            if sheet.row(i)[2].ctype == 2 and sheet.row(i)[2].value != 0:
                reTry = sheet.row(i)[2].value
            print("内容:",description)
            mouseClick(1,"left",img,reTry)
            print("单击左键",img)
        # 2代表双击左键
        elif cmdType.value == 2.0:
            # 取图片名称
            img = sheet.row(i)[1].value
            # 取重试次数
            reTry = 1
            if sheet.row(i)[2].ctype == 2 and sheet.row(i)[2].value != 0:
                reTry = sheet.row(i)[2].value
            mouseClick(2,"left",img,reTry)
            print("双击左键",img)
        # 3代表右键
        elif cmdType.value == 3.0:
            # 取图片名称
            img = sheet.row(i)[1].value
            # 取重试次数
            reTry = 1
            if sheet.row(i)[2].ctype == 2 and sheet.row(i)[2].value != 0:
                reTry = sheet.row(i)[2].value
            mouseClick(1,"right",img,reTry)
            print("右键",img) 
        # 4代表输入
        elif cmdType.value == 4.0:
            inputValue = sheet.row(i)[1].value
            pyperclip.copy(inputValue)
            pyautogui.hotkey('ctrl','v')
            time.sleep(0.5)
            print("输入:",inputValue)                                        
        # 5代表等待
        elif cmdType.value == 5.0:
            #取图片名称
            waitTime = sheet.row(i)[1].value
            time.sleep(waitTime)
            print("等待",waitTime,"秒")
        # 6代表滚轮
        elif cmdType.value == 6.0:
            #取图片名称
            scroll = sheet.row(i)[1].value
            pyautogui.scroll(int(scroll))
            print("滚轮滑动",int(scroll),"距离")
        # 7代表读取数据
        elif cmdType.value == 7.0:
            # 读取数据
            strList = sheet.row(i)[1].value
            sheetIndex, times = strList.split(',', 1)
            print('sheet页:', (int(sheetIndex)), ', 执行次数:', int(times))
            readAndOperation(sheetIndex, times)
        print("第", i ,"次循环")
        i += 1

# 读取操作并且执行
def readAndOperation(sheetIndex, times):
    # 通过索引获取表格sheet页
    sheet = wb.sheet_by_index((int(sheetIndex)-1))
    # print('进来了')
    dataCheckResult = dataCheck(sheet)
    if dataCheckResult:
        # print('进来了mainwork')
        mainWork(sheet)
        # print('mainWork结束')
        loopOperation(sheetIndex, times)


def loopOperation(sheetIndex, times):
    # print('进来循环操作了')
    # 设置文件名
    loopOperationFile = 'loopOperation.xls'
    # 打开文件
    loopOperationWb = xlrd.open_workbook(filename=loopOperationFile)

    # 御魂重复刷 sheetIndex == 2、
    # 探索重复刷 sheetIndex == 3、
    # 麒麟觉醒重复刷 sheetIndex == 4:
    # 通过索引获取表格sheet页
    loopOperationSheet = loopOperationWb.sheet_by_index((int(sheetIndex) - 2))

    names = loopOperationWb.sheet_names()
    print("sheet名:", names)
    loopOperationCheckResult = dataCheck(loopOperationSheet)
    # 循环执行
    if loopOperationCheckResult:
        timesInt = int(times)
        i = 0
        while i < timesInt:
            mainWork(loopOperationSheet)
            i += 1

if __name__ == '__main__':
    # 设置文件名
    file = 'cmd.xls'
    # 打开文件
    wb = xlrd.open_workbook(filename=file)
    checkCmd = False
    while True:
        key=input('选择功能: 1.日常任务 2.御魂 3.探索 4.麒麟 \n')
        key=int(key)
        if key>4 or key <0:
            print('请重新输入:')
            checkCmd = False
        else:
            # 通过索引获取表格sheet页
            sheet1 = wb.sheet_by_index((key-1))
            checkCmd = dataCheck(sheet1)
            if checkCmd:
                mainWork(sheet1)
                checkCmd = False

        # # 日常任务
        # if key=='1':
        #     #通过索引获取表格sheet页
        #     sheet1 = wb.sheet_by_index(0)
        #         #数据检查
        #     checkCmd = dataCheck(sheet1)
        # # 御魂
        # elif key=='2':
        #     #通过索引获取表格sheet页
        #     sheet1 = wb.sheet_by_index(1)
        #         #数据检查
        #     checkCmd = dataCheck(sheet1)
        # # 探索
        # elif key=='3':
        #     #通过索引获取表格sheet页
        #     sheet1 = wb.sheet_by_index(2)
        #         #数据检查
        #     checkCmd = dataCheck(sheet1)
        # # 麒麟
        # elif key=='4':
        #     #通过索引获取表格sheet页
        #     sheet1 = wb.sheet_by_index(3)
        #         #数据检查
        #     checkCmd = dataCheck(sheet1)
        # else:
        #     print('请重新输入:')
        #     key=input('选择功能: 1.日常任务 2.御魂 3.探索 4.麒麟 \n')

        # if checkCmd:
        #     mainWork(sheet1)
        #     checkCmd = False

        
    # file = 'cmd.xls'
    # #打开文件
    # wb = xlrd.open_workbook(filename=file)
    # #通过索引获取表格sheet页
    # sheet1 = wb.sheet_by_index(0)
    # print('欢迎使用本脚本')
    # #数据检查
    # checkCmd = dataCheck(sheet1)
    # if checkCmd:
    #     key=input('选择功能: 1.日常任务 2.御魂 3.探索 \n')
    #     if key=='1':
    #         #循环拿出每一行指令
    #         mainWork(sheet1)
    #     elif key=='2':
    #         while True:
    #             mainWork(sheet1)
    #             time.sleep(2)
    #             print("等待2秒")
    #     elif key=='3':
    #         while True:
    #             mainWork(sheet1)
    #             time.sleep(2)
    #             print("等待2秒")    
    # else:
    #     print('输入有误或者已经退出!')

    # key=input('选择功能: 1.日常任务 2.御魂 3.探索 \n')



