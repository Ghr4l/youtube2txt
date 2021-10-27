from logging import Formatter
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from youtube_transcript_api import YouTubeTranscriptApi
from os.path import abspath
###
video_id = ""

class customFormatter(Formatter):
    def format_transcript(self, transcript, **kwargs):
        #Returns a plain text without line breaks.
        return ' '.join(line['text'] for line in transcript)
class ventana( Frame ):
    def __init__( self ):
        tk.Frame.__init__(self)
        self.pack()
        self.master.geometry('500x250')
        self.master.title("Youtube2Txt")
        self.l1 = Label(self, text="Video ID")
        self.l1.pack(side = TOP)
        self.e1 = Entry(self, bd = 5, width=35)
        self.e1.pack(side=TOP)
        self.button1 = Button( self, text = "Limpiar", width = 15,
                               command = self.limpiar )
        self.button1.pack(side=LEFT)
        self.button2 = Button( self, text = "Ok", width = 15,
                               command = self.sacarTexto )
        self.button2.pack(side=RIGHT)
        
    def limpiar(self):
        self.e1.delete(0,'end')
    
    def sacarTexto(self):
        video_id = self.e1.get()
        print(video_id)
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['es'])
        formatter = customFormatter()
        txt_formatted = formatter.format_transcript(transcript, indent=5)
        try:
            with open('texto.txt', 'w', encoding='utf-8') as text_file:
                text_file.write(txt_formatted)
        except Exception as e:
            messagebox.showerror(title="¡Error!", message="No se pudo realizar la conversión.")
        else:
            messagebox.showinfo(title="¡Éxito!", message=("Archivo guardado en", abspath("texto.txt")))

def main(): 
    ventana().mainloop()

if __name__ == '__main__':
    main()