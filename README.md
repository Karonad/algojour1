# algojour1
Repository Algo Yannis Battiston, Rémy Pachocinski, Quentin Flé TD 1

bubble sort:
    2 Boucle, 1 boucle for qui recupere chaque valeur du tableau et une deuxieme qui compare les valeurs du tableau jusqu'a i-1 et échange les deux nombre si l'élément suivant est plus grand que le précédent. j est remis remis à 0 apres chaque échange afin de le ramener jusqu'a la plus petite valeur du tableau

selection sort:
    2 boucle, 1 boucle for qui recupere chaque valeur du tableau et qui associe la valeur comme la plus petite pour le moment(smallest) et une deuxieme qui compare smallest aux valeurs futur du tableau qui deviennes smallest si ils sont inferieur a celle ci et ceux jusqu'a la fin du tableau.

insertion sort:
    2 boucle, 1 boucle for qui recupere chaque valeur du tableau qui recupere l'index précédente et stock la valeur a l'index i. Une deuxieme qui traverse les valeurs déja parcouru dans le sens inverse. Pour échanger les 2, on remplace la valeur u+1 par u puis u par la valeur de i stocké plus tot.

merge sort:
    La fonction divise l'array en 2 qui lui est donné en une valeur L qui contient la moitié gauche de l'array et R qui contient la moitié droite de l'array. Si la taille de l'array est supérieur à 1, on réexecute cet étape sinon on les compare pour reformer un array de 2 valeurs trié qui sera comparer avec un deuxième array de deux valeurs triés et ainsi de suite jusqu'à retrouver notre array initial mais trié. 
        
quick sort:
    2 "boucle": La fonction selectionne un pivot et séparre le reste de la liste en 2 list, 1 avec les nombre plus petit et 1 avec les nombres plus grand la fonction s'appelle elle meme dans le return afin de répeter l'opération jusqu'à avoir tout les nombres dans des list de 1 ou des pivots pour les additionner en 1 seul liste


