#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 13:30:36 2020

@author: elisa
but : librairie tp1
"""

def fBissextile (pAnnee):
    if (pAnnee % 400 == 0) or (pAnnee % 100 != 0 and pAnnee % 4 == 0):
        return True
    else:
        return False

def fVerifNbJour (pAnnee, pMois):
    if pMois > 12 :
        print ("Rentrer un mois valide")
    else :
        if pMois in [1,3,5,7,8,10,12]:
            print("Mois à 31 jours")
        elif pMois in [4,6,9,11]:
            print("Mois à 30 jours")
        elif pMois == 2:
            if fBissextile(pAnnee) == True:
                print("Mois à 29 jours")
            else :
                print("Mois à 28 jours")
                
def fVerifDateValide(pJour, pMois, pAnnee):
    valide = "Date valide"
    pasvalide = "Jour non valide"
    if pAnne < 1582 :
        print ("Date non valide")        
    elif pMois > 12 :
        print ("Mois non valide") 
    elif pMois == 2 :
        if fBissextile(pAnnee) == True :
            if pJour > 29 :
                print (pasvalide)
            else : 
                print (valide)
        else :
            if pJour >28 :
                print (pasvalide)
            else :
                print (valide)
    elif pMois in [1,3,5,7,8,10,12] :
        if pJour > 31 :
            print (pasvalide)
        else :
            print (valide)
    elif pMois in [4,6,9,11] :
        if pJour > 30 :
            print(pasvalide)
        else :
            print(valide)

def fMesImpots(pRevenu) : 
    aPayer=0
    if pRevenu < 9964 :
        aPayer = 0
    elif 9964<pRevenu<27519 :
        tranche2 = pRevenu - 9964
        aPayer = 14/100*tranche2
    elif 27519<pRevenu<73779:
        tranche3 = pRevenu - 27519
        tranche2 = pRevenu - 9964 - tranche3
        aPayer = 14/100*tranche2 + 30/100*tranche3 
    elif 73779<pRevenu<156244:
        tranche4 = pRevenu - 73779
        tranche3 = pRevenu - 27519 - tranche4
        tranche2 = pRevenu - 9964 - tranche4 - tranche3
        aPayer = 14/100*tranche2 + 30/100*tranche3 + 41/100*tranche4
    elif 156244 < pRevenu:
        tranche5 = pRevenu - 156244
        tranche4 = pRevenu - 73779 - tranche5
        tranche3 = pRevenu - 27519 - tranche5 - tranche4
        tranche2 = pRevenu - 9964 - tranche5 - tranche4 - tranche3
        aPayer = 14/100*tranche2 + 30/100*tranche3 + 41/100*tranche4 + 45/100*tranche5
    return aPayer

def fProduitMat (pA,pB) :
    













