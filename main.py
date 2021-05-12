from tkinter import *
import pandas
import random as r

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Language Flash Cards")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)


# Changes visual appearance of the card and displays the correct translation of the word:
def flip_card():
    canvas.itemconfig(card_side, image=canvas_image_back)
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(current_word, text=next_word["English"], fill="white")


# Gets the next random word from the list and sets timer before the card is flipped:
def get_next_word():
    global next_word, timer
    window.after_cancel(timer)

    next_word = words_dict[r.randint(0, len(words_dict) - 1)]

    canvas.itemconfig(card_side, image=canvas_image_front)
    canvas.itemconfig(language, text="French", fill="black")
    canvas.itemconfig(current_word, text=next_word["French"], fill="black")
    canvas.update()

    timer = window.after(3000, flip_card)


# Custom method called only when the word is flagged as know, word is removed from list and progress is saved into
# a separate file:
def word_is_known():
    words_dict.remove(next_word)
    unknown_known_words = pandas.DataFrame(words_dict)
    unknown_known_words.to_csv("data/words_to_learn.csv", index=False)

    get_next_word()


# Reads from the csv file and loads all the words into a list of dictionaries:
# Try/Catch block will load words as per previous progress or from the full list of words if the progress file does
# not exist in the data folder.
try:
    words_cvs_file_data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    words_cvs_file_data = pandas.read_csv("data/french_words.csv")
    words_dict = words_cvs_file_data.to_dict(orient="records")
    next_word = words_dict[r.randint(0, len(words_dict) - 1)]
else:
    words_dict = words_cvs_file_data.to_dict(orient="records")
    next_word = words_dict[r.randint(0, len(words_dict) - 1)]

# Loading all the pictures to be used in the program:
canvas_image_front = PhotoImage(file="images/card_front.png")
canvas_image_back = PhotoImage(file="images/card_back.png")
button_img_right = PhotoImage(file="images/right.png")
button_img_wrong = PhotoImage(file="images/wrong.png")

# Displaying all the elements of the program:
canvas = Canvas(width=800, height=526, highlightthickness=0, bd=0, bg=BACKGROUND_COLOR)

card_side = canvas.create_image(400, 263, image=canvas_image_front)
language = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
current_word = canvas.create_text(400, 264, text="trouve", font=("Ariel", 60, "bold"))

canvas.grid(column=0, row=0, columnspan=2)

timer = window.after(3000, func=flip_card)

button_wrong = Button(image=button_img_wrong, highlightthickness=0, bd=0, command=get_next_word)
button_wrong.grid(column=0, row=1)

button_right = Button(image=button_img_right, highlightthickness=0, bd=0, command=word_is_known)
button_right.grid(column=1, row=1)

# Getting our first word by calling the method manually
get_next_word()

mainloop()
