from currency_converter import CurrencyConverter
import tkinter as tk
from tkinter import *
from customtkinter import *

c = CurrencyConverter()


#print (c.convert(12, "USD", "EUR"))
#print(c.currencies)

root = tk.Tk()
root.geometry("750x550")
root.resizable(width=False, height=False)
root.title("Currency Converter")
    
def clicked():
    amount = int(Amount1.get())
    country1 = Country1.get()
    country2 = Country2.get()
    result = c.convert(amount, country1, country2)
    label4 = CTkLabel(root, text=result, font=("McLaren", 20),height=62,width=212, fg_color="#FFD600")
    label4.place(x=481.7, y=391)
# Background image
bg = PhotoImage(file="Frame 1 (6).png")

canvas1 = Canvas(root, width=750, height=550)
canvas1.pack(fill="both", expand=True)

canvas1.create_image(0, 0, image=bg, anchor="nw") 

# Button
button = CTkButton(root, text="Convert", font=("McLaren", 31), border_color="#FFCC15", fg_color="#FFCC15", corner_radius=0, text_color="White", hover_color="#FFD600", border_width=0, height=54, width=160, command=clicked)
button.place(x=295, y=268.2)

# Entry

Amount1 = CTkEntry(root, font=("McLaren", 20), corner_radius=0,border_color="#FFD600", height=62,width=212, fg_color="#FFD600")
Amount1.place(x=55.2, y=391)

Country1 = CTkEntry(root, font=("McLaren", 20), corner_radius=0,border_color="#FFFFFF", height=42,width=211, fg_color="#FFFFFF")
Country1.place(x=56.7, y=152)

Country2 = CTkEntry(root, font=("McLaren", 20), corner_radius=0,border_color="#FFFFFF", height=42,width=211, fg_color="#FFFFFF")
Country2.place(x=481.7, y=152)

root.mainloop()