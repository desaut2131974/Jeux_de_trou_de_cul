import random

#classes :
from classes.carte import Carte


def fct_cree_cartes() :
    ""


def fct_distribuer_Cartes(cartes , nombre_joueur = 4):
    cartes = random.shuffle(cartes)

    if nombre_joueur is 4 : 
        president   = cartes[0:14] # to come back later 
        vice        = cartes[15:29]
        secretaire  = cartes[30:42]
        trou_de_cul = cartes[43:55]
        return president , vice , secretaire , trou_de_cul
    
    elif nombre_joueur is 5 :
        "" # to come back later  
