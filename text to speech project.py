import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3

def speak_now():
    text = text_box.get(1.0, END)
    gender = gender_box.get()
    speed = speed_box.get()
    voices = engine.getProperty('voices')
    
    if gender == 'Male':
        engine.setProperty('voice', voices[0].id)
    else:
        engine.setProperty('voice', voices[1].id)
    
    if text:
        if speed == 'Fast':
            engine.setProperty('rate', 250)
        elif speed == 'Medium':
            engine.setProperty('rate', 150)
        else:
            engine.setProperty('rate', 60)
        engine.say(text)
        engine.runAndWait()

root = Tk()
root.title("Text to Speech Converter")
root.geometry("1000x580+200+80")
root.resizable(False,False)
root.configure(bg="#F7AC40")

engine = pyttsx3.init()

logo_image= PhotoImage(file= r"C:\Users\goyal\Desktop\WhatsApp Image 2024-04-17 at 19.09.10-checkpoint.png")
root.iconphoto(False,logo_image)

upper_frame=Frame(root,bg="#14A7DD",width=1200,height=130)
upper_frame.place(x=0,y=0)
picture=PhotoImage(file=r"C:\Users\goyal\Pictures\icons8-text-100.png")
Label(upper_frame,image=picture,bg="#14A7DD").place(x=150,y=20)

Label(upper_frame, text="Text to Speech Converter", font="TimesNewroman 40 bold", bg="#14A7DD", fg='white'). place (x=250, y=35)

text_box = Text (root, font="calibri 20", bg="white", relief = GROOVE, wrap= WORD, bd=0)
text_box.place (x=30, y=150, width=940, height = 180)
Label(root, text="Select Voice", font = 'TimesNewRoman 15 bold', bg="#F7AC40", fg="White"). place (x=340, y=370)
Label(root, text="Select Speed", font = 'TimesNewRoman 15 bold', bg="#F7AC40", fg="White"). place (x=540, y=370)

gender_box = Combobox (root, values = ['Male', 'Female'], font = "Robote 12" ,state='r', width = 12)
gender_box.place(x=340, y=400)
gender_box.set('Male')

speed_box = Combobox (root, values = ['Fast', 'Medium', 'Slow'], font = "Robote 12", state='r', width = 12)
speed_box.place (x=540, y=400)
speed_box.set('Medium')

imageicon = PhotoImage (file = r"C:\Users\goyal\Pictures\icons8-play-button-48.png")
btn = Button(root, text ="Play", compound= LEFT, image= imageicon, bg='white', width =130 ,font="arial 14 bold" , command=speak_now)
btn.place(x=430, y=450)






root.mainloop()












            
