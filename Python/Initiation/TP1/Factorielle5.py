# On va utiliser la boucle for car la boucle se termine à la fin d’un intervalle.
# On connait la valeur de n donc on sait combien de fois on va tourner dans la boucle. Au moment ou on démarre la boucle, on sait
# qu’on va faire n tours, on connait le nombre de tours.

Fact = 1
N = 5
i = 1
for i in range (1, 6, 1) :
# i = 1 n'est pas indipensable dans la mesure où on le précise dans le range
    Fact = Fact * i
Resultat = str(Fact)
print("La factorielle de "+ str(N) + " est "+ Resultat)
