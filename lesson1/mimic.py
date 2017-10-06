#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Mimic pyquick exercise -- optional extra exercise.
Google's Python Class

Read in the file specified on the command line.
Do a simple split() on whitespace to obtain all the words in the file.
Rather than read the file line by line, it's easier to read
it into one giant string and split it once.

Build a "mimic" dict that maps each word that appears in the file
to a list of all the words that immediately follow that word in the file.
The list of words can be be in any order and should include
duplicates. So for example the key "and" might have the list
["then", "best", "then", "after", ...] listing
all the words which came after "and" in the text.
We'll say that the empty string is what comes before
the first word in the file.

With the mimic dict, it's fairly easy to emit random
text that mimics the original. Print a word, then look
up what words might come next and pick one at random as
the next work.
Use the empty string as the first word to prime things.
If we ever get stuck with a word that is not in the dict,
go back to the empty string to keep things moving.

Note: the standard python module 'random' includes a
random.choice(list) method which picks a random element
from a non-empty list.

For fun, feed your program to itself as input.
Could work on getting it to put in linebreaks around 70
columns, so the output looks better.

"""

import random
import sys


def mimic_dict(filename):
  """Returns mimic dict mapping each word to list of words which follow it."""
  # +++your code here+++
  with open(filename,'r') as fichier:
      texte=fichier.read()
  liste_mot=texte.split(" ")
  liste_mot_unique=list(set(liste_mot))
  
  mimic_dic=dict((mot_cle,0) for mot_cle in liste_mot_unique)
  #Pour chaque mot clé je constitue une liste 
  #lourd double for...
  for mot_cle in mimic_dic.keys():
      buffer_liste=list()
      for i,mot in enumerate(liste_mot):
          #les mots suivant le mot clé dans le texte sont stockés dans une liste
          if(mot==mot_cle and i!=len(liste_mot)-1):
              buffer_liste.append(liste_mot[i+1])
      mimic_dic[mot_cle]=buffer_liste

  return mimic_dic
  
#mimic dict améliorés
def mimic_dict2(filename):
    with open(filename,'r') as fichier:
        texte=fichier.read()
    liste_mot=texte.split()
      
    mimic_dic2=dict()
      
    for i,mot in enumerate(liste_mot):
        if(i!= len(liste_mot)-1):
            try:
                #opération "normale"
                mimic_dic2[mot].append(liste_mot[i+1])
            except (KeyError):
                #si keyerror => initialisation !
                mimic_dic2[mot]=list()
                mimic_dic2[mot].append(liste_mot[i+1])
                
        #quid du dernier mot
        else:
    return mimic_dic2


def print_mimic(mimic_dict, word):
  """Given mimic dict and start word, prints 200 random words."""
  # +++your code here+++
  #j'initialise mimic_word avec le mot entré en param
  mimic_string=''
  mimic_string+=word
  
  for i in range(0,50):
      #je récupère la liste de mot correspondants
      #necessaire de vérifier si le mot existe et à une liste
      try:
          liste_mot=mimic_dict[word]
      except(NameError):
          print("Le mot n'existe pas dans le texte")
          word=""
          liste_mot=mimic_dict[word]
      if(len(liste_mot)>0 ):
          #je prend un numéro d'index au hasard dans cette liste
          mot_tire=random.choice(liste_mot)
          #je l'ajoute à mimic string
          mimic_string+=" "+mot_tire
          #je change le mot par le mot pris en param
          word=mot_tire
      else:
          word=''
          
  print(mimic_string)




# Provided main(), calls mimic_dict() and mimic()
def main():
  #if len(sys.argv) != 2:
   #@ print ('usage: ./mimic.py file-to-read')
    #sys.exit(1)

  mim_dict = mimic_dict('small.txt')
  print_mimic(mim_dict, 'not')


if __name__ == '__main__':
  main()
