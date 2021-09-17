import matplotlib.pyplot as plt
import numpy as np

def pic(b,a):
#plt画图
    x = np.arange(0,10,0.1)#可增加根据输入的数据调节plt中x的功能。
    y = b * x + a
    plt.plot(x,y)
    plt.title(f"liner fitting y = {b}x + {a}")
    plt.grid()
    plt.show()
