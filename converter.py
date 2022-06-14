from google_currency import convert
from tkinter import *
from tkinter.ttk import Combobox


def clicked():
    currency_from = combo_one.get()
    currency_to = combo_two.get()
    ammount = int(entry_three.get())
    result = convert(currency_from, currency_to, ammount, False)
    result_four.configure(text="{}".format(result))
    

conv = Tk()
conv.title("Currency Converter v.1.0")
conv.geometry("310x170")

field_empty =Label(conv, text="")
field_empty.grid(column=0, row=0)

field_one = Label(conv, text="From:", width=10)
field_one.grid(column=0, row=1)

field_two = Label(conv, text="To:")
field_two.grid(column =0, row=2)

field_three = Label(conv, text="Ammount:")
field_three.grid(column =0, row=3)

field_four = Label(conv, text="Result: ")
field_four.grid(column=0, row=5)

combo_one = Combobox(conv, width=20)
combo_one['values'] = ('EUR', 'USD', 'RUB', 'CNY', 'JPY')
combo_one.current(0)
combo_one.grid(column=1, row=1)
combo_one.focus()

combo_two = Combobox(conv, width=20)
combo_two['values'] = ('EUR', 'USD', 'RUB', 'CNY', 'JPY')
combo_two.current(2)
combo_two.grid(column=1, row=2)

entry_three = Entry(conv, width=21)
entry_three.grid(column=1, row=3)


result_four = Label(conv, text="", font=("Arial Bold", 20), fg='green')
result_four.grid(column=1, row=5)

btn = Button(conv, text="Convert", command=clicked)
btn.grid(column=1, row=4, padx=5, pady=5)


conv.mainloop()
