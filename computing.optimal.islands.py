import random

def nakljucne_tocke(n, k):
    #nam da seznam k točk v koordinatnem sistemu na intervalu [0,n]x[0,n]
    #koordinate so zaokrožene na 3 decimalna mesta
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

tocke = nakljucne_tocke(10,10)
print(tocke)

#randPoints = [[6.795, 6.982], [3.744, 7.532], [6.621, 1.728], [8.745, 9.22], [3.676, 3.392], [4.494, 8.904], [9.794, 8.195], [2.055, 3.823], [2.384, 1.969], [6.45, 8.747]]  

def najvisja_tocka(randPoints):
    #določi točko, ki ima največjo y koordinato          
    return max(randPoints,key=lambda item: item[1])

najvisja = najvisja_tocka(tocke)
print(najvisja)

def povezave(randPoints):
    #določi seznam vseh možnih povezav med dvema točkama na množici točk, brez najvišje
    x = najvisja_tocka(randPoints)
    randPoints.remove(x)
    seznam = []
    for i in range(0, len(randPoints)):
        a = randPoints[i]
        for j in range(i, len(randPoints)):
            b = randPoints[j]
            seznam.append((a,b))
    return seznam

print(povezave(tocke))
print(len(povezave(tocke)))

#def trikotnik(a,b,c):
    #določi vse legalne trikotnike na najvišji točki in povezavah
    

def ploscina_trikotnika(a,b,c):
    #ploščina trikotnika z oglišči a, b in c
    x=[a[0],b[0],c[0]]
    y=[a[1],b[1],c[1]]
    area=0.5*( (x[0]*(y[1]-y[2])) + (x[1]*(y[2]-y[0])) + (x[2]*(y[0]-y[1])) )
    return area
