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
    if targetSheet.nrows<2:
        print("没数据啊哥")
        checkCmd = False
    # 每行数据检查
    i = 1
    while i < targetSheet.nrows:
        # 第1列 操作类型检查
        cmdType = targetSheet.row(i)[0]
        if cmdType.ctype != 2 or (cmdType.value != 1.0 and cmdType.value != 2.0 and cmdType.value != 3.0 
        and cmdType.value != 4.0 and cmdType.value != 5.0 and cmdType.value != 6.0 and cmdType.value != 7.0):
            print('第',i+1,"行,第1列数据有毛病")
            checkCmd = False
        # 第2列 内容检查
        cmdValue = targetSheet.row(i)[1]
        # 读图点击类型指令，内容必须为字符串类型
        if cmdType.value ==1.0 or cmdType.value == 2.0 or cmdType.value == 3.0 or cmdType.value == 7.0 or cmdType.value == 8.0:
            if cmdValue.ctype != 1:
                print('第',i+1,"行,第2列数据有毛病")
                checkCmd = False
        # 输入类型，内容不能为空
        if cmdType.value == 4.0:
            if cmdValue.ctype == 0:
                print('第',i+1,"行,第2列数据有毛病")
                checkCmd = False
        # 等待类型，内容必须为数字
        if cmdType.value == 5.0:
            if cmdValue.ctype != 2:
                print('第',i+1,"行,第2列数据有毛病")
                checkCmd = False
        # 滚轮事件，内容必须为数字
        if cmdType.value == 6.0:
            if cmdValue.ctype != 2:
                print('第',i+1,"行,第2列数据有毛病")
                checkCmd = False
        # 读取数据事件，内容必须为数字
        if cmdType.value == 7.0:
            col4thData = targetSheet.row(i)[3]
            if col4thData.ctype != 2:
                print('第',i+1,"行,第4列数据有毛病")
                checkCmd = False
        # 读取数据事件，内容必须为数字
        if cmdType.value == 8.0:
            col4thData = targetSheet.row(i)[3]
            if col4thData.ctype != 2:
                print('第',i+1,"行,第4列数据有毛病")
                checkCmd = False
        # 读取数据事件，内容必须为数字
        if cmdType.value == 9.0:
            col4thData = targetSheet.row(i)[3]
            if col4thData.ctype != 2:
                print('第',i+1,"行,第4列数据有毛病")
                checkCmd = False
        i += 1
    return checkCmd
