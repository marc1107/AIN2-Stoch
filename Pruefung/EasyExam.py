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


print('Funktion auswählen:\n1: Mittelwert\n2: Median\n3: Modalwert'
      '\n4: Quantile/Percentile\n5: Interquartilabstand'
      '\n6: Spannweite\n7: empirische Standardabweichung'
      '\n8: Varianz\n9: Korrelationskoeffizient\n10: Fakultät'
      '\n11: lineare Reggressionsfunktion\n12:')

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
else:
    print("Funktion nicht verfügbar")
