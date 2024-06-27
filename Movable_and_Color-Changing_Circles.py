from tkinter import *

class Kurye(Frame):
    
    def __init__(self, parent):
        Frame.__init__(self , parent)
        self.parent = parent
        self.initUI()
        
    def initUI(self):
        self.pack()
        self.canvas = Canvas(self, bg="white")
        self.canvas.create_oval(50, 50, 60, 60, outline="black", fill="red")
        self.canvas.create_oval(100, 100, 110, 110, outline="black", fill="red")
        self.canvas.create_oval(150, 150, 160, 160, outline="black", fill="red")
        self.canvas.create_oval(200, 200, 210, 210, outline="black", fill="red")
        self.canvas.create_oval(250, 250, 260, 260, outline="black", fill="red")
        self.canvas.pack()
        self.canvas.bind("<ButtonPress 3>", self.button3)
        self.canvas.bind("<ButtonPress 1>", self.button1)
        
    def button1(self,event):
        self.item = self.canvas.find_closest(event.x, event.y)[0]
        if self.canvas.itemcget(self.item, 'fill')  == 'red':
            self.canvas.itemconfig(self.item, fill="blue")
        elif self.canvas.itemcget(self.item, 'fill')  == 'green':
            self.canvas.itemconfig(self.item, fill="blue")
        else:
            self.canvas.itemconfig(self.item, fill="red")


    def button3(self,event):
        self.a=self.canvas.find_closest(event.x, event.y)[0]
        suanki_pozisyon=self.canvas.coords(self.a)
        self.canvas.move(self.a,event.x- suanki_pozisyon[0],event.y- suanki_pozisyon[1])
        if self.canvas.itemcget(self.a, 'fill')  == 'blue':
            self.canvas.itemconfig(self.a, fill="green")
       

def main():
    root = Tk()
    root.geometry("500x400+200+100")
    app = Kurye(root)
    root.mainloop()

main()
