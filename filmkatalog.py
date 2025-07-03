# Dein Filmkatalog-Programm
import json

filme = {} # Ein Dictionary zum Speichern der Filme. Schlüssel: Filmtitel, Wert: Dictionary mit Details
DATEINAME = "filme.json" # Dateiname für die Speicherung des Katalogs

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

def film_suchen():
    print("\n--- Film suchen ---")
    suchbegriff = input("Geben Sie einen Suchbegriff für den Titel ein: ").lower()
    gefundene_filme = {} # Dictionary, um die gefundenen Filme zu speichern

    # Iteriere durch alle Filme im Katalog
    for titel, details in filme.items():
        # Überprüfe, ob der Suchbegriff im Titel (kleingeschrieben) enthalten ist
        if suchbegriff in titel.lower():
            gefundene_filme[titel] = details # Füge den gefundenen Film hinzu

    # Wenn keine Filme gefunden wurden
    if not gefundene_filme:
        print(f"Keine Filme gefunden, die '{suchbegriff}' im Titel enthalten.")
        return

    print(f"\n--- Gefundene Filme für '{suchbegriff}' ---")
    # Zeige die Details der gefundenen Filme an (ähnlich wie filme_anzeigen)
    for titel, details in gefundene_filme.items():
        print(f"Titel: {titel}")
        print(f"  Regisseur: {details.get('regisseur', 'N/A')}")
        print(f"  Jahr: {details.get('jahr', 'N/A')}")
        print("-----------------------")

def film_loeschen():
    print("\n--- Film löschen ---")
    titel_zu_loeschen = input("Titel des zu löschenden Films: ")
    # Überprüfe, ob der Film im Katalog existiert
    if titel_zu_loeschen in filme:
        del filme[titel_zu_loeschen] # Entferne den Film aus dem Dictionary
        print(f"Film '{titel_zu_loeschen}' wurde aus dem Katalog entfernt.")
    else:
        print(f"Fehler: Film '{titel_zu_loeschen}' nicht im Katalog gefunden.")

def katalog_speichern():
    try:
        # Öffne die Datei im Schreibmodus ('w') mit UTF-8-Kodierung
        with open(DATEINAME, 'w', encoding='utf-8') as f:
            # Speichere das 'filme'-Dictionary als JSON in der Datei
            # indent=4 für schöne Formatierung, ensure_ascii=False für Umlaute
            json.dump(filme, f, indent=4, ensure_ascii=False)
        print(f"Katalog erfolgreich in '{DATEINAME}' gespeichert.")
    except IOError as e:
        print(f"Fehler beim Speichern des Katalogs: {e}")

def katalog_laden():
    global filme # Erlaube den Zugriff auf die globale 'filme'-Variable
    try:
        # Versuche, die Datei im Lesemodus ('r') zu öffnen
        with open(DATEINAME, 'r', encoding='utf-8') as f:
            filme = json.load(f) # Lade die JSON-Daten in das 'filme'-Dictionary
        print(f"Katalog erfolgreich aus '{DATEINAME}' geladen.")
    except FileNotFoundError:
        # Wenn die Datei nicht existiert, ist das normal beim ersten Start
        print("Keine vorhandene Katalogdatei gefunden. Starte mit leerem Katalog.")
        filme = {} # Stelle sicher, dass 'filme' initialisiert ist
    except json.JSONDecodeError as e:
        # Wenn die Datei existiert, aber kein gültiges JSON enthält
        print(f"Fehler beim Laden des Katalogs (ungültiges JSON): {e}. Starte mit leerem Katalog.")
        filme = {}
    except Exception as e:
        # Fange alle anderen unerwarteten Fehler ab
        print(f"Ein unerwarteter Fehler beim Laden ist aufgetreten: {e}. Starte mit leerem Katalog.")
        filme = {}


def zeige_menue():
    print("\n--- Filmkatalog Menü ---")
    print("1. Film hinzufügen")
    print("2. Filme anzeigen")
    print("3. Film suchen")
    print("4. Film löschen") # NEU
    print("5. Beenden")     # NUMMER GEÄNDERT
    print("------------------------")

def main():
    katalog_laden() # Hier am Anfang aufrufen, um den Katalog zu laden
    while True:
        zeige_menue()
        wahl = input("Ihre Wahl: ")

        if wahl == '1':
            film_hinzufuegen()
        elif wahl == '2':
            filme_anzeigen()
        elif wahl == '3':
            film_suchen()
        elif wahl == '4':
            film_loeschen()
        elif wahl == '5':
            katalog_speichern() # Hier vor dem Beenden aufrufen
            print("Programm wird beendet. Auf Wiedersehen!")
            break
        else:
            print("Ungültige Eingabe. Bitte versuchen Sie es erneut.")

# Startet das Hauptprogramm, wenn die Datei direkt ausgeführt wird
if __name__ == "__main__":
    main()