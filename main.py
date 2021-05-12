from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Language Flash Cards")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

canvas_image_front = PhotoImage(file="images/card_front.png")
canvas_image_back = PhotoImage(file="images/card_back.png")
button_img_right = PhotoImage(file="images/right.png")
button_img_wrong = PhotoImage(file="images/wrong.png")

canvas = Canvas(width=800, height=526, highlightthickness=0, bd=0, bg=BACKGROUND_COLOR)

card_side = canvas.create_image(400, 263, image=canvas_image_front)
language = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
current_word = canvas.create_text(400, 264, text="trouve", font=("Ariel", 60, "bold"))

canvas.grid(column=0, row=0, columnspan=2)

button_wrong = Button(image=button_img_wrong, highlightthickness=0, bd=0)
button_wrong.grid(column=0, row=1)

button_right = Button(image=button_img_right, highlightthickness=0, bd=0)
button_right.grid(column=1, row=1)

mainloop()
