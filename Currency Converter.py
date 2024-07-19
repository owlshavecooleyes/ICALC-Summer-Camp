from tkinter import *
from tkinter import ttk

class CurrencyConverter:
    def __init__(self):
        self.currencies = dict()
        with open("currency.py", encoding="utf-8") as file:
            for line in file:
                line = line.rstrip("\n")
                currency, rate = line.split(":")
                self.currencies[currency] = float(rate)

    def convert(self, from_currency, to_currency, amount):
        if from_currency != "USD":
            amount = amount / self.currencies[from_currency]  #  Calculate amount in USD
        amount = amount * self.currencies[to_currency]
        amount = round(amount, 2)
        return amount


class App(Tk):
    def __init__(self, converter):
        Tk.__init__(self)
        self.title("Currency Converter")
        self.my_converter = converter
        #  set background color and size
        self.config(bg="lightblue")
        self.geometry("800x400")
        #  Title
        self.intro_label = Label(self, text="Currency Converter")
        self.intro_label.config(font=("Courier", 15, "bold"))
        self.intro_label.place(x=300, y=5)
        #  Entry Box
        self.amount = Entry(self, bd=3, justify=CENTER)
        self.amount.place(x=330, y=150)
        self.amount_label = Label(self, text="Type Amount", relief=RIDGE, bg="yellow")
        self.amount_label.config(font=("Courier", 12, "bold"))
        self.amount_label.place(x=330, y=120)
        #  DropDown List
        self.from_currency_list = StringVar(self)
        self.from_currency_list.set("CAD")
        self.to_currency_list = StringVar(self)
        self.to_currency_list.set("USD")
        # Make the dropdown list
        self.option_add("*TCombobox*Listbox.font", ("Courier", 12))
        self.from_currency_dropdown = ttk.Combobox(self, textvariable=self.from_currency_list,values=list(self.my_converter.currencies.keys()))
        self.from_currency_dropdown.place(x=270,y=200)
        self.to_currency_dropdown = ttk.Combobox(self, textvariable=self.to_currency_list,values=list(self.my_converter.currencies.keys()))
        self.to_currency_dropdown.place(x=480,y=200)
        # Convert Button
        self.convert_button = Button(self,text="Convert",command=self.do_convert)
        self.convert_button.config(font=('Courier',12))
        self.convert_button.place(x=350,y=250)
        #show converted amount
        self.converted=Label(self,text="",relief=RIDGE,bg='white',fg='red')
        self.converted.config(font=('Courier',14,'bold'))
        self.converted.place(x=450,y=250)

    def do_convert(self):
        # 1.read user input
        amount = self.amount.get()
        from_curr = self.from_currency_dropdown.get()
        to_curr = self.to_currency_list.get()
        #2. use convert function
        result = self.my_converter.convert(from_currency,to_curr,amount)
        self.converted.config(text=str(result))

# launch our application
my_converter = CurrencyConverter()
App(my_converter)
mainloop()
