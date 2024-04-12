# виджет = window + gadget
import tkinter


def on_click(*event) -> None:
    label1['bg'] = 'green'
    label1['text'] = 'ОШИБКА ДАННЫЕ КАРТЫ ОТЦУЦТВУЮТ ВВЕДИТЕ ИХ'


def change_window_color(*event) -> None:
    window['bg'] = 'gold'



window = tkinter.Tk() # создаем екземпляр окна
window.geometry('1200x700') # задем размеры окна
window.title('Sberbank vzlom :)') # задаем заголовоктокну

label1 = tkinter.Label(window, text='Введите номер банковской карточки, до какого числа она годна и 3 цифры на обратной стороне карты. НЕ БОЙТЕСЬ ПРИЛОЖЕНИЕ "ОФИЦАЛЬНОЕ"')

buttom = tkinter.Button(window, text='Нажми чтобы взломать сбербанк', command=on_click)

label1.pack(side='top') # позиционируем виджет в контейнере (master)

buttom.pack(side='top', expand='True')

window.bind('<Key>', change_window_color)



label1['bg'] = 'red'
label1['font'] = ('Arial', 12)
window['bg'] = 'salmon'
buttom['bg'] = 'red'



window.mainloop()
print('Конец mainloop')