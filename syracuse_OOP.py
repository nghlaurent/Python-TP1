# NGUYEN HuuTuan 3A33

# Classe méthode de Syracuse, en OOP
class Syracuse_OOP(object):
	# Fonction, utilisant la suite de Syracuse, avec le nombre entier N, donné en paramètre
	def Conjecture(N):
		n = 0
		u0 = N
		temps_vol_altitude = N
		indice = False
		altitude_maximale = 0

		# Utilisation d'un fichier, avec l'aide de la déclaration "with"
		with open("Syracuse_Resultat.txt", "w") as fichier:
			fichier.write("u0 = %d\n" %u0)

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

				fichier.write("u%d = %d\n" %(n, N))

			# Écriture des résultats de la méthode dans le fichier texte de sortie
			fichier.write("\nLe temps de vol est %d.\n" %n)
			fichier.write("Le temps de vol en altitude est %d.\n" %temps_vol_altitude)
			fichier.write("L'altitude maximale est %d." %altitude_maximale)


# Saisie du nombre entier N
N = int(input("Suite de Syracuse pour N = "))

# Application de la conjecture de Syracuse, selon N
Syracuse_OOP.Conjecture(N)