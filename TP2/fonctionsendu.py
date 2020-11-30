'''auteur = elisa
date = 30 novembre
to do = fonctions du jeu'''

import random

def fRandomMot():
    mots = open('mots.txt','r')
    mot = random.choice(mots.readlines())
    return mot

def fRecupPremiereLettre(pMot):
    PremiereLettre = pMot[0]
    return PremiereLettre

def fAfficherMot(pMot):
    PremiereLettre = fRecupPremiereLettre(pMot)
    motcache=''
    for i in pMot :
        if i == PremiereLettre :
            motcache += i + " "
        else :
            motcache += '_' + " "
    return motcache

def fRecupLettreJoueur(pLettre) :
    lettre=pLettre.lower()
    if len(lettre)>1 or not lettre.isalpha():
        print('Saisissez une lettre valide')
        return fRecupLettreJoueur(pLettre)
    else :
        return lettre
    
def fChercherLettre(pLettre, pMot) :
    lettre = fRecupLettreJoueur(pLettre)
    symbole = '_'
    mot = pMot
    motcache = fAfficherMot(pMot)
    motcache = motcache.split(" ")[0:len(pMot)]
    for i in range(len(mot)) :
        if mot[i] == lettre :
            motcache[i] = lettre
    motcache = ' '.join(motcache)
    if symbole not in motcache :
        print('Victoire')
    return motcache

def fGagné(pLettre, pMot) :
    mot = fChercherLettre(pLettre, pMot)
    symbole ='_'    
    if symbole not in mot :
        print('Victoire')
        return True
    else :
        return False

def fEssai(pLettre, pMot) :
    NbCoups = 8
    if fGagné(pLettre, pMot) == False :
        NbCoups -= 1
    return NbCoups