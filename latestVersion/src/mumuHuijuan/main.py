import os
import sys
import time
import pyautogui
import action
import win32gui
from Function import Daily
import threading

# 读取文件 精度控制   显示名字
toplist, winlist = [], []
imgs = action.load_imgs()
pyautogui.PAUSE = 0.1
start_time = time.time()

print('程序启动,现在时间', time.ctime())


def enum_cb(hwnd, results):
    winlist.append((hwnd, win32gui.GetWindowText(hwnd)))


def choose_menu():
    daily1.solo()


if __name__ == '__main__':
    win32gui.EnumWindows(enum_cb, toplist)

    yys_1 = [(hwnd1, title) for hwnd1, title in winlist if '阴阳师-网易游戏' in title]  # [#] 阴阳师-网易游戏 [#]

    if not yys_1 == []:
        sandbox = yys_1[0]
        hwnd1 = sandbox[0]
        bbox1 = win32gui.GetClientRect(hwnd1)
        bbox1_1 = win32gui.GetWindowRect(hwnd1)
        W1 = bbox1_1[2] - bbox1_1[0]
        H1 = bbox1_1[3] - bbox1_1[1]
        L_Boarder1 = (W1 - bbox1[2]) // 2
        U_Boarder1 = H1 - bbox1[3] - L_Boarder1
        daily1 = Daily(hwnd1, bbox1, imgs, L_Boarder1, U_Boarder1)

    choose_menu()
