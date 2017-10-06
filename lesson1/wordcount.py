#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

import sys


# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.

def get_count(filename):
    """create a dictionnary keys :word, values: count"""
    #je retranscris mon fichier dans un str
    with open(filename) as file:
        texte=file.read()
    #je split les mots dans une liste
    liste_mot=texte.split()
    
    dico=dict()
    #je parcours la liste de mot
    for mot in liste_mot:
        #j'ajoute +1 au count associé au mot, s'il n'existe pas encore dans le dict je l'instancie
        try:
            dico[mot]+=1
        except(KeyError):
            dico[mot]=1
    return dico


def print_words(filename):
    """Renvoie la liste des mots et leur count associé au fichier"""
    dico=get_count(filename)
    #j'affiche pour chaque tuple (cle,valeur) le mot et le count
    [print(mot,valeur) for mot,valeur in dico.items()]
        
def print_top(filename):
    """Renvoie les 20 mots les plus communs et leur count"""
    dico=get_count(filename)
    #necessité de trier le dictionnaire selon ses valeurs
    # => trie des tuples  (cle,valeur) selon leur valeur
    dico_sorted=sorted(dico.items(),key=lambda tuple_item:tuple_item[1],reverse=True)
    [print(dico_sorted[i]) for i in range(0,20)]
        
###

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
  #if len(sys.argv) != 3:
   # print ('usage: ./wordcount.py {--count | --topcount} file')
  #  sys.exit(1)

   # option = sys.argv[1]
  #  filename = sys.argv[2]
   # if (option == '--count'):
     print_words("alice.txt")
   # elif (option == '--topcount'):
     print("---------")
     print_top("alice.txt")
   # else:
    #   print ('unknown option: ' + option)
     #  sys.exit(1)

if __name__ == '__main__':
  main()
