import tkinter as tk

window = tk.Tk()
window.title('hello world')

label = tk.Label(window, text="testing")
label.pack()

button = tk.Button(window, text="click me")
button.pack()
window.mainloop()
