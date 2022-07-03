import marcpy as mp


def einzelwerte():
    print("Array eingeben:")
    arr = input()
    # arr = list(map(int, arr.split(' ')))
    arrf = list(map(float, arr.split(' ')))
    # arrtemp = []
    arrftemp = []
    # for i in arr:
    # arrtemp.append(i)
    for i in arrf:
        arrftemp.append(i)

    print("Mittelwert (marcpy.mean(arr)): ", mp.mean(arrftemp))
    print("Median (marcpy.median(arr)): ", mp.median(arrftemp))
    print("Modalwert (marcpy.mode(arr)): ", mp.mode(arrftemp))
    print("Interquartilabstand (marcpy.interquartilefiff(arr)): ", mp.interquartilediff(arrftemp))
    print("Spannweite (marcpy.span(arr)): ", mp.span(arrftemp))
    print("Standardabweichung (marcpy.std(arr)): ", mp.std(arrftemp))
    print("Varianz (marcpy.var()): ", mp.var(arrftemp))
    print(25, "% Quantil (marcpy.percentile(arr, pct)): ", mp.percentile(arrftemp, 25))
    print(50, "% Quantil (marcpy.percentile(arr, pct)): ", mp.percentile(arrftemp, 50))
    print(75, "% Quantil (marcpy.percentile(arr, pct)): ", mp.percentile(arrftemp, 75))
    abs_haeufigkeit(arrftemp)
    rel_haeufigkeit(arrftemp)
    kum_haeufigkeit(arrftemp)

    loop = 1
    while loop == 1:
        print("\nWeitere Berechnungen mit diesem Array?\nJ: ja\nN: nein")
        yes_no = input()
        if yes_no == 'J' or yes_no == 'j':
            print("1: Quantile\n2: Korrelationskoeffizient")
            func = int(input())
            if func == 1:
                percentile(arrf)
            if func == 2:
                corrcoef(arrf)
        else:
            break


def percentile(arr):
    if arr == 0:
        print("Array für Quantile eingeben: ")
        arr = input()
        arr = list(map(int, arr.split(' ')))

    print("Prozentzahl eingeben: ")
    pct = float(input())
    print(pct, "% Quantil (marcpy.percentile(arr, pct)): ", mp.percentile(arr, pct))


def corrcoef(arr):
    if arr == 0:
        print("Array 1 für Korrelationskoeffizienten eingeben:")
        arr = input()
        arr = list(map(int, arr.split(' ')))

    print("Array 2 für Korrelationskoeffizienten eingeben:")
    arr2 = input()
    arr2 = list(map(float, arr2.split(' ')))
    print("Array 1:", arr)
    print("Array 2:", arr2)
    print("Korrelationskoeffizient (marcpy.corrcoef(arr1, arr2)): ", mp.corrcoef(arr, arr2))


def fak():
    print("Zahl für Fakultät eingeben:")
    n = int(input())
    print("Fakultät (marcpy.fak(n)): ", mp.fak(n))


def plotlinregress():
    print("Array 1 für lineare Reggressionsfunktion eingeben:")
    arr1 = input()
    arr1 = list(map(int, arr1.split(' ')))
    print("Array 2 für lineare Reggressionsfunktion eingeben:")
    arr2 = input()
    arr2 = list(map(int, arr2.split(' ')))
    print("Label X-Achse eingeben:")
    lbl_x = input()
    print("Label Y-Achse eingeben:")
    lbl_y = input()
    print("lineare Reggressionsfunktion wird geplottet...")
    mp.plotlinregress(arr1, arr2, lbl_x, lbl_y)


def abs_haeufigkeit(arr):
    print("Absolute Häufigkeiten (marcpy.abs_haeufigkeit(arr)):", mp.abs_haeufigkeit(arr))


def rel_haeufigkeit(arr):
    print("Relative Häufigkeiten (marcpy.arel_haeufigkeit(arr)):", mp.rel_haeufigkeit(arr))


def kum_haeufigkeit(arr):
    print("Kumulierte Häufigkeiten (marcpy.kum_haeufigkeit(arr)):", mp.kum_haeufigkeit(arr))


def haeufigkeit():
    print("Welche Häufigkeit soll berechnet werden?\n1: absolute Häufigkeit"
          "\n2: relative Häufigkeit\n3: kumulierte Häufigkeit")
    f = int(input())
    print("Array eingeben:")
    arr = input()
    arr = list(map(int, arr.split(' ')))

    if f == 1:
        abs_haeufigkeit(arr)
    elif f == 2:
        rel_haeufigkeit(arr)
    elif f == 3:
        kum_haeufigkeit(arr)
    else:
        print("Wrong function")
        return

    loop = 1
    while loop == 1:
        print("Soll eine weitere Häufigkeit berechnet werden?\n"
              "J: ja\nN: nein")
        yes_no = input()
        if yes_no == "j" or yes_no == "J":
            print("Welche?\n1: absolute Häufigkeit"
                  "\n2: relative Häufigkeit\n3: kumulierte Häufigkeit")
            f = int(input())

            if f == 1:
                abs_haeufigkeit(arr)
            elif f == 2:
                rel_haeufigkeit(arr)
            elif f == 3:
                kum_haeufigkeit(arr)
            else:
                print("Wrong function")
                return
        else:
            return


def verteilung():
    print("Was soll berechnet werden?\n1: Bernoulli-verteilt"
          "\n2: Binomialkoeffizient\n3: binomial-verteilt"
          "\n4: geometrisch-verteilt\n5: poisson-verteilt"
          "\n6: gleichverteilt\n7: exponentialverteilt\n8: normalverteilt\n")
    func = int(input())

    if func == 1:
        bernoulliverteilt()
    elif func == 2:
        bincoef()
    elif func == 3:
        binomialverteilt()
    elif func == 4:
        geomverteilt()
    elif func == 5:
        poissonverteilt()
    elif func == 6:
        gleichverteilt()
    elif func == 7:
        exponentialverteilt()
    elif func == 8:
        normalverteilt()
    else:
        print("Wrong function")
        return


def bernoulliverteilt():
    print("Bernoulli-verteilt")
    print("Wahrscheinlichkeit p eingeben:")
    inp = input()

    if "/" in inp:
        index = inp.find("/")
        p = float(inp[0: index]) / float(inp[index + 1: len(inp)])
    else:
        p = float(inp)

    arr = mp.bernoulliverteilt(p)

    for pack in arr:
        print("P(X = {}) = {}".format(pack[0], pack[1]))
    print("Binomial Erwartungswert (marcpy.bernoullierwartung(p)):", mp.bernoullierwartung(p))
    print("Binomial Varianz (marcpy.bernoullivar(p)):", mp.bernoullivar(p))


def bincoef():
    print("n für (n über k) eingeben:")
    n = int(input())
    print("k für (n über k) eingeben:")
    k = int(input())
    bincoef = mp.bincoef(n, k)
    print("Binomialkoeffizient (marcpy.bincoef(n, k)) für n = {} und k = {}: {}".format(n, k, bincoef))


def binomialverteilt():
    print("Formel: (n über t) * p^t * q^(n-t)")
    print("Es werden alle t's berechnet!")
    print("n eingeben:")
    n = int(input())
    print("p eingeben (Kommazahl mit Punkt getrennt oder Bruch!):")
    inp = input()

    if "/" in inp:
        index = inp.find("/")
        p = float(inp[0: index]) / float(inp[index + 1: len(inp)])
    else:
        p = float(inp)

    print("Binomial verteilt P(X = t) (marcpy.binomialverteilt(n, p)):")
    arr = mp.binomialverteilt(n, p)
    for pack in arr:
        print("t: P(X = {}) = {}".format(pack[0], pack[1]))
    print("Binomial Erwartungswert (marcpy.binerwartung(n, p)):", mp.binerwartung(n, p))
    print("Binomial Varianz (marcpy.binvar(n, p)):", mp.binvar(n, p))

    loop = 1
    while loop == 1:
        print("\nSoll noch etwas mit diesen Werten berechnet werden?"
              "\n1: P(mindestens x)\n2: P(höchstens x)"
              "\n3: P(mindestens x und höchstens y)\n4: nein")
        func = int(input())
        if func == 1:
            print("x eingeben:")
            x = int(input())
            print("P(X >= {}) = {} (marcpy.binmindestens(arr, x))".format(x, mp.binmindestens(arr, x)))
        elif func == 2:
            print("x eingeben:")
            x = int(input())
            print("P(X <= {}) = {} (marcpy.binhoechtsens(arr, x))".format(x, mp.binhoechstens(arr, x)))
        elif func == 3:
            print("x (mindestens) eingeben:")
            x = int(input())
            print("y (höchstens) eingeben:")
            y = int(input())
            print("P(mindestens {} / höchstens {}) = {} (marcpy.binminhoe(arr, x, y))".format(x, y,
                                                                                              mp.binminhoe(arr, x, y)))
        else:
            break


def geomverteilt():
    print("Formel: p * q^(x-1)")
    print("Anzahl Versuche x für P(X = x) eingeben:")
    x = int(input())
    print("Wahrscheinlichkeit p eingeben (Kommazahl mit Punkt getrennt oder Bruch!):")
    inp = input()

    if "/" in inp:
        index = inp.find("/")
        p = float(inp[0: index]) / float(inp[index + 1: len(inp)])
    else:
        p = float(inp)

    print("Geometrisch verteilt P(X = {}):{} (marcpy.geomverteilt(x, p))".format(x, mp.geomverteilt(x, p)))
    print("Geometrisch Erwartungswert (marcpy.geomerwartung(p)):", mp.geomerwartung(p))
    print("Geometrisch Varianz (marcpy.geomvar(p)):", mp.geomvar(p))


def poissonverteilt():
    print("Poissonverteilt Formel: lambda^x / x! * e^(-lambda)")
    print("Lambda = gegebene Wahrscheinlichkeit/Anzahl")
    print("x = zu prüfende Anzahl für P(X = x)")
    print("Lambda eingeben:")
    lbd = float(input())
    if lbd < 0:
        print("Lambda muss größer als 0 sein!")
        return

    print("x eingeben:")
    x = int(input())

    print("poissonverteilt P(X = {}) = {} (marcpy.poissonverteilt(x, lambda))".format(x, mp.poissonverteilt(x, lbd)))
    print("poissonverteilt P(X <= {}) = {} (marcpy.poissonverteiltF(x, lambda))".format(x, mp.poissonverteiltF(x, lbd)))
    print("Poisson Erwartungswert = Lambda:", lbd)
    print("Poisson Varianz = Lambda:", lbd)

    loop = 1
    while loop == 1:
        print("Mit anderem x erneut rechnen?\nJ: ja\nN: nein")
        yes_no = input()
        if yes_no == "j" or yes_no == "J":
            print("x eingeben:")
            x = int(input())
            print("poissonverteilt P(X = {}) = {} (marcpy.poissonverteilt(x, lambda))".format(x, mp.poissonverteilt(x,
                                                                                                                    lbd)))
            print("poissonverteilt P(X <= {}) = {} (marcpy.poissonverteiltF(x, lambda))".format(x,
                                                                                                mp.poissonverteiltF(x,
                                                                                                                    lbd)))
        else:
            return


def gleichverteilt():
    print("a eingeben:")
    a = float(input())
    print("b eingeben:")
    b = float(input())
    print("x eingeben:")
    x = float(input())

    print("gleichverteilt (a = {}, b = {}, x = {}) = {} (marcpy.gleichverteilt({}, {}, {}))".format(a, b, x,
                                                                                                    mp.gleichverteilt(a,
                                                                                                                      b,
                                                                                                                      x),
                                                                                                    a, b, x))
    print("E[X] = {} (marcpy.gleicherwartung({}, {}))".format(mp.gleicherwartung(a, b), a, b))
    print("Var[X] = {} (marcpy.gleichvar({}, {}))".format(mp.gleichvar(a, b), a, b))


def exponentialverteilt():
    print("Lambda eingeben:")
    inp = input()

    if "/" in inp:
        index = inp.find("/")
        lbd = float(inp[0: index]) / float(inp[index + 1: len(inp)])
    else:
        lbd = float(inp)

    print("x eingeben:")
    inp = input()

    if "/" in inp:
        index = inp.find("/")
        x = float(inp[0: index]) / float(inp[index + 1: len(inp)])
    else:
        x = float(inp)

    print("X:", x)
    print("Exponentialverteilt f({}) = {} (marcpy.expverteilt({}, {}))".format(x, mp.expverteilt(lbd, x), lbd, x))
    print("P(X <= {}) = {} (marcpy.expverteiltF({}, {}))".format(x, mp.expverteiltF(lbd, x), lbd, x))
    print("E[X] = {} (marcpy.experwartung({}))".format(mp.experwartung(lbd), lbd))
    print("Var[X] = {} (marcpy.expvar({}))".format(mp.expvar(lbd), lbd))


def normalverteilt():
    print("u (Erwartungswert) eingeben:")
    u = float(input())
    print("o (Standardabweichung) eingeben:")
    o = float(input())
    print("x eingeben:")
    x = float(input())

    print("Normalverteilung f({}) = {} (marcpy.normalverteilt({}, {}, {}))".format(x, mp.normalverteilt(x, u, o), x, u,
                                                                                   o))
    print("P(X <= {}) = {} (marcpy.normalverteiltF({}, {}, {}))".format(x, mp.normalverteiltF(x, u, o), x, u, o))
    print("E[X] = {} (marcpy.normalerwartung({}))".format(mp.normalerwartung(u), u))
    print("Var[X] = {} (marcpy.normalvar({}))".format(mp.normalvar(0), o))

    loop = 1
    while loop == 1:
        print("Weiteres x berechnen?\nj: ja\nn: nein")
        yes_no = input()
        if yes_no == 'J' or yes_no == 'j':
            print("x eingeben:")
            x = float(input())
            print(
                "P(X <= {}) = {} (marcpy.normalverteiltF({}, {}, {}))".format(x, mp.normalverteiltF(x, u, o), x, u, o))
        else:
            break


def nueberk():
    print("n ueber k")
    print("n eingeben:")
    n = int(input())
    print("k eingeben:")
    k = int(input())

    print("{} ueber {} = {} (marcpy.nueberk({}, {}))".format(n, k, mp.nueberk(n, k), n, k))


def zaehlverfahren():
    print("n eingeben:")
    n = int(input())
    print("k eingeben:")
    k = int(input())

    print("Werden alle Elemente angeordnet?\nj: ja\nn: nein")
    yes_no = input()
    if yes_no == 'N' or yes_no == 'n':
        print("Ist die Reihenfolge wichtig?\nj: ja\nn: nein")
        yes_no = input()
        if yes_no == 'J' or yes_no == 'j':
            print("Mit Wiederholung?\nj: ja\nn: nein")
            yes_no = input()
            if yes_no == 'J' or yes_no == 'j':
                print("Ergebnis: {}".format(n ** k))
            else:
                print("Ergebnis: {}".format(mp.fak(n) / mp.fak(n - k)))
        else:
            print("Mit Wiederhgolung?\nj: ja\nn: nein")
            yes_no = input()
            if yes_no == 'J' or yes_no == 'j':
                print("Ergebnis: {}".format(mp.nueberk(n, k)))
            else:
                print("Ergebnis: {}".format(mp.nueberk(n + k - 1, k)))
    else:
        print("Ergebnis: {}".format(mp.fak(n)))


print('Funktion auswählen:\n1: Mittelwert/Median/Modalwert'
      '/Interquartilabstand/Spannweite/empirische Standardabweichung'
      '/Varianz\n2: Quantile\n3: Korrelationskoeffizient\n4: Fakultät'
      '\n5: lineare Reggressionsfunktion\n6: Häufigkeiten (absolut, relativ, kumuliert)'
      '\n7: Verteilung\n8: Zählverfahren\n9: n über k')

# Arrays werden in den Funktionen zu Numpy Arrays konvertiert,
# können also als normale Listen übergeben werden!
func_code = int(input())

if func_code == 1:
    einzelwerte()
elif func_code == 2:
    percentile(0)
elif func_code == 3:
    corrcoef(0)
elif func_code == 4:
    fak()
elif func_code == 5:
    plotlinregress()
elif func_code == 6:
    haeufigkeit()
elif func_code == 7:
    verteilung()
elif func_code == 8:
    zaehlverfahren()
elif func_code == 9:
    nueberk()
else:
    print("Funktion nicht verfügbar")
