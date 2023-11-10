from tkinter import *

root = Tk()  # create root window
root.title("Tkinter Example")  # title of the GUI window
root.maxsize(900, 600)  # specify the max size the window can expand to
root.config(bg="skyblue")  # specify background color

# Create left and right frames
left_frame = Frame(root, width=200, height=400, bg='grey')
left_frame.grid(row=0, column=0, padx=100, pady=50)


# Create frames and labels in left_frame
Label(left_frame, text="Hello World!").grid(row=1, column=1, padx=5, pady=5)

root.mainloop()
