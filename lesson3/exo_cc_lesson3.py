#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 13:32:38 2017

@author: mehdiregina
"""
import requests
import json
from bs4 import BeautifulSoup
import functools
import time
from multiprocessing import Pool
import numpy as np



url_top_100 = "https://lespoir.jimdo.com/2015/03/05/classement-des-plus-grandes-villes-de-france-source-insee/"

def get_soup_from_url():
    """Renvoie le top 100 des villes les plus peuplées en france"""
    page = requests.get("https://lespoir.jimdo.com/2015/03/05/classement-des-plus-grandes-villes-de-france-source-insee/")
   
    return BeautifulSoup(page.content,'html.parser')

def get_top_100() :
    soup=get_soup_from_url
    liste_row=soup.select("tbody tr")
    
    liste_name = [ row.select("td:nth-of-type(2)")[0].get_text().strip('\n').strip() for row in liste_row]
    return liste_name



#adresse url
api_key = "AIzaSyBCz0ytRM2bXOMAv6d4XYuEMuoUL7BJBMg"


def get_distance_matrix():
    """Utilisation de l'api googl pour obtenir la matrice des distances"""
   
    
    orgine = get_top_100()
    destination = get_top_100()
    #tab_dist= nd array ?
    
    
    for i,origin in enumerate(origine) :
        for j,dest in enumerate(destination) :
            if(j>i):
                url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins="+origin+"&destinations="+dest+"&key="+api_key
                page = requests.get(url)
                json_obj = json.loads(page.content)
                json_obj["rows"]["elements"]["distance"]["value"]
            
            
    
   
    return tab_distance

            
    