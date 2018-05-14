def CheckWin(): #Cette fonction permet de savoir qui gagne la partie
                #renvoie Tru si le dernier joueur qui a joué a gagné
                #renvoie false sinon (pas gagné)
grille[0][0]=[
               [0][0][0][0][0][0][0]
               [0][0][0][0][0][0][0]
               [0][0][0][0][0][0][0]
               [0][0][0][0][0][0][0]
               [0][0][0][0][0][0][0]
               [0][0][0][0][0][0][0]
                ]

    #Check Horizontal 
    for i in range(6): #il y a 6 lignes
        for j in range(4): #4 cases pour win donc obvious
            if grille[i][j] + grille[i][j+1] + grille[i][j+2] + grille[i][j+3] == 4:
                winer = "Red"
            if grille[i][j] + grille[i][j+1] + grille[i][j+2] + grille[i][j+3] == -4:
                winner = "Yellow"

    #Check vertical 
    for j in range(7): #il y a 7 colonnes 
        for i in range(4): #4 cases pour win donc obvious
            if grille[i][j] + grille[i+1][j] + grille [i+2][j] + grille[i+3][j] == 4:
                winner = "Red"
            if grille[i][j] + grille[i+1][j] + grille [i+2][j] + grille[i+3][j] == -4:
                winner = "Yellow"

    #Diagonales : on va toujours de la gauche vers la droite
                #on compte de bas en haut si diagonale montante vers la droite
                #on compte de haut en bas si diagonale descendantes vers la droite (i.e. montantes vers la gauche) 

    #Check diagonales montantes
    for i in range(4):
        for j in range(4):
            if grille[i][j] + grille[i+1][j+1] + grille [i+2][j+2] + grille[i+3][j+3] == 4:
                winner = "Red"
            if grille[i][j] + grille[i+1][j+1] + grille [i+2][j+2] + grille[i+3][j+3] == -4:
                winner = "Yellow"

    #Check diagonales descendantes
    for i in range(4):
        for j in range(4):
            if grille[i][j] + grille[i-1][j-1] + grille [i-2][j-2] + grille[i-3][j-3] == 4:
                winner = "Red"
            if grille[i][j] + grille[i-1][j-1] + grille [i-2][j-2] + grille[i-3][j-3] == -4:
                winner = "Yellow"

    #Display winner
    if winner == "Red" or winner == "Yellow"
        return True
    else:
        return False 
