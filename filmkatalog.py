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