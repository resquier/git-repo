# https://yadi.sk/d/uSNwOo2A3GThZW - код игры
# https://yadi.sk/d/6vCPIXmr3GThS5 - картинки к игре
# 1. Сделать выбор случайно картинки для пятнашек
# 2. Сделать счётчик ходов

# Подключаем модуль OS
import os

from tkinter import *
from random import choise
from PIL import Image, ImageTk

SIDE = 4 # Константа – величина стороны квадрата (для пятнашек квадрат 4х4)

# Создаём окошко
main_window = Tk()

# Создаём заголовок окошку
main_window.title('Пятнашки')

# Создаём кнопку в окошке
#label = Label(main_window, text="Нажми меня")
#label.pack()
#label.bind('<Button-1>', cmd)

# Пишем функцию
# def cmd(event='x'):
#    ''' Это функция с документацией
#        Х = значенеи параметра
#    '''
#    print(x)


def grid_x(curr, near):


def exchange(curr, near):

def label_above(curr):
    pass
    return labels[(curr.row-1)*SIDE + curr.column]

def label_under(curr):
    pass
    return labels[(curr.row+1)*SIDE + curr.column]

def label_left(curr):
    pass
    return labels[(curr.row-1)*SIDE + curr.column + 1]

def label_right(curr):
    pass
    return labels[(curr.row+1)*SIDE + curr.column - 1]

def key_press(btn):
    near = None

    if btn == 'R' and curr.column > 0

# print(os.listdir('./nums'))
num_files = []
for f in os.listdir('nums'):
    num_files.append(os.path.join('nums', f))

print(num_files)


nums = [PhotoImage(file = f) for f in num_files]

main_window.bind('<Right>', lambda e: key_press('R'))
main_window.bind('<Left>', lambda e: key_press('L'))
main_window.bind('<Up>', lambda e: key_press('U'))
main_window.bind('<Down>', lambda e: key_press('D'))


main_window.mainloop()