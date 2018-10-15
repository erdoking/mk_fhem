# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]
 - new agent with support for empty readings

## [0.9.3] - 2018-10-15
### Added
 - support for MAX! readings (desiredTemperature,mode,window,groupid)
 - support for XiaomiFlowerSens readings (fertility,lux,moisture)

### Changed
 - tranform on/off (HomeMatic/MAX desiredTemp) to zero

## [0.9.2] - 2018-07-03
### Added
 - change req. check_mk version to 1.2.8 [thanks to mab] 
 - support for more Luxtronik 2.0 readings (counterHoursHeatPump,counterHoursHeating,counterHoursHotWater) [thanks to mab]

## [0.9.1] - 2018-06-25
### Added
 - wato config for HomeMatic reading 'activity' [thanks to MarkusN]
 - support for Luxtronik 2.0 (incl. readings, wato and pnp4nagios) [thanks to mab]

## [0.9.0] - 2018-06-20
### Added
 - mkp erstellt
 - first release version

### Changed
 - Complete rewrite of the WATO configuration page. Now there are categories for better sorting.
 - Extensive rewrite of the FHEM-plugin was necessary.
