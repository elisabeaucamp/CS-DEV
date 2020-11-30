'''auteur = elisa
date = 30 novembre
to do = tout '''

import fonctionspendu

NbCoups = 8 
motchoisit = fonctionspendu.fRandomMot()
motencours = motchoisit
print(fonctionspendu.fAfficherMot(motchoisit))
lettrejoueur = fonctionspendu.fDemanderLettreJoueur()
fonctionspendu.fRecupLettreJoueur(lettrejoueur)
while fonctionspendu.fDedans(lettrejoueur,motchoisit, motencours) == False :
    lettrejoueur = fonctionspendu.fDemanderLettreJoueur()
if fonctionspendu.fDedans(lettrejoueur, motchoisit, motencours) == True :
    motencours = fonctionspendu.fChercherLettre(lettrejoueur, motchoisit, motencours)
    while fonctionspendu.fGagné(lettrejoueur, motchoisit, motencours) == False :
        lettrejoueur = fonctionspendu.fDemanderLettreJoueur()
        fonctionspendu.fDedans(lettrejoueur,motchoisit, motencours)

