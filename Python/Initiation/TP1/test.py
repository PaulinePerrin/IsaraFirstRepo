from tkinter import *
from tkinter.messagebox import *

window = Tk()
window.title("Calcul Factorielle")
window.geometry("480x360")
window.minsize(480, 360)
label_title = Label(window, text="Entrez un nombre entier")
label_title.pack()

def calculate() :
    Fact = 1
    N = input.get()
    try :
        N = int(N)
    except ValueError :
        showerror("La valeur entrée est invalide, veuillez saisir un nombre entier")
        
    if N == 0 :
            showinfo("Resultat du calcul", f"La factorielle de {N} est {Fact}")
    elif N < 0 :
            showerror("Vous ne pouvez pas entrer de valeurs négatives, veuillez relancer le programme")
    else :
        for i in range (1, N + 1) :
            Fact = Fact * i
            showinfo("Resultat du calcul", f"La factorielle de {N} est {Fact}")
 
value = StringVar()
input = Entry(window, textvariable=value, width=30)
input.pack()
 
calculate_button = Button(window, text="Calculer", command=calculate)
calculate_button.pack()
 
window.mainloop()