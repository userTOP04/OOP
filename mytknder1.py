import tkinter
import random
import time 
from questions import questions


class App:
    '''
    Приложение
    '''
    def __init__(self, shuffle_answers=False, shuffle_questions=False) -> None:
        self.window = tkinter.Tk()
        self.window.option_add('*Font', ('Arial', 20))
        self.window.bind('<Escape>', lambda _: self.window.destroy())
        screen_width = self.window.winfo_screenwidth()
        screen_hight = self.window.winfo_screenheight()
        self.window.geometry(f'{screen_width}x{screen_hight}')
        self.shuffle_answers = shuffle_answers
        self.shuffle_questions = shuffle_questions
        self.main_frame = tkinter.Frame(self.window)
        self.main_frame.place(relx=0.5, rely=0.5, anchor='center')
        self.results_frame = None
        self.questions_frame = None
        self.time_starter = None
        self.time_finish = None
        self.question_index = 0
        self.true_answers = 0
        self.false_answers = 0
        self.start(False)
        self.window.mainloop()

    def show_question(self) -> None:
        question = questions[self.question_index]
        if self.shuffle_answers:
            random.shuffle(question['ответы'])
        tkinter.Label(
            self.main_frame, 
            text=f'{self.question_index + 1}/{len(question) + 1}'
        ).pack()
        tkinter.Label(self.main_frame, text=question['вопрос']).pack(pady=10)
        button_frame = tkinter.Frame(self.main_frame)
        button_frame.pack()

        for answer in question['ответы']:
            tkinter.Button(
                button_frame,
                text=answer, 
                command=lambda arg=answer: self.on_click(arg)
            ).pack(side='left', padx=20, ipadx=30)

    def on_click(self, button_text):
        question = questions[self.question_index]
        if button_text == question['ответ']:
            self.true_answers += 1
        else:
            self.false_answers += 1

        self.clear()

        self.question_index += 1
        if self.question_index < len(questions):           
           self.show_question()
        else:
            self.show_result()

    def clear(self) -> None:
        for widget in self.main_frame.winfo_children():
            widget.destroy() 

    def show_result(self) -> None:
        self.time_finish = time.time()
        time_total = self.time_finish - self.time_starter
        tkinter.Label(
            self.main_frame, text=f'Время: {round(time_total, 1)}'
        ).pack()
        tkinter.Label(
            self.main_frame, 
            text='Вопросы викторины закончились'
        ).pack()
        tkinter.Label(
            self.main_frame, 
            text=f'Всего вопросов: {len(questions)}'
        ).pack()
        tkinter.Label(
            self.main_frame, 
            text=f'Правильных ответов: {self.true_answers}'
        ).pack()
        tkinter.Label(
            self.main_frame, 
            text=f'Неверных ответов: {self.false_answers}'
        ).pack()
        tkinter.Button(
            self.main_frame, 
            text='Начать заново', 
            command=lambda: self.start(True)
        ).pack(pady=(30,0))

    def start(self, start_over: bool) -> None:
        self.question_index = 0
        self.true_answers = 0
        self.false_answers = 0
        if self.shuffle_questions:
            random.shuffle(questions)
        if start_over:
            self.clear()
        self.time_starter = time.time()
        self.show_question()
        
        
App(shuffle_answers=True,  shuffle_questions=True)
