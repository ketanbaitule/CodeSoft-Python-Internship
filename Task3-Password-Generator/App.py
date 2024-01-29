import random
import customtkinter as ctk
import tkinter as tk
import string

ctk.set_appearance_mode("dark") 

class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Password Generator")
        ctk.CTkLabel(self, text="Password Generator", font=ctk.CTkFont(size=27, weight="bold")).grid(row=0, column=0, columnspan=4, sticky="ew", pady=20)

        passwordLengthLabel = ctk.CTkLabel(self, text="Length Of Password")
        passwordLengthLabel.grid(row=1, column=0, padx=20, pady=20, sticky="ew")
        
        self.passwordLengthVar = tk.IntVar(self, 5)

        self.passwordLengthSlider = ctk.CTkSlider(self, from_=4, to=100, variable=self.passwordLengthVar)
        self.passwordLengthSlider.grid(row=1, column=1, columnspan=2, padx=20, pady=20, sticky="ew")

        self.passwordLengthValue = ctk.CTkLabel(self, textvariable=self.passwordLengthVar)
        self.passwordLengthValue.grid(row=1, column=3, sticky="w")

        includeLabel = ctk.CTkLabel(self, text="Character Types")
        includeLabel.grid(row=3, column=0, padx=20, pady=20, sticky="ew")

        # Choice Character Type        
        self.lower_char = ctk.CTkCheckBox(self, text="Lower Char")
        self.lower_char.grid(row=3, column=1, padx=20, pady=20, sticky="ew")
        
        self.upper_char = ctk.CTkCheckBox(self, text="Upper Char")
        self.upper_char.grid(row=3, column=2, padx=20, pady=20, sticky="ew")
        
        self.digits = ctk.CTkCheckBox(self, text="Digits")
        self.digits.grid(row=4, column=1, padx=20,
                         pady=20, sticky="ew")
        
        self.punctuation = ctk.CTkCheckBox(self, text="Punctuation")
        self.punctuation.grid(row=4, column=2, padx=20, pady=20, sticky="ew")


        self.generatePasswordButton = ctk.CTkButton(self, text="Generate Password", command=self.generatePasswordFunc)
        self.generatePasswordButton.grid(row=5, column=1, columnspan=2, padx=20, pady=20, sticky="ew")

        self.passwordDisplayBox = ctk.CTkTextbox(self, width=200, height=100)
        self.passwordDisplayBox.grid(row=6, column=0, columnspan=4, padx=20, pady=20, sticky="nsew")
    
    def generatePasswordFunc(self):
        lengthOfPassword = self.passwordLengthVar.get()
        includeLower = self.lower_char.get()
        includeUpper = self.upper_char.get()
        includeDigit = self.digits.get()
        includePunctuation = self.punctuation.get()

        password = self.generatePassword(lengthOfPassword, includeLower, includeUpper, includeDigit, includePunctuation)
        self.passwordDisplayBox.delete("0.0", "end") 
        self.passwordDisplayBox.insert("0.0", password)

    def generatePassword(self, length, includeLower, includeUpper, includeDigit, includePunctuation):
        selection_list = ''
        password = ''
        try:
            if includeLower:
                selection_list += string.ascii_lowercase
                password += random.choice(string.ascii_lowercase)
            if includeUpper:
                selection_list += string.ascii_uppercase
                password += random.choice(string.ascii_uppercase)
            if includeDigit:
                selection_list += string.digits
                password += random.choice(string.digits)
            if includePunctuation:
                selection_list += string.punctuation
                password += random.choice(string.punctuation)
            
            for _ in range(length - len(password)):
                password += random.choice(selection_list)
            
            password=list(password)
            
            random.shuffle(password)
            password = ''.join(password)
        except:
            print("Error Occured")
        finally:
            return password

        


if __name__ == "__main__":
    app = App()
    app.mainloop()
