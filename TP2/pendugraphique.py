'''auteur : Elisa
date : 7 décembre
to do : affcihage graphique du mot en cours, points '''

from tkinter import Tk, Canvas, Entry, Button, Label, Image, PhotoImage, StringVar
import fonctionspendu

'''recupération des mots'''
'''je sais que j'ai cette meme fonction dans focntionspendu mais pour la partie'''
'''graphique, elle m'affichait un _ de trop mais pas en console, j'ai préféré en refaire une '''
def AfficherMot(pMot) : 
    PremiereLettre = fonctionspendu.fRecupPremiereLettre(pMot)
    MotCache= []
    for i in pMot :
        if i == PremiereLettre :
            MotCache.append(i + " ")
        else :
            MotCache.append('_' + " ")
    MotCache = MotCache[0:len(MotCache)-1]
    MotCache = ' '.join(MotCache)
    return MotCache

def Soumettre(pMotChoisit, pMotEnCours) :
    global nbrTentatives
    nbrTentatives = 0
    for i in range(len(pMotChoisit)) :
        if pMotChoisit[i] == Reponse.get() :
            pMotEnCours = pMotEnCours.split()[0:len(pMotChoisit)]
            pMotEnCours[i] = Reponse.get()
            pMotEnCours = ' '.join(pMotEnCours)
        else :
            nbrTentatives += 1
            nbrTentatives = Image(nbrTentatives)
    return pMotEnCours, nbrTentatives
    
def RemplacementAffichage(pMotChoisit, pMotEnCours) :
    global MotEnCours
    MotEnCours, nbrTentatives = Soumettre(pMotChoisit,pMotEnCours)
    print(MotEnCours)
    return MotEnCours

def Images(pNbrTentatives):
    if pNbrTentatives == 1 :
        image = 'Images/bonhomme2.gif'
    elif pNbrTentatives == 2 :
        image = 'Images/bonhomme3.gif'
    elif pNbrTentatives == 3 :
        image = 'Images/bonhomme4.gif'
    elif pNbrTentatives == 4 :
        image = 'Images/bonhomme5.gif'
    elif pNbrTentatives == 5 :
        image = 'Images/bonhomme6.gif'
    elif pNbrTentatives == 6 :
        image = 'Images/bonhomme7.gif'
    elif pNbrTentatives == 7 :
        image = 'Images/bonhomme8.gif'
    return image

'''Définition des mots'''
MotChoisit = fonctionspendu.fRandomMot()
MotEnCours = AfficherMot(MotChoisit)
print(MotChoisit)

'''création de la fenêtre'''
MaFenetre = Tk()
MaFenetre.title('Jeu du pendu')

'''création d'un bouton commencer'''
'''BoutonCommencer = Button(MaFenetre, text = 'Commencer', command = lambda : AfficherMot(MotChoisit))
BoutonCommencer.pack(side = 'right', padx = 5, pady = 5)'''

'''création d'un bouton soumettre'''
BoutonSoumettre = Button(MaFenetre, text = 'Soumettre', command = lambda : RemplacementAffichage(MotChoisit,MotEnCours))
'''lambda : RemplacementAffichage(MotChoisit,MotEnCours)'''
BoutonSoumettre.pack(side = 'right', padx = 5, pady = 5)

'''Création d'une entry'''
Reponse = StringVar()
Champ = Entry(MaFenetre, textvariable = Reponse)
Champ.focus_set()
Champ.pack(side = 'right', padx = 5, pady = 5)

'''Création de l'image'''
'''MEC, nbrTentatives = Soumettre(MotChoisit,MotEnCours)
image = StringVar()
image.set(nbrTentatives)
photo = PhotoImage(file = image)'''

'''création d'un widget canvas pour l'image'''
'''Canevas = Canvas(MaFenetre, height = 520, width = 680)
item = Canevas.create_image(0,0, anchor = 'nw', image = photo)
print('Image du pendu(item',item,')')
Canevas.pack()'''

'''Création du label affichage'''
MEC = RemplacementAffichage(MotChoisit,MotEnCours)
Mot = StringVar()

LabelMotEC = Label(MaFenetre, textvariable = Mot).pack(padx = 10, pady = 10)
Mot.set(MEC)
'''Création du label NbDeCoups'''
LabelNbCoups = Label(MaFenetre, textvariable = str(8)).pack(padx = 10, pady = 10)

MaFenetre.mainloop()