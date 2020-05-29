# @title : Password Generateur 
# @auteur :  walid.menghour
# @Date : 10/05/2020
#
#
from tkinter import *
from random import choice
from tkinter import font
from tkinter import messagebox
# ============== Code ========================
root = Tk()
root.title("Password Generateur")
root.geometry("800x630")
windowWidth = root.winfo_reqwidth()
windowHeight = root.winfo_reqheight()
positionRight = int(root.winfo_screenwidth() / 2 - windowWidth)
positionDown = int(root.winfo_screenheight() / 2 - windowHeight)
root.geometry(f"800x630+{positionRight-220}+{positionDown-150}")
root.configure(bg='#00b894')
root.resizable(False, False)
root.bind("x", quit)
# ====================================================
# Declaration var
# ====================================================
bgc = "#00b894"  # fildes color
bgbtnc = "#636e72"
choice_lev = IntVar()
sizepass = IntVar()
sizepass.set(0)
nbpass = IntVar()
nbpass.set(0)
TabC = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'i', 'v',
        'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
        'S', 'T', 'I', 'V', 'W', 'X', 'Y', 'Z']
TabS = ['!', '.', '#']
TabN = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
Tab = []
l = []

# ====================================================
# Declaration Function
# ====================================================
def quit(*args):
    root.destory()
def Clear():
    l = []
    Listpass.delete(0, END)
    ennbpass.delete(0, END)
    btn1.configure(stat="disable")
    choice_lev.set(1)
    sizepass.set(1)
    nbpass.set(1)
def GiveMeo():
    return (choice_lev.get())
def saveinfile():
    f = open("PasswordsGenere.txt", "a")
    for i in l:
        f.write(i + "\n")
    messagebox.showinfo("Save in File", "Successful \nSaving passwords in file")

def whatischoise():
    l.clear()
    ch = choice_lev.get()
    if (ch == 1):
        Tab.extend(TabN)
    elif (ch == 2):
        Tab.extend(TabN)
        Tab.extend(TabC)
    elif (ch == 3):
        Tab.extend(TabC)
        Tab.extend(TabS)
        Tab.extend(TabN)
    else:
        messagebox.showwarning("Warning", "SVP CHOISE LA COMPLEXICITY\nOn va Genere des password de bon qualit")
        Clear()
        ch = 1
        nbpass.set(0)

def Genere():
    num = nbpass.get()
    T = sizepass.get()
    ch = choice_lev.get()

    whatischoise()
    if (T == None):
        T = 1
    if (num == None):
        num = 1
    Listpass.delete(0, END)

    x = 0
    for i in range(num): 
        strpass = ""

        for i in range(T):  
            strpass += choice(Tab)
        l.append(strpass)
        Listpass.insert(x, strpass)
        x += 1
    l.clear()
    for i in enumerate(l, 1):
        print(i, "\n")
    btn1.configure(stat='normal')
    btn2.configure(stat='normal')

# ====================================================
# Declaration Layuat
# ====================================================


# Labeles
fnttitre = font.Font(family='Roboto', size=20, weight='bold')
fnttext = font.Font(family='Roboto', size=14, weight='bold')
fnttextbtn = font.Font(family='Roboto', size=14, weight='bold')
fnttextch = font.Font(family='Roboto', size=14, weight='bold')
lbtitre = Label(root, text="Password Generateur", font=fnttitre, bg="#00cec9", padx=30, pady=30)
lbtitre.grid(row=0, column=1, columnspan=3)
lbsize = Label(root, text="length of Passwords :", font=fnttext, bg=bgc)
lbsize.grid(row=3, column=1, pady=20)
lbnbps = Label(root, text="Number of Passwords :", font=fnttext, bg=bgc)
lbnbps.grid(row=4, column=1, pady=10)
lbchcomp = Label(root, text="Complexity of Passwords :", font=fnttext, bg=bgc)
lbchcomp.grid(row=5, column=1)
# Entry



ensizepass=Spinbox(root,from_=1,to=100,textvariable=sizepass)
ensizepass.grid(row=3, column=2)

ennbpass=Spinbox(root,from_=1,to=100,textvariable=nbpass)
ennbpass.grid(row=4, column=2)


# Radiobutton
R1 = Radiobutton(root, text="Weak ", variable=choice_lev, value=1, command=GiveMeo, font=fnttextch, bg=bgc)
R1.grid(row=6, column=1, columnspan=3)
R2 = Radiobutton(root, text="Average", variable=choice_lev, value=2, command=GiveMeo, font=fnttextch, bg=bgc)
R2.grid(row=7, column=1, columnspan=3)
R3 = Radiobutton(root, text="strong", variable=choice_lev, value=3, command=GiveMeo, font=fnttextch, bg=bgc)
R3.grid(row=8, column=1, columnspan=3)

lblistepass = Label(root, text="100")
Listpass = Listbox(root, width=144, bg=bgc)
Listpass.grid(row=9, column=0, padx=20, pady=10, columnspan=20, rowspan=3)

btn0 = Button(root, text="Generate", padx=20, pady=10, relief=GROOVE, font=fnttextbtn, command=Genere)
btn0.grid(row=12, column=0)
btn1 = Button(root, text="Save in File", padx=20, pady=10, relief=GROOVE, font=fnttextbtn, command=saveinfile)
btn1.grid(row=12, column=1)
btn2 = Button(root, text="Clear", padx=20, pady=10, relief=GROOVE, font=fnttextbtn, command=Clear)
btn2.grid(row=12, column=2)

btn1.configure(stat='disable')
btn2.configure(stat='disable')


root.mainloop()
