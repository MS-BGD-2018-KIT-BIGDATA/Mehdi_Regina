#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 22:15:40 2017

@author: mehdiregina
"""

import requests
from bs4 import BeautifulSoup

#Rappel pour naviguer dans l'arborescence lors du webcrawling .parents .siblings 
#=> on peut ainsi remonter à la div contenant une classe particulière en child

#donneess
years=[2010,2011,2012,2013,2014,2015]
index_per_hab=[1,4,10,13]
index_tot_eur=[0,3,9,12]
lettres=["A","B","C","D"]

def get_soup_from_url(annee):
    """Retourne BeautifulSoup object associé aux resultat des comptes de Paris de 
    l'année passée en paramètre"""
    try:
        url="http://alize2.finances.gouv.fr/communes/eneuro/detail.php?icom=056&dep=075&type=BPS&param=5&exercice="+str(annee)
    except(ValueError):
        print("L'année voulue doit être passée en paramètre, par exemple 2012")
    page=requests.get(url)
    return BeautifulSoup(page.content,'html.parser')

def data_treatment(string):
    """prend en entré le get_text et retour l'int associé"""
    return int("".join(string.strip('\xa0').split()))

def get_data(annee):
    """Retourne les valeurs des données ABCD pour l'année voulue)"""
    soup=get_soup_from_url(annee)

    liste_div_nb=soup.select(".montantpetit.G")

    data_eur_per=[data_treatment(liste_div_nb[i].get_text()) for i in index_per_hab]
    data_tot_eur=[data_treatment(liste_div_nb[i].get_text()) for i in index_tot_eur]
    return zip(lettres,data_tot_eur,data_eur_per)
    
for year in years :
    raw_data=list(get_data(year))
    print(raw_data)
    print("--------------")
