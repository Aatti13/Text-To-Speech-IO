from tkinter import *

from PIL import Image, ImageTk
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os
from random import choice


class AppWindow:
    def __init__(self, window, master=None):
        self.root = window
        self.bg = "#12023a"
        self.gray_scale = "black"
        self.font = "Leelawadee UI Semilight"
        self.engine = pyttsx3.init()
        # --------------------------------------------------------------------------------------------------------------
        self.root.config(bg=self.bg)
        # --------------------------------------------------------------------------------------------------------------
        # Functions


        def speak_now():
            text = self.text_box.get(1.0, END)
            gender = self.gender_drop_box.get()
            speed = self.speed_drop_box.get()
            voices = self.engine.getProperty('voices')

            def set_voice():
                if gender == 'Man':
                    self.engine.setProperty('voice', voices[0].id)

                    self.engine.say(text)
                    self.engine.runAndWait()
                elif gender == 'Woman':
                    self.engine.setProperty('voice', voices[1].id)
                    self.engine.say(text)
                    self.engine.runAndWait()
                else:
                    self.engine.setProperty('voice', choice(voices).id)
                    self.engine.say(text)
                    self.engine.runAndWait()

            if text:
                if speed == "2x":
                    self.engine.setProperty('rate', 300)
                elif speed == "1.5x":
                    self.engine.setProperty('rate', 225)
                elif speed == "1x":
                    self.engine.setProperty('rate', 150)
                elif speed == "0.5x":
                    self.engine.setProperty('rate', 75)
                else:
                    self.engine.setProperty('rate', 37)
            set_voice()


        def download():
            text = self.text_box.get(1.0, END)
            gender = self.gender_drop_box.get()
            speed = self.speed_drop_box.get()
            voices = self.engine.getProperty('voices')

            def set_voice():
                if gender == 'Man':
                    self.engine.setProperty('voice', voices[0].id)
                    path = filedialog.askdirectory()
                    os.chdir(path)
                    self.engine.save_to_file(text, 'text.mp3')
                    self.engine.runAndWait()
                elif gender == 'Woman':
                    self.engine.setProperty('voice', voices[1].id)
                    path = filedialog.askdirectory()
                    os.chdir(path)
                    self.engine.save_to_file(text, 'text.mp3')
                    self.engine.runAndWait()
                else:
                    self.engine.setProperty('voice', choice(voices).id)
                    path = filedialog.askdirectory()
                    os.chdir(path)
                    self.engine.save_to_file(text, 'text.mp3')
                    self.engine.runAndWait()

            if text:
                if speed == "2x":
                    self.engine.setProperty('rate', 300)
                elif speed == "1.5x":
                    self.engine.setProperty('rate', 225)
                elif speed == "1x":
                    self.engine.setProperty('rate', 150)
                elif speed == "0.5x":
                    self.engine.setProperty('rate', 75)
                else:
                    self.engine.setProperty('rate', 37)
            set_voice()
        # --------------------------------------------------------------------------------------------------------------
        'Window Images'
        self.search_image = Image.open("search.png")
        self.search_image = ImageTk.PhotoImage(self.search_image)

        self.title_text_image = Image.open("logo text.png")
        self.title_text_image = ImageTk.PhotoImage(self.title_text_image)

        self.speak_icon_image = Image.open("Copy of speak.png")
        self.speak_icon_image = ImageTk.PhotoImage(self.speak_icon_image)

        self.logo_image = Image.open("speaker logo.png")
        self.logo_image = ImageTk.PhotoImage(self.logo_image)

        self.download_image = Image.open("download image.png")
        self.download_image = self.download_image.resize((60, 60), Image.Resampling.LANCZOS)
        self.download_image = ImageTk.PhotoImage(self.download_image)

        # --------------------------------------------------------------------------------------------------------------
        # Buttons
        self.speak_button = Button(self.root, image=self.speak_icon_image, bg=self.bg, bd=0, command=speak_now)
        self.speak_button.place(x=750, y=540)

        self.download_button = Button(self.root, image=self.download_image, bg=self.bg, bd=0, command=download)
        self.download_button.place(x=905, y=538)

        # --------------------------------------------------------------------------------------------------------------
        'Labels'
        # Logo Label
        # Label(self.root, bg="white", width=180, height=7).place(x=0, y=0)
        Label(self.root, image=self.title_text_image,
              fg="#cf5d17", bg=self.bg).place(x=100, y=21)
        self.text_logo_label = Label(self.root, image=self.search_image, bd=0, bg=self.bg)
        self.text_logo_label.place(x=10, y=630)
        Label(self.root, text="Text to speech...Simple & Easy", bg="#110D19",
              fg="white", font=(self.font, 15)).place(x=50, y=650)

        Label(self.root, image=self.logo_image, bg=self.bg, bd=0).place(x=10, y=10)

        # TextBox Labels
        self.instructions_text_label = Label(self.root, text="--Enter text in the box below--",
                                             font=(self.font, 19), bg=self.bg, fg="white")
        self.instructions_text_label.place(x=50, y=210)

        # DropBox Labels
        Label(self.root, text="VOICE: ", font=(self.font, 18), bg=self.bg, fg="white").place(x=800, y=250)
        Label(self.root, text="SPEED: ", font=(self.font, 18), bg=self.bg, fg="white").place(x=800, y=350)

        # Button Labels
        Label(self.root, text="SPEAK", font=(self.font, 16), bg=self.bg, fg="white").place(x=745, y=595)
        Label(self.root, text="DOWNLOAD", font=(self.font, 16), bg=self.bg, fg="white").place(x=875, y=595)

        # --------------------------------------------------------------------------------------------------------------
        # Text Label
        self.text_box = Text(self.root, bg=self.gray_scale, font=("Bahnschrift", 15),
                             relief=GROOVE, wrap=WORD, width=50, height=10, fg="white",
                             bd=0)
        self.text_box.place(x=50, y=250)

        # --------------------------------------------------------------------------------------------------------------
        'Dropbox'


        self.gender_drop_box = Combobox(self.root, values=["Man", "Woman", "Surprise Me"],
                                        font=(self.font, 16), state='r',
                                        width=10, background=self.bg)
        self.gender_drop_box.place(x=900, y=250)
        self.gender_drop_box.set("Gender")

        self.speed_drop_box = Combobox(self.root, values=["0.25x", "0.5x", "1x", "1.5x", "2x"],
                                       font=(self.font, 16), state='r', width=10, background=self.bg)
        self.speed_drop_box.place(x=900, y=350)
        self.speed_drop_box.set("1x")


if __name__ == "__main__":
    window = Tk()
    window.geometry("1080x720")
    window.title("Text-To-Speech.io")
    window.iconbitmap('icon.ico')
    window.resizable(False, False)
    x = AppWindow(window)
    window.mainloop()