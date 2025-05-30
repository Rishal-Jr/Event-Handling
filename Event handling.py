from tkinter import *
window=Tk()
window.title("Event Handler")
window.geometry("400x400")

def key_press(event):
    """Print the charecter associated to the key pressed"""
    print(event.char)

window.bind("<KeyPress>", key_press)

def mouse_click(event):
    print('\n The button was clicked')

button=Button(text="Click Me")
button.pack()

button.bind("<Button-1>", mouse_click)

window.mainloop()