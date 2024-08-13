# Importing libraries and modules
import tkinter as tk
import pyttsx3
from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES
from PIL import Image, ImageTk
from tkinter import PhotoImage

expression = ""

text_speech = pyttsx3.init()


def txt_converter():
    # text_speech=pyttsx3.init()
    msg = sor_txt.get("1.0", "end-1c")
    # answer=input(msg)
    text_speech.say(msg)
    text_speech.runAndWait()


def change(text="type", src="English", dest="Hindi"):
    text1 = text
    src1 = src
    dest1 = dest
    trans = Translator()
    trans1 = trans.translate(text1, src=src1, dest=dest1)
    return trans1.text


def clear():
    sor_txt.delete(1.0, tk.END)
    dest_txt.delete(1.0, END)
    sor_txt.set(" ")
    dest_txt.set(" ")


def data():
    s = comb_sor.get()
    d = comb_dest.get()
    msg = sor_txt.get(1.0, END)
    textget = change(text=msg, src=s, dest=d)
    dest_txt.delete(1.0, END)
    dest_txt.insert(END, textget)


# main frame
root = Tk()
root.title("Translator")
root.geometry("700x800")
root.configure(bg="light blue")
root.resizable(0, 0)

# Load the background image
bg_image = Image.open("background.jpg")
image = ImageTk.PhotoImage(bg_image)

# Create a Canvas to display the background image
canvas = Canvas(root, width=image.width(), height=image.height())
canvas.pack()
canvas.create_image(0, 0, anchor=NW, image=image)
Label(image=image).pack()

# create input box
equation = StringVar()
exp = Entry(root, textvariable=equation, font=('arialorange', 20, 'bold'))

# Create label of the frame
lab_txt = Label(root, text="Translator", font=("Roman", 40, "bold"), bg="orange", fg="black")
lab_txt.place(x=200, y=10, height=50, width=300)

frame = Frame(root).pack(side=BOTTOM)

lab_txt = Label(root, text="Enter Text", font=("Time New Roman", 20, "bold"), bg="rosybrown1")
lab_txt.place(x=50, y=110, height=20, width=300)

sor_txt = Text(frame, font=("Swiss", 20, "bold"), wrap=WORD)
sor_txt.place(x=50, y=140, height=120, width=600)

list_text = list(LANGUAGES.values())

# create translation language : Engilsh box
comb_sor = ttk.Combobox(frame)
comb_sor.place(x=50, y=300, height=80, width=150)
comb_sor.set("English")
comb_sor.font = ('arialorange', 50, 'bold')

# create translation button
button_change = Button(frame, text="Translate", font=("Roman", 20, "bold"), relief=RAISED, command=data, bg="cyan",
                       fg="black")
button_change.place(x=250, y=300, height=80, width=150)

# create drop down menu
comb_dest = ttk.Combobox(frame, value=list_text)
comb_dest.place(x=450, y=300, height=80, width=150)
comb_dest.set("Lang2")
comb_dest.font = ('arialorange', 500, 'bold')

lab_txt = Label(root, text="Translation", font=("Time New Roman", 20, "bold"), bg="rosybrown1")
lab_txt.place(x=50, y=420, height=30, width=350)

# create box for output
dest_txt = Text(frame, font=("Time New Roman ", 20, "bold"), wrap=WORD)
dest_txt.place(x=50, y=460, height=180, width=600)

red = Button(root, text="txt-speech", width=2, height=5)

# create Text to speech button
redB = Button(root, text="txt-to-speech", width=25, height=5, bg="light pink", fg="black",
              font=("Time New Roman", 15, "bold"), command=txt_converter)
redB.place(x=400, y=680, height=50, width=300)

# create clear button
redB = Button(root, text="clear", bg="light yellow", fg="black", font=("Time New Roman", 15, "bold"),
              command=lambda: clear())
redB.place(x=50, y=680, width=300, height=50)

root.mainloop()