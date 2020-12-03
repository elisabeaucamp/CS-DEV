'''auteur = elisa
date = 30 novembre 3 decembre
to do = vérifs lettre valide '''

import fonctionspendu
motchoisit = fonctionspendu.fRandomMot()
motencours = fonctionspendu.fAfficherMot(motchoisit)
NbCoups = 8
ListeLettre = ''
while fonctionspendu.fGagné(motencours) == False and NbCoups >0 :
    print(motencours)
    print('Lettres testées : ', ListeLettre)
    motencours, lettre = fonctionspendu.fChercherLettre(motchoisit,motencours)
    lettre = fonctionspendu.fRecupLettreJoueur(lettre)
    ListeLettre += lettre
    if lettre not in motchoisit :
        print('Non pas cette lettre')
        NbCoups -= 1
    print('Erreurs possibles : ', NbCoups)


if NbCoups == 0 :
    print ('Défaite')

print('Le mot était : ', motchoisit)
print('Score : ', fonctionspendu.fScore(NbCoups,motchoisit))

