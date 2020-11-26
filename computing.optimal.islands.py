import random

def nakljucne_tocke(n, k):
    rangeX = (0, n)
    rangeY = (0, n)
    qty = k  
    randPoints = []
    i = 0
    while i<qty:
        x = round(random.uniform(*rangeX),3)
        y = round(random.uniform(*rangeY),3)
        randPoints.append([x,y])
        i += 1
    return randPoints

#tocke = nakljucne_tocke(10,10)
#print(tocke)

randPoints = [[6.795, 6.982], [3.744, 7.532], [6.621, 1.728], [8.745, 9.22], [3.676, 3.392], [4.494, 8.904], [9.794, 8.195], [2.055, 3.823], [2.384, 1.969], [6.45, 8.747]]  

def najvecji_otok(randPoints):
    for i in randPoints:
        najvisja_tocka = max(randPoints,key=lambda item: item[1])            
    return najvisja_tocka

najvisja_tocka = najvecji_otok(randPoints)
print(najvisja_tocka)

randPoints = randPoints.remove(najvisja_tocka)
print(randPoints)

def povezave(randPoints):
    randPoints = randPoints.remove(najvisja_tocka)
    seznam = []
    for i in randPoints:
        for j in (randPoints.remove(i)):
            if (i,j) not in seznam:
                seznam.append((i,j))
    return seznam

print(povezave(randPoints))
print(randPoints)

def trikotnik(a,b,c):
    

def ploscina_trikotnika(a, b,c):
    x=[a[0],b[0],c[0]]
    y=[a[1],b[1],c[1]]
    area=0.5*( (x[0]*(y[1]-y[2])) + (x[1]*(y[2]-y[0])) + (x[2]*(y[0]-y[1])) )
    return area

print(ploscina_trikotnika(a, b,c))
