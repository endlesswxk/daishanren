from fianlVersion.src.Commons import getExcelPath
from fianlVersion.src.LogOutput import SpiderLog
from pathlib import Path

# 引入日志打印模块
spiderLog = SpiderLog()


# 数据检查
# cmdType.value  1.0 左键单击    2.0 左键双击  3.0 右键单击  4.0 输入  5.0 等待  6.0 滚轮 7.0 读取数据
# ctype     空：0
#           字符串：1
#           数字：2
#           日期：3
#           布尔：4
#           error：5
def dataCheck(targetSheet):
    checkCmd = True
    # 行数检查
    if targetSheet.nrows < 2:
        print("没数据啊哥")
        checkCmd = False
    # 每行数据检查
    i = 1
    while i < targetSheet.nrows:
        # 第1列 操作类型检查
        cmdType = targetSheet.row(i)[0]
        if cmdType.ctype != 2 or (cmdType.value != 1.0 and cmdType.value != 2.0 and cmdType.value != 3.0
                                  and cmdType.value != 4.0 and cmdType.value != 5.0 and cmdType.value != 6.0 and cmdType.value != 7.0):
            spiderLog.error(' 第' + str(i + 1) + "行,第1列数据有毛病")
            checkCmd = False
        # 第2列 内容检查
        cmdValue = targetSheet.row(i)[1]
        # 读图点击类型指令，内容必须为字符串类型
        if cmdType.value == 1.0 or cmdType.value == 2.0 or cmdType.value == 3.0 or cmdType.value == 7.0 or cmdType.value == 8.0:
            if cmdValue.ctype != 1:
                spiderLog.error(' 第' + str(i + 1) + "行,第2列数据有毛病")
                checkCmd = False
        # 输入类型，内容不能为空
        if cmdType.value == 4.0:
            if cmdValue.ctype == 0:
                spiderLog.error(' 第' + str(i + 1) + "行,第2列数据有毛病")
                checkCmd = False
        # 等待类型，内容必须为数字
        if cmdType.value == 5.0:
            if cmdValue.ctype != 2:
                spiderLog.error(' 第' + str(i + 1) + "行,第2列数据有毛病")
                checkCmd = False
        # 滚轮事件，内容必须为数字
        if cmdType.value == 6.0:
            if cmdValue.ctype != 2:
                spiderLog.error(' 第' + str(i + 1) + "行,第2列数据有毛病")
                checkCmd = False
        # 读取数据事件，内容必须为数字
        if cmdType.value == 7.0:
            col4thData = targetSheet.row(i)[3]
            if col4thData.ctype != 2:
                spiderLog.error(' 第' + str(i + 1) + "行,第4列数据有毛病")
                checkCmd = False

        # 第5列 6列 数据类型检查
        locationX = targetSheet.row(i)[4]
        locationY = targetSheet.row(i)[5]
        if locationX.ctype != 0.0 or locationY.ctype != 0.0:
            if locationX.ctype != 2.0 or locationY.ctype != 2.0:
                checkCmd = False
                spiderLog.error(' 第' + str(i + 1) + "行,第5 或 6列数据有毛病,不是数值")

        i += 1
    return checkCmd


# 主目录 menu sheet数据检查
def cmdExcelDataCheck(targetSheet, fileName):

    checkCmd = True
    # 行数检查
    if targetSheet.nrows < 2:
        spiderLog.error(fileName + " 没有数据")
        checkCmd = False
    # 每行数据检查
    i = 1
    while i < targetSheet.nrows:
        # 第1列 序列号 数值类型检查
        cmdType = targetSheet.row(i)[0]
        if cmdType.ctype != 2:
            spiderLog.error(fileName + ' 第' + str(i + 1) + "行,第1列数据有毛病,不是数值")
            checkCmd = False

        # 第2列 内容描述 字符串类型检查
        desc = targetSheet.row(i)[1]
        if desc.ctype != 1:
            checkCmd = False
            spiderLog.error(fileName + '第' + str(i + 1) + "行,第2列数据有毛病, 不是字符串")

        # 第3列 对应的excel文件 文件类型以及存在检查
        excelName = targetSheet.row(i)[2]
        # 字符串类型校验
        if excelName.ctype == 1:
            # 文件校验
            my_file = Path(getExcelPath() + excelName.value)
            # 指定的文件存在
            if not my_file.is_file():
                checkCmd = False
                spiderLog.error(fileName + '第' + str(i + 1) + "行,第3列数据有毛病" + excelName.value + "不存在")
        else:
            spiderLog.error(fileName + '第' + str(i + 1) + "行,第4列数据有毛病,不是字符串")
            checkCmd = False

        # 第4列 对应的sheet名 字符串类型检查
        sheetName = targetSheet.row(i)[3]
        if sheetName.ctype != 1:
            checkCmd = False
            spiderLog.error(fileName + '第' + str(i + 1) + "行,第5列数据有毛病, 不是字符串")

        # 第5列 对应的 sheet类型判断
        isRepeat = targetSheet.row(i)[4]
        if isRepeat.ctype != 2:
            checkCmd = False
            spiderLog.error(fileName + '第' + str(i + 1) + "行,第6列数据有毛病, 不是数值")
        else:
            if isRepeat.value != 1.0 and isRepeat.value != 2.0:
                checkCmd = False
                spiderLog.error(fileName + '第' + str(i + 1) + "行,第6列数据有毛病, sheet类型设置不正确")

        # 第6列 对应的 是否重复 数值类型检查
        isRepeat = targetSheet.row(i)[5]
        if isRepeat.ctype != 2:
            checkCmd = False
            spiderLog.error(fileName + '第' + str(i + 1) + "行,第7列数据有毛病, 不是数值")
        else:
            if isRepeat.value != 0.0 and isRepeat.value != 1.0:
                checkCmd = False
                spiderLog.error(fileName + '第' + str(i + 1) + "行,第7列数据有毛病, 数值范围不正确")

        # 第7列 对应的 重复次数 数值类型检查
        repeatTimes = targetSheet.row(i)[6]
        if isRepeat.value == 1.0:
            if repeatTimes.ctype != 2:
                checkCmd = False
                spiderLog.error(fileName + '第' + str(i + 1) + "行,第8列数据有毛病, 不是数值")
            else:
                if repeatTimes.value < 0:
                    checkCmd = False
                    spiderLog.error(fileName + '第' + str(i + 1) + "行,第8列数据有毛病, 数值范围不正确")
        i += 1
    return checkCmd
