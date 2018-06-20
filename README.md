# mk_fhem

check_MK Plugin für FHEM

Getestet mit CheckMK 1.4.0p33 (Stand: 06.2018)
FHEM-Forum: https://forum.fhem.de/index.php/topic,63723.0.html

ACHTUNG! In Version v0.9 hat sich die WATO Konfiguration massiv geändert, ältere WATO-Konfigurationen funktinieren nicht mehr und müssen neu erstellt werden!

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

## Installation
* Dateien auf den checkMK-Server kopieren (~/local/share/check_mk)
* local/share/check_mk/agents/mk_fhem auf dem FHEM-Server nach /usr/lib/check_mk_agent/plugins/ kopieren
* chmod +x /usr/lib/check_mk_agent/plugins/mk_fhem
* ggf. telnet Passwort/Port anpassen

## ToDo
* Einbindung weiterer Geräte/Hersteller
* Perf-O-Meter
* Aufnahme weiterer Überwachungs-Parameter (Readings,...)
