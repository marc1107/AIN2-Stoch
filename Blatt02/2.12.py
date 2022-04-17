import hashlib
import sys
import time

chars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
         "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O",
         "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7",
         "8", "9"]
pw_hash = "39228d06a988045c5caaa97bf0a6158893d51862"
#pw_hash = "df51e37c269aa94d38f93e537bf6e2020b21406c"  #Test-Hash von aaaaa

# ausrechnen, wie viele Möglichkeiten es gibt
# gleiche for Schleifen wie unten, die unteren werden aber abgebrochen
# bei richtigem Passwort
counter = 0
for first in chars:
    for second in chars:
        for third in chars:
            for fourth in chars:
                for fifth in chars:
                    counter += 1

print("Anzahl Möglichkeiten:", counter)

# Zeit starten zur Messung wie lange das Knacken benötigt
start_time = time.time()

# Eine Schleife pro Zeichen in Passwort
for first in chars:
    for second in chars:
        for third in chars:
            for fourth in chars:
                for fifth in chars:
                    # Passwort aus den 5 Zeichen zusammensetzen
                    password = first + second + third + fourth + fifth
                    # Hash bilden
                    sha1 = hashlib.sha1(password.encode("utf-8"))
                    #print(password)

                    if sha1.hexdigest() == pw_hash:
                        # Wenn Passwort richtig, Passwort ausgeben
                        exit_string = "Passwort: " + password
                        print("--- %s seconds ---" % (time.time() - start_time))
                        sys.exit(exit_string)
