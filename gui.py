import tkinter as tk

def calibrate():
	print('calibrate:\n')

def execute():
	print('execute:\n')

def reset():
	print('reset:\n')

def interface():
	print('interface:\n')

root = tk.Tk() #creates window
Tframe = tk.Frame(root) #creates frame in window
Tframe.pack() #packs frame into window

Bframe = tk.Frame(root)
Bframe.pack(side=tk.BOTTOM)

root.title('Chess Robot')

#cB = calibrate Button
cB = tk.Button(Tframe, text="Calibrate", bg="yellow", command=calibrate)
cB.pack(side=tk.LEFT)

eB = tk.Button(Tframe, text="Execute", bg="green", command=execute)
eB.pack(side=tk.LEFT)

rB = tk.Button(Tframe, text="Reset", bg="purple", command=reset)
rB.pack(side=tk.LEFT)

iB = tk.Button(Tframe, text="Interface", bg="blue", command=interface)
iB.pack(side=tk.LEFT)

qB = tk.Button(Bframe, text="QUIT", fg="red", command=quit)
qB.pack()


root.mainloop()
