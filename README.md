# check_fhem

check_MK Plugin für FHEM

## Vorraussetzung
* laufendender FHEM-Server
* laufender checkMK-Server
* FHEM als Agent eingebunden

## Feature
* automatische Inventarisierung neuer Endgeräte
* Graphen (NagVis)
* Zeitlicher Verlauf des letzten Jahres
* Konfigurationsüberwachung
* Überwachung des Batterie-Status

## extended Feature
* DewPoint-optimierte Ünerwachung (sofern in FHEM aktiviert)
* Unterschützung von HomeMatic-Channel

## ToDo
* Einbindung weiterer Geräte/Hersteller
* Perf-O-Meter
* Aufnahme weiterer Überwachungs-Parameter (Readings,...)

## Installation
* Dateien auf den checkMK-Server kopieren (~/local/share/check_mk)
* local/share/check_mk/agents/mk_fhem auf dem FHEM-Server nach /usr/lib/check_mk_agent/plugins/ kopieren
* ggf. telnet Passwort/Port anpassen
