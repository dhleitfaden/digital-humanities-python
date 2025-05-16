# main.py
import string
from collections import Counter
import nltk
from nltk.corpus import stopwords
import matplotlib.pyplot as plt

# Sicherstellen, dass die erforderlichen NLTK-Daten geladen werden
nltk.download('stopwords')

# Bereinigung des Textes (alles in Kleinbuchstaben, Entfernen von Satzzeichen und Stoppwörtern)
def bereinige_text(text):
    # Kleinbuchstaben
    text = text.lower()
    # Satzzeichen entfernen
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Wörter trennen
    woerter = text.split()
    # Stoppwörter für die deutsche Sprache
    deutsch_stoppwoerter = set(stopwords.words('german'))
    # Stoppwörter entfernen
    gefiltert = [wort for wort in woerter if wort not in deutsch_stoppwoerter]
    return gefiltert

# Beispieltext aus einer Datei lesen
def lade_text(dateipfad):
    with open(dateipfad, 'r', encoding='utf-8') as file:
        return file.read()

# Häufigkeit der Wörter im Text zählen
def zaehle_woerter(woerter):
    return Counter(woerter)

# Balkendiagramm der häufigsten Wörter anzeigen
def zeige_balkendiagramm(counter):
    haeufigste = counter.most_common(10)
    woerter, werte = zip(*haeufigste)
    plt.bar(woerter, werte, color='skyblue')
    plt.xticks(rotation=45)
    plt.title("Die 10 häufigsten Wörter")
    plt.xlabel("Wort")
    plt.ylabel("Anzahl")
    plt.tight_layout()
    plt.show()

# Hauptfunktion
def main():
    text = lade_text('data/text.txt')
    woerter = bereinige_text(text)
    haeufigkeit = zaehle_woerter(woerter)
    print("Die 10 häufigsten Wörter:")
    for wort, anzahl in haeufigkeit.most_common(10):
        print(f"{wort}: {anzahl}")
    zeige_balkendiagramm(haeufigkeit)

if __name__ == "__main__":
    main()
