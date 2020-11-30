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
def fDemanderLettreJoueur():
    pLettre = input('Saisisser une lettre : ')
    return pLettre
def fRecupLettreJoueur(pLettre) :
    lettre= pLettre.lower()
    if len(lettre)>1 or not lettre.isalpha():
        print('Saisissez une lettre valide : ')
        return fRecupLettreJoueur(pLettre)
    else :
        return lettre
    
def fChercherLettre(pLettre, pMot, pMotEnCours) :
    lettre = fRecupLettreJoueur(pLettre)
    mot = pMot
    motcache = fAfficherMot(pMotEnCours)
    motcache = motcache.split(" ")[0:len(pMot)]
    for i in range(len(mot)) :
        if mot[i] == lettre :
            motcache[i] = lettre
    motcache = ' '.join(motcache)
    return motcache

def fGagné(pLettre, pMot, pMotEnCours) :
    mot = fChercherLettre(pLettre, pMot, pMotEnCours)
    symbole ='_'    
    if symbole not in mot :
        print('Victoire')
        return True
    else :
        return False

def fDedans (pLettre, pMot, pMotEnCours) :
    NbCoups = 8
    if pLettre not in pMot :
        print (pLettre,'? non.')
        NbCoups -=1
        return False
    else :
        print (fChercherLettre(pLettre,pMot, pMotEnCours))
        return True