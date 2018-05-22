import tkinter as tk

def calibrate():
	print('calibrate')

def execute():
	print('execute')

def reset():
	print('reset')

def interface():
	print('interface')

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()


#cB = calibrate Button
cB = tk.Button(frame, text="Calibrate", command=calibrate)
cB.pack(side=tk.LEFT)

eB = tk.Button(frame, text="Execute", command=execute)
eB.pack(side=tk.LEFT)

rB = tk.Button(frame, text="Reset", command=reset)
rB.pack(side=tk.LEFT)

iB = tk.Button(frame, text="Interface", command=interface)
iB.pack(side=tk.LEFT)

qB = tk.Button(frame, text="QUIT", fg="red", command=quit)
qB.pack(side=tk.LEFT)


root.mainloop()
