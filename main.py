from tkinter import * 
from tkinter import ttk
import cypher

class Window:

    def __init__(self, root):

        self.root = root
        # self.root.geometry("900x600")
        self.root.title("Cypher")

        self.main_frame = ttk.Frame(root, borderwidth=25, relief="raised")
        self.main_frame.grid(column=0, row=0)

        self.scale_value = IntVar()
        self.scale_value_text = StringVar()
        self.scale_value_text.set("0")
        self.sentence_text = StringVar()
        self.result_text = StringVar()

        self.f1 = ttk.Frame(self.main_frame, borderwidth=5, relief="raised")
        self.f1.grid(column=0, row=0, sticky=(N, E, W))
        self.f2 = ttk.Frame(self.main_frame, borderwidth=5, relief="raised")
        self.f2.grid(column=0, row=1, sticky=(E, W))
        self.f3 = ttk.Frame(self.main_frame, borderwidth=5, relief="raised")
        self.f3.grid(column=0, row=2, sticky=(E, W))
        self.f4 = ttk.Frame(self.main_frame, borderwidth=50, relief="raised", width=900, height=25)
        self.f4.grid(column=0, row=3)

        self.title_label = ttk.Label(self.f1, text="CAESAR CYPHER TOOL")
        self.title_label.pack()

        self.sentence_label = ttk.Label(self.f2, text="Enter your sentence below")
        self.sentence_label.grid(column=0, row=0)
        self.sentence_entry = ttk.Entry(self.f2, textvariable=self.sentence_text)
        self.sentence_entry.grid(column=0, row=1)
        self.clear_button = ttk.Button(self.f2, text="Clear", command=self.clear_text)
        self.clear_button.grid(column=0, row=2)
        
        self.shift_number_label = ttk.Label(self.f3, textvariable=self.scale_value_text)
        self.shift_number_label.grid(column=0, row=0)
        self.shift_label = ttk.Label(self.f3, text="Select your desired shift")
        self.shift_label.grid(column=0, row=1)

        self.shift_scale = ttk.Scale(self.f3, from_=-27, to=27, orient=HORIZONTAL, variable=self.scale_value, command=self.set_number_label)
        self.shift_scale.grid(column=0, row=2)
        self.shift_scale.bind("<ButtonRelease-1>", self.on_scale_release)

        self.result_label = ttk.Label(self.f4, textvariable=self.result_text)
        self.result_label.grid(column=0, row=0)

        self.main_frame.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        self.f2.grid_columnconfigure(0, weight=1)
        self.f3.grid_columnconfigure(0, weight=1)
        

    def on_scale_release(self, event):
        self.r = cypher.Caesar(self.sentence_text.get(), self.scale_value.get())
        self.result_text.set(self.r.encode())
        print(self.r.encode())

    def set_number_label(self, event):
        self.scale_value_text.set(self.scale_value.get())

    def clear_text(self):
        self.sentence_text.set("")
        self.result_text.set("")
        self.scale_value.set(0)
        self.scale_value_text.set("0")


if __name__ == "__main__":
    root = Tk()
    my_window = Window(root)
    root.mainloop()
