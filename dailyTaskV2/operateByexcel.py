import time
import pyperclip
import pyautogui


# 任务
def mainWork(sheet):
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
        # 7代表循环操作
        elif cmdType.value == 7.0:
            # 循环操作
            strList = sheet.row(i)[1].value
            sheetIndex, times = strList.split(',', 1)
            print('sheet页:', (int(sheetIndex)), ', 执行次数:', int(times))
            readAndOperation(sheetIndex, times)
        i += 1


