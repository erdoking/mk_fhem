# mk_fhem

check_MK Plugin für FHEM

Getestet mit CheckMK 1.6.0p22 (Stand: 09/2021)

FHEM-Forum: https://forum.fhem.de/index.php/topic,63723.0.html

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
* DewPoint-optimierte Überwachung (sofern in FHEM aktiviert)
* Unterschützung von HomeMatic-Channel

## Installation
* Installatation des mkp:
  * mkp install fhem-<<version>>.mkp
* Agent-Plugin auf dem FHEM-Server nach /usr/lib/check_mk_agent/plugins/ kopieren
  * ~/local/share/check_mk/agents/mk_fhem 
  * ODER https://\<\<UrlVonCheckMK\>\>/\<\<sitename\>\>/check_mk/agents/plugins/mk_fhem
* chmod +x /usr/lib/check_mk_agent/plugins/mk_fhem
* ggf. telnet Passwort/Port anpassen
  * vi /usr/lib/check_mk_agent/plugins/mk_fhem

## ToDo
* Einbindung weiterer Geräte/Hersteller
* Perf-O-Meter
* Aufnahme weiterer Überwachungs-Parameter (Readings,...)

## Known Bugs
* batteryLevel wird bei den meisten Herstellern als Volt geschicht, bei FlowerCare aber als Prozent. (Einheit wird als V ausgegeben)
