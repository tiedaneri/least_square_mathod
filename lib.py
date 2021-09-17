import numpy as np



def xy_input():
#分别输入x,y的值存入列表list,返回两个列表。
    x_list = list(map(int,input("请输入x值，用空格隔开\n>").split()))
    y_list = list(map(int,input("请输入y值，用空格隔开\n>").split()))
    # print(type(x_list),x_list)
    return x_list, y_list

def judge(x_list,y_list):
#判断x,y个数是否相等,返回输入的数据组数n。
    if len(x_list) == len(y_list):
        n = len(x_list)
        print(f"有{n}组数据。")
    else:
        print("输入的x,y的个数不相等。")
        quit()
    return n

def calculate_b(x_list,y_list,n):
#计算b_estimate,返回b_estimate,x_mean, y_mean。
    x_mean = np.mean(x_list)
    y_mean = np.mean(y_list)
    #b_estimate, b_up, b_down
    b_up = 0.0
    b_down = 0.0
    for i in range(n):
        b_up += ((x_list[i] * y_list[i]) - x_mean * y_mean)
        b_down += (np.square(x_list[i]) - np.square(x_mean))
    b_estimate = b_up/b_down
    return b_estimate, x_mean, y_mean

def calculate_a(b_estimate,x_mean, y_mean):
#计算a_estimate的值，返回a_estimate。
    a_estimate = y_mean - b_estimate * x_mean
    return a_estimate    
