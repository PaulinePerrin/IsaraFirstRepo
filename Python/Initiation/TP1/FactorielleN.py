# Initialisations

Fact = 1
N = -1

# Boucler tant que N est strictement négatif

# Contrôle de saisie 
while (N < 0) :
    
    # Récupération de la valeur de N
    ch_N = input("Quelle est la factorielle que vous voulez calculer ?\n")
    #\n pour revenir à la ligne
    
    N = int(ch_N)
    # On transforme la chaîne de caractères en entier
    
    # Tester si N est négatif
    if N < 0 :
        
        # Ecrire un message
        print("erreur : valeur négative interdite\n")
        
# Tester si N > 0
if N > 0 :
    
    # Boucler
    for i in range(1, N + 1) :
        Fact = Fact * i
        
# Afficher le résultat

print("La factorielle de " + str(N) + " est " + str(Fact))