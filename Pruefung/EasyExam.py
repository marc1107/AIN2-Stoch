import marcpy as mp


def mean():
    print("Array für Mittelwert eingeben: ")
    arr = input()
    arr = list(map(int, arr.split(' ')))
    print("Mittelwert: ", mp.mean(arr))


def median():
    print("Array für Median eingeben: ")
    arr = input()
    arr = list(map(int, arr.split(' ')))
    print("Median: ", mp.median(arr))


def mode():
    print("Array für Modalwert eingeben: ")
    arr = input()
    arr = list(map(int, arr.split(' ')))
    print("Modalwert(e): ", mp.mode(arr))


def percentile():
    print("Array für Quantile/Percentile eingeben: ")
    arr = input()
    arr = list(map(int, arr.split(' ')))
    print("Prozentzahl eingeben: ")
    pct = int(input())
    print(pct, " Percentile: ", mp.percentile(arr, pct))


def interquartilediff():
    print("Array für Interquartilabstand eingeben: ")
    arr = input()
    arr = list(map(int, arr.split(' ')))
    print("Interquartilabstand: ", mp.interquartilediff(arr))


def span():
    print("Array für Spannweite eingeben: ")
    arr = input()
    arr = list(map(int, arr.split(' ')))
    print("Spannweite: ", mp.span(arr))


def std():
    print("Array für Standardabweichung eingeben: ")
    arr = input()
    arr = list(map(int, arr.split(' ')))
    print("Standardabweichung: ", mp.std(arr))


def var():
    print("Array für Varianz eingeben:")
    arr = input()
    arr = list(map(int, arr.split(' ')))
    print("Varianz: ", mp.var(arr))


def corrcoef():
    print("Array 1 für Korrelationskoeffizienten eingeben:")
    arr1 = input()
    arr1 = list(map(int, arr1.split(' ')))
    print("Array 2 für Korrelationskoeffizienten eingeben:")
    arr2 = input()
    arr2 = list(map(int, arr2.split(' ')))
    print("Korrelationskoeffizient: ", mp.corrcoef(arr1, arr2))


def fak():
    print("Zahl für Fakultät eingeben:")
    n = int(input())
    print("Fakultät: ", mp.fak(n))


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
    print("Absolute Häufigkeiten:", mp.abs_haeufigkeit(arr))


def rel_haeufigkeit(arr):
    print("Relative Häufigkeiten:", mp.rel_haeufigkeit(arr))


def kum_haeufigkeit(arr):
    print("Kumulierte Häufigkeiten:", mp.kum_haeufigkeit(arr))


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
    print("Was soll berechnet werden?\n1: Binomialkoeffizient\n2: binomial verteilt"
          "\n3: ...")
    func = int(input())

    if func == 1:
        bincoef()
    elif func == 2:
        binomialverteilt()
    else:
        print("Wrong function")
        return


def bincoef():
    print("n für (n über k) eingeben:")
    n = int(input())
    print("k für (n über k) eingeben:")
    k = int(input())
    bincoef = mp.bincoef(n, k)
    print("Binomialkoeffizient für n = {} und k = {}: {}".format(n, k, bincoef))


def binomialverteilt():
    print("Formel: (n über t) * p^t * q^(n-t)")
    print("Es werden alle t's berechnet!")
    print("n eingeben:")
    n = int(input())
    print("p eingeben (Kommazahl mit Punkt getrennt!):")
    p = float(input())
    print("q eingeben (Kommazahl mit Punkt getrennt!):")
    q = float(input())
    print("Binomial verteilt P(X = t):")
    arr = mp.binomialverteilt(n, p, q)
    for pack in arr:
        print("t: P(X = {}) = {}".format(pack[0], pack[1]))

    loop = 1
    while loop == 1:
        print("\nSoll noch etwas mit diesen Werten berechnet werden?"
              "\n1: P(mindestens x)\n2: P(höchstens x)"
              "\n3: P(mindestens x und höchstens y)\n4: nein")
        func = int(input())
        if func == 1:
            print("x eingeben:")
            x = int(input())
            print("P(mindestens {}) = {}".format(x, mp.binmindestens(arr, x)))
        elif func == 2:
            print("x eingeben:")
            x = int(input())
            print("P(höchstens {}) = {}".format(x, mp.binhoechstens(arr, x)))
        elif func == 3:
            print("x (mindestens) eingeben:")
            x = int(input())
            print("y (höchstens) eingeben:")
            y = int(input())
            print("P(höchstens {}) = {}".format(x, mp.binminhoe(arr, x, y)))
        else:
            return



print('Funktion auswählen:\n1: Mittelwert\n2: Median\n3: Modalwert'
      '\n4: Quantile/Percentile\n5: Interquartilabstand'
      '\n6: Spannweite\n7: empirische Standardabweichung'
      '\n8: Varianz\n9: Korrelationskoeffizient\n10: Fakultät'
      '\n11: lineare Reggressionsfunktion\n12: Häufigkeiten (absolut, relativ, kumuliert)'
      '\n13: Verteilung')

# Arrays werden in den Funktionen zu Numpy Arrays konvertiert,
# können also als normale Listen übergeben werden!
func_code = int(input())

if func_code == 1:
    mean()
elif func_code == 2:
    median()
elif func_code == 3:
    mode()
elif func_code == 4:
    percentile()
elif func_code == 5:
    interquartilediff()
elif func_code == 6:
    span()
elif func_code == 7:
    std()
elif func_code == 8:
    var()
elif func_code == 9:
    corrcoef()
elif func_code == 10:
    fak()
elif func_code == 11:
    plotlinregress()
elif func_code == 12:
    haeufigkeit()
elif func_code == 13:
    verteilung()
else:
    print("Funktion nicht verfügbar")
