import xlrd
import sys

sys.path.append('../..')

from fianlVersion.src.Commons import getMainOperations, getExcelPath
from fianlVersion.src.LogOutput import SpiderLog
from fianlVersion.src.Operations import doOperations
from fianlVersion.src.dataCheck import cmdExcelDataCheck

spiderLog = SpiderLog()


# 主要功能部分
def chooseToDo(desc, task):
    spiderLog.info("进入 chooseToDo 方法")

    taskDesc = '选择功能: ' + desc + '\n'
    key = int(input(taskDesc))

    if len(desc) >= key > 0:
        # 文件名
        fileName = task[key - 1].excelName
        # sheet名
        sheetName = task[key - 1].sheetName
        # 设置文件名
        filePath = getExcelPath() + fileName
        # 打开文件
        wbs = xlrd.open_workbook(filename=filePath)
        # 从文件中读取所有的配置 固定读取第一个sheet
        targetSheet = wbs.sheet_by_name(sheetName)

        # 对 targetSheet 的数据进行检查, 数据正常则进行操作
        checkResult = cmdExcelDataCheck(targetSheet, fileName)

        subtaskLists = []
        getMainOperations(subtaskLists, targetSheet)

        # sheet 内容例如： 主sheet 主要包含需要读取的sheet 名 以及excel名
        # 所有的操作都配置在excel中， 即使有新的操作 也无需调整代码
        if checkResult:
            doOperations(subtaskLists)
        else:
            spiderLog.error("cmdExcelDataCheck方法 数据检验有误！")

    spiderLog.info("退出 chooseToDo 方法")


if __name__ == '__main__':

    spiderLog.info("进入 main 方法")

    # 设置文件名
    file = 'cmd.xls'
    # 打开文件
    wb = xlrd.open_workbook(filename=file)
    # 从文件中读取所有的配置 固定读取第一个sheet
    mainSheet = wb.sheet_by_index(0)

    # 对cmd.xls 的数据进行检查, 数据正常则进行操作
    checkCmd = cmdExcelDataCheck(mainSheet, file)

    if checkCmd:
        spiderLog.info("cmd.xls 文件数据检查完成, 进入任务选择!")

        taskDisplaylist = ""
        j = 1
        while j < mainSheet.nrows:
            # sheet 内容例如： 1.日常 2.御魂 3.探索 4.麒麟 5.活动 6.御灵
            # 所有的操作都配置在excel中， 即使有新的操作 也无需调整代码
            taskDisplaylist += str(j) + ":" + mainSheet.row(j)[1].value + " "
            j += 1

        taskLists = []
        getMainOperations(taskLists, mainSheet)

        while True:
            # 此处封装到方法中 避免过于臃肿
            chooseToDo(taskDisplaylist, taskLists)
            spiderLog.info("本次任务执行结束，即将进入下次任务选择！")

    spiderLog.error("cmd.xls 文件数据检查完成， 数据有误")
