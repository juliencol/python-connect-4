def Danger (M,J):

	for i in range (1,7):

		#i est la colonne

		#k est la ligne

		k=J[i][2]

	#danger à droite

		#compt fait varier la colonne

		compt=i
		compt+=1

		while M[k][compt]=1 and compt<=7:

			compt+=1
			J[i][3]+=1

	#danger à gauche

		#compt fait varier la colonne

		compt=i
		compt-=1

		while M[k][compt]=1 and compt>=1:

			compt-=1
			J[i][3]+=1

	#danger en bas (yen a pas en haut lol)

		#compte fait varier la ligne

		compt=k
		compt+=1

		while M[compt][i]=1 and compt<=7:

			compt+=1
			J[i][3]+=1

	#comptL fait varier la ligne
	#comptC fait varier la colonne

	#danger diagonale bas droite

		comptL=k
		comptC=i

		comptL+=1
		comptC+=1

		while M[comptL][comptC]=1 and compL<=6 and comptC<=7:

			comptL+=1
			comptC+=1
			J[i][3]+=1

	#danger diagonale bas gauche

		comptL=k
		comptC=i

		comptL+=1
		comptC-=1

		while M[comptL][comptC]=1 and compL<=6 and comptC>=1:

			comptL+=1
			comptC-=1
			J[i][3]+=1

	#danger diagonale haut droite

		comptL=k
		comptC=i

		comptL-=1
		comptC+=1

		while M[comptL][comptC]=1 and compL>=1 and comptC<=7:

			comptL-=1
			comptC+=1
			J[i][3]+=1

	#danger diagonale haut gauche

		comptL=k
		comptC=i

		comptL-=1
		comptC-=1

		while M[comptL][comptC]=1 and compL<=6 and comptC>=1:

			comptL-=1
			comptC-=1
			J[i][3]+=1

