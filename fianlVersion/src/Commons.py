from fianlVersion.model.Task import Task, Operation
from fianlVersion.src.LogOutput import SpiderLog

spiderLog = SpiderLog()


def getExcelPath():
    return "../excel/"


def getImgPath():
    return "../picture/"


def getMainOperations(taskList, tarSheet):
    i = 1
    while i < tarSheet.nrows:
        # TODO: 思考增加列的时候应该怎么优化
        # spiderLog.info(mainSheet.row_values(i))

        taskList.append(
            Task(
                tarSheet.row(i)[0].value,
                tarSheet.row(i)[1].value,
                tarSheet.row(i)[2].value,
                tarSheet.row(i)[3].value,
                tarSheet.row(i)[4].value,
                tarSheet.row(i)[5].value,
                tarSheet.row(i)[6].value))
        i += 1


def getSubOperations(taskList, tarSheet):
    i = 1
    while i < tarSheet.nrows:
        # TODO: 思考增加列的时候应该怎么优化
        # spiderLog.info(mainSheet.row_values(i))

        taskList.append(
            Operation(
                tarSheet.row(i)[0].value,
                tarSheet.row(i)[1].value,
                tarSheet.row(i)[2].value,
                tarSheet.row(i)[3].value,
                tarSheet.row(i)[4].value,
                tarSheet.row(i)[5].value))
        i += 1
