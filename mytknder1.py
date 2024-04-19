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
    '''
    def __init__(self) -> None:
        self.window = tkinter.Tk()
        self.window.option_add('*Font', ('Arial', 20))
        screen_width = self.window.winfo_screenwidth()
        screen_hight = self.window.winfo_screenheight()
        self.window.geometry(f'{screen_width}x{screen_hight}')
        self.make_widgets()
        self.position_widgets()
        self.question_index = 0
        self.true_answers = 0
        self.false_answers = 0
        self.show_question()
        self.window.mainloop()

    def make_widgets(self) -> None:
        self.questions_frame = tkinter.Frame(self.window)
        self.questions_frame['bg'] = 'gold'
        self.question_text = tkinter.Label(self.questions_frame)
        self.question_answer_1 = tkinter.Label(self.questions_frame)
        self.question_answer_2 = tkinter.Label(self.questions_frame)
        self.question_answer_3 = tkinter.Label(self.questions_frame)
        self.question_answer_4 = tkinter.Label(self.questions_frame)
        self.answer_button_1 = tkinter.Button(
            self.questions_frame, text=1, command=lambda: self.on_click(0)
        )
        self.answer_button_2 = tkinter.Button(
            self.questions_frame, text=2, command=lambda: self.on_click(1)
        )
        self.answer_button_3 = tkinter.Button(
            self.questions_frame, text=3, command=lambda: self.on_click(2)
        )
        self.answer_button_4 = tkinter.Button(
            self.questions_frame, text=4, command=lambda: self.on_click(3)
        )

    def position_widgets(self) -> None:
        self.questions_frame.pack()
        self.question_text.pack()
        self.question_answer_1.pack() 
        self.question_answer_2.pack()
        self.question_answer_3.pack()
        self.question_answer_4.pack()
        self.answer_button_1.pack()
        self.answer_button_2.pack()
        self.answer_button_3.pack()
        self.answer_button_4.pack()

    def show_question(self) -> None:
        question = questions[self.question_index]
        self.question_text['text'] = question['вопрос']
        self.question_answer_1['text'] = '1.' + question['ответы'][0]
        self.question_answer_2['text'] = '2.' + question['ответы'][1]
        self.question_answer_3['text'] = '3.' + question['ответы'][2]
        self.question_answer_4['text'] = '4.' + question['ответы'][3]

    def on_click(self, button_index: int):
        question = questions[self.question_index]
        if button_index == question['индекс правильного ответа']:
            self.true_answers += 1
        else:
            self.false_answers += 1
        if self.question_index + 1 == len(questions):           
           self.show_statistics()
        else:
            self.question_index += 1
            self.show_question()

    def show_statistics(self) -> None:
        self.questions_frame.pack_forget()
        frame = tkinter.Frame(self.window)
        frame.pack()
        tkinter.Label(frame, text='Вопросы викторины закончились').pack()
        tkinter.Label(frame, text=f'Всего вопросов: {len(questions)}').pack()
        tkinter.Label(frame, text=f'Правильных ответов: {self.true_answers}').pack()
        tkinter.Label(frame, text=f'Неверных ответов: {self.false_answers}').pack()

App()
