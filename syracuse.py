# NGUYEN HuuTuan 3A33

# Saisie du nombre entier N
N = int(input("Suite de Syracuse pour N = "))

n = 0
u0 = N
temps_vol_altitude = N
indice = False
altitude_maximale = 0

print("\nu0 = %d" %u0)

# Décompostion de la méthode de la conjecture de Syracuse
while(N != 1):
	if(N % 2 == 0):		# Si Un est pair
		uN = N / 2
	else:				# Si Un est impair
		uN = (3 * N) + 1
	
	if(uN < u0 and indice == False):	# Si c'est le plus petit indice n tel que : Un+1 < U0
		temps_vol_altitude = n
		indice = True

	if(N > altitude_maximale):			# Si c'est la valeur maximale, ..
		altitude_maximale = N

	N = uN
	n = n + 1

	print('u%d = %d' %(n, N))

# Affichage des résultats de la méthode
print("\nLe temps de vol est %d." %n)
print("Le temps de vol en altitude est %d." %temps_vol_altitude)
print("L'altitude maximale est %d." %altitude_maximale)