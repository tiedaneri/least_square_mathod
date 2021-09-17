import xlrd

# file = "me.xlsx" #在main文件中修改。

def rd_exl(file):
    #读取csv表格文件，输入文件名（同目录下），输出x_list, y_list
    me = xlrd.open_workbook(r"{}".format(file))
    sheet1 = me.sheet_by_index(0)

    x_list = list(map(int,sheet1.col_values(0)[1:]))
    y_list = list(map(int,sheet1.col_values(1)[1:]))

    return x_list, y_list


