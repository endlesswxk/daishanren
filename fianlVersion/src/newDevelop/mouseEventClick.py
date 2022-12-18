import time

import pyautogui
import pythoncom
import PyHook3 as pyHook
from ctypes import *

from fianlVersion.src.newDevelop.LogOutput import SpiderLog

spiderLog = SpiderLog()

i, j, k = 0, 0, 0


def funcLeft(event):
    if event.MessageName != "mouse move":  # 因为鼠标一动就会有很多mouse move，所以把这个过滤下
        global i
        i = i + 1
        pid = c_ulong(0)
        windowTitle = create_string_buffer(512)
        windll.user32.GetWindowTextA(event.Window, byref(windowTitle), 512)
        windll.user32.GetWindowThreadProcessId(event.Window, byref(pid))
        windowName = windowTitle.value.decode('gbk')
        print("当前您处于%s窗口" % windowName)
        print("当前窗口所属进程id %d" % pid.value)
    return True


def funcMiddle(event):
    if event.MessageName != "mouse move":  # 因为鼠标一动就会有很多mouse move，所以把这个过滤下
        global j
        j = j + 1
    return True


def funcRight(event):
    if event.MessageName != "mouse move":  # 因为鼠标一动就会有很多mouse move，所以把这个过滤下
        global k
        k = k + 1
    return True


def initListenEvent():
    # 创建管理器
    hm = pyHook.HookManager()
    # 监听鼠标
    # hm.MouseLeftDown 是将“鼠标左键按下”这一事件和func这个函数绑定，即每次鼠标左键按下都会执行func
    # 如果希望监测鼠标中键按下则：hm.MouseMiddleDown，鼠标右键按下则：hm.MouseRightDown
    hm.MouseLeftDown = funcLeft  # 监测鼠标左键是否按下
    hm.MouseMiddleDown = funcMiddle  # 监测鼠标中键是否按下
    hm.MouseRightDown = funcRight  # 监测鼠标右键是否按下
    hm.HookMouse()

    # 循环监听
    pythoncom.PumpMessages()


if __name__ == '__main__':
    while True:
        # 输入1之后开始记录鼠标的动作， 从第一次点击开始
        taskDesc = '输入 1 之后，开始记录鼠标的所有操作， 并写入excel。' + '\n'
        inputValue = input(taskDesc)
        if inputValue and isinstance(int(inputValue), int):
            key = int(inputValue)
            print(key)
            if key == 1:
                print("开始记录")
                spiderLog.info("#################开始记录操作##################")
                initListenEvent()
            else:
                spiderLog.error("输入不准确，请重新输入")
