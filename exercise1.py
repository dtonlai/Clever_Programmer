import tkinter as tk
from PIL import Image, ImageTk

#Root/Frames
root = tk.Tk()
root.title("Invoice App")

#Class

#Functions


#Image Properties
invoiceImage = Image.open('/Users/david-ton-lai/PycharmProjects/CP_Python_OOP/Images/invoice.jpg')
invoiceImage.thumbnail((100,160), Image.ANTIALIAS)
tkInvoiceImage = ImageTk.PhotoImage(invoiceImage)
labelImage = tk.Label(image=tkInvoiceImage)
labelImage.grid(column=4, row=0, rowspan=6)

#Variables
subjectEntered = tk.StringVar()
hourEntered = tk.StringVar()
amountEntered = tk.StringVar()
paidStatus = tk.BooleanVar()

#Widgets
subjectLabel = tk.Label(root, text="Lesson Subject")
subjectLabel.grid(column=0, row=0, sticky=tk.W)

subjectEntry = tk.Entry(root)
subjectEntry.grid(column=1, row=0, columnspan=2)

hourLabel = tk.Label(root, text="Hours")
hourLabel.grid(column=0, row=1, sticky=tk.W)

hourEntry = tk.Entry(root)
hourEntry.grid(column=1, row=1, columnspan=2)

amountLabel = tk.Label(root, text="Amount")
amountLabel.grid(column=0, row=2, sticky=tk.W)

amountEntry = tk.Entry(root)
amountEntry.grid(column=1, row=2, columnspan=2)

paidLabel = tk.Label(root, text="Paid")
paidLabel.grid(column=0, row=3, sticky=tk.W)

paidYesRadio = tk.Radiobutton(root, text="Yes", variable=paidStatus, value="True")
paidNoRadio = tk.Radiobutton(root, text="No", variable=paidStatus, value="False")

paidYesRadio.grid(column=1, row=3)
paidNoRadio.grid(column=2, row=3)

notesLabel = tk.Label(root, text="Notes")
notesLabel.grid(column=0, row=4, sticky=tk.W)

submitButton = tk.Button(root, text="Submit")
submitButton.grid(column=1, row=6, columnspan=2)


root.mainloop()

