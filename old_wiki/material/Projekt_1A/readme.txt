Hallo lieber Entwickler,

hier findest du die Readme Datei zu dem Code Modul im Bereich Qualitätssicherung und Aftersales.
Aus Zeitgründen ist der Code nicht ausgereift, aber er funktioniert, und wird bei uns im Betrieb verwendet.

Exemplarisch findest du Daten einer Flotte von 30 Fahrzeugen mit folgenden Angaben:

vins: Hierbei handelt es sich um die jeweilige (gehashte also anonymisierte) Fahrzeugidentifikationsnummer (Vehicle Identification Number = VIN)
vehicle_models: Die Modellbezeichnung des Fahrzeugs
mobile_numbers: Die Telefonnummer des Fahrzeughalters
emails: Die eMail des Fahrzeughalters
registration_dates: Das Datum der Erstzulassung des Fahrzeugs
service_contract_durations: Die Zahl gibt an, für wie viele Jahre der vereinbarte Werkstattservice gilt.
locations: Der Standort des Fahrzughalters
service_partner_ids: Die ID der zugeordneten Partnerwerkstatt. Hier kann die Zuordnung fehlerhaft sein. Dann können wir dem Kunden auch keinen Termin vorschlagen. 
service_fees: Interne Kosten in Euro für kleine Inspektion nach Fahrzeugtyp.
last_workshop_visit: Datum des letzten Werkstattbesuchs.
mileage_readings: Der aktuelle Kilometerstand des Fahrzugs. 
mileage_at_last_service: Der Kilometerstand zum letzten Werkstattbesuch.

Service_Pauschale: Pauschale in Euro für interne Kosten, die nochmals auf die Servicekosten drauf kommen.