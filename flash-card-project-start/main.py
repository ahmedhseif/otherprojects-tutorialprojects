import random
from tkinter import *
from random import randint
import pandas

BACKGROUND_COLOR = "#B1DDC6"

try:
    file = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    file = pandas.read_csv("data/french_words.csv")

to_learn = file.to_dict(orient="records")
current_card = {}



def next_card():
    # My Work >>> random = randint(0, len(file))
    # My Work >>> canvas.itemconfig(en_txt, text=file["French"][random])
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    canvas.itemconfig(image, image=front_img)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    # My Work >>> window.after(3000, flip_card, current_card)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    global current_card
    canvas.itemconfig(image, image=back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")


def remove_word():
    global current_card
    # index = to_learn.index(current_card)
    # to_learn.pop(index)
    to_learn.remove(current_card)
    new_file = pandas.DataFrame(to_learn)
    new_file.to_csv("data/words_to_learn.csv", index=False)
    next_card()




window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
image = canvas.create_image(400, 263, image=front_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))

wrong_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
unknown_button.grid(column=0, row=1)

right_image = PhotoImage(file="images/right.png")
known_button = Button(image=right_image, highlightthickness=0, command=remove_word)
known_button.grid(column=1, row=1)

next_card()

window.mainloop()
