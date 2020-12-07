'''auteur = elisa
date = 30 novembre 6 décembre
to do = partie graphique'''

import random

def fRandomMot():
    fichier = open('mots.txt','r')
    mot = random.choice(fichier.readlines())
    mot = mot.lower()
    fichier.close()
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
    pLettre = input('Saisissez une lettre : ')
    return pLettre

def fRecupLettreJoueur(pLettre) :
    lettre= pLettre.lower()
    if len(lettre)>1 or not lettre.isalpha():
        return False
    else :
        return True
    
def fChercherLettre(pMot,pMotEnCours) :
    pLettre = fDemanderLettreJoueur()
    mot = pMot
    motcache = pMotEnCours
    motcache = motcache.split(" ")[0:len(pMot)-1]
    for i in range(len(mot)) :
        if mot[i] == pLettre :
            motcache[i] = pLettre
    motcache = ' '.join(motcache)
    return motcache,pLettre

def fGagné(pMot) :
    symbole ='_'    
    if symbole not in pMot :
        print('Victoire')
        return True
    else :
        return False

def fDedans (pLettre, pMot, pMotEnCours) :
    if pLettre not in pMot :
        print (pLettre,'? non.')
        return False
    else :
        print (fChercherLettre(pMot, pMotEnCours))
        return True

def fScore(pScore, pMot) :
    ListeLettreFaciles =['a','e','i','o','u','r','s','t','n','m','l','p','c']
    score = int(pScore)
    NbFacile = 0
    NbDur = 0
    for i in pMot :
        if i in ListeLettreFaciles :
            NbFacile += 1
        else :
            NbDur += 1
    score = (NbFacile*2 + NbFacile*3)*score
    return score

def fDejaTestée(pLettre,pListe) :
    if pLettre in pListe :
        return True
    else :
        return False

def fJouer() :
    motchoisit = fRandomMot()
    motencours = fAfficherMot(motchoisit)
    NbCoups = 8
    ListeLettre = []
    while fGagné(motencours) == False and NbCoups >0 :
        print(motencours)
        print('Lettres testées : ', ListeLettre)
        motencours, lettre = fChercherLettre(motchoisit,motencours)
        if fRecupLettreJoueur(lettre) == False :
            print('--RENTREZ UNE LETTRE VALIDE--')
        else :
            if fDejaTestée(lettre,ListeLettre) == True :
                    print('--DEJA TESTEE--')
            else :
                ListeLettre.append(lettre)
                if lettre not in motchoisit :
                    print('Non pas cette lettre')
                    NbCoups -= 1
        print('Erreurs possibles : ', NbCoups)
        print('|')


    if NbCoups == 0 :
        print ('Défaite')

    print('Le mot était : ', motchoisit)
    print('Score : ', fScore(NbCoups,motchoisit))
    rep = input('tapez y pour rejouer : ')

    return fScore(NbCoups,motchoisit), rep

def fOncontinue(pRep) :
    print('je suis appelée')
    if pRep == 'y' :
        return fJouer()