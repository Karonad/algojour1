import sys
import time

def selection(data):
    array = data.split(';')
    nbCompar  = 0
    nbIter  = 0
    start_time = time.time()
    j = 0
    separator = ";"
    array2 = []

    # for i in range(0, len(array)) :
    #     array2.append(min(array))
    #     array.remove(min(array))
    #     print(array2)
    for i in range(0, len(array)):
        array[i] = float(array[i])  
    for i in range(0, len(array)):
        smallest = i
        for j in range(i, len(array)):
            nbCompar += 1
            if array[smallest] > array[j]:
                smallest = j
        nbIter += 1
        temp = array[i]
        array[i] = array[smallest]
        array[smallest] = temp

    
    array = [ '%g' % elem for elem in array ]
    endTime = time.time() - start_time
    print("Série : " + str(data))
    print("Résultat : " + separator.join(array))
    print("Nb de comparaison : " + str(nbCompar))
    print("Nb d'itération : " + str(nbIter))
    print("Temps (sec) : " + str(endTime))
selection(sys.argv[1])
    
