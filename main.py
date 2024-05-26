import re
import fonctions_jeux as UI 

def jeux_de_trou_de_cul() :
    cartes = UI.fct_cree_cartes()
    while not valide :
        print("Quelle est votre nombre de joueurs ? : ")
        rep = input("") ###
        choix = re.search(r'\d+', rep)
        valide = choix
        if valide:
            choix = int(choix.group())
            valide = 4 <= choix <= 5

    jouer = True
    while jouer == True :
        ""

