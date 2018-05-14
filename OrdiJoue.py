
def OrdiJoue(M,J):

	k=MaxE(J)   #on prend la ligne avec l'eval max

	ligne=J[k][2]

	colonne=k   #meme valeur que J[k][1]

	M[ligne][colonne]=0

	if colonne>1:

		M[ligne][colonne-1]=2

	return(ligne,colonne)
