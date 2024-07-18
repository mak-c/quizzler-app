from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, 'italic')


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.configure(background=THEME_COLOR, padx=20, pady=20)

        self.score = Label(text="Score: 0", padx=20, pady=20, bg=THEME_COLOR, foreground='white')
        self.score.grid(column=1, row=0, sticky='WE')

        self.canvas = Canvas(height=250, width=300, bg='white')
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Question goes here",
            font=FONT,
            fill=THEME_COLOR
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50, sticky="we")

        true = PhotoImage(file="./images/true.png")
        self.tick = Button(image=true, padx=20, pady=20, borderwidth=0, highlightthickness=0, command=self.true_pressed)
        self.tick.grid(column=0, row=2)

        false = PhotoImage(file="./images/false.png")
        self.cross = Button(image=false, padx=20, pady=20, borderwidth=0, highlightthickness=0, command=self.false_pressed)
        self.cross.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz!")
            self.tick.config(state="disabled")
            self.cross.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
