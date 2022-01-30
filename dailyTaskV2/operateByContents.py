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

wb: any

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
def openExcelAndGetSheet(fileName, sheetName):
    # 打开文件
    wb = xlrd.open_workbook(filename=fileName)
    # 从文件中读取所有的配置 固定读取第一个sheet
    return wb.sheet_by_name(sheetName)

# 根据sheet名 获取sheet
def getSheetBySheetName(wb, sheetName):
    # 从文件中读取所有的配置 固定读取第一个sheet
    return wb.sheet_by_name(sheetName)


# 根据不同类型，执行不同操作
def doActionByOperateType(operateType, strList):
    if operateType == 1:
        # 1.文件名 2.sheet名
        fileNameFixs = strList.split('|')
        # 根据文件名,sheet名 获取sheet
        targetSheet = openExcelAndGetSheet(fileNameFixs[0], fileNameFixs[1])
        # 对cmd.xls 的数据进行检查, 数据正常则进行操作
        checkCmd = dataCheck(targetSheet)
        if checkCmd: 
            print("1")
            # operaterBySheet(targetSheet)

    if operateType == 2:
        # 1.文件名 2.sheet名
        fileNameFixs = strList.split('|')
        if wb is not NULL:
            # 根据文件名,sheet名 获取sheet
            targetSheet = getSheetBySheetName(wb, fileNameFixs[0])
            # 对cmd.xls 的数据进行检查, 数据正常则进行操作
            checkCmd = dataCheck(targetSheet)
            if checkCmd: 
                print("2")
                # operaterBySheet(targetSheet)
        else:
            print("对应的Excel未获取到")
        
# 读取操作并且执行
def readAndCheckOperation(sheet, i):

    # 第四列 操作类型
    operateType = int(sheet.row(i)[3].value)
    # 第二列 操作内容
    strList = sheet.row(i)[1].value

    if contentsCheck(operateType, strList):
        doActionByOperateType(operateType, strList)




