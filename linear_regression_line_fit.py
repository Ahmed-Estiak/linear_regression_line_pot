import matplotlib.pyplot as plt
import numpy as np
#%matplotlib widget

def my_linfit(x, y):
    x = np.array(x)
    y = np.array(y)
    n = len(x)
    sum_of_x = np.sum(x)
    sum_of_y = np.sum(y)
    sum_of_xy = np.sum(x * y)
    sum_of_x_squared = np.sum(x ** 2)
    a = (n * sum_of_xy - sum_of_x * sum_of_y) / (n * sum_of_x_squared - sum_of_x ** 2) #From my solution
    b = (sum_of_y - a * sum_of_x) / n                                                  #From my solution
    return a, b

x = []
y = []

def onclick(point):
    if point.button == 1:  
        x.append(point.xdata)
        y.append(point.ydata)
        plt.plot(point.xdata, point.ydata, 'kx')
        plt.draw()
    elif point.button == 3:  
        if len(x) > 1:
            a, b = my_linfit(x, y)
            extended_min_x=min(x)-2
            extended_max_x=max(x)+2
            x_values = np.array([extended_min_x, extended_max_x])
            y_values = a * x_values + b
            print(f"My fit: a={a} and b={b}")
            plt.plot(x_values, y_values, 'r-')
            plt.draw()
            
            
        
        plt.disconnect(click_on_off)
       



fig, ax = plt.subplots()
ax.set_title("Left click: Create a point, Right click: Draw line")
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
click_on_off = plt.connect('button_press_event', onclick)


plt.show()