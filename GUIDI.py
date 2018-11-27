import tkinter as tk 

#Variables: Store data about my program

def clicked1(event):


root = tk.Tk()

output = tk.Text(root,height = 30, width = 30)

output.config(state = "disable", background = "white")
output.grid(row = 0, column = 0, rowspan = 5)


labInput1 = tk.Label(root, text = "Side a")
labInput1.grid(row = 0, column = 0, stick = "NESW")
labInput1.bind()

labInput2 = tk.Label(root, text = "Side b")
labInput2.grid(row = 1, column = 0,)

labInput3 = tk.Label(root, text = "Side c")
labInput3.grid(row = 2, column = 0,)

root.mainloop()