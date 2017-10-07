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
import pandas as pd


#donnes
api_key = "AIzaSyBCz0ytRM2bXOMAv6d4XYuEMuoUL7BJBMg"
url_top_100 = "https://lespoir.jimdo.com/2015/03/05/classement-des-plus-grandes-villes-de-france-source-insee/"

def get_soup_from_url():
    """Renvoie le top 100 des villes les plus peuplées en france"""
    page = requests.get("https://lespoir.jimdo.com/2015/03/05/classement-des-plus-grandes-villes-de-france-source-insee/")
   
    return BeautifulSoup(page.content,'html.parser')

def get_top_100() :
    soup = get_soup_from_url()
    liste_row = soup.select("tbody tr")
    
    liste_name = [ row.select("td:nth-of-type(2)")[0].get_text().strip('\n').strip() for row in liste_row]
    return liste_name[1:101]



def get_distance_matrix():
    """Utilisation de l'api googl pour obtenir la matrice des distances, 
    2 boucles for méthodes peu performante"""
   
    
    origine = get_top_100()
    destination = list(origine)
    ndarray_dist=np.ndarray((100,100),dtype = np.float)
    
    #boucle for à éviter si plus de temps y réfléchir
    for i_row,origin in enumerate(origine) :
        for i_col,dest in enumerate(destination) :
            if(i_col>i_row):
                url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins="+origin+"&destinations="+dest+"&key="+api_key
                page = requests.get(url)
                json_obj = json.loads(page.content)
                try :
                    ndarray_dist[i_row,i_col] = float(json_obj["rows"][0]["elements"][0]["distance"]["text"].split()[0])
                except KeyError :
                     ndarray_dist[i_row,i_col] = -9999
            
    np.savetxt("matrix", ndarray_dist, delimiter = ",")
    return ndarray_dist
        

matrix = get_distance_matrix()
    