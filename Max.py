
def MaxE(J):

	E=0

	case=0

	for i in range (1,7):

		if J[i][7]>E:

			E=J[i][7]   #on retient la plus grande valeur de E

			case=i   #on retient les coordonnées qui correspondent

	return(case)
