import sys
import time


def mergeSort(arr, nbCompar, nbIter):
    if len(arr) > 1:
        
         # Finding the mid of the array
        mid = len(arr)//2
 
        # Dividing the array elements
        L = arr[:mid]
        
        # into 2 halves
        R = arr[mid:]
 
        # Sorting the first half
        mergeSort(L, nbCompar, nbIter)
 
        # Sorting the second half
        mergeSort(R, nbCompar, nbIter)
 
        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            nbCompar += 1
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
 
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
def printing(array, nbCompar, nbIter):
    separator = ";"
    array = [ '%g' % elem for elem in array ]
    endTime = time.time() - start_time
    print("Série : " + sys.argv[1])
    print("Résultat : " + separator.join(array))
    print("Nb de comparaison : " + str(nbCompar))
    print("Nb d'itération : " + str(nbIter))
    print("Temps (sec) : " + str(endTime))

def main(data):
    arr = data.split(';')

    nbCompar  = 0
    nbIter  = 0
    
    j = 0
    for i in range(0, len(arr)):
        arr[i] = float(arr[i])

    mergeSort(arr, nbCompar, nbIter)
    printing(arr, nbCompar, nbIter)


start_time = time.time()
main(sys.argv[1]) 