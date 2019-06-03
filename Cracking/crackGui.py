try:
    from tkinter import *
    from crack import crack
except ImportError:
    print("ImportError in " + __file__)
    exit(1)


def getString():
    sTemp = entry.get()
    label2["text"] = crack(sTemp.split(' '))
    print("sTemp : {}".format(sTemp))


root = Tk()

sTemp = ""

label = Label(root, text="Enter text: ")
label2 = Label(root)
entry = Entry(root)
button = Button(root, text="Confirm", command=getString)

label.grid(row=0, column=0)
entry.grid(row=0, column=1)
button.grid(row=1, column=0)
label2.grid(row=1, column=1)

root.mainloop()
