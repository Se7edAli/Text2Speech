import tkinter as tk
import pyttsx3

engine = pyttsx3.init()

class MainWin():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Text2Speech")
        self.root.geometry("250x125")
        self.root.resizable(0, 0)
        self.maintext = tk.Label(self.root,text="Write Here What you want to Speech")
        self.maintext.pack()
        self.entry = tk.Entry(self.root)
        self.entry.pack()
        self.button = tk.Button(self.root, text="Speech!", command=self.clicked)
        self.button.pack()
        self.root.mainloop()

    def speeech(self,text):
        engine.say(text)
        engine.runAndWait()
    
    def clicked(self):
        text = self.entry.get()
        self.speeech(text)

if __name__ == '__main__':
    mainwin = MainWin()

