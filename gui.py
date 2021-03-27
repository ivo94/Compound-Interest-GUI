from tkinter import *
from tkinter import ttk
import tkinter.font as font
# =============================================================================
# Functions
# =============================================================================
def compoundInterest(a, b, c, d, e, f):
    initialAmount_ = float(a.get())
    interest_ = float(b.get())
    times_= int(float(c.get()))
    partialAmount = initialAmount_
    try:
        for i in range(times_):
            partialAmount = partialAmount + partialAmount * (interest_/100)
        d.set(round(partialAmount,2))
        e.set(round(float(d.get()) - initialAmount_, 2))
        f.set(round(float(e.get())/initialAmount_ * 100,2))
    except ValueError:
        pass
# =============================================================================
# Initializes the main window
# =============================================================================
root = Tk()
root.title("Compound Interest Calculator")
root.geometry("500x430")
#root.config(background="light gray")
# =============================================================================
# Variables 
# =============================================================================
initialAmount = StringVar()
interest = StringVar()
times = StringVar()
finalAmount = StringVar()
netProfit = StringVar()
perProfit = StringVar()

initialAmount2 = StringVar()
interest2 = StringVar()
times2 = StringVar()
finalAmount2 = StringVar()
netProfit2 = StringVar()
perProfit2 = StringVar()
# =============================================================================
# Creates the structure of strategy 1
# =============================================================================
firstTitle = Label(root, text="Strategy 1")
firstTitle.grid(row=0, column=0)
initialLabel = Label(root, text="Initial amount")
initialLabel.grid(row=1, column=0)
interestLabel = Label(root, text="Interest")
interestLabel.grid(row=2, column=0)
timesLabel = Label(root, text="Times")
timesLabel.grid(row=3, column=0)

initialEntry = Entry(root, textvariable=initialAmount)
initialEntry.grid(row=1, column=1)
interestEntry = Entry(root, textvariable=interest)
interestEntry.grid(row=2, column=1)
timesEntry = Entry(root, textvariable=times)
timesEntry.grid(row=3, column=1)

secondTitle = Label(root, text="Results")
secondTitle.grid(row=0, column=3)
finalLabel = Label(root, text="Final amount")
finalLabel.grid(row=1, column=3)
netProfitLabel = Label(root, text="Net profit")
netProfitLabel.grid(row=2, column=3)
perProfitLabel = Label(root, text="% Profit")
perProfitLabel.grid(row=3, column=3)

finalLabel = Label(root, textvariable=finalAmount)
finalLabel.grid(row=1, column=4)
netLabel = Label(root, textvariable=netProfit)
netLabel.grid(row=2, column=4)
perLabel = Label(root, textvariable=perProfit)
perLabel.grid(row=3, column=4)

calculateButton = Button(root, text="Calculate", 
                         command=lambda: compoundInterest(initialAmount, interest, times, finalAmount, netProfit, perProfit))
calculateButton.grid(row=4, column=0)

#clearButton = Button(root, width=7, text="Clear", command=clear)
#clearButton.grid(row=4, column=1)
# =============================================================================
# Creates the structure of strategy 2
# =============================================================================
firstTitle2 = Label(root, text="Strategy 2")
firstTitle2.grid(row=5, column=0)
initialLabel2 = Label(root, text="Initial amount")
initialLabel2.grid(row=6, column=0)
interestLabel2 = Label(root, text="Interest")
interestLabel2.grid(row=7, column=0)
timesLabel2 = Label(root, text="Times")
timesLabel2.grid(row=8, column=0)

initialEntry2 = Entry(root, textvariable=initialAmount2)
initialEntry2.grid(row=6, column=1)
interestEntry2 = Entry(root, textvariable=interest2)
interestEntry2.grid(row=7, column=1)
timesEntry2 = Entry(root, textvariable=times2)
timesEntry2.grid(row=8, column=1)

secondTitle2 = Label(root, text="Results")
secondTitle2.grid(row=5, column=3)
finalLabel2 = Label(root, text="Final amount")
finalLabel2.grid(row=6, column=3)
netProfitLabel2 = Label(root, text="Net profit")
netProfitLabel2.grid(row=7, column=3)
perProfitLabel2 = Label(root, text="% Profit")
perProfitLabel2.grid(row=8, column=3)

finalLabel2 = Label(root, textvariable=finalAmount2)
finalLabel2.grid(row=6, column=4)
netLabel2 = Label(root, textvariable=netProfit2)
netLabel2.grid(row=7, column=4)
perLabel2 = Label(root, textvariable=perProfit2)
perLabel2.grid(row=8, column=4)

calculateButton = Button(root, text="Calculate", 
                         command=lambda: compoundInterest(initialAmount2, interest2, times2, finalAmount2, netProfit2, perProfit2))
calculateButton.grid(row=9, column=0)
# =============================================================================
# If return is hit, execute compoundInterest
# =============================================================================
root.bind('<Return>', lambda key: compoundInterest(initialAmount, interest, times, finalAmount, netProfit, perProfit))
# =============================================================================
# The cursor starts in Initial amount
# =============================================================================
initialEntry.focus()
# =============================================================================
# Some padding to all of root's children
# =============================================================================
for child in root.winfo_children():
    child.grid_configure(padx=10, pady=10)
    #child.configure(background="light gray")
    
root.mainloop()