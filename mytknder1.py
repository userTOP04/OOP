import tkinter


questions = [
    {
        'вопрос': 'Какой оператор умножает числа в Python?',
        'ответы': ['-', 'x', '*', '**'],
        'индекс правильного ответа': 2
    },
    {
        'вопрос': 'Какой из этих типов изменяемый?',
        'ответы': ['list', 'str', 'tuple', 'int'],
        'индекс правильного ответа': 0
    }
]


class App:
    '''
    Приложение
    TODO: Окно во весь экрон
    '''
    def __init__(self) -> None:
        self.window = tkinter.Tk()
        self.window.option_add('*Font', ('Arial', 20))
        screen_width = self.window.winfo_screenwidth()
        screen_hight = self.window.winfo_screenheight()
        self.window.geometry(f'{screen_width}x{screen_hight}')
        
        
        self.question_text = tkinter.Label(self.window)
        self.question_answer_1 = tkinter.Label(self.window)
        self.question_answer_2 = tkinter.Label(self.window)
        self.question_answer_3 = tkinter.Label(self.window)
        self.question_answer_4 = tkinter.Label(self.window)
        self.answer_button_1 = tkinter.Button(self.window, text=1, command=lambda: self.on_click(1))
        self.answer_button_2 = tkinter.Button(self.window, text=2, command=lambda: self.on_click(2))
        self.answer_button_3 = tkinter.Button(self.window, text=3, command=lambda: self.on_click(3))
        self.answer_button_4 = tkinter.Button(self.window, text=4, command=lambda: self.on_click(4))



        self.question_text.pack()
        self.question_answer_1.pack() 
        self.question_answer_2.pack()
        self.question_answer_3.pack()
        self.question_answer_4.pack()
        self.answer_button_1.pack()
        self.answer_button_2.pack()
        self.answer_button_3.pack()
        self.answer_button_4.pack()


        for question in questions:
            self.question_text['text'] = question['вопрос']
            self.question_answer_1['text'] = '1.' + question['ответы'][0]
            self.question_answer_2['text'] = '2.' + question['ответы'][1]
            self.question_answer_3['text'] = '3.' + question['ответы'][2]
            self.question_answer_4['text'] = '4.' + question['ответы'][3]

        self.window.mainloop()

    def on_click(self, button_number: int):
        print('Кнопка нажата №', button_number)


        


App()
