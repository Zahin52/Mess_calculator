import math
from tkinter import *
from tkinter import ttk

root=Tk()

root.title("Mess calculator")
def Bazar(self):
    fixed = 2375
    spent=float(spenta.get())
    meal=float(meala.get())
    

    spenth = float(spentH.get())
    mealh = float(mealH.get())
   

    spentt = float(spentT.get())
    mealt = float(mealT.get())
    

    spentz = float(spentZ.get())
    mealz = float(mealZ.get())
    
    mealrate = (spent + spenth + spentt + spentz) / (meal + mealh + mealt + mealz)

    a = str(fixed - spent  + (mealrate*meal))
    h = str(fixed - spenth + (mealrate*mealh))
    t = str(fixed - spentt + (mealrate*mealt))
    z = str(fixed - spentz + (mealrate*mealz))

    totala.delete(0, "end")
    totala.insert(0,a)

    totalH.delete(0, "end")
    totalH.insert(0,h)


    totalT.delete(0, "end")
    totalT.insert(0,t)

    totalZ.delete(0, "end")
    totalZ.insert(0,z)



Label(root,text="AYON").grid(row=0,column=1)
Label(root,text="spent").grid(row=1,column=0)
spenta = Entry(root)
spenta.grid(row=2,column=0)

Label(root,text="meal").grid(row=1,column=1)
meala=Entry(root)
meala.grid(row=2,column=1)

Label(root,text="Have to Pay").grid(row=1,column=2)
totala=Entry(root)
totala.grid(row=2,column=2)



Label(root,text="Himo").grid(row=3,column=1)
Label(root,text="spent").grid(row=4,column=0)
spentH = Entry(root)
spentH.grid(row=5,column=0)

Label(root,text="meal").grid(row=4,column=1)
mealH=Entry(root)
mealH.grid(row=5,column=1)

Label(root,text="Have to Pay").grid(row=4,column=2)
totalH=Entry(root)
totalH.grid(row=5,column=2)


Label(root,text="Tajbi").grid(row=6,column=1)
Label(root,text="spent").grid(row=7,column=0)
spentT = Entry(root)
spentT.grid(row=8,column=0)

Label(root,text="meal").grid(row=7,column=1)
mealT=Entry(root)
mealT.grid(row=8,column=1)

Label(root,text="Have to Pay").grid(row=7,column=2)
totalT=Entry(root)
totalT.grid(row=8,column=2)

Label(root,text="Zahin").grid(row=9,column=1)
Label(root,text="spent").grid(row=10,column=0)
spentZ = Entry(root)
spentZ.grid(row=11,column=0)

Label(root,text="meal").grid(row=10,column=1)
mealZ=Entry(root)
mealZ.grid(row=11,column=1)

Label(root,text="Have to Pay").grid(row=10,column=2)
totalZ=Entry(root)
totalZ.grid(row=11,column=2)


equalbutton=Button(root,text="=")
equalbutton.bind("<Button-1>",Bazar)
equalbutton.grid(row=12,column=2)


root.mainloop()






