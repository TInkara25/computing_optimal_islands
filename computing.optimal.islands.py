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

#-------------------------------------POMOŽNE FUNKCIJE--------------------------------------------------


def ploscina_trikotnika(a,b,c):
    #ploščina trikotnika z oglišči a, b in c
    x=[a[0],b[0],c[0]]
    y=[a[1],b[1],c[1]]
    area=abs(0.5*( (x[0]*(y[1]-y[2])) + (x[1]*(y[2]-y[0])) + (x[2]*(y[0]-y[1]))))
    return area


def legalen(a,b,c,d):
    # legalen_trikotnik preveri ali je d znotraj trikotnika abc
    pl = ploscina_trikotnika(a,b,c)
    pl1 = ploscina_trikotnika(d,b,c)
    pl2 = ploscina_trikotnika(a,d,c)
    pl3 = ploscina_trikotnika(a,b,d)
    
    if pl == pl1 + pl2 + pl3:
        return False
    else:
        return True


def urejena_vozlisca(points, a):
    #uredi seznam točk points glede na lego v odvisnosti od a, v nasprotni smeri urinega kazalca
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

 
def ustrezna_tocka(a,b,c):
#funkcija preveri ali točka c leži nad premico, ki gre skozi a in b
    if b[0] == a[0]:
        return True 
    else:
        k = (b[1] - a[1]) / (b[0] - a[0])
        y = k*c[0] - k*a[0] + a[1]
        if y <= c[1]:
            return True
        else:
            return False

#----------------------------------------------------------------------------------------------------------------------

def legalni_trikotniki(points):
    #na seznamu poišče prazne trikotnike
    #vrne seznam trikotnikov, urejeni so tako, da je njihovo prvo oglišče tisto z najvišjo koordinato, 
    #ostali dve pa sta urejeni od leve proti desni glede na prvega
    seznam_legalnih_povezav = []
    n = len(points)
    for i in range(0,n): 
        a = max(points,key=lambda item: item[1])
        points.remove(a) 
        urejena = urejena_vozlisca(points, a)
        for i in range(0,len(urejena)):
            b = urejena[i]
            urejena.remove(b)
            for j in range(0,len(urejena)):
                c = urejena[j]
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
                urejena.append(c)
                urejena = urejena_vozlisca(urejena, a)
                if test == True:
                    if [a,c,b]  in seznam_legalnih_povezav:
                        pass
                    elif [a,b,c] in seznam_legalnih_povezav:
                        pass
                    else:
                        e = urejena_vozlisca([b,c],a)[0]
                        f = urejena_vozlisca([b,c],a)[1]
                        seznam_legalnih_povezav.append([a,e,f])
            urejena.append(b)
            urejena = urejena_vozlisca(urejena, a)
    return seznam_legalnih_povezav


def maximalni_veckotniki(points):
    #išče maksimalno ploščino večkotnika, tako da za vsak trikotnik iz seznama preveri kako bi ga lahko povečali
    #ko najdemo potencialno povečavo, na njej rekurzivno zopet iščemo maksimalni večkotnik
    M = 0
    opt = dict()
    tc = points.copy()
    trikotniki = legalni_trikotniki(points)
    for i in range(0, len(trikotniki)):
        trikotnik = trikotniki[i]
        a = trikotnik[0]
        b = trikotnik[1]
        c = trikotnik[2]
        opt[str(a) + str(b) + str(c)] = ploscina_trikotnika(a,b,c)
        for j in tc:
            if ustrezna_tocka(j, b, c) == True and ([a, j, b] in trikotniki):
                opt[str(a) + str(b) + str(c)]  = max(opt[str(a) + str(b) + str(c)] , ploscina_trikotnika(a,b,c) + opt[str(a) + str(j) + str(b)])
        M = max(M, opt[str(a) + str(b) + str(c)])
    return M

#-------------------------------------TESTIRANJE--------------------------------------------------

print("Sledijo poskusne meritve, točke bodo naključno razporejene v kvadrant velikosti 50x50 enot. Izvajali bomo poskus za 5, 10, 20, 30, 50, 100, in 150 točk")

#===============================================

print("Izvajamo poskus za 5 točk")

print("1. poskus")
start_time = time.time()

print(maximalni_veckotniki(nakljucne_tocke(50, 50, 5)))

elapsed_time = time.time() - start_time
print(elapsed_time)

print("2. poskus")
start_time = time.time()

print(maximalni_veckotniki(nakljucne_tocke(50, 50, 5)))

elapsed_time = time.time() - start_time
print(elapsed_time)

print("3. poskus")
start_time = time.time()

print(maximalni_veckotniki(nakljucne_tocke(50, 50, 5)))

elapsed_time = time.time() - start_time
print(elapsed_time)

print("4. poskus")
start_time = time.time()

print(maximalni_veckotniki(nakljucne_tocke(50, 50, 5)))

elapsed_time = time.time() - start_time
print(elapsed_time)

print("5. poskus")
start_time = time.time()

print(maximalni_veckotniki(nakljucne_tocke(50, 50, 5)))

elapsed_time = time.time() - start_time
print(elapsed_time)

print("6. poskus")
start_time = time.time()

print(maximalni_veckotniki(nakljucne_tocke(50, 50, 5)))

elapsed_time = time.time() - start_time
print(elapsed_time)

print("7. poskus")
start_time = time.time()

print(maximalni_veckotniki(nakljucne_tocke(50, 50, 5)))

elapsed_time = time.time() - start_time
print(elapsed_time)

print("8. poskus")
start_time = time.time()

print(maximalni_veckotniki(nakljucne_tocke(50, 50, 5)))

elapsed_time = time.time() - start_time
print(elapsed_time)

print("9. poskus")
start_time = time.time()

print(maximalni_veckotniki(nakljucne_tocke(50, 50, 5)))

elapsed_time = time.time() - start_time
print(elapsed_time)

print("10. poskus")
start_time = time.time()

print(maximalni_veckotniki(nakljucne_tocke(50, 50, 5)))

elapsed_time = time.time() - start_time
print(elapsed_time)

#=========================================================

print("Izvajamo poskus za 10 točk")

print("1. poskus")
start_time = time.time()

print(maximalni_veckotniki(nakljucne_tocke(50, 50, 10)))

elapsed_time = time.time() - start_time
print(elapsed_time)

print("2. poskus")
start_time = time.time()

print(maximalni_veckotniki(nakljucne_tocke(50, 50, 10)))

elapsed_time = time.time() - start_time
print(elapsed_time)

print("3. poskus")
start_time = time.time()

print(maximalni_veckotniki(nakljucne_tocke(50, 50, 10)))

elapsed_time = time.time() - start_time
print(elapsed_time)

print("4. poskus")
start_time = time.time()

print(maximalni_veckotniki(nakljucne_tocke(50, 50, 10)))

elapsed_time = time.time() - start_time
print(elapsed_time)

print("5. poskus")
start_time = time.time()

print(maximalni_veckotniki(nakljucne_tocke(50, 50, 10)))

elapsed_time = time.time() - start_time
print(elapsed_time)

print("6. poskus")
start_time = time.time()

print(maximalni_veckotniki(nakljucne_tocke(50, 50, 10)))

elapsed_time = time.time() - start_time
print(elapsed_time)

print("7. poskus")
start_time = time.time()

print(maximalni_veckotniki(nakljucne_tocke(50, 50, 10)))

elapsed_time = time.time() - start_time
print(elapsed_time)

print("8. poskus")
start_time = time.time()

print(maximalni_veckotniki(nakljucne_tocke(50, 50, 10)))

elapsed_time = time.time() - start_time
print(elapsed_time)

print("9. poskus")
start_time = time.time()

print(maximalni_veckotniki(nakljucne_tocke(50, 50, 10)))

elapsed_time = time.time() - start_time
print(elapsed_time)

print("10. poskus")
start_time = time.time()

print(maximalni_veckotniki(nakljucne_tocke(50, 50, 10)))

elapsed_time = time.time() - start_time
print(elapsed_time)

#=========================================================

print("Izvajamo poskus za 20 točk")

print("1. poskus")
start_time = time.time()

print(maximalni_veckotniki(nakljucne_tocke(50, 50, 20)))

elapsed_time = time.time() - start_time
print(elapsed_time)

print("2. poskus")
start_time = time.time()

print(maximalni_veckotniki(nakljucne_tocke(50, 50, 20)))

elapsed_time = time.time() - start_time
print(elapsed_time)

print("3. poskus")
start_time = time.time()

print(maximalni_veckotniki(nakljucne_tocke(50, 50, 20)))

elapsed_time = time.time() - start_time
print(elapsed_time)

print("4. poskus")
start_time = time.time()

print(maximalni_veckotniki(nakljucne_tocke(50, 50, 20)))

elapsed_time = time.time() - start_time
print(elapsed_time)

print("5. poskus")
start_time = time.time()

print(maximalni_veckotniki(nakljucne_tocke(50, 50, 20)))

elapsed_time = time.time() - start_time
print(elapsed_time)

print("6. poskus")
start_time = time.time()

print(maximalni_veckotniki(nakljucne_tocke(50, 50, 20)))

elapsed_time = time.time() - start_time
print(elapsed_time)

print("7. poskus")
start_time = time.time()

print(maximalni_veckotniki(nakljucne_tocke(50, 50, 20)))

elapsed_time = time.time() - start_time
print(elapsed_time)

print("8. poskus")
start_time = time.time()

print(maximalni_veckotniki(nakljucne_tocke(50, 50, 20)))

elapsed_time = time.time() - start_time
print(elapsed_time)

print("9. poskus")
start_time = time.time()

print(maximalni_veckotniki(nakljucne_tocke(50, 50, 20)))

elapsed_time = time.time() - start_time
print(elapsed_time)

print("10. poskus")
start_time = time.time()

print(maximalni_veckotniki(nakljucne_tocke(50, 50, 20)))

elapsed_time = time.time() - start_time
print(elapsed_time)

#=========================================================

print("Izvajamo poskus za 30 točk")

print("1. poskus")
start_time = time.time()

print(maximalni_veckotniki(nakljucne_tocke(50, 50, 30)))

elapsed_time = time.time() - start_time
print(elapsed_time)

print("2. poskus")
start_time = time.time()

print(maximalni_veckotniki(nakljucne_tocke(50, 50, 30)))

elapsed_time = time.time() - start_time
print(elapsed_time)

print("3. poskus")
start_time = time.time()

print(maximalni_veckotniki(nakljucne_tocke(50, 50, 30)))

elapsed_time = time.time() - start_time
print(elapsed_time)

print("4. poskus")
start_time = time.time()

print(maximalni_veckotniki(nakljucne_tocke(50, 50, 30)))

elapsed_time = time.time() - start_time
print(elapsed_time)

print("5. poskus")
start_time = time.time()

print(maximalni_veckotniki(nakljucne_tocke(50, 50, 30)))

elapsed_time = time.time() - start_time
print(elapsed_time)

print("6. poskus")
start_time = time.time()

print(maximalni_veckotniki(nakljucne_tocke(50, 50, 30)))

elapsed_time = time.time() - start_time
print(elapsed_time)

print("7. poskus")
start_time = time.time()

print(maximalni_veckotniki(nakljucne_tocke(50, 50, 30)))

elapsed_time = time.time() - start_time
print(elapsed_time)

print("8. poskus")
start_time = time.time()

print(maximalni_veckotniki(nakljucne_tocke(50, 50, 30)))

elapsed_time = time.time() - start_time
print(elapsed_time)

print("9. poskus")
start_time = time.time()

print(maximalni_veckotniki(nakljucne_tocke(50, 50, 30)))

elapsed_time = time.time() - start_time
print(elapsed_time)

print("10. poskus")
start_time = time.time()

print(maximalni_veckotniki(nakljucne_tocke(50, 50, 30)))

elapsed_time = time.time() - start_time
print(elapsed_time)

#=========================================================

print("Izvajamo poskus za 50 točk")

print("1. poskus")
start_time = time.time()

print(maximalni_veckotniki(nakljucne_tocke(50, 50, 50)))

elapsed_time = time.time() - start_time
print(elapsed_time)

print("2. poskus")
start_time = time.time()

print(maximalni_veckotniki(nakljucne_tocke(50, 50, 50)))

elapsed_time = time.time() - start_time
print(elapsed_time)

print("3. poskus")
start_time = time.time()

print(maximalni_veckotniki(nakljucne_tocke(50, 50, 50)))

elapsed_time = time.time() - start_time
print(elapsed_time)

print("4. poskus")
start_time = time.time()

print(maximalni_veckotniki(nakljucne_tocke(50, 50, 50)))

elapsed_time = time.time() - start_time
print(elapsed_time)

print("5. poskus")
start_time = time.time()

print(maximalni_veckotniki(nakljucne_tocke(50, 50, 50)))

elapsed_time = time.time() - start_time
print(elapsed_time)

print("6. poskus")
start_time = time.time()

print(maximalni_veckotniki(nakljucne_tocke(50, 50, 50)))

elapsed_time = time.time() - start_time
print(elapsed_time)

print("7. poskus")
start_time = time.time()

print(maximalni_veckotniki(nakljucne_tocke(50, 50, 50)))

elapsed_time = time.time() - start_time
print(elapsed_time)

print("8. poskus")
start_time = time.time()

print(maximalni_veckotniki(nakljucne_tocke(50, 50, 50)))

elapsed_time = time.time() - start_time
print(elapsed_time)

print("9. poskus")
start_time = time.time()

print(maximalni_veckotniki(nakljucne_tocke(50, 50, 50)))

elapsed_time = time.time() - start_time
print(elapsed_time)

print("10. poskus")
start_time = time.time()

print(maximalni_veckotniki(nakljucne_tocke(50, 50, 50)))

elapsed_time = time.time() - start_time
print(elapsed_time)

#=========================================================
print("Izvajamo poskus za 100 točk")

print("1. poskus")
start_time = time.time()

print(maximalni_veckotniki(nakljucne_tocke(50, 50, 100)))

elapsed_time = time.time() - start_time
print(elapsed_time)

print("2. poskus")
start_time = time.time()

print(maximalni_veckotniki(nakljucne_tocke(50, 50, 100)))

elapsed_time = time.time() - start_time
print(elapsed_time)

print("3. poskus")
start_time = time.time()

print(maximalni_veckotniki(nakljucne_tocke(50, 50, 100)))

elapsed_time = time.time() - start_time
print(elapsed_time)

print("4. poskus")
start_time = time.time()

print(maximalni_veckotniki(nakljucne_tocke(50, 50, 100)))

elapsed_time = time.time() - start_time
print(elapsed_time)

print("5. poskus")
start_time = time.time()

print(maximalni_veckotniki(nakljucne_tocke(50, 50, 100)))

elapsed_time = time.time() - start_time
print(elapsed_time)

print("6. poskus")
start_time = time.time()

print(maximalni_veckotniki(nakljucne_tocke(50, 50, 100)))

elapsed_time = time.time() - start_time
print(elapsed_time)

print("7. poskus")
start_time = time.time()

print(maximalni_veckotniki(nakljucne_tocke(50, 50, 11000)))

elapsed_time = time.time() - start_time
print(elapsed_time)

print("8. poskus")
start_time = time.time()

print(maximalni_veckotniki(nakljucne_tocke(50, 50, 100)))

elapsed_time = time.time() - start_time
print(elapsed_time)

print("9. poskus")
start_time = time.time()

print(maximalni_veckotniki(nakljucne_tocke(50, 50, 100)))

elapsed_time = time.time() - start_time
print(elapsed_time)

print("10. poskus")
start_time = time.time()

print(maximalni_veckotniki(nakljucne_tocke(50, 50, 100)))

elapsed_time = time.time() - start_time
print(elapsed_time)

#=========================================================

print("Izvajamo poskus za 150 točk")

print("1. poskus")
start_time = time.time()

print(maximalni_veckotniki(nakljucne_tocke(50, 50, 150)))

elapsed_time = time.time() - start_time
print(elapsed_time)

print("2. poskus")
start_time = time.time()

print(maximalni_veckotniki(nakljucne_tocke(50, 50, 150)))

elapsed_time = time.time() - start_time
print(elapsed_time)

print("3. poskus")
start_time = time.time()

print(maximalni_veckotniki(nakljucne_tocke(50, 50, 150)))

elapsed_time = time.time() - start_time
print(elapsed_time)

print("4. poskus")
start_time = time.time()

print(maximalni_veckotniki(nakljucne_tocke(50, 50, 150)))

elapsed_time = time.time() - start_time
print(elapsed_time)

print("5. poskus")
start_time = time.time()

print(maximalni_veckotniki(nakljucne_tocke(50, 50, 150)))

elapsed_time = time.time() - start_time
print(elapsed_time)

print("6. poskus")
start_time = time.time()

print(maximalni_veckotniki(nakljucne_tocke(50, 50, 150)))

elapsed_time = time.time() - start_time
print(elapsed_time)

print("7. poskus")
start_time = time.time()

print(maximalni_veckotniki(nakljucne_tocke(50, 50, 150)))

elapsed_time = time.time() - start_time
print(elapsed_time)

print("8. poskus")
start_time = time.time()

print(maximalni_veckotniki(nakljucne_tocke(50, 50, 150)))

elapsed_time = time.time() - start_time
print(elapsed_time)

print("9. poskus")
start_time = time.time()

print(maximalni_veckotniki(nakljucne_tocke(50, 50, 150)))

elapsed_time = time.time() - start_time
print(elapsed_time)

print("10. poskus")
start_time = time.time()

print(maximalni_veckotniki(nakljucne_tocke(50, 50, 150)))

elapsed_time = time.time() - start_time
print(elapsed_time)

#=========================================================
