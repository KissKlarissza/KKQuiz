import tkinter as tk
from tkinter import messagebox
from QuizDatabase import create_database, get_questions_random

class KKQuizApp(tk.Tk):
    backroundColor = 'lightblue'
    frameColor = '#e6bbad'

    def __init__(self):
        super().__init__()
        self.title("KK Quiz játék")
        self.resizable(False,False)
        self.geometry("640x360")
        self.configure(bg=self.backroundColor)
        self.score = 0
        self.current_question = 0
        self.questions = get_questions_random()
        
        self.main_menu()

    def main_menu(self):
        frame = tk.Frame(self)
        frame.pack(expand=True)
        frame.configure(bg=self.frameColor, highlightbackground="blue", highlightthickness=2)

        title = tk.Label(frame, text="KK Quiz játék", font=('Arial', 22), background=self.frameColor)
        title.pack(pady=20)
        
        start_button = tk.Button(frame, text="Játék indítása", font=('Arial', 14), command=self.start_game)
        start_button.pack(pady=10)

    def start_game(self):
        self.score = 0
        self.current_question = 0
        
        self.show_question()

    def show_question(self):
        #ablak tisztítása
        for widget in self.winfo_children():
            widget.destroy()

        question, _ = self.questions[self.current_question]
        
        frame = tk.Frame(self)
        frame.configure(bg=self.frameColor, highlightbackground="blue", highlightthickness=2)
        frame.pack(expand=True)
        
        score_label = tk.Label(frame, text=f"{self.score} pont", font=("Arial", 16), background=self.frameColor)
        score_label.place(x=10, y=10) 

        question_label = tk.Label(frame, text=f"{self.current_question + 1}. kérdés:", font=("Arial", 16), background=self.frameColor)
        question_label.pack(pady=10)
        
        question_text = tk.Label(frame, text=question, font=("Arial", 14), wraplength=400, justify="center", background=self.frameColor)
        question_text.pack(pady=10)
        
        
        self.answer_entry = tk.Entry(frame, font=("Arial", 14))
        self.answer_entry.pack(pady=10)
        
        submit_button = tk.Button(frame, text="Válasz küldése", font=("Arial", 12), command=self.check_answer)
        submit_button.pack(pady=10)

    def check_answer(self):
        user_answer = self.answer_entry.get()
        _, correct_answer = self.questions[self.current_question]
        
        if user_answer == correct_answer:
            self.score += 1
            messagebox.showinfo("Eltaláva!", "Eltaláltad!")
        else:
            messagebox.showinfo("Hibás válasz!", f"Hibás válasz, a helyes válasz {correct_answer}.")
        
        self.current_question += 1
        
        if self.current_question < len(self.questions):
            self.show_question()

if __name__ == "__main__":
    create_database()
    app = KKQuizApp()
    app.mainloop()