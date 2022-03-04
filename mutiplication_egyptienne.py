# NGUYEN HuuTuan 3A33

# Saisie des deux nombres à calculer
a = int(input("a = "))
b = int(input("b = "))

resultat = 0

# Décomposition de la méthode de calcul
while(b > 0):
	if(b % 2 == 0):		# Si b est pair, ..
		a += a
		b /= 2
	else:				# Sinon, ..
		resultat += a
		b -= 1


# Affichage du résultat
print(resultat)