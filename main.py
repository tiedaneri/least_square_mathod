import lib
import draw
import read_excel as rd

file = "C:\\Users\\24963\\Desktop\\python_learn\\least_square\\me.xlsx"

#两种输入数据的方法。
# x,y = lib.xy_input()
x, y = rd.rd_exl(file)

n = lib.judge(x,y)
b,x_m,y_m = lib.calculate_b(x,y,n)
a = lib.calculate_a(b,x_m,y_m)
# print(f'y = {b}x + {a}')
draw.pic(b,a)
