import random

def nakljucne_tocke(m, n, k):
    #nam da seznam k točk v koordinatnem sistemu na intervalu [0,m]x[0,n]
    #koordinate so zaokrožene na 3 decimalna mesta
    rangeX = (0, m)
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

tocke = nakljucne_tocke(10,10,10)
#print(tocke)

#randPoints = [[6.795, 6.982], [3.744, 7.532], [6.621, 1.728], [8.745, 9.22], [3.676, 3.392], [4.494, 8.904], [9.794, 8.195], [2.055, 3.823], [2.384, 1.969], [6.45, 8.747]]  
#randPoints = [[0, 0], [5, 0], [0, 5], [0, 3], [1, 1], [7, 4]]

def najvisja_tocka(randPoints):
    #določi točko, ki ima največjo y koordinato (najvišjo točko)
    return max(randPoints,key=lambda item: item[1])

najvisja = najvisja_tocka(tocke)
#print(najvisja)

def povezave(randPoints):
    #določi seznam vseh možnih povezav med dvema točkama na množici točk, brez najvišje točke
    x = najvisja_tocka(randPoints)
    randPoints.remove(x)
    seznam = []
    for i in range(0, len(randPoints)):
        a = randPoints[i]
        for j in range(i+1, len(randPoints)):
            b = randPoints[j]
            seznam.append((a,b))
    return seznam


#print(randPoints)
#print(povezave(randPoints))
#print(len(povezave(randPoints)))

#print(povezave(randPoints)[1])
#print(povezave(randPoints)[20])

def ploscina_trikotnika(a,b,c):
    #ploščina trikotnika z oglišči a, b in c
    x=[a[0],b[0],c[0]]
    y=[a[1],b[1],c[1]]
    area=abs(0.5*( (x[0]*(y[1]-y[2])) + (x[1]*(y[2]-y[0])) + (x[2]*(y[0]-y[1]))))
    return area

#a = [0,0]
#b = [5,0]
#c = [0,5]
#d = [10,10]

#print(ploscina_trikotnika(a,b,c))

def legalen_trikotnik(a,b,c,d):
    #preveri, če točka d leži v trikotniku a, b, c
    pl = ploscina_trikotnika(a,b,c)
    pl1 = ploscina_trikotnika(d,b,c)
    pl2 = ploscina_trikotnika(a,d,c)
    pl3 = ploscina_trikotnika(a,b,d)
    if pl == pl1 + pl2 + pl3:
        return False
    else:
        return True

#print(legalen_trikotnik(a, b, c, d))
#print(randPoints)

def koncna(randPoints):
    #poišče legalne trikotnike na množici točk
    seznam = povezave(randPoints)
    a = najvisja
    for i in seznam: 
        nov_seznam = randPoints
        b = i[0]
        c = i[1]
        #print(b)
        #print(c)
        #nov_seznam.remove()
        nov_seznam.remove(b)
        nov_seznam.remove(c)
        #print(nov_seznam)
        for j in range(0, len(nov_seznam)): 
            d = nov_seznam[j]
            if legalen_trikotnik(a,b,c,d) == True:
                pl = ploscina_trikotnika(a, b, c)
                return pl
                #print(pl)
            else:
                pass
        nov_seznam.append(b)
        nov_seznam.append(c)

#print(randPoints)

def ustrezna_tocka(a,b,c):
    #preveri, če točka c leži nad premico skozi točki a in b
    k = (b[1] - a[1]) / (b[0] - a[0])
    y = k*c[0] - k*a[0] + a[1]
    if y <= c[1]:
        return True
    else:
        return False

#a = (0,0)
#b = (5,0)
#c = (0,5)
#d = (1,1)

#print(predznak(a, b, c))
#print(legalen_trikotnik(a, b, c, d))
#print(koncna(randPoints))

#print(ustrezna_tocka(a,b,c))
#print(randPoints)
