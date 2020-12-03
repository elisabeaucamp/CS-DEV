import random
import fonctionspendu

fichier = open('mots.txt','r')
mot = random.choice(fichier.readlines())
print(fonctionspendu.fAfficherMot(mot))
motencours = mot
lettrejoueur = input('Saisissez une lettre : ')
lettrejoueur = fonctionspendu.fRecupLettreJoueur(lettrejoueur)
while fonctionspendu.fGagné(mot,motencours)== False :
    if fonctionspendu.fDedans(lettrejoueur,mot,motencours) == True :
        fonctionspendu.fChercherLettre(lettrejoueur,mot,motencours)
        motencours = fonctionspendu.fChercherLettre(lettrejoueur,mot,motencours)
    else :
        lettrejoueur = fonctionspendu.fDemanderLettreJoueur()
