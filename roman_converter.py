from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import re


def clear():
	roman_entry.delete(0,END)
	number_entry.delete(0,END)

def converter(*args):

	if number_entry.get():
		if number_entry.get().isdigit() and int(number_entry.get()) in range(1,1000000):
			return ToRoman(int(number_entry.get()))
		else:messagebox.showwarning(message="Number should be in the range of 1-1000000")
	elif roman_entry.get():
		return check(roman_entry.get().upper())

# This function validates the user given roman numeral.
def check(x):

	pattern = re.search(r'^(M{0,3})(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$', x)
	if pattern != None:
		return ToInteger(x)
	else:
		messagebox.showwarning(message="Invalid input")

# This function converts a roman numeral to a number.
def ToInteger(word):

	d=dict(zip(['M','D','C','L','X','V','I'],[1000,500,100,50,10,5,1]))		
	integer = 0  
	while word:
		if len(word)==1 or d[word[0]] >= d[word[1]]:
			integer += d[word[0]]   
			word = word[1:]      
		else: 
			integer += (d[word[1]] - d[word[0]])     
			word = word[2:]		

	number.set(integer)


# This function converts a number into a roman numeral.
def ToRoman(number):
	
	x=list(zip(['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I'],[1000,900,500,400,100,90,50,40,10,9,5,4,1]))

	word=''
	for letter,integer in x:
		while number >= integer:      
			word += letter        
			number -= integer   
	
	roman.set(word)
		

root = Tk()
root.title("Roman Converter")
root.resizable(width=False,height=False)

frame=ttk.Frame(root, relief='ridge', padding = "8 12 8 12")
frame.grid()

roman = StringVar()
number = StringVar()

roman_entry = ttk.Entry(frame, textvariable = roman)
roman_entry.config(font=("verdana",'12','bold'),foreground="blue")
roman_entry.grid(row=2,column=2)

number_entry = ttk.Entry(frame, textvariable = number)
number_entry.config(font=("verdana",'12','bold'),foreground='blue')
number_entry.grid(row=1, column=2)

roman_label = ttk.Label(frame, text="Roman", relief = 'ridge')
roman_label.config(font=("verdana","12","bold italic"),foreground = 'white', background = 'black')
roman_label.grid(row=2,column=1)

number_label = ttk.Label(frame, text="Number", relief = 'ridge')
number_label.config(font=("verdana",'12','bold italic'),foreground = 'white', background = 'black')
number_label.grid(row=1, column=1)

button1 = ttk.Button(frame, text="Convert", command=converter, width=15)
button1.grid(row=3, column=2,sticky="W")

button2 = ttk.Button(frame, text="Clear", command=clear, width=15)
button2.grid(row=3, column=2,sticky="E")

button3 = ttk.Button(frame,text = "Exit",width = 15,command = root.destroy)
button3.grid(row=3, column=1,sticky="W")

for child in frame.winfo_children():
	child.grid_configure(padx=10,pady=10)

number_entry.focus()
root.bind("<Return>", converter)

root.mainloop()
