import csv
import random
tab=[
"""
+-------+
|
|
|
|
|
==============
""" ,
"""
+-------+
|       |
|       O
|
|
|
==============
""",
"""
+-------+
|       |
|       O
|       |
|
|      
==============
"""
,
"""
+-------+
|       |
|       O
|      -|
|
|
==============
"""
,
"""
+-------+ 
|       |
|       O
|      -|-
|
|
==============
"""
,
"""
+-------+
|     |
|     O 
|    -|-
|    |
|
==============
"""
,
"""
+-------+
|       O
|      -|-
|      | |
|
==============
"""
]
def propositions_lettres(mot,mot_liste, mot_affiche):
      """
      Cette fonction permet de proposer une lettre puis d'effectuer une action en fonction de la lettre proposée
      entrée: La foction pour ces listes (:mot_affiche, mot_liste, propositions)
              La variable 'lettre' qui demande une letrre
      sortie: Renvoie un message si : on a proposé une lettre déjà proposée
                                      la lettre n'est pas dans le mot
                                      il ne nous reste plus aucune tentative
                                      on a trouvé le mot
      """
      n=0
      total = 0
      tentative = 0
      propositions = []
      while mot_affiche != mot_liste :
        lettre = input('Choisir une nouvelle lettre (en minuscule) : ')#demande au joueur de choisir une nouvelle lettre
        compteur=0#on définit un compteur comme = 0
        for lettres_proposees in propositions: #pour chaque lettre de propositions
            if lettres_proposees == lettre:#si la lettre proposée l'a déjà été, le compteur augmente
                compteur+=1
        if compteur!=0: #si le compteur a augmenté la lettre a déjà été proposée
            print("Attention ! Vous avez déjà proposé cette lettre.")
        else:#si elle ne l'est pas, on l'ajoute à la liste des lettres proposées
            propositions.append(lettre)
        tentative += 1
        for lettre4 in range (len(mot[0])) : #parcours le mot que l'on cherche
            if mot_liste[lettre4]==lettre :#si une lettre du mot correspond à la lettre proposée, on l'affiche
                mot_affiche[lettre4] = lettre#affiche la lettre
            else:
                total += 1
        if total >= len(mot_affiche) :
            if n <=4:
                  print("La lettre n'est pas dans le mot",tab[n],"Il reste",6-n,"tentatives")
            else:
                  print("La lettre n'est pas dans le mot",tab[n],"Il reste",6-n,"tentative")
            if tab[n] == tab[6]:
                print("GAME OVER","Le mot était",mot_liste)
                break
            n+=1
        total = 0
        for caractere3 in range (len(mot_affiche)) :
              print (mot_affiche[caractere3],end='')
        print(" ")
        print("Vous avez déjà proposé ces lettres :", propositions)
        print(" ")
        if mot_affiche==mot_liste:
            print("Bravo! Tu as trouvé en",tentative,"tentatives")


def AccentMaj(mot,mot_affiche):
    """
    Cette fonction permet de supprimer les accents et majuscules potentiels des mots 
    Entrée: Le mot choisi
    Sortie: Renvoie le mot sans accent ni majuscule 
    """
    alphabetM = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    alphabetm = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    accent = ['é','è','ë','ô','ù','â','ï','à','ç','û','ü','î','ê']
    sans_accent = ['e','e','e','o','u','a','i','a','c','u','u','i','e'] 
    mot_liste = []
    for letter in range (len(mot[0])): 
        mot_liste.append(mot[0][letter])#transforme la liste 'mot' en une liste qui ressemble à 'mot_affiche' 
    for lettre in range (len(alphabetM)) :
        if mot_liste[0]== alphabetM[lettre] : #majuscules -> minuscules
            mot_liste[0]= alphabetm[lettre]
    for letters in range (len(mot_liste)) :
        for accents in range (len(accent)) :
            if mot_liste[letters]==accent[accents] :
                mot_liste[letters]=sans_accent[accents]
    propositions_lettres (mot,mot_liste, mot_affiche)

    
def affiche (mot) :
    """
    Cette fonction affiche un message au début de chaque nouvelle partie et remplace les lettres composant le mot par des "_"
    Entrée: Le mot choisi aléatoirement 
    Sortie: Une liste comportant autant de "_" que de caractères dans le mot
    """
    mot_affiche = []
    print ("Nouvelle partie !")
    for caractere in mot[0] :
        mot_affiche.append('-')#représente l'état du mot qui est affiché à l'écran
    AccentMaj(mot , mot_affiche)

    
def mots_indésirables(mot):
    """
    Cette fonction complète la fonction AccentMaj et empêche que la fonction choix_du_mot prenne un mot avec l'un des caractères suivants
    Entrée: Le mot choisi aléatoirement
    Sortie: Le mot choisi aléatoirement s'il ne comporte pas de caractères indésirables
    """
    for w in range (len(mot[0])) :
        while mot[0][w] == 'œ' or mot[0][w] == '-' or mot [0][w] == ' ' :
            mot = random.choice(L_mots)
    affiche(mot)

    
def choix_du_mot () :
    """
    Cette fonction choisit un mot parmis les mots présent dans le fichier csv liste_mot_francais_pour_pendu_motus.csv
    Entrée : cette fonction est la première de notre programme et ne prend pas d'entrée
    Sortie : Renvoie le mot choisit à la fonction suivante
    """
    mon_fichier=open("liste_mots_francais_pour pendu_motus.csv",'r')#Ouvre le fichier en csv
    contenu=csv.reader(mon_fichier,delimiter=";")#Lie le fichier et le délimite
    L_mots=[]#Création d’une liste vide
    for i in contenu:#Met le fichier dans dans la liste
        L_mots.append(i)
    mon_fichier.close()#Ferme le fichier
    mot=random.choice(L_mots)
    mots_indésirables(mot)

    
choix_du_mot()    
