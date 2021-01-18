import sys
import time

def insertion(data):
    array = data.split(';')
    nbCompar  = 0
    nbIter  = 0
    start_time = time.time()
    separator = ";"
    for i in range(0, len(array)):
        array[i] = float(array[i])
    for i in range(1, len(array)):
        u = i- 1
        j = array[i]
        while True:
            nbCompar += 1
            if(u >= 0 and j < array[u]):
                array[u + 1] = array[u]
                u -= 1
            else:
                break
        nbIter += 1
        array[u+1] = j
    array = [ '%g' % elem for elem in array ]
    endTime = time.time() - start_time
    print("Série : " + str(data))
    print("Résultat : " + separator.join(array))
    print("Nb de comparaison : " + str(nbCompar))
    print("Nb d'itération : " + str(nbIter))
    print("Temps (sec) : " + str(endTime))

insertion(sys.argv[1])

    # for i in range(0, len(array)):
        # j = i - 1
        # while j >= 0 and array[j] < array[i]
            # array[i] = array[j]
