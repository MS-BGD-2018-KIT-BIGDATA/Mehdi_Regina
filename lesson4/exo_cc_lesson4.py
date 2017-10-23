#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 13:30:36 2017

@author: mehdiregina
"""
import requests
import json
import numpy as np
import pandas as pd
import re

def get_json_from_url(url):
    page = requests.get(url)
    json_obj = json.loads(page.content)
    return json_obj

def get_list_cis(url):
    """Renvoie la liste des codecis associés à la query ibuprofene"""
    json_obj = get_json_from_url(url)
    liste_cis = [med["codeCIS"] for med in json_obj]
    return liste_cis

def get_med_info(code_cis):
    """Pour chaque cis je retourne les infos : ..."""
    
    json_obj2 = get_json_from_url("https://www.open-medicaments.fr/api/v1/medicaments/"+code_cis)
        
    #get med datas
    denomination = json_obj2["denomination"]
    lab = json_obj2["titulaires"][0]
    ref_dosage = json_obj2["compositions"][0]["referenceDosage"]
    dosage_sub = json_obj2["compositions"][0]["substancesActives"][0]["dosageSubstance"]
    libelle =  json_obj2["presentations"][0]['libelle']
    
    #get name
    name = " ".join(re.findall(r'[A-Z]+',denomination))
  

    #compute ratio
    if "comprimé" in libelle :
        nb_comprime = re.findall(r'[0-9]+',libelle)[0]
        ratio =  "%.2f" % (int(dosage_sub.split()[0])/float(nb_comprime))
        ratio = ratio+"mg/comprime"
    elif "ml" in libelle :
        ratio = int(dosage_sub.split()[0])/float(ref_dosage.split()[0])
        ratio = str(ratio)+ dosage_sub.split()[1] +"/"+ ref_dosage.split()[1]
    else:
        ratio = "n/a"
  
    #compute price
    prix = json_obj2["presentations"][0]['prix']
    if prix is None :
        prix = "libre"
    
    return code_cis, name, lab, prix, ratio

    

#main
list_cis = get_list_cis("https://www.open-medicaments.fr/api/v1/medicaments?query=ibuprofene")

res = [get_med_info(cis) for cis in list_cis]

df = pd.DataFrame(data = res, columns=["CodeCis","Denomination","Lab","Prix","Ratio_Ibuprofene"])
print (df)
