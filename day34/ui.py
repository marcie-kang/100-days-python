from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.user_answer = ""

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = 0
        self.score_label = Label(text=f"Score: {self.score}", font=("Arial", 15), bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.question = self.canvas.create_text(150, 125, width=280, text="quiz", fill=THEME_COLOR, font=("Ariel", 20, "italic"))

        check_image = PhotoImage(file="images/true.png")
        self.check_button = Button(image=check_image, highlightthickness=0, command=self.user_answered_checked)
        self.check_button.grid(row=2, column=0)
        wrong_image = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=wrong_image, highlightthickness=0, command=self.user_answered_wrong)
        self.wrong_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")

        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
        else:
            self.canvas.itemconfig(self.question, text="You've reached the end of the question.")
            self.check_answer.config(state="disabled")

    def user_answered_checked(self):
        self.user_answer = "checked"
        self.check_answer()

    def user_answered_wrong(self):
        self.user_answer = "wrong"
        self.check_answer()


    def check_answer(self):
        answer = self.quiz.get_answer()

        if (answer == "True" and self.user_answer == "checked") or (answer == "False" and self.user_answer == "wrong"):
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)
