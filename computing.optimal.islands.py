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

#points = [[0, 0], [5, 0], [0, 5], [0, 3], [1, 1], [7, 4]]

#---------------POMOŽNE FUNKCIJE---------------------------------------------------------------
    
def ploscina_trikotnika(a,b,c):
    #ploščina trikotnika z oglišči a, b in c
    x=[a[0],b[0],c[0]]
    y=[a[1],b[1],c[1]]
    area=abs(0.5*( (x[0]*(y[1]-y[2])) + (x[1]*(y[2]-y[0])) + (x[2]*(y[0]-y[1]))))
    return area


# legalen_trikotnik preveri ali je d znotraj trikotnika abc
def legalen(a,b,c,d):
    pl = ploscina_trikotnika(a,b,c)
    pl1 = ploscina_trikotnika(d,b,c)
    pl2 = ploscina_trikotnika(a,d,c)
    pl3 = ploscina_trikotnika(a,b,d)
    
    if pl == pl1 + pl2 + pl3:
        return False
    else:
        return True

#print(points)

#uredi vozlišča glede na lego glede na a, od leve proti desni (nasprotni smeri urinega kazalca)
def urejena_vozlisca(points, a):
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

#tukaj a ni najvišja točka ampak eno izmed krajišč trikotnika, ki ni najvišje, c pa je novo oglišče potencialnega večkotnika
#preverja konveksnost potencialnega večkotnika
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

#--------------------------------------------------------------------------------------------------------

#na seznamu poišče prazne trikotnike
#vrne seznam trikotnikov, urejeni so tako, da je njihovo prvo oglišče tisto z najvišjo koordinato, ostali dve
    #pa sta urejeni od leve proti desni glede na prvega
def legalni_trikotniki(points):
    seznam_legalnih_povezav = []
    n = len(points)
    for i in range(0,n): 
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
                    if [a,c,b]  in seznam_legalnih_povezav:
                        pass
                    elif [a,b,c] in seznam_legalnih_povezav:
                        pass
                    else:
                        e = urejena_vozlisca([b,c],a)[0]
                        f = urejena_vozlisca([b,c],a)[1]
                        seznam_legalnih_povezav.append([a,e,f])
    return seznam_legalnih_povezav
                
tocke = [[0, 0], [5, 0], [0, 5], [0, 3], [1, 1], [7, 4]]
print(legalni_trikotniki(tocke))


#dodaja povezave k trikotnikom
def maximalni_veckotniki(points):
    tc = points.copy()
    trikotniki = legalni_trikotniki(points)
    #print(trikotniki)
    for i in trikotniki:
        #pobere vsak trikotnik
        #print(i)
        a = i[0]
        b = i[1]
        c = i[2]
        print(a)
        print(b)
        print(c)
        #tc.remove(a)
        #tc.remove(b)   
        #tc.remove(c)
        opt = 0
        #print(trikotniki)
        for j in tc:
            if ustrezna_tocka(b,c,j) == True and ([a, c, j] or [a, j, c]) in trikotniki:
                print([a, c, j])
                opt = max(opt, opt + ploscina_trikotnika(a,c,j))
            else:
                pass
        #print(trikotniki)
        #print(points)
    return opt
        
print(maximalni_veckotniki(points))

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
