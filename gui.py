from tkinter import *
from tkinter import ttk
import graph

window = Tk();
window.minsize(600, 400)
window.title("Tree Map Application")
g = graph.Graph()

message = Label(window, text="Select type of tree you would like map to be generated for")
message.grid(row=0, pady=10, padx = 10)

comboBox = ttk.Combobox()
comboBox["values"] = tuple(g.unique_cn)
comboBox.grid(row=1)

select = ttk.Button(window, text="Generate Document")
select.grid(row=2, pady=10)
select.bind("<Button-1>", lambda event, arg=comboBox: g.filter(event, arg))

window.mainloop()
