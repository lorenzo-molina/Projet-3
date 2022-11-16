from random import *
choix = ["pierre", "feuille", "ciseaux"]
ordi = choix[randint(0,2)]
rejouer = 0
scoreOrdi = 0
scoreJoueur = 0

while rejouer == 0:
    joueur = input("Faire une partie de pierre feuille ciseaux ? \n>")
    if joueur == "yes" or joueur == "oui":
        rejouer = 1
    elif joueur == "no" or joueur == "non":
        rejouer = 2
        print("Jeu terminé")
    else:
        rejouer == 0
        print("Erreur, veuillez entrer oui ou non")

nomJoueur = input("Entrez votre pseudo : \n")
nomOrdi = input("Entrez le pseudo de votre adversaire : \n")

while rejouer == 1:
    ordi = choix[randint(0,2)]
    joueur = input("Pierre, feuille ou ciseaux \n>")
    if joueur == "ciseaux" or joueur == "Ciseaux":
        if ordi == "pierre":
            scoreOrdi += 1
            print( nomOrdi + " a gagné")
            print("-----------------------\n" + nomJoueur + " : " + str(scoreJoueur) + " | "   +joueur +"\n"+ "" + nomOrdi + " : " + str(scoreOrdi) + " | " +ordi + "\n-----------------------")
        elif ordi == "feuille":
            scoreJoueur += 1
            print("Bravo, tu as gagné")
            print("-----------------------\n" + nomJoueur + " : " + str(scoreJoueur) + " | "   +joueur +"\n"+ "" + nomOrdi + " : " + str(scoreOrdi) + " | " +ordi + "\n-----------------------")
        else:
            print("Egalité")
            print("-----------------------\n" + nomJoueur + " : " + str(scoreJoueur) + " | "   +joueur +"\n"+ "" + nomOrdi + " : " + str(scoreOrdi) + " | " +ordi + "\n-----------------------")
    elif joueur == "feuille" or joueur == "Feuille":
        if ordi == "pierre":
            scoreJoueur += 1
            print("Bravo, tu as gagné")
            print("-----------------------\n" + nomJoueur + " : " + str(scoreJoueur) + " | "   +joueur +"\n"+ "" + nomOrdi + " : " + str(scoreOrdi) + " | " +ordi + "\n-----------------------")
        elif ordi == "feuille":
            print("Egalité")
            print("-----------------------\n" + nomJoueur + " : " + str(scoreJoueur) + " | "   +joueur +"\n"+ "" + nomOrdi + " : " + str(scoreOrdi) + " | " +ordi + "\n-----------------------")
        else:
            scoreOrdi += 1
            print( nomOrdi + " a gagné")
            print("-----------------------\n" + nomJoueur + " : " + str(scoreJoueur) + " | "   +joueur +"\n"+ "" + nomOrdi + " : " + str(scoreOrdi) + " | " +ordi + "\n-----------------------")
    elif joueur == "pierre" or joueur == "Pierre":
        if ordi == "pierre":
            print("Egalité")
            print("-----------------------\n" + nomJoueur + " : " + str(scoreJoueur) + " | "   +joueur +"\n"+ "" + nomOrdi + " : " + str(scoreOrdi) + " | " +ordi + "\n-----------------------")
        elif ordi == "feuille":
            scoreOrdi += 1
            print( nomOrdi + " a gagné")
            print("-----------------------\n" + nomJoueur + " : " + str(scoreJoueur) + " | "   +joueur +"\n"+ "" + nomOrdi + " : " + str(scoreOrdi) + " | " +ordi + "\n-----------------------")
        else:
            scoreJoueur += 1
            print("Bravo, tu as gagné")
            print("-----------------------\n" + nomJoueur + " : " + str(scoreJoueur) + " | "   +joueur +"\n"+ "" + nomOrdi + " : " + str(scoreOrdi) + " | " +ordi + "\n-----------------------")
    if scoreJoueur == 3:
        print("Félicitations, tu remporté la partie")
        print(nomJoueur + " : " + str(scoreJoueur)  +"\n"+ "" + nomOrdi + " : " + str(scoreOrdi) )
        rejouer = 0
        joueur = input("Voulez-vous rejouer ?\n")
        if joueur == "yes" or joueur == "oui":
            rejouer = 1
            scoreOrdi = 0
            scoreJoueur = 0
        else:
            print("Jeu terminé")
    elif scoreOrdi == 3:
        print("Dommage, tu as perdu, réessaye la prochaine fois")
        print(nomJoueur + " : " + str(scoreJoueur)  +"\n"+ "" + nomOrdi + " : " + str(scoreOrdi))
        rejouer = 0
        joueur = input("Voulez-vous rejouer ? \n")
        if joueur == "yes" or joueur == "oui":
            rejouer = 1
            scoreOrdi = 0
            scoreJoueur = 0
        else:
            print("Jeu terminé")