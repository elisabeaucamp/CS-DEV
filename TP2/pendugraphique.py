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
    for i in range(len(pMotChoisit)) :
        if pMotChoisit[i] == Reponse.get() :
            pMotEnCours = pMotEnCours.split(' ')[:len(pMotChoisit)]
            print(pMotEnCours)
            pMotEnCours[i] = Reponse.get()
            print(pMotEnCours)
            pMotEnCours = ' '.join(pMotEnCours)
            print(pMotEnCours)
    return pMotEnCours
    
def RemplacementAffichage(pMotChoisit, pMotEnCours) :
    pMotEnCours = Soumettre(pMotChoisit,pMotEnCours)

'''Définition des mots'''
MotChoisit = fonctionspendu.fRandomMot()
MotEnCours = AfficherMot(MotChoisit)
print(MotChoisit,MotEnCours)

'''création de la fenêtre'''
MaFenetre = Tk()
MaFenetre.title('Jeu du pendu')

'''création d'un bouton commencer'''
'''BoutonCommencer = Button(MaFenetre, text = 'Commencer', command = Commencer)
BoutonCommencer.pack(side = 'right', padx = 5, pady = 5)'''

'''création d'un bouton soumettre'''
BoutonSoumettre = Button(MaFenetre, text = 'Soumettre', command = lambda : RemplacementAffichage(MotChoisit,MotEnCours))
BoutonSoumettre.pack(side = 'right', padx = 5, pady = 5)

'''Création d'une entry'''
Reponse = StringVar()
Champ = Entry(MaFenetre, textvariable = Reponse)
Champ.focus_set()
Champ.pack(side = 'right', padx = 5, pady = 5)

'''Création de l'image'''
photo = PhotoImage(file = 'bonhomme1.gif')

'''création d'un widget canvas pour l'image'''
Canevas = Canvas(MaFenetre, height = 520, width = 680)
item = Canevas.create_image(0,0, anchor = 'nw', image = photo)
print('Image du pendu(item',item,')')
Canevas.pack()

'''Création du label affichage'''
Mot = StringVar()
LabelMotEC = Label(MaFenetre, textvariable = Mot).pack(padx = 10, pady = 10)
Mot.set(MotEnCours)

'''Création du label NbDeCoups'''
LabelNbCoups = Label(MaFenetre, text = str(8)).pack(padx = 10, pady = 10)

MaFenetre.mainloop()