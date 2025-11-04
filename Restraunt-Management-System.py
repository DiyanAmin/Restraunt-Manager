import tkinter as tk
import tkinter.ttk as ttk


#Prices

TheMenu={'INR','USD','GBP'}
currencyExchange=1 #Changes using drp menu
happy_meal_price= 2.99*currencyExchange

r=tk.Tk()
r.geometry('400x200')
r.title('Restraunt Order')

happyMeal=tk.Label(r,text=f'Happy Meal: {happy_meal_price}').pack(pady=10)

currency=ttk.Combobox(r,).pack(pady=10)

r.mainloop()