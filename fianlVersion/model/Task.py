class Task(object):
    def __init__(self, taskId=None, taskDesc=None, excelName=None, sheetName=None,
                 sheetType=None, isRepeat=None, repeatTimes=None):
        # 序列号
        self.taskId = taskId
        # 任务描述
        self.taskDesc = taskDesc
        # excel文件名
        self.excelName = excelName
        # excel sheet名
        self.sheetName = sheetName
        # sheet的类型
        self.sheetType = sheetType
        # 是否重复 0/1
        self.isRepeat = isRepeat
        # 重复次数 > 0
        self.repeatTimes = repeatTimes


class Operation(object):
    def __init__(self, cmdType=None, content=None, retryTimes=None, desc=None, x=None, y=None):
        self.cmdType = cmdType
        self.content = content
        self.retryTimes = retryTimes
        self.desc = desc
        self.x = x
        self.y = y
