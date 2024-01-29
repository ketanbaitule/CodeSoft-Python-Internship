import math
import tkinter as tk
import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.font = ctk.CTkFont("poppins", size=25)
        self.title("Calculator")
        ctk.set_appearance_mode("dark")

        # Input box
        self.input = ctk.CTkEntry(self, font=self.font, fg_color="gray14", bg_color="gray14", border_width=0, text_color="white", placeholder_text="0", justify="right")
        # self.input.cget("font").configure(size=48)
        self.input.grid(row=0, column=0, columnspan=4, sticky="ew", padx= 10, pady=12)

        number_input_style = {
            "fg_color":"#303136",
            "text_color": "#29A8FF",
            "width": 60,
            "height": 62,
            "font": self.font,
            "border_spacing": 5,
            "corner_radius": 16
        } 

        placement={
            "padx": 10,
            "pady": 12
        }

        for i in range(9, 0, -1):
            new_placement={
                "row": 3-math.ceil(i / 3) + 1+1,
                "column": math.floor(i % 3) - 1 if math.floor(i % 3) != 0 else 2,
                **placement
            }
            self.add_btn(i, style=number_input_style, placement=new_placement, onclick=lambda i=i: self.add(str(i)))
        
        # 0
        self.add_btn(0, style=number_input_style, placement={**placement, "row":5, "column": 0, "columnspan":2, "sticky": "we"}, onclick=lambda : self.add(0))
        self.add_btn(".", style=number_input_style, placement={**placement, "row":5, "column": 2}, onclick=lambda : self.add("."))
        # Operations
        self.add_btn("C", style=number_input_style, placement={**placement, "row":1, "column": 0}, onclick=lambda : self.clear())
        self.add_btn("X", style=number_input_style, placement={**placement, "row":1, "column": 1}, onclick=lambda : self.last_clear())
        self.add_btn("/", style=number_input_style, placement={**placement, "row":1, "column": 2}, onclick=lambda : self.add("/"))
        self.add_btn("*", style=number_input_style, placement={**placement, "row":1, "column": 3}, onclick=lambda : self.add("*"))
        self.add_btn("-", style=number_input_style, placement={**placement, "row":2, "column": 3}, onclick=lambda : self.add("-"))
        self.add_btn("+", style=number_input_style, placement={**placement, "row":3, "column": 3}, onclick=lambda : self.add("+"))
        self.add_btn("=", style=number_input_style, placement={**placement, "row":4, "column": 3, "rowspan":2, "sticky": "ns"}, onclick=self.ans)


    
    def add_btn(self, label, style, placement, onclick):
        btn = ctk.CTkButton(self, text=label, command=onclick,  **style)
        btn.grid(**placement)
    
    def add(self, data):
        self.input.insert(tk.END, data)
    
    def clear(self):
        self.input.delete(0, tk.END)
    
    def last_clear(self):
        self.input.delete(self.input.index("end") - 1)
    
    def ans(self):
        try:
            result= eval(self.input.get())
            self.clear()
            self.input.insert(0,result)
        except:
            print("An Error Occured")

app = App()
app.mainloop()