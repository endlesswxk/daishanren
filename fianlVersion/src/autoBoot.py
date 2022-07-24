import sys

sys.path.append('../..')

import pyautogui
import xlrd

from fianlVersion.src.Commons import getExcelPath, getMainOperations
from fianlVersion.src.Operations import doOperations
from fianlVersion.src.dataCheck import autoBootDataCheck, cmdExcelDataCheck



import subprocess
import time
from threading import Timer
from apscheduler.schedulers.blocking import BlockingScheduler
from fianlVersion.src.LogOutput import SpiderLog

spiderLog = SpiderLog()


def allOperations(param):
    spiderLog.info("allOperations enter")
    # 启动exe
    myPopenObj = subprocess.Popen(param[1])
    # 等待 8 秒钟
    time.sleep(15)
    # 移至并点击屏幕中间
    screenWidth, screenHeight = pyautogui.size()
    pyautogui.moveTo(screenWidth / 2, screenHeight / 2, duration=2, tween=pyautogui.linear)
    pyautogui.click(screenWidth / 2, screenHeight / 2, clicks=1, interval=0.2, duration=0.2, button="left")

    # sheet名
    sheetName = param[3]
    # 设置文件名
    filePath = getExcelPath() + param[2]
    # 打开文件
    spiderLog.info("打开excel: " + filePath)
    wbs = xlrd.open_workbook(filename=filePath)
    # 从文件中读取所有的配置 固定读取第一个sheet
    spiderLog.info("读取sheet: " + sheetName)
    targetSheet = wbs.sheet_by_name(sheetName)

    # 对 targetSheet 的数据进行检查, 数据正常则进行操作
    spiderLog.info("对sheet: " + sheetName + " 进行数据检查")
    checkResult = cmdExcelDataCheck(targetSheet, param[2])

    subtaskLists = []
    getMainOperations(subtaskLists, targetSheet)
    spiderLog.info("取得操作流程! ")

    # sheet 内容例如： 主sheet 主要包含需要读取的sheet 名 以及excel名
    # 所有的操作都配置在excel中， 即使有新的操作 也无需调整代码
    if checkResult:
        doOperations(subtaskLists)
    else:
        spiderLog.error("cmdExcelDataCheck方法 数据检验有误！")

    spiderLog.info("allOperations exit")


def job(param):
    spiderLog.info("job enter")
    # 打印执行时间
    spiderLog.info('job:' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    allOperations(param)
    spiderLog.info("job exit")


def intervalTask(param):
    spiderLog.info("intervalTask enter")
    # 阻塞的方式
    scheduler = BlockingScheduler(timezone='Asia/Shanghai')

    # 采用固定时间间隔（interval）的方式，每隔1小时执行一次
    # 每隔1小时执行一次 scheduler.add_job(job, 'cron', minute=0)
    # 每300秒执行一次   scheduler.add_job(job, 'interval', seconds=300)
    scheduler.add_job(job, 'interval', args=[param], hours=5, minutes=59)

    try:
        # 这是一个独立的线程
        spiderLog.info('startTime' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        scheduler.start()
        spiderLog.info('endTime' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
    spiderLog.info("intervalTask exit")


def func(param):
    spiderLog.info("func enter")
    allOperations(param)
    intervalTask(param)
    spiderLog.info("func exit")


def timer(parameters):
    spiderLog.info("timer enter")
    t = Timer(parameters[0], func, (parameters,))  # 三个参数分别是：延迟时间 调用函数 (传入调用函数的参数（必须是tuple）)
    t.start()
    spiderLog.info("timer exit")


if __name__ == '__main__':

    # 设置文件名
    file = 'scheduledTask.xls'
    # 打开文件
    wb = xlrd.open_workbook(filename=file)
    # 从文件中读取所有的配置 固定读取第一个sheet
    mainSheet = wb.sheet_by_index(0)

    checkCmd = autoBootDataCheck(mainSheet, file)

    if checkCmd:
        spiderLog.info("scheduledTask.xls 文件数据检查完成, 进入定时任务!")
        # 定时时间
        delayTime = mainSheet.row(1)[2].value
        # exe 所在位置
        daiShanRenEXE = mainSheet.row(2)[2].value
        # 操作excel 名
        operationExcel = mainSheet.row(3)[2].value
        # 操作sheet 名
        operationSheet = mainSheet.row(4)[2].value

        params = [delayTime, daiShanRenEXE, operationExcel, operationSheet]
        timer(params)
