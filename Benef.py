def Benef (M,J):

	for i in range (1,7):

		#i est la colonne

		#k est la ligne

		k=J[i][2]

	#benef à droite

		#compt fait varier la colonne

		compt=i
		compt+=1
		print(k)

		while compt<7 and M[k][compt]==0:
			compt+=1
			J[i][4]+=1

	#benef à gauche

		#compt fait varier la colonne

		compt=i
		compt-=1

		while M[k][compt]==0 and compt>=1:

			compt-=1
			J[i][4]+=1

	#benef en bas (yen a pas en haut lol)

		#compte fait varier la ligne

		compt=k
		compt+=1

		while compt<6 and M[compt][i]==0 :

			compt+=1
			J[i][4]+=1

	#comptL fait varier la ligne
	#comptC fait varier la colonne

	#benef diagonale bas droite

		comptL=k
		comptC=i

		comptL+=1
		comptC+=1

		while M[comptL][comptC]==0 and compL<6 and comptC<7:

			comptL+=1
			comptC+=1
			J[i][4]+=1

	#benef diagonale bas gauche

		comptL=k
		comptC=i

		comptL+=1
		comptC-=1

		while M[comptL][comptC]==0 and compL<=6 and comptC>=1:

			comptL+=1
			comptC-=1
			J[i][4]+=1

	#benef diagonale haut droite

		comptL=k
		comptC=i

		comptL-=1
		comptC+=1

		while M[comptL][comptC]==0 and compL>=1 and comptC<=7:

			comptL-=1
			comptC+=1
			J[i][4]+=1

	#benef diagonale haut gauche

		comptL=k
		comptC=i

		comptL-=1
		comptC-=1

		while M[comptL][comptC]==0 and compL<=6 and comptC>=1:

			comptL-=1
			comptC-=1
			J[i][4]+=1
