from tkinter import * 
from tkinter import ttk
import cypher

class Window:
    
    def __init__(self, root):
        
        self.root = root
        self.root.geometry("860x560+397+243")
        self.root.minsize(148, 1)
        self.root.maxsize(1924, 1055)
        self.root.resizable(0, 0)
        self.root.title("Caesar Cypher Tool")

        self.scale = IntVar()
        self.scale_value = IntVar()
        
        self.Text1 = Text(self.root)
        self.Text1.place(relx=0.081, rely=0.606, relheight=0.282, relwidth=0.591)

        self.Text1.configure(background="white")
        self.Text1.configure(font="TkTextFont")
        self.Text1.configure(foreground="black")
        self.Text1.configure(highlightbackground="#d9d9d9")
        self.Text1.configure(highlightcolor="black")
        self.Text1.configure(insertbackground="black")
        self.Text1.configure(selectbackground="blue")
        self.Text1.configure(selectforeground="white")
        self.Text1.configure(wrap="word")

        self.TEntry1 = Text(self.root)
        self.TEntry1.configure(font="TkTextFont")
        self.TEntry1.place(relx=0.083, rely=0.157, relheight=0.278, relwidth=0.586)

        self.TLabel1 = ttk.Label(self.root, text='''Insert your sentence below''')
        self.TLabel1.place(relx=0.081, rely=0.107, height=24, width=184)
        self.TLabel1.configure(font="TkDefaultFont")
        self.TLabel1.configure(relief="flat")
        self.TLabel1.configure(anchor='w')
        self.TLabel1.configure(justify='left')

        self.TLabel2 = ttk.Label(self.root, text='''Here is the result''')
        self.TLabel2.place(relx=0.081, rely=0.553, height=24, width=138)
        self.TLabel2.configure(font="TkDefaultFont")
        self.TLabel2.configure(relief="flat")
        self.TLabel2.configure(anchor='w')
        self.TLabel2.configure(justify='left')

        self.Label1 = ttk.Label(self.root)
        self.Label1.place(relx=0.788, rely=0.178, height=26, width=79)
        self.Label1.configure(text='''Select shift''')

        self.Label2 = ttk.Label(self.root, textvariable=self.scale_value)
        self.Label2.place(relx=0.892, rely=0.178, height=26, width=42)

        self.TButton1 = ttk.Button(self.root, command=lambda: self.code('encode'))
        self.TButton1.place(relx=0.336, rely=0.446, height=30, width=98)
        self.TButton1.configure(takefocus="")
        self.TButton1.configure(text='''Encode''')

        self.TButton2 = ttk.Button(self.root, command=self.clear_text)
        self.TButton2.place(relx=0.081, rely=0.446, height=30, width=98)
        self.TButton2.configure(takefocus="")
        self.TButton2.configure(text='''Clear''')

        self.TScale1 = ttk.Scale(self.root, from_=26, to=-26, variable=self.scale, command=self.set_int_scale_val)
        self.TScale1.place(relx=0.823, rely=0.267, relwidth=0.0, relheight=0.57, width=26, bordermode='ignore')
        self.TScale1.configure(orient="vertical")
        self.TScale1.configure(takefocus="")

        self.TButton3 = ttk.Button(self.root, command=lambda: self.code('decode'))
        self.TButton3.place(relx=0.209, rely=0.446, height=30, width=98)
        self.TButton3.configure(takefocus="")
        self.TButton3.configure(text='''Decode''')
        

    def code(self, m):

        self.sentence = self.TEntry1.get("1.0",'end-1c')
        if m == 'encode':
            self.message = cypher.Caesar(self.sentence, self.scale_value.get()).encode()
        elif m == 'decode':
            self.message = cypher.Caesar(self.sentence, (self.scale_value.get()*-1)).encode()
        self.Text1.delete("1.0", END)
        self.Text1.insert(END, self.message)

    def set_int_scale_val(self, event):
        self.scale_value.set(int(float(self.scale.get())))

    def clear_text(self):
        self.TEntry1.delete("1.0", END)
        self.Text1.delete("1.0", END)
        self.scale.set(0)
        self.scale_value.set(0)
        


if __name__ == "__main__":
    root = Tk()
    my_window = Window(root)
    root.mainloop()
