#DEBUT
r = 12000
s = 1250
e = 10
rh = 230
assertionFinale = (( (365 * 3) / (24 - (16 - 8)) ) * (rh)  > r) == (e * s  < r)
partieUne = (( (365 * 3) / (24 - (16 - 8)) ) * (rh)  > r) = (( 1095 / 16)) * 230  > 12000 = (15740.625 > 12000) #True
partieDeux = (e * s < r) = (10 * 1250 < 12000) = (12500 < 12000) #False
assertionFinale = partieUne == partieDeux #False


assertionFinaleDeux = ((365 * 3) / (4 - (12 - 8) ) * (rh)  > r) == (e * s  < r)
partieTrois = ((365 * 3) / (4 - (12 - 8) ) * (rh)  > r) = (1095 / 0 * 230 > 12000) #False
partieQuatre = (e * s < r) = (10 * 1250 < 12000) = (12500 < 12000) #False
assertionFinaleDeux = partieTrois = partieQuatre == #True

def retournerSixPlusTrois():
    return 6 + 3
def retournerYPlusX(x, y):
    return y + x
def add(x,y)
    return x + y
def sub(x,y)
    return x - y
def multiply(x,y)
    return x * y
def divide(x,y):
    if (y==0)
        return print #error
    else:
        return result
    return x / y
def modulo(x,y)
    return x % y
def salaireNet(brut,coefficient)
    return brut * 0.23
def salaireParSeconde(salaireHoraire,heureParJourOuvré,jourOuvréParAn):
    #Calculer mon salaire annuel
    salaireAnnuel = salaireHoraire * heureParJourOuvré * jourOuvréParAn
    #Calculer le nombre de secondes dans une année
    nbSecondesParAn = 365*24*60*60
    #Je pose et retourne la division
    return salaireAnnuel / nbSecondesParAn

#Définir une fonction withdrawFees qui retire un pourcentage à un total en fonction d'un total et d'un pourcentage
    def withdrawFees(total,percent)
    #Définir fees en fonction d'un total et d'un pourcentage
    fees = total * (percent/100)
    #Soustraire fees au total
    result = total - fees
    #Retourner la valeur obtenue
    return result


#Définir une fonction qui retourne le salaire net en fonction du salaire brut (float) et du secteur d'activité (isPublic > booleen)
def calculBrutEnNet(salaireBrut, isPublic):
    #Si je suis un travailleur du secteur public
    if isPublic:
        #Alors je soustrais 15% de mon salaire brut a mon salaire brutet je l'assigne à la variable salaireNet
        #salaireNet = salaireBrut - (salaireBrut * (15/100))
        salaireNet = withdrawFees(salaireBrut, 15)
    #Sinon : je suis un travailleur du secteur privé
    else:
        #Alors je soustrais 23% de mon salaire brut a mon salaire brutet je l'assigne à la variable salaireNet
        #salaireNet = salaireBrut - (salaireBrut * (23/100))
        salaireNet = withdrawFees(salaireBrut, 23)
    #Retourner salaireNet
    return salaireNet

def input():
    #Renvoie un caractère de type string au hasard
    return 1
input()    
#Exercice
    #Faire un mini jeu qui affiche un message lorsque input renvoie le bon caractère
    #Le caractère doit etre parametrable

#Je définis un mini-jeu
def miniJeu(x):
    #Compteur à 0
    compteur = 0
    #Je définis une variable y
    y=input("Devinez")
    #Tant que y est différent de x
    while y!=x:
        #Ajouter 1 au compteur
        compteur = compteur + 1
        #Afficher le compteur
        print(compteur)
        #Alors j'appelle une nouvelle y
        y=input("Devinez")
    #Lorsque la variable y est égale à la variable x alors
    print("Bravo")

integerValue = 342 #Retourne 342
stringIntegerValue = str(342) #Retourne "342"

tableau = [0,10,15,5,1]
#Pour récupérer 15 je prends dans tableau l'index 2

print (tableau[2]) #Affiche 15

len(tableau) #Renvoie la longueur du tableau, renvoie 5

#Exercice 1
#Faire une fonction qui concatene 2 chaines de caractere, les séparants par un virgule
def concatWithComma(str1, str2)
    #Retourner str1 + ',' + str2
    stringified1 = str(str1)
    stringified2 = str(str2)
    return str1 + ", " + str2

#Exercice 2
#Faire une fonction qui itere sur tous les index d'un tableau renvoyant une chaine de caractere avec l'ensemble des occurences d'un chiffre, exemple :
#Pour tableau = [0,1,1,1,0,1,1,0,1], la fonction (tableau, 0) doit renvoyer "0, 4, 7" n'hésitez pas a implementer la premiere fonction
tableau = [0,1,1,1,0,1,1,0,1]
#Définir la fonction findIndex qui itere sur tableau, cherchant l'index des différentes occurences de x
def findIndex(tableau, x):
    #Définir i un index de départ
    i = 0
    #Définir chainRetour telle qu'une chaine de caractere vide
    chaineRetour = ''
    #Définir un booléen tel que firstTurn est true
    
    #Tant que i est différent du nombre d'element dans le tableau
    while i != len(tableau):
        #Alors j'attribue a une variable la valeur de tableau a l'index i
        selected = tableau[i]
        #Si selected est égal a x Et que firstTurn est True
            #Alors on assigne a chaineRetour le retour de str(i)
            #Changer la valeur de firstTurn a False
        #Sinon si selected est égal a x
        if selected == x
            #Alors j'assigne le retour de concatwithComma tel que : concatWithComma(chaineRetour, i) à chaineRetour
            chaineRetour = concatWithComma(chaineRetour, i)
        #J'incrémente i de 1
        i = i + 1    
    #Retourne la chaine retour
    return chaineRetour

#Exercice 3
#Renvoyer/Afficher un message
msg=str(input("Entrez votre message : ")) print(msg)

#FIN