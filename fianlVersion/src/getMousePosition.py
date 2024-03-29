import time

import pyautogui

from fianlVersion.src.LogOutput import SpiderLog

spiderLog = SpiderLog()

if __name__ == '__main__':
    # 等待 6 秒钟
    time.sleep(6)
    # 移至并点击屏幕中间
    x, y = pyautogui.position()
    spiderLog.info("x: " + x.__str__() + " y: " + y.__str__())
    print("x: " + x.__str__() + " y: " + y.__str__())
    screenWidth, screenHeight = pyautogui.size()
    print("x%: " + (x/screenWidth).__str__() + " y: " + (y/screenHeight).__str__())
    spiderLog.info("x%: " + (x/screenWidth).__str__() + " y: " + (y/screenHeight).__str__())