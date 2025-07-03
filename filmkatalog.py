# Dein Filmkatalog-Programm

filme = {} # Ein Dictionary zum Speichern der Filme. Schlüssel: Filmtitel, Wert: Dictionary mit Details

def filme_anzeigen():
    # Überprüfe, ob das 'filme'-Dictionary leer ist
    if not filme:
        print("Der Katalog ist leer.")
        return # Beende die Funktion hier, wenn keine Filme vorhanden sind

    print("\n--- Dein Filmkatalog ---")
    # Iteriere über alle Filme im Dictionary
    for titel, details in filme.items():
        print(f"Titel: {titel}")
        # Verwende .get(), um 'N/A' anzuzeigen, falls ein Detail fehlt
        print(f"  Regisseur: {details.get('regisseur', 'N/A')}")
        print(f"  Jahr: {details.get('jahr', 'N/A')}")
        print("-----------------------")

# Test der Funktion (diese Zeile wird später durch ein Menü ersetzt)
# filme_anzeigen()

def film_hinzufuegen():
    print("\n--- Film hinzufügen ---")
    titel = input("Titel des Films: ")
    regisseur = input("Regisseur des Films: ")
    jahr = input("Erscheinungsjahr des Films: ")

    # Überprüfe, ob der Film bereits existiert
    if titel in filme:
        print(f"Fehler: Film '{titel}' existiert bereits im Katalog.")
        return # Beende die Funktion, wenn der Film schon da ist

    # Füge den neuen Film zum 'filme'-Dictionary hinzu
    filme[titel] = {
        "regisseur": regisseur,
        "jahr": jahr
    }
    print(f"Film '{titel}' wurde hinzugefügt.")

# Test der Funktion (wird später durch ein Menü ersetzt)
# film_hinzufuegen()
# filme_anzeigen()

def zeige_menue():
    print("\n--- Filmkatalog Menü ---")
    print("1. Film hinzufügen")
    print("2. Filme anzeigen")
    print("3. Beenden")
    print("------------------------")

def main():
    while True: # Eine Endlosschleife für das Menü
        zeige_menue() # Zeige das Menü an
        wahl = input("Ihre Wahl: ") # Erfasse die Benutzereingabe

        if wahl == '1':
            film_hinzufuegen()
        elif wahl == '2':
            filme_anzeigen()
        elif wahl == '3':
            print("Programm wird beendet. Auf Wiedersehen!")
            break # Beende die Schleife und damit das Programm
        else:
            print("Ungültige Eingabe. Bitte versuchen Sie es erneut.")

# Startet das Hauptprogramm, wenn die Datei direkt ausgeführt wird
if __name__ == "__main__":
    main()