import PyHook3 as pyHook
import pythoncom  # 没这个库的直接pip install pywin32安装
from ctypes import *
i, j, k = 0, 0, 0


def funcLeft(event):
    if event.MessageName != "mouse move":  # 因为鼠标一动就会有很多mouse move，所以把这个过滤下
        global i
        i = i + 1
        print("onKeyboardEvent")
        pid = c_ulong(0)
        windowTitle = create_string_buffer(512)
        windll.user32.GetWindowTextA(event.Window, byref(windowTitle), 512)
        windll.user32.GetWindowThreadProcessId(event.Window, byref(pid))
        windowName = windowTitle.value.decode('gbk')
        print("当前您处于%s窗口" % windowName)
        print("当前窗口所属进程id %d" % pid.value)
        print("当前刚刚按下了%s键" % str(event.Ascii))

        print('第{:3d}次：按下鼠标左键我就会出现，嘻嘻'.format(i))
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


def main():
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


if __name__ == "__main__":
    main()
