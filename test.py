# 'import' werden üblicherweise alle an den Anfang des Scripts
# gesetzt
import random


name = input("Name eingeben: ")
#anzahl = input("Anzahl zu generierender Anagramme: ")
anzahl = int(input("Anzahl zu generierender Anagramme: "))

# Um später besser den Überblick zu behalten, versuchen wir, den
# Variablen einen sinnvollen Namen zu geben

name_ohne_abstand = name.replace(" ", "")
name_als_liste = list(name_ohne_abstand)
for _ in range(anzahl):
    #print("Durchlauf: ", index)
    # random.shuffle verändert die übergebene Liste an Ort.
    # Das heisst, wir müssen kein Resultat entgegen nehmen.
    # Man sagt auch, die Liste wird 'inplace' verändert
    random.shuffle(name_als_liste)
    # Die Funktion 'join' des Typs 'string' verändert die
    # übergebene Liste 'name_als_liste' nicht, sondern gibt
    # einen neuen Wert zurück, den wir in einer Variablen
    # speichern müssen.
    anagram = "".join(name_als_liste)

    #split_punkt = name.index(" ")
    # Jetzt fügen wir den Abstand zwischen zwei Worten wieder
    # ein. Dazu suchen wir einen zufälligen Ort innerhalb der
    # Zeichenkette, so dass mindestens ein Zeichen am Anfang
    # und ein Zeichen am Ende übrig bleibt.
    split_punkt = random.randrange(1, len(anagram)-1)
    # Die Worte 'wort1' und 'wort2' holen wir aus dem Anagram,
    # indem wir 'anagram' entsprechend slicen.
    wort1 = anagram[:split_punkt]
    wort2 = anagram[split_punkt:]
    # Jetzt fügen wir die beiden Wort zusammen und fügen noch
    # ein Leerzeichen dazwischen
    anagram = wort1 + " " + wort2
    # Zum Schluss stellen wir noch sicher, dass immer die Anfangs-
    # buchstaben gross und die restlichen Buchstaben klein sind.
    anagram = anagram.title()
    print(anagram)