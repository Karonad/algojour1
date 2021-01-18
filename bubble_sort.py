import sys

import time

def bubble(data):
    array = data.split(';')
    nbCompar  = 0
    nbIter  = 0
    start_time = time.time()
    j = 0
    separator = ";"
    

    for i in range(0, len(array)) :
        while j < i:
            nbCompar += 1
            if (array[j+1] < array[j]):
                array[j], array[j+1] = array[j+1], array[j]
                nbIter += 1
                j = 0
            else:
                j += 1

    endTime = time.time() - start_time
    print("Série : " + str(data))
    print("Résultat : " + separator.join(array))
    print("Nb de comparaison : " + str(nbCompar))
    print("Nb d'itération : " + str(nbIter))
    print("Temps (sec) : " + str(endTime))

bubble(sys.argv[1])
