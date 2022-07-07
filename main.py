from tkinter import *
import tkinter as tk
import random

class FlashcardApp:

    def __init__(self, root):

        root.title("Flashcard App")

        #Setting of Frames
        frame = Frame(root, borderwidth=2, relief="sunken")
        frame.grid(column=1, row=1)

        #Header Label
        header = Label(frame, width=40, text="Flash Cards", font=("Courier", 20))
        header.grid(column=1, row=1, sticky=(N, W), columnspan=4)

        # Holder
        self.main_random_index = IntVar()

        #Body
        question_label = Label(frame, text="Question:", font=("Courier", 15))
        question_label.grid(column=1, row=2, sticky=(N, W))

        self.question_str = StringVar()
        self.question_text = Entry(frame, textvariable=self.question_str, width=100)
        self.question_text.grid(column=1, row=3, sticky=(N, W), columnspan=4, pady=12)

        answer_label = Label(frame, text="Answer:", font=("Courier", 15))
        answer_label.grid(column=1, row=4, sticky=(N, W))

        self.answer_str = StringVar()
        answer_text = Entry(frame, textvariable=self.answer_str, width=75)
        answer_text.grid(column=1, row=5, sticky=(N, W), columnspan=3)

        self.card_list_string = [QuestionAnswers("Test Question", "Test Answer"),
                                 QuestionAnswers("Test Question1", "Test Answer1"),
                                 QuestionAnswers("Test Question2", "Test Answer2"),
                                 QuestionAnswers("Test Question3", "Test Answer3")]

        num_cards_label = Label(frame, text="# of cards:", font=("Courier", 12))
        num_cards_label.grid(column=4, row=2, sticky=(E))

        self.card_count_str = StringVar()
        num_cards = Label(frame, textvariable=self.card_count_str, font=("Courier", 12))
        num_cards.grid(column=5, row=2, sticky=(W))
        self.card_count_str.set(len(self.card_list_string))

        self.start_question_str = StringVar()
        self.start_question = Label(frame, textvariable=self.start_question_str, font=("Courier", 18))

        #Buttons
        self.save_button = Button(frame, text="Save", font=("Courier", 12), command=self.save_question)
        self.save_button.grid(column=2, row=6, sticky=(N, W), pady=4)

        self.start_button = Button(frame, text="Start", font=("Courier", 12), command=self.start_quiz)
        self.start_button.grid(column=3, row=6, sticky=(N, W), pady=4)

        self.stop_button = Button(frame, text="Stop", font=("Courier", 12), command=self.stop_quiz)

        self.skip_button = Button(frame, text="Skip", font=("Courier", 12), command=self.skip)

        self.submit_button = Button(frame, text="Submit", font=("Courier", 12), command=self.submit)

        #Results
        self.text_results = StringVar()
        self.results = Label(frame, width=40, textvariable=self.text_results, font=("Courier", 20))

    def save_question (self):
        question = self.question_str.get()
        answer = self.answer_str.get()

        new_question = QuestionAnswers(question, answer)
        self.card_list_string.append(new_question)
        self.card_count_str.set(len(self.card_list_string))

        print(self.card_list_string)

        self.question_str.set("")
        self.answer_str.set("")


    def start_quiz (self):
        self.remove(self.question_text)
        self.remove(self.start_button)
        self.remove(self.save_button)

        #Questions widget
        self.start_question.grid(column=1, row=3, sticky=(N, W), columnspan=4)

        #Buttons
        self.stop_button.grid(column=3, row=6, sticky=(N, W), pady=4)
        self.skip_button.grid(column=2, row=6, sticky=(N, W), pady=4)
        #///Submit Button
        self.submit_button.grid(column=4, row=5)

        #clearing entries
        self.question_str.set("")
        self.answer_str.set("")

        #Adding results area
        self.results.grid(column=1, row=7, sticky=(N, W), columnspan=4)

        #makes random number for index and sets the question
        random_index_num = self.random_index()
        self.main_random_index.set(random_index_num)
        self.start_question_str.set(self.random_question(random_index_num))

        #test
        print(random_index_num)
        print(self.random_question(random_index_num))
        print(self.random_answer(random_index_num))

    def stop_quiz (self):
        #remove widgets
        self.remove(self.start_question)
        self.remove(self.skip_button)
        self.remove(self.stop_button)
        self.remove(self.submit_button)
        self.remove(self.results)

        # Question widget
        self.question_text.grid(column=1, row=3, sticky=(N, W), columnspan=4)

        # Buttons
        self.save_button.grid(column=2, row=6, sticky=(N, W), pady=4)
        self.start_button.grid(column=3, row=6, sticky=(N, W), pady=4)

    def skip (self):
        random_index_num = self.random_index()
        self.main_random_index.set(random_index_num)
        self.start_question_str.set(self.random_question(random_index_num))

        # clearing entries
        self.answer_str.set("")
        self.text_results.set("")

        #test
        #print(random_index_num)
        #print(self.random_question(random_index_num))
        #print(self.random_answer(random_index_num))

    def submit(self):
        index_num = self.main_random_index.get()
        if self.answer_str.get() == self.random_answer(index_num):
            self.text_results.set("Correct!!!")

            #Goes to next question
            random_index_num = self.random_index()
            self.main_random_index.set(random_index_num)
            self.start_question_str.set(self.random_question(random_index_num))

            self.answer_str.set("")
        else:
            self.text_results.set("Wrong!!!")
            self.answer_str.set("")

    def remove(self, widget):
        widget.grid_remove()

    def random_question(self, index):
        question_list = self.card_list_string[index]
        question = question_list.question
        return question

    def random_answer(self, index):
        question_list = self.card_list_string[index]
        answer = question_list.answer
        return answer

    def random_index(self):
        total_count = self.card_count_str
        random_num = random.randrange(0, int(total_count.get()))
        return random_num

class QuestionAnswers:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def __repr__(self):
        return self.question + ", " + self.answer

root = Tk()
FlashcardApp(root)
root.mainloop()

