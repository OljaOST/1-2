"""
Das Ziel dieses Skripts ist es, einen Weihnachtsbaum zu zeichnen.

Wir stellen uns deshalb vor, dass wir eine Funktion schreiben wollen, welche
weihnachtsbaum_zeichnen() heisst und die Parameter "Baumkronenhöhe" sowie
"Stammhöhe" entgegen nimmt. Wenn wir also zum Beispiel
weihnachtsbaum_zeichnen(4, 2) aufrufen würden, erwarten wir folgende Ausgabe:

    *
   ***
  *****
 *******
    #
    #
"""


def schicht_zeichnen(schicht_nummer, baum_breite):
    """
    Zeichne eine einzelne Schicht der Baumkrone.
    Um die Schicht korrekt anzuordnen, übernimmt die Funktion auch die
    Baumbreite.
    """
    # Die Baumschicht muss eine bestimmte Menge an Zeichen eingerückt werden.
    # Um die exakte Grösse an Einrückung zu berechnen, müssen wir die
    # entsprechende Formel herausfinden.
    # Ein einfacher Weg zum Bestimmen der Formel besteht darin, sich die
    # möglichen Werte einfach mal aufzuschreiben.
    #
    # Wir gehen mal von der Baumhöhe 4 aus, wie sie im Beispiel oben
    # verwendet wird. Dann schreiben wir uns für die vier Schichten auf,
    # wieviele Abstände/Leerzeichen wir jeweils noch einsetzen müssten:
    #
    #   Schicht nummer 1 --> 3 Abstände
    #   Schicht nummer 2 --> 2 Abstände
    #   Schicht nummer 3 --> 1 Abstand
    #   Schicht nummer 4 --> 0 Abstände
    #
    # Mit grösser werdenden Schichten nehmen die Abstände linear ab, es
    # scheint sich also um irgendeine Form von Differenz zu handeln.
    # Sehr wahrscheinlich hängt die tatsächliche Formel auch noch
    # von der maximalen Baumbreite ab.
    #
    # Wenn wir also mal nur die Schicht Nummer 1 für verschiedene Baum-
    # höhen bzw. Baumbreiten anschauen, sieht dies so aus:
    #
    #   Baumhöhe 3, maximale Breite 5 --> 2 Abstände
    #   Baumhöhe 4, maximale Breite 7 --> 3 Abstände
    #   Baumhöhe 5, maximale Breite 9 --> 4 Abstände
    #
    # Wir leiten also einfach mal die folgende Formel für die Berechnung
    # der Anzahl Abstände her. Wir wir aus den Experimenten mit
    # verschiedenen Schichtzahlen und Baumöhen herausfinden, passt
    # diese Formel perfekt. In der Realität würden wir die Formel aber
    # nochmal durch Testen von Randwerten überprüfen.
    anzahl_abstände = (baum_breite//2) - schicht_nummer + 1
    abstände = anzahl_abstände * " "

    # Auch für die Anzahl der Sterne pro Schicht müssen wir uns noch
    # eine passende Formel überlegen. Diese scheint bei genauer
    # Betrachtung glücklicherweise nur von der Schichtnummer ab-
    # zuhängen. Nch einigem Überlegen erhalten wir folgende Formel:
    sterne = (2*schicht_nummer - 1) * "*"
    print(f"{abstände}{sterne}")


def weihnachtsbaum_zeichnen(kronen_höhe, stammhöhe):
    """
    Zeichne einen vollständigen "Weihnachtsbaum".

    Die oberste Schicht besteht nur aus einem einzelnen Zeichen.
    Jede weitere Schicht enthält 2 weitere Zeichen.
    """
    maximale_baum_breite = 2*kronen_höhe - 1
    for schicht in range(kronen_höhe):
        # In dieser for-Schleife wird die Variable 'schicht'
        # hochgezählt von 0 beginnend bis kronen_höhe-1. In
        # der Funktion schicht_zeichnen() gehen wir davon aus,
        # dass die Schichten von 1-beginnend nummeriert sind.
        # Wir müssen also 'schicht' noch um 1 erhöhen.
        schicht_zeichnen(schicht+1, maximale_baum_breite)

    for schicht in range(stammhöhe):
        print(f" {((maximale_baum_breite//2)-1)*' '}#")


# Zum Schluss noch ein kleines Experiment, ob unsere Funktion
# tatsächlich das gewünschte Resultat liefert
weihnachtsbaum_zeichnen(10, 2)