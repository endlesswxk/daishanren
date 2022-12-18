import xlrd

from fianlVersion.src.dataCheck import autoBootDataCheck, configValueCheck
from fianlVersion.src.LogOutput import SpiderLog

spiderLog = SpiderLog()


def getCommonConfigs():
    # 设置文件名
    file = 'common.xls'
    # 打开文件
    wb = xlrd.open_workbook(filename=file)
    # 从文件中读取所有的配置 固定读取第一个sheet
    mainSheet = wb.sheet_by_index(0)
    # 参数校验
    checkCmd = configValueCheck(mainSheet)

    if checkCmd:
        # 每行数据检查
        i = 1
        subtaskLists = []
        while i < mainSheet.nrows:
            subtaskLists.append()
            # 第2列 操作类型检查
            configName = mainSheet.row(i)[1]
            # 第3列 操作类型检查
            configValue = mainSheet.row(i)[2]


            i += 1

        spiderLog.info("common.xls 文件数据检查完成, 获取configValue!")
        # 查看是否
        delayTime = mainSheet.row(1)[2].value * 60
        # exe 所在位置
        daiShanRenEXE = mainSheet.row(2)[2].value
        # 操作excel 名
        operationExcel = mainSheet.row(3)[2].value
        # 操作sheet 名
        operationSheet = mainSheet.row(4)[2].value

        return [delayTime, daiShanRenEXE, operationExcel, operationSheet]


class CommonConfig(object):

    def __init__(self):
        self.configs = getCommonConfigs()


commonConfig = CommonConfig()
