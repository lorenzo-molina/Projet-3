#DEBUT

#On admets une fonction random renvoyant un nombre aléatoire entre 1 et 3

#On admets une fonction input

#Définir une variable pierre qui vaut 1
#Définir une variable feuille qui vaut 2
#Définir une variable ciseaux qui vaut 3

#Définir une fonction pfc 

    #Définir une variable joueur qui récupère le retour de l'éxecution de la fonction input

    #Définir un booléen rejouer égal à True

    #Tant que rejouer est égal à True

        #Si le retour de l'exécution de random est égal à joueur
            #Alors écrire "égalité"
        
        #Sinon si le retour de l'exécution de random est égal à pierre et joueur est égal à feuille
            #Alors écrire "gagné"
            
        #Sinon si le retour de l'exécution de random est égal à feuille et joueur est égal à ciseaux
            #Alors écrire "gagné"

        #Sinon si le retour de l'exécution de random est égal à ciseaux et joueur est égal à pierre
            #Alors écrire "gagné"

        #Sinon si le retour de l'exécution de random est égal à pierre et joueur est égal à ciseaux
            #Alors écrire "perdu"

        #Sinon si le retour de l'exécution de random est égal à feuille et joueur est égal à pierre
            #Alors écrire "perdu"

        #Sinon si le retour de l'exécution de random est égal à ciseaux et joueur est égal à feuille
            #Alors écrire "perdu"
    
        #Renvoyer un message "Voulez vous rejouer ?"
        #Si le retour de l'éxecution de la fonction input est oui
            #Alors le booléen rejouer est égal à True
        #Sinon si le retour de l'éxecution de la fonction input est non
            #Alors le booléen rejouer est égal à False

    #Si rejouer est égal à False
        #Alors renvoie le message "jeu terminé"

#FIN