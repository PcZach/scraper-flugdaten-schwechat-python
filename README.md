Scraped alle Ankünfte von Flügen an Flughafen Schwechat und speichert die Flugdaten ab.
Damit wir die Flüge korrekt in die Datenbank speichern können, verwenden wir für die richtige Datenstruktur pydantic.

Die Felder für die Datenbank heißen:

flight_number (string, 12 char max)
arrival_datetime_planned (datetime object)
arrival_datetime_actual (datetime object)
canceled (Boolean, default False)
airline_iata (str, max 4 char) IATA Code
arrival_airport_iata (str, max 12 char)
departure_airport_iata (str, max 12 char)
departure_datetime_planned (datetime object)
departure_datetime_actual (datetime object)
Wir speichern diese Daten in eine csv Datei und fügen jeden neuen Flug einfach hinzu.

Ablauf:

Hole dir alle Flüge
Loop über die Flüge
2.1. Check jeden Flug ob er "landed" ist
2.2 Falls nein, nächster Flug, nix machen
2.3. Falls ja, check ob Flug bereits eingetragen ist in csv liste (flugnummer und arrival_datetime_planned zusammen ist unique
2.4. falls flug bereits eingetragen, nächster flug
2.5.. falls nicht, flug eintragen
Das sollte sich eigentlich morgen locker ausgehen.
