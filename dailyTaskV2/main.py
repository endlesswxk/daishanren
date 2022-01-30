import xlrd
from dataCheck import dataCheck
from operateByExcel import operaterBySheet

if __name__ == '__main__':
    # 设置文件名
    file = 'cmd.xls'
    # 打开文件
    wb = xlrd.open_workbook(filename=file)
    # 从文件中读取所有的配置 固定读取第一个sheet
    mainSheet = wb.sheet_by_index(0)
    # 对cmd.xls 的数据进行检查, 数据正常则进行操作
    checkCmd = dataCheck(mainSheet)

    # sheet 内容例如： 1.日常 2.御魂 3.探索 4.麒麟 5.活动 6.御灵
    # 所有的操作都配置在excel中， 即使有新的操作 也无需调整代码
    if checkCmd:
        while True:
            operaterBySheet(mainSheet)



        # key=input('选择功能: 1.日常任务 2.御魂 3.探索 4.麒麟 \n')
        # key=int(key)
        # if key>4 or key <0:
        #     print('请重新输入:')
        #     checkCmd = False
        # else:
        #     # 通过索引获取表格sheet页
        #     sheet1 = wb.sheet_by_index((key-1))
        #     checkCmd = dataCheck(sheet1)
        #     if checkCmd:
        #         mainWork(sheet1)
        #         checkCmd = False

