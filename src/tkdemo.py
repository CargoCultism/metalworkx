import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import json
from json import JSONEncoder
from dataclasses import dataclass

@dataclass
class InventoryItem:
	name: str
	unit_price: float
	quantity_on_hand: int = 0

	def total_cost(self) -> float:
		return self.unit_price * self.quantity_on_hand

class InventoryItemEnconder(JSONEncoder):
	def default(self,o):
		return o.__dict__

version = "0.1a"

window = tk.Tk()
window.title(version)
window.resizable(0, 0)

def loadCallBack():
	filename = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("metalworxs file","*.mwx"),("all files","*.*")))
	if not filename:
		msg = messagebox.showinfo("Hello Python", "Filename is empty")
	else:
		f = open("s1", "r")
		content = f.read()
		f.close()
		
		parsed = json.loads(content)
		ii = InventoryItem(**parsed)
		print(ii.name)
		filenameLabel.delete(0, tk.END)
		filenameLabel.insert(0, filename)
		productName.delete(0, tk.END)
		productName.insert(0, ii.name)
		productQty.delete(0, tk.END)
		productQty.insert(0, ii.quantity_on_hand)
		unitPrice.delete(0, tk.END)
		unitPrice.insert(0, ii.unit_price)

def saveCallBack():
	filename = filedialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("metalworxs file","*.mwx"),("all files","*.*")))
	if not filename:
		msg = messagebox.showinfo("Hello Python", "Filename is empty")
	else:
		f = open(filename, "a")
		item = InventoryItem(name = productName.get(), quantity_on_hand = productQty.get(), unit_price = unitPrice.get())
		f.write(InventoryItemEnconder().encode(item))
		f.close()


window.columnconfigure(0,weight=4)
window.columnconfigure(1,weight=1)

leftframe = ttk.Frame(window)
leftframe.columnconfigure(0,weight=0)
leftframe.grid(column=0,row=0)

ttk.Label(leftframe, text='Filename:').grid(column=0,row=0)
filenameLabel = ttk.Entry(leftframe, width='30')
filenameLabel.grid(column=1,row=0)

ttk.Label(leftframe, text='Product Name:').grid(column=0,row=1)
productName = ttk.Entry(leftframe, width='30')
productName.grid(column=1,row=1)

ttk.Label(leftframe, text='Product Quantity:').grid(column=0,row=2)
productQty = ttk.Entry(leftframe, width='30')
productQty.grid(column=1,row=2)

ttk.Label(leftframe, text='Unit Price:').grid(column=0,row=3)
unitPrice = ttk.Entry(leftframe, width='30')
unitPrice.grid(column=1,row=3)

topframe = ttk.Frame(window)
topframe.columnconfigure(0,weight=1)
topframe.grid(column=1,row=0)

#bottomframe = tk.Frame(window)
#bottomframe.pack(side = tk.BOTTOM)

ttk.Button(topframe, text = "Load", command = loadCallBack).grid(column=0,row=0)
ttk.Button(topframe, text = "Save", command = saveCallBack).grid(column=0,row=1)

#buttonExit = tk.Button(bottomframe, text = "Exit") 

window.mainloop()