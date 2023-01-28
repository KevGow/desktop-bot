from bot import call_bot
from tkinter import *

main = Tk()
main.title("Assistant")

width = 1800
height = 1200

def submit():  # Callback function for SUBMIT Button
    text = textbox.get("1.0", END)  # For line 1, col 0 to end.
    response = call_bot(text)
    tboxMessage.config(text = response)

def reset():  # Callback function for RESET Button
    tboxMessage.config(text="")

c = Canvas(main, width=width, height=height, highlightthickness=0)
c.pack()

text = Label(c, text="Message:")
text.pack()

textbox = Text(c, width=60, height=10)
textbox.pack()

submitbutton = Button(c, width=10, height=1, text='Submit', command=submit)
submitbutton.pack( side = RIGHT )

resetbutton = Button(c, width=10, height=1, text='Reset', command=reset)
resetbutton.pack( side = RIGHT )

frame1 = Label(main)
frame1.pack(padx=10, pady=10)

text = Label(frame1, text="Response:")
text.pack()

tboxMessage = Message(frame1)
tboxMessage.pack()

mainloop()