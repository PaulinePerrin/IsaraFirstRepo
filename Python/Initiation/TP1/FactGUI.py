from tkinter import *
from tkinter.messagebox import *
fenetre = Tk()
fenetre.title("Calcul Factorielle")
label_title = Label(fenetre, text="Entrez un nombre entier")
label_title.pack()

def calculate() :
    Fact = 1
    N = -1
    while (N < 0) : 
        ch_N = input("Quelle est la factorielle que vous voulez calculer ?\n")
        N = int(ch_N)
        if N < 0 :
            print("erreur : valeur négative interdite\n")
    if N > 0 :
        for i in range(1, N + 1) :
            Fact = Fact * i
    print("La factorielle de " + str(N) + " est " + str(Fact))

 
value = StringVar()
entree = Entry(fenetre, textvariable=value, width=30)
entree.pack()
calculate_button = Button(fenetre, text="Calculer", command=calculate)
calculate_button.pack() 
fenetre.mainloop()