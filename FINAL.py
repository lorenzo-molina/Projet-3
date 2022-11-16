#DEBUT
import random
#On admets une fonction random renvoyant un nombre aléatoire entre 1 et 3
random = random.randint(1, 3)
#On admets une fonction input
print ("Pierre, feuille ou ciseaux ?")
#Définir une variable pierre qui vaut 1
#Définir une variable feuille qui vaut 2
#Définir une variable ciseaux qui vaut 3
pierre = 1
feuille = 2
ciseaux = 3
#Définir une fonction pfc 
def pfc():
    #Définir une variable joueur qui récupère le retour de l'éxecution de la fonction input
    joueur = input
    #Définir un booléen rejouer égal à True
    rejouer = True
    #Tant que rejouer est égal à True
    while rejouer==True:
        #Si le retour de l'exécution de random est égal à joueur
            #Alors écrire "égalité"
        if random == joueur:
            print("Egalité")
        #Sinon si le retour de l'exécution de random est égal à pierre et joueur est égal à feuille
            #Alors écrire "gagné"
        elif random == pierre & joueur == feuille:
            print("Gagné")
        #Sinon si le retour de l'exécution de random est égal à feuille et joueur est égal à ciseaux
            #Alors écrire "gagné"
        elif random == feuille & joueur == ciseaux:
            print("Gagné")
        #Sinon si le retour de l'exécution de random est égal à ciseaux et joueur est égal à pierre
            #Alors écrire "gagné"
        elif random == ciseaux & joueur == pierre:
            print("Gagné")
        #Sinon si le retour de l'exécution de random est égal à pierre et joueur est égal à ciseaux
            #Alors écrire "perdu"
        elif random == pierre & joueur == ciseaux:
            print("Gagné")
        #Sinon si le retour de l'exécution de random est égal à feuille et joueur est égal à pierre
            #Alors écrire "perdu"
        elif random == feuille & joueur == pierre:
            print("Gagné")
        #Sinon si le retour de l'exécution de random est égal à ciseaux et joueur est égal à feuille
            #Alors écrire "perdu"
        elif random == ciseaux & joueur == feuille:
            print("Gagné")
        #Renvoyer un message "Voulez vous rejouer ?"
        print("Voulez-vous rejouer ?")
        #Si le retour de l'éxecution de la fonction input est oui
        if input("oui"):
            #Alors le booléen rejouer est égal à True
            rejouer = True
        #Sinon si le retour de l'éxecution de la fonction input est non
        else: input("non")
        #Alors le booléen rejouer est égal à False
        rejouer = False
    #Si rejouer est égal à False
    if rejouer == False:
        #Alors renvoie le message "jeu terminé"
        print("Jeu terminé")
pfc()
#FIN