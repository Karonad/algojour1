# liste = [3, 4, 5, 18.25, 24.23]

import sys
import time

def fusion(gauche,droite):
    resultat = []
    iG, iD = 0, 0
    while iG < len(gauche) and iD < len(droite):        
        if gauche[iG] <= droite[iD]:
            resultat.append(gauche[iG])
            iG += 1
        else:
            resultat.append(droite[iD])
            iD += 1
    if gauche:
            resultat.extend(gauche[iG:])
    if droite:
        resultat.extend(droite[iD:])
    return resultat    

def insertion(data):
    tableau = []
    separator = ";"
    if(isinstance(data, str)):
        tableau = data.split(';')
        for i in range(0, len(tableau)):
            tableau[i] = float(tableau[i])
    else:
        tableau = data
    print(tableau)
    if  len(tableau) <= 1: 
        return tableau
    split = len(tableau)//2
    tab1 = tableau[:split]
    tab2 = tableau[split:]
    print(tab1)
    print(tab2)
    gauche = insertion(tab1)
    droite = insertion(tab2)
    fusionne = fusion(gauche,droite)
    # print(fusionne) 
    # for i in range(0, len(array)):
    #     u = i - 1
    #     test = False
    
    #     while array[u] > array[i] and u >= 0:
    #         u = u - 1
    #         test = True
    #     u = u + 1
    #     if test == True:
    #         tmp = array[i]
    #         while i > u:
    #             array[i] = array[i-1]
    #             i -= 1
    #         array[u] = tmp
    #     print(array)
insertion(sys.argv[1])
# ------------------------- 
   
# for i in range(0, len(liste)):
#     u = i- 1
#     j = liste[i]
#     while u >= 0 and j < liste[u]
#         liste[u + 1] = liste[u]
#         liste -= 1
#     liste[u+1] = j









# # ------------
    
# liste = [4, 5, 3, 1, 2]
# # u = index 1 = liste[u] = 5
# # i = index 2 = liste[i] = 3
# for i in range(0, len(liste)):
#     u = i - 1
#     test = False
 
#     while liste[u] > liste[i] and u >= 0:
#         u = u - 1
#         test = True
#     u = u + 1
#     if test == True:
#         # tmp = 4
#         tmp = liste[u]
#         # liste[u] = 3
#         liste[u] = liste[i]
        

#     print(liste)