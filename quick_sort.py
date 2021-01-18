
import sys
import time


def quick(data, isArray = True):
    nbCompar = 0
    nbIter = 0
    if isArray == True:
        array = data.split(';')
        start_time = time.time()
        separator = ";"
    else:
        array = data

    length = len(array)


    if length <= 1:
        return array
    else:
        pivot = array.pop()

    items_lower = []
    items_greater = []
    
    for item in array:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)
    
    # print(quick(items_lower, False))
    # print(quick(items_lower, False) + [pivot] + quick(items_greater, False))
    result = quick(items_lower, False) + [pivot] + quick(items_greater, False)
    print(result)



quick(sys.argv[1])
