from tkinter import *
from adventure import *


class MainDisplay:
    def __init__(self):
        root = Tk()  # create root window
        root.title("Python Adventure")  # title of the GUI window
        root.maxsize(900, 600)  # specify the max size the window can expand to
        root.config(bg="skyblue")  # specify background color

        # Create left and right frames
        left_frame = Frame(root, width=200, height=400, bg='grey')
        left_frame.grid(row=0, column=0, padx=10, pady=5)

        right_frame = Frame(root, width=450, height=400, bg='grey')
        right_frame.grid(row=0, column=1, padx=10, pady=5)

        # Description area
        description_label = Label(
            left_frame, text="description label", wraplength=200)
        description_label.grid(row=0, column=0, padx=15, pady=15)

        # Create tool bar frame
        tool_bar = Frame(left_frame, width=180, height=185)
        tool_bar.grid(row=2, column=0, padx=20, pady=20)

        # Create Weath Display
        # Description area
        wealth_label = Label(
            left_frame, text="", wraplength=200)
        wealth_label.grid(row=3, column=0, padx=15, pady=15)

        # Create Image Frame
        img_label = Label(right_frame, image='')
        img_label.grid(
            row=0, column=0, padx=5, pady=5)

        self.root = root
        self.left_frame = left_frame
        self.right_frame = right_frame
        self.tool_bar = tool_bar
        self.img_label = img_label
        self.description_label = description_label
        self.wealth_label = wealth_label

    def display_node(self, node: AdventureNode):
        image = PhotoImage(file=node.img)
        self.img_label.configure(image=image)
        self.img_label.image = image

    def set_choice(self, node: AdventureNode):
        self.node = node

        self.display_node(node)

        # Update description label
        self.description_label.configure(text=node.description)

        # Clear toolbar frame
        for widget in self.tool_bar.winfo_children():
            widget.destroy()

        # Build buttons
        for idx, choice in enumerate(node.choices):
            image_button = Button(self.tool_bar, text=choice.text,
                                  command=lambda c=choice: self.set_choice(c.next_node))
            image_button.grid(row=idx, column=0, padx=5, pady=5)

        # Fire events
        node.fire_on_arrive()

    def set_wealth(self, wealth: int):
        self.wealth_label.configure(text='Wealth: ' + str(wealth))

    def start(self):
        self.root.mainloop()
