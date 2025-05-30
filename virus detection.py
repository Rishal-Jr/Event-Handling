from tkinter import*
from tkinter import messagebox
root = Tk()
root.geometry("400x400")

def virus_detected():
    messagebox.showinfo("Alert", "Stop! Virus Detected!")
button= Button(root, text="Scan For Virus Detection", command=virus_detected)    
button.place(x=100, y=100)
root.mainloop()