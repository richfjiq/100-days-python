from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.window.title("Quizzler")

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white", font=FONT)
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_label = self.canvas.create_text(
            150, 125, width=280, text="Some question text.", font=FONT
        )
        self.canvas.grid(column=0, columnspan=2, row=1, pady=50)

        self.true_image = PhotoImage(file="images/true.png")
        self.button_true = Button(
            image=self.true_image,
            highlightthickness=0,
            highlightbackground=THEME_COLOR,
        )
        self.button_true.grid(column=0, row=2)

        self.false_image = PhotoImage(file="images/false.png")
        self.button_false = Button(
            image=self.false_image,
            highlightthickness=0,
            highlightbackground=THEME_COLOR,
        )
        self.button_false.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_label, text=q_text)
