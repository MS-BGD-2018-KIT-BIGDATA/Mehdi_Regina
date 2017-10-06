#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 13:32:55 2017

@author: mehdiregina
"""

#Attention bien découper ses étapes pour avoir un code incrémental qui tourne, agile 


import requests
from bs4 import BeautifulSoup
import functools

url_dell = "https://www.cdiscount.com/informatique/ordinateurs-pc-portables/pc-portables/lf-228394_6-dell.html#_his_"
url_acer = "https://www.cdiscount.com/informatique/ordinateurs-pc-portables/pc-portables/lf-228394_6-acer.html#_his_"

def get_soup_from_url(url):
    """Retourne le BeautifulSoup object associé à l'html de l'url passe en param"""
    page = requests.get(url)
    return BeautifulSoup(page.content,'html.parser')

def data_treatment1(nombre):
    """Traite les entree str de type 432,44 et retourne le double associé au nombre"""
    return double(".".join(str(nombre).split(',')))

def data_treatment2(nombre):
    """Traite les enttree str de type 432€44 et retourne le double associé"""
    return double(".".join(str(nombre).split('€')))

def percent(nombre1,nombre2):
    """Donne le pourcentage d'évolution du nombre1 au nombre2"""
    return ((nombre1-nombre2)/nombre1)*100

def get_rebate(url):
    """Calcul le rebate rate en se basant sur l'url de la page cdiscount"""
    soup = get_soup_from_url(url)
    
    liste_price = soup.find_all(class_="prdtBZPrice")
    liste_ex_prix = [div.select(".prdtPrSt") for div in liste_price]
    liste_prix = [div.select(".price") for div in liste_price]
    
    #pour gérer les liste nulle if len(liste) =0 ! dans les div ou il n'y a pas de tags prix barrés
    liste_moy = [percent(data_treatment1(liste_ex_prix[i][0].get_text()),data_treatment2(liste_prix[i][0].get_text())) for i in range(0,len(liste_prix)) if len(liste_ex_prix[i])>0]
    
    return functools.reduce(lambda x, y: x + y, liste_moy) / len(liste_moy)
    
#Main
rebate_rate_acer = get_rebate(url_acer)
rebate_rate_dell = get_rebate(url_dell)
print("rebate acer : ",rebate_rate_acer)
print("_______")
print("rebate dell : ",rebate_rate_dell)
