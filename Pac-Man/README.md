# Pacman-Search

breadth first sech

# Exercici 1: A*
- Manhattan
Tenim un node "n" i que la seva heurística es 5. Si avançem cap al node "n'" i avançem 3 caselles, la heurística de "n'" serà 2, i k(n,n') serà 3, ja que el cost de desplaçar-se per una casella es de 1. Per tant sempre es complirà que h(n) serà més petit o igual que la suma del cost d'anar des de "n" fins a "n'" i la heurística de "n'", perquè la resta que apliquem a l'heurística es compensa amb la distància entre els 2 nodes.

- Euclidean
No sabíem si era consistent o no així que hem fet path-max i va que xute
