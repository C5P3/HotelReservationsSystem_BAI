# HotelReservationsSystem_BAI

# Beteiligte am Projekt

- Elia Geromin
- Felipe Wüthrich


# Aufteilung der Aufgaben und Zeitplan

https://github.com/users/C5P3/projects/1/views/1


# Wichtiger Hinweis

Wir (Elia und Felipe) haben uns am 21.05.2025 dazu entschieden, unsere bisherige Gruppe zu verlassen. Grund dafür war, dass wir mit der Komplexität und der Vorgehensweise des ursprünglichen Projekts überfordert waren. Dadurch fiel es uns schwer, inhaltlich und fachlich mit dem Rest der Gruppe mitzuhalten und eigene Ideen einzubringen.

Nach intensiven Gesprächen und auf Anraten von Phillip Gachnang haben wir uns entschieden, ein eigenes Projekt in unserem Tempo umzusetzen – mit dem Ziel, den grösstmöglichen Lerneffekt für uns zu erzielen.


# Projektstruktur

Das Projekt ist ein Hotelreservierungssystem, das die Verwaltung von Hotels, Zimmern, Buchungen, Gästen und Rechnungen ermöglicht. Es ist modular aufgebaut und folgt dem MVC-Architekturprinzip (Model-View-Controller). Die Hauptbestandteile des Projekts sind:
1.	Model: Definiert die Datenstrukturen und -modelle.
2.	Business Logic: Enthält die Geschäftslogik, die die Interaktion zwischen den Datenmodellen und der Datenzugriffsschicht steuert.
3.	Data Access: Stellt die Verbindung zur Datenbank her und führt CRUD-Operationen aus.
4.	Database: Enthält SQL-Skripte zur Definition und Initialisierung der Datenbank.
Das Projekt ist in Python geschrieben und verwendet SQLite als Datenbank. Es ist so konzipiert, dass es leicht erweiterbar ist, z.B. durch Hinzufügen neuer Funktionen oder die Integration mit anderen Datenbanken.



# Hauptverzeichnis

**source**

Das Verzeichnis source enthält den gesamten Quellcode des Projekts, einschliesslich der Geschäftslogik, Datenzugriffsschicht, Datenmodelle und Testskripte.


**hotelreservation.ipynb (Jupyter Notebook)**

Allgemeine Informationen:
-	Bei den Zellen wird der Output unterhalb des Blocks. Sollten Sie einen Input machen müssen, wird dieser oben angezeigt mit einer Beschreibung, was eingefügt werden muss.
-	Sollten Sie sich bei einer Zelle anmelden müssen, ist der Benutzername wie auch das Passwort im Code angegeben. 
Starten des Notebook:
-	Notebook öffnen
-	Datei hotelreservation.ipynb suchen und öffnen
-	Jupyter Notebook mit dem Dreieck starten
Verwendung das Notebook
Das Notebook enthält Codezellen, die verschiedene Funktionen des Hotelreservierungssystems demonstrieren.
Um eine Zelle auszuführen:
-	Eine Zelle auswählen.
-	Mit  Shift + Enter oder dem Dreieck die Zelle starten und testen.



# businessLogic
Das Verzeichnis businessLogic enthält die Geschäftslogik des Systems. Es steuert die Interaktion zwischen den Datenmodellen und der Datenzugriffsschicht.

**addressManager.py**

Beschreibung:
-	Enthält die Logik zur Verwaltung von Adressen.
Funktionen:
-	add_address(address): Fügt eine neue Adresse hinzu.
-	update_address(address_id, new_data): Aktualisiert eine bestehende Adresse.
-	delete_address(address_id): Löscht eine Adresse.
Verwendet die Klasse AddressAccess aus der Datenzugriffsschicht.

**bookingManager.py**

Beschreibung:
-	Enthält die Logik zur Verwaltung von Buchungen.
Funktionen:
-	create_booking(guest_id, room_id, check_in, check_out): Erstellt eine neue Buchung.
-	cancel_booking(booking_id): Storniert eine Buchung.
-	get_booking_details(booking_id): Ruft Details zu einer Buchung ab.
Verwendet die Klasse BookingAccess aus der Datenzugriffsschicht.

**facilityManager.py**

Beschreibung:
-	Enthält die Logik zur Verwaltung von Einrichtungen (z. B. WiFi, TV).
Funktionen:
-	add_facility(facility): Fügt eine neue Einrichtung hinzu.
-	update_facility(facility_id, new_data): Aktualisiert eine Einrichtung.
-	delete_facility(facility_id): Löscht eine Einrichtung.

**guestManager.py**

Beschreibung:
-	Enthält die Logik zur Verwaltung von Gästen.
Funktionen:
-	search_guest(name): Sucht Gäste basierend auf ihrem Namen.
-	add_guest(guest): Fügt einen neuen Gast hinzu.

**hotelManager.py**

Beschreibung:
-	Enthält die Logik zur Verwaltung von Hotels.
Funktionen:
-	Google Hotels(city, stars): Sucht Hotels basierend auf Stadt und Sternebewertung.
-	add_hotel(hotel): Fügt ein neues Hotel hinzu.
-	update_hotel(hotel_id, new_data): Aktualisiert ein Hotel.
-	delete_hotel(hotel_id): Löscht ein Hotel.

**invoiceManager.py**

Beschreibung:
-	Enthält die Logik zur Verwaltung von Rechnungen.
Funktionen:
-	generate_invoice(booking_id): Erstellt eine Rechnung für eine Buchung.

**roomManager.py**

Beschreibung:
-	Enthält die Logik zur Verwaltung von Zimmern.
Funktionen:
-	add_room(room): Fügt ein neues Zimmer hinzu.
-	update_room(room_id, new_data): Aktualisiert ein Zimmer.
-	delete_room(room_id): Löscht ein Zimmer.
-	search_available_rooms(check_in, check_out): Sucht verfügbare Zimmer für einen bestimmten Zeitraum.

**roomTypeManager.py**

Beschreibung:
-	Enthält die Logik zur Verwaltung von Zimmertypen.
Funktionen:
-	add_room_type(room_type): Fügt einen neuen Zimmertyp hinzu.
-	update_room_type(room_type_id, new_data): Aktualisiert einen Zimmertyp.
-	delete_room_type(room_type_id): Löscht einen Zimmertyp.

**userManager.py**

Enthält die Logik zur Verwaltung von Benutzern.

Funktionen:
-	is_admin(user_id): Überprüft, ob ein Benutzer ein Administrator ist.



# dataAccess
Das Verzeichnis dataAccess enthält die Datenzugriffsschicht des Systems. Es stellt die Verbindung zur SQLite-Datenbank her und führt CRUD-Operationen aus.

**addressAccess.py**

Diese Datei enthält die Datenzugriffsfunktionen für Adressen. Sie ermöglicht CRUD-Operationen (Create, Read, Update, Delete) auf der Tabelle Address in der Datenbank.

Funktionen:
-	get_all_addresses(): Ruft alle Adressen aus der Datenbank ab.
-	get_address_by_id(address_id): Ruft eine Adresse basierend auf ihrer ID ab.
-	add_address(address): Fügt eine neue Adresse in die Datenbank ein.
-	update_address(address_id, new_data): Aktualisiert eine bestehende Adresse.
-	delete_address(address_id): Löscht eine Adresse aus der Datenbank.
Verwendung: Wird von der Klasse AddressManager in der Geschäftslogik verwendet, um Adressdaten zu verwalten.

**baseDataAccess.py**

Beschreibung:
-	Basisklasse für den Datenzugriff.
Funktionen:
-	execute_query(query, params): Führt eine SQL-Abfrage aus.
-	fetch_all(query, params): Ruft alle Ergebnisse einer Abfrage ab.
-	fetch_one(query, params): Ruft ein einzelnes Ergebnis ab.

**bookingAccess.py**

Diese Datei enthält die Datenzugriffsfunktionen für Buchungen. Sie ermöglicht die Verwaltung von Buchungsdaten in der Tabelle Booking.

Funktionen:
-	get_all_bookings(): Ruft alle Buchungen aus der Datenbank ab.
-	get_booking_by_id(booking_id): Ruft eine Buchung basierend auf ihrer ID ab.
-	add_booking(booking): Fügt eine neue Buchung in die Datenbank ein.
-	update_booking(booking_id, new_data): Aktualisiert eine bestehende Buchung.
-	delete_booking(booking_id): Löscht eine Buchung aus der Datenbank.
-	check_booking_conflicts(room_id, check_in, check_out): Überprüft, ob es Buchungskonflikte für ein bestimmtes Zimmer gibt.
Verwendung:
-	Wird von der Klasse BookingManager in der Geschäftslogik verwendet, um Buchungsdaten zu verwalten.

**facilityAccess.py**

Diese Datei enthält die Datenzugriffsfunktionen für Einrichtungen (Facilities). Sie ermöglicht die Verwaltung von Daten in der Tabelle Facility.

Funktionen:
-	get_all_facilities(): Ruft alle Einrichtungen aus der Datenbank ab.
-	get_facility_by_id(facility_id): Ruft eine Einrichtung basierend auf ihrer ID ab.
-	add_facility(facility): Fügt eine neue Einrichtung in die Datenbank ein.
-	update_facility(facility_id, new_data): Aktualisiert eine bestehende Einrichtung.
-	delete_facility(facility_id): Löscht eine Einrichtung aus der Datenbank.
Verwendung:
-	Wird von der Klasse FacilityManager in der Geschäftslogik verwendet, um Einrichtungsdaten zu verwalten.

**guestAccess.py**

Diese Datei enthält die Datenzugriffsfunktionen für Gäste. Sie ermöglicht die Verwaltung von Daten in der Tabelle Guest.

Funktionen:
-	get_all_guests(): Ruft alle Gäste aus der Datenbank ab.
-	get_guest_by_id(guest_id): Ruft einen Gast basierend auf seiner ID ab.
-	add_guest(guest): Fügt einen neuen Gast in die Datenbank ein.
-	update_guest(guest_id, new_data): Aktualisiert die Daten eines bestehenden Gastes.
-	delete_guest(guest_id): Löscht einen Gast aus der Datenbank.
Verwendung:
-	Wird von der Klasse GuestManager in der Geschäftslogik verwendet, um Gästedaten zu verwalten.

**hotelAccess.py**

Diese Datei enthält die Datenzugriffsfunktionen für Hotels. Sie ermöglicht die Verwaltung von Daten in der Tabelle Hotel.

Funktionen:
-	get_all_hotels(): Ruft alle Hotels aus der Datenbank ab.
-	get_hotel_by_id(hotel_id): Ruft ein Hotel basierend auf seiner ID ab.
-	add_hotel(hotel): Fügt ein neues Hotel in die Datenbank ein.
-	update_hotel(hotel_id, new_data): Aktualisiert die Daten eines bestehenden Hotels.
-	delete_hotel(hotel_id): Löscht ein Hotel aus der Datenbank.
-	Google Hotels(city, stars, guest_count): Sucht Hotels basierend auf Stadt, Sternebewertung und Gästeanzahl.
Verwendung:
-	Wird von der Klasse HotelManager in der Geschäftslogik verwendet, um Hotelinformationen zu verwalten.

**invoiceAccess.py**

Diese Datei enthält die Datenzugriffsfunktionen für Rechnungen. Sie ermöglicht die Verwaltung von Daten in der Tabelle Invoice.
Funktionen:
-	get_all_invoices(): Ruft alle Rechnungen aus der Datenbank ab.
-	get_invoice_by_id(invoice_id): Ruft eine Rechnung basierend auf ihrer ID ab.
-	add_invoice(invoice): Fügt eine neue Rechnung in die Datenbank ein.
-	update_invoice(invoice_id, new_data): Aktualisiert eine bestehende Rechnung.
-	delete_invoice(invoice_id): Löscht eine Rechnung aus der Datenbank.
Verwendung:
-	Wird von der Klasse InvoiceManager in der Geschäftslogik verwendet, um Rechnungsdaten zu verwalten.

**roomAccess.py**

Diese Datei enthält die Datenzugriffsfunktionen für Zimmer. Sie ermöglicht die Verwaltung von Daten in der Tabelle Room.
Funktionen:
-	get_all_rooms(): Ruft alle Zimmer aus der Datenbank ab.
-	get_room_by_id(room_id): Ruft ein Zimmer basierend auf seiner ID ab.
-	add_room(room): Fügt ein neues Zimmer in die Datenbank ein.
-	update_room(room_id, new_data): Aktualisiert die Daten eines bestehenden Zimmers.
-	delete_room(room_id): Löscht ein Zimmer aus der Datenbank.
-	search_available_rooms(check_in, check_out): Sucht verfügbare Zimmer für einen bestimmten Zeitraum.
Verwendung:
-	Wird von der Klasse RoomManager in der Geschäftslogik verwendet, um Zimmerdaten zu verwalten.

**roomTypeAccess.py**

Diese Datei enthält die Datenzugriffsfunktionen für Zimmertypen. Sie ermöglicht die Verwaltung von Daten in der Tabelle RoomType.
Funktionen:
-	get_all_room_types(): Ruft alle Zimmertypen aus der Datenbank ab.
-	get_room_type_by_id(room_type_id): Ruft einen Zimmertyp basierend auf seiner ID ab.
-	add_room_type(room_type): Fügt einen neuen Zimmertyp in die Datenbank ein.
-	update_room_type(room_type_id, new_data): Aktualisiert die Daten eines bestehenden Zimmertyps.
-	delete_room_type(room_type_id): Löscht einen Zimmertyp aus der Datenbank.
Verwendung:
-	Wird von der Klasse RoomTypeManager in der Geschäftslogik verwendet, um Zimmertypdaten zu verwalten.



# model
Die Dateien in diesem Verzeichnis enthalten die Datenmodelle des Systems. Sie definieren die Struktur und Eigenschaften der Datenobjekte, die in der Geschäftslogik und der Datenzugriffsschicht verwendet werden. Jedes Modell repräsentiert eine Tabelle in der Datenbank und enthält Attribute, die den Spalten der Tabelle entsprechen.

**Address.py**

Modelliert eine Adresse. Dieses Modell wird verwendet, um Adressdaten für Hotels, Gäste oder andere Entitäten zu speichern.

Attribute:
-	id (int): Eindeutige ID der Adresse.
-	street (str): Strassenname und Hausnummer.
-	city (str): Stadt, in der sich die Adresse befindet.
-	postal_code (str): Postleitzahl der Adresse.
-	country (str): Land der Adresse.

**Booking.py**

Beschreibung: Modelliert eine Buchung. Dieses Modell wird verwendet, um Buchungsinformationen zu speichern.

Attribute:
-	id (int): Eindeutige ID der Buchung.
-	guest_id (int): ID des Gastes, der die Buchung vorgenommen hat.
-	room_id (int): ID des gebuchten Zimmers.
-	check_in (date): Check-in-Datum.
-	check_out (date): Check-out-Datum.
-	total_price (float): Gesamtkosten der Buchung.

**Facility.py**

Modelliert eine Einrichtung (Facility), die einem Zimmer oder einem Hotel zugeordnet werden kann.

Attribute:
-	id (int): Eindeutige ID der Einrichtung.
-	name (str): Name der Einrichtung (z. B. "WiFi", "TV").

**Guest.py**

Modelliert einen Gast. Dieses Modell wird verwendet, um Informationen über Gäste zu speichern.

Attribute:
-	id (int): Eindeutige ID des Gastes.
-	first_name (str): Vorname des Gastes.
-	last_name (str): Nachname des Gastes.
-	email (str): E-Mail-Adresse des Gastes.
-	phone (str): Telefonnummer des Gastes.

**Hotel.py**

Modelliert ein Hotel. Dieses Modell wird verwendet, um Hotelinformationen zu speichern.

Attribute:
-	id (int): Eindeutige ID des Hotels.
-	name (str): Name des Hotels.
-	stars (int): Sternebewertung des Hotels (z. B. 3, 4, 5).
-	address_id (int): ID der Adresse des Hotels.
-	city (str): Stadt, in der sich das Hotel befindet.

**Invoice.py**

Modelliert eine Rechnung. Dieses Modell wird verwendet, um Rechnungsinformationen zu speichern.

Attribute:
-	id (int): Eindeutige ID der Rechnung.
-	booking_id (int): ID der zugehörigen Buchung.
-	issue_date (date): Ausstellungsdatum der Rechnung.
-	total_amount (float): Gesamtbetrag der Rechnung.

**Room.py**

Modelliert ein Zimmer. Dieses Modell wird verwendet, um Zimmereigenschaften zu speichern.

Attribute:
-	id (int): Eindeutige ID des Zimmers.
-	hotel_id (int): ID des Hotels, zu dem das Zimmer gehört.
-	room_number (str): Zimmernummer.
-	price_per_night (float): Preis pro Nacht.
-	room_type_id (int): ID des Zimmertyps.

**RoomFacility.py**

Modelliert die Beziehung zwischen Zimmern und Einrichtungen. Dieses Modell wird verwendet, um zu speichern, welche Einrichtungen einem Zimmer zugeordnet sind.

Attribute:
-	room_id (int): ID des Zimmers.
-	facility_id (int): ID der Einrichtung.

**RoomType.py**

Modelliert einen Zimmertyp (z. B. Einzelzimmer, Doppelzimmer, Suite). Dieses Modell wird verwendet, um Zimmertypinformationen zu speichern.

Attribute:
-	id (int): Eindeutige ID des Zimmertyps.
-	description (str): Beschreibung des Zimmertyps (z. B. "Einzelzimmer mit Balkon").
-	max_guests (int): Maximale Anzahl an Gästen, die in diesem Zimmertyp untergebracht werden können.
