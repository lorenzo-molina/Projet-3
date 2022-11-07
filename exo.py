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
def divide(x,y)
    return x / y
def modulo(x,y)
    return x % y
def salaireNet(brut,coefficient)
    return brut * 0.23
def salaireParSeconde(salaireHoraire,heureParJourOuvré,NbJourOuvréParAn)
    return salaireHoraire * heureParJourOuvré 
#FIN