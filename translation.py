import requests
import tkinter as tk
from tkinter import *
import json


url = "https://google-translate1.p.rapidapi.com/language/translate/v2"
  
w = tk.Tk()

w.geometry("500x200")

options = [
    "en",
    "de",
    "it",
    "pl",
]
  
clicked = StringVar()
  
clicked.set(options)

drop = OptionMenu(w, clicked, *options)
drop.pack(side=tk.LEFT)

options1 = [
    "en",
    "de",
    "it",
    "pl",
]
  
clicked1 = StringVar()
  
clicked1.set(options1)

drop1 = OptionMenu(w, clicked1, *options)
drop1.pack(side=tk.RIGHT)

frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
frm_form.pack()

lbl_enter = tk.Label(master=frm_form, text="Enter:")
ent_enter = tk.Entry(master=frm_form, width=50)

lbl_enter.grid(row=0, column=0)
ent_enter.grid(row=0, column=1)

def translate_word():
	clicked_enter = clicked.get()
	clicked1_enter = clicked1.get()
	get_enter = ent_enter.get()
	payload = {
	 "q":"{}".format(get_enter),
	 "source": "{}".format(clicked_enter),
	 "target": "{}".format(clicked1_enter),
	}

	headers = {
 	 "content-type":"application/json",
 	 "X-RapidAPI-Key":"f0eda7c17amsha10f3c793fdf668p1ba57fjsn4b46df9be184",
 	 "X-RapidAPI-Host":"deep-translate1.p.rapidapi.com"
	}
	response = requests.request("POST", url, json=payload, headers=headers)
	json = response.json()

	text_translate = json['data']['translations']['translatedText']
	label.config(text="Translated text: {}".format(text_translate))

label = tk.Label(
    text="",
    bg="white", 
    fg="black"
)
label.pack()

frm_buttons = tk.Frame()
frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)

btn_submit = tk.Button(master=frm_buttons, text="Push", command=translate_word)
btn_submit.pack(side=tk.RIGHT, padx=10, ipadx=10)

w.mainloop()