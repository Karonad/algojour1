
import sys
import time


nbCompar = 0

def quick_sort(array):

    global nbCompar

    length = len(array)


    if length <= 1:
        return array
    else:
        pivot = array.pop()

    items_lower = []
    items_greater = []
    nbCompar += 1
    for item in array:
        if int(item) >= int(pivot):
            items_greater.append(item)
        else:
            items_lower.append(item)
    return quick_sort(items_lower) + \
        [pivot] + quick_sort(items_greater)

def main(data):

    global nbCompar

    array = data.split(';')
    separator = ";"
    start_time = time.time()

    result = quick_sort(array)
    execution_time = round(time.time() - start_time, 2)

    print("Serie : " + sys.argv[1])
    print("Resultat : " + separator.join(result))
    print("Nb de comparaison : " + str(nbCompar))
    print("Temps (sec) : " + str(execution_time))


main(sys.argv[1])
