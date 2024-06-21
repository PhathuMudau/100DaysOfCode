from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_ONE = ("Ariel", 60, "bold")
FONT_TWO = ("Ariel", 40, "italic")
to_learn = {}
random_word = {}

# --------------------------------- Generating New Word --------------------------------- #

try:
    dataset = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = dataset.to_dict(orient="records")


def new_word():
    global random_word, flip_timer
    window.after_cancel(flip_timer)
    random_word = random.choice(to_learn)
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=random_word["French"], fill="black")
    canvas.itemconfig(card_bg, image=card_front)
    flip_timer = window.after(5000, func=switch_word)


# --------------------------------- Generating New Word --------------------------------- #


def switch_word():
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=random_word["English"], fill="white")
    canvas.itemconfig(card_bg, image=card_back)


# --------------------------------- Generating New Word --------------------------------- #


def remove_word():
    to_learn.remove(random_word)
    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)

    new_word()


# --------------------------------- UI Setup --------------------------------- #

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(5000, func=switch_word)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
card_bg = canvas.create_image(400, 263, image=card_front)
title_text = canvas.create_text(400, 150, text="Title", font=FONT_TWO)
word_text = canvas.create_text(400, 300, text="Word", font=FONT_ONE)
canvas.grid(column=0, row=0, columnspan=2)

r_button_image = PhotoImage(file="images/right.png")
right_button = Button(image=r_button_image, highlightthickness=0, command=remove_word)
right_button.grid(column=1, row=1)

w_button_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=w_button_image, highlightthickness=0, command=new_word)
wrong_button.grid(column=0, row=1)


new_word()



window.mainloop()


