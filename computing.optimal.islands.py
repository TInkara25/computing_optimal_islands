import random
import math


def nakljucne_tocke(m, n, k):
    #nam da seznam k točk v koordinatnem sistemu na intervalu [0,m]x[0,n]
    #koordinate so zaokrožene na 3 decimalna mesta
    rangeX = (0, m)
    rangeY = (0, n)
    qty = k  
    points = []
    i = 0
    while i<qty:
        x = round(random.uniform(*rangeX),3)
        y = round(random.uniform(*rangeY),3)
        points.append([x,y])
        i += 1
    return points

#tocke = nakljucne_tocke(10,10,10)
#print(tocke)

#points = [[6.795, 6.982], [3.744, 7.532], [6.621, 1.728], [8.745, 9.22], [3.676, 3.392], [4.494, 8.904], [9.794, 8.195], [2.055, 3.823], [2.384, 1.969], [6.45, 8.747]]  
points = [[0, 0], [5, 0], [0, 5], [0, 3], [1, 1], [7, 4]]


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

def predznak(a, b, c):
    return (a[0] - c[0]) * (b[1] - c[1]) - (b[0] - c[0]) * (a[1] - c[1])


def legalen(a,b,c,d):
    #legalen preveri ali je točka d znotraj trikotnika abc
    pl = ploscina_trikotnika(a,b,c)
    pl1 = ploscina_trikotnika(d,b,c)
    pl2 = ploscina_trikotnika(a,d,c)
    pl3 = ploscina_trikotnika(a,b,d)
    
    if pl == pl1 + pl2 + pl3:
        return False
    else:
        return True


def urejena_vozlisca(points, a):
    #funkcija vrne seznam urejenih vozlišč glede na točko a v nasprotni smeri urinega kazalca
    seznam_kotov = []
    for tocka in points:
        if tocka[0] == a[0]:
            kot1 = math.pi / 2
            seznam_parov = [tocka,kot1]
            seznam_kotov.append(seznam_parov)
        else:
            kot1 = math.atan((tocka[1]-a[1]) / (tocka[0]-a[0]))
            if kot1 < 0:
                kot1 += math.pi
                seznam_parov = [tocka,kot1]
                seznam_kotov.append(seznam_parov)
            else:
                seznam_parov = [tocka,kot1]
                seznam_kotov.append(seznam_parov)   
    seznam_kotov = sorted(seznam_kotov,key = lambda item: item[1])
    urejen_seznam_vozlisc = [item[0] for item in seznam_kotov]
    return urejen_seznam_vozlisc


def legalni_trikotniki(points):
    #vrne seznam praznih trikotnikov
    #prvo oglišče v vsakem trikotniku je tisto z najvišjo koordinato
    seznam_legalnih_trikotnikov = []
    for point in points: 
        a = max(points,key=lambda item: item[1])
        points.remove(a) 
        urejena = urejena_vozlisca(points, a)
        for i in range(0,len(urejena)):
            for j in range(i+1,len(urejena)):
                b = urejena[i]
                c = urejena[j]
                urejena.remove(b)
                urejena.remove(c)
                k = 0
                test = True
                while k < len(urejena) and test == True:
                    d = urejena[k]
                    if not legalen(a,b,c,d):
                        test = False
                        k +=1
                    else:
                        k += 1
                urejena.append(b)
                urejena.append(c)
                if test == True:
                    if [a,c,b]  in seznam_legalnih_trikotnikov:
                        pass
                    elif [a,b,c] in seznam_legalnih_trikotnikov:
                        pass
                    else:
                        seznam_legalnih_trikotnikov.append([a,b,c])
    return seznam_legalnih_trikotnikov

                
v = [4, 6]
tocke = [[0, 0], [5, 0], [0, 5], [0, 3], [1, 1], [7, 4]]


#print(urejena_vozlisca(tocke, v))
#print(legalni_trikotniki(tocke))

#tukaj a ni najvišja točka ampak eno izmed krajišč trikotnika, ki ni najvišje, c pa je novo oglišče potencialnega večkotnika. 
def ustrezna_tocka(a,b,c):
    if b[0] == a[0]:
        return True 
    else:
        k = (b[1] - a[1]) / (b[0] - a[0])
        y = k*c[0] - k*a[0] + a[1]
        if y <= c[1]:
            return True
        else:
            return False


#dodaja povezave k trikotnikom
def maximalni_veckotniki(points):
    tc = points.copy()
    trikotniki = legalni_trikotniki(points)
    #print(trikotniki)
    for i in trikotniki:
        #pobere vsak trikotnik
        legalne_tocke = [] #seznam moznih tock (brez oglisc trikotnika in tistih ki so pod premico b,c)
        #print(i)
        a = i[0]
        b = i[1]
        c = i[2]
        print(a)
        print(b)
        print(c)
        tc.remove(a)
        tc.remove(b)   
        tc.remove(c)
        for j in tc:
            if ustrezna_tocka(b,c,j) == True and legalen(a, b, c, j):
                legalne_tocke.append(j)
            else:
                pass
            urejene_legalne = urejena_vozlisca(legalne_tocke, b) #urejena vozlišča glede na oglišče b
        #print(trikotniki)
        #print(points)
    return legalne_tocke

        
#print(maximalni_veckotniki(points))

def max_ploscina(points):
    #na seznamu maksimalnih večkotnikov poišče tistega z največjo ploščino 
    #vrne njegovo ploščino in število njegovih oglišč
    max_veckotniki = maximalni_veckotniki(points)
    ploscine = []
    for i in range(0,len(max_veckotniki)):
        st_oglisc = 2
        pl = 0
        veckotnik = max_veckotniki[i]
        for j in range(0,len(veckotnik)-2):
            a = veckotnik[0]
            b = veckotnik[j+1]
            c = veckotnik[j+2]
            pl += ploscina_trikotnika(a,b,c)
            st_oglisc += 1
        ploscine.append([pl, st_oglisc])
    return max(ploscine, key = lambda item: item[0])

#print(max_ploscina(points))
