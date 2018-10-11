<?php
# PNP4Nagios template for check_fhem FHEM check
# Author: Jonas Nickl <kontakt@jonasnickl.de>

#$defopt = "--vertical-label 'Bytes' -l0 -b 1024 ".
$defopt = "--color MGRID\"#cccccc\" --color GRID\"#dddddd\" ";

#$def[] = "";
#$opt[] = "";

# Work with names rather then numbers.
global $fhem_defines;
$fhem_defines = array();
foreach ($NAME as $i => $n) {
    $fhem_defines[$n] = "DEF:$n=$RRDFILE[$i]:$DS[$i]:MAX ";
}

# avoid redeclaration errors if this file is include multiple times (e.g. by basket)
if (!function_exists('fhem_area')) {
    function fhem_area($varname, $color, $title, $unit, $stacked)
    {
        return fhem_curve("AREA", $varname, $color, $title, $unit, $stacked);
    }

    function fhem_line($varname, $color, $title, $unit, $stacked)
    {
        return fhem_curve("LINE1", $varname, $color, $title, $unit, $stacked);
    }

    function fhem_curve($how, $varname, $color, $title, $unit, $stacked)
    {
        global $fhem_defines;
        $tit = sprintf("%-30s", $title);
        if (isset($fhem_defines[$varname])) {
            $x = $fhem_defines[$varname] . "$how:$varname#$color:\"$tit\"";
            if ($stacked)
                $x .= ":STACK";
            $x .= " ";
#            $x .= "CDEF:${varname}_gb=$varname,1073741824,/ ";
            $x .= "GPRINT:${varname}:LAST:\"%6.1lf ${unit} last\" ";
            $x .= "GPRINT:${varname}:AVERAGE:\"%6.1lf ${unit} avg\" ";
            $x .= "GPRINT:${varname}:MAX:\"%6.1lf ${unit} max\\n\" ";
            return $x;
        }
        else {
            return "";
        }
    }
}

# 1. Overview
if (isset($fhem_defines['temperature']) && isset($fhem_defines['humidity']) ) {
   $ds_name[] = 'temperature';
   $opt[] = $defopt . "--title \"Temperature + Humidity\"";
   $def[] = ""
        . fhem_area("humidity",         "00bfff", "Humidity",       "%% ", FALSE)
        . fhem_area("temperature",      "80ff40", "Temperature",    "°C",  FALSE)
        . fhem_line("desiredtemp",      "408f20", "Desired temp",   "°C",  FALSE)
        . fhem_area("dewpoint",         "B40404", "Dewpoint",       "°C",  FALSE)  
        . fhem_line("valveposition",    "00bfff", "Valve position", "%% ",  FALSE)
        ;
}

# 2. Temperature
if (isset($fhem_defines['temperature']) or isset($fhem_defines['moisture'])) {
   $ds_name[] = 'temperature';
   $opt[] = $defopt . "--title \"Temperature\"";
   $def[] = ""
        . fhem_area("temperature",      "80ff40", "Temperature",    "°C",  FALSE)
        . fhem_line("desiredtemp",      "408f20", "Desired temp",   "°C",  FALSE)
        . fhem_area("dewpoint",         "B40404", "Dewpoint",       "°C",  FALSE)  
        . fhem_line("valveposition",    "00bfff", "Valve position", "%% ",  FALSE)
        ## XiaomiFlowerSens
        . fhem_curve("LINE2", "moisture", "00bfff", "moisture", "%%",  FALSE)
        ;
}


## 2. Valveposition 
#if (isset($fhem_defines['valveposition']) ) {
#   $opt[] = $defopt . "--title \"Valveposition\"";
#   $def[] = ""
#        . fhem_area("temperature",     "80ff40", "Temperature",    "°C",  FALSE)
#        . fhem_area("desiredtemp",     "408f20", "Desired temp",   "°C",  FALSE)
#        . fhem_line("valveposition",   "00bfff", "Valve Position", "%% ",  FALSE)
#        ;
#}


# 3. BatteryLevel
if (isset($fhem_defines['batteryLevel']) ) {
   $ds_name[] = 'batteryLevel';
   $opt[] = $defopt . "--title \"batteryLevel\"";
   $def[] = ""
        . fhem_area("batteryLevel",   "e0e0e0", "Battery Level", "V",  FALSE)
        ;
}

# 4. Power (kWh)
if (isset($fhem_defines['power']) ) {
   $ds_name[] = 'power';
   $opt[] = $defopt . "--title \"Power\"";
   $def[] = ""
        . fhem_area("power",   "e0e0e0", "Power", "kWh",  FALSE)
#        . fhem_area("dewpoint",     "80ff40", "",          FALSE)
#        . fhem_area("swap_used",    "408f20", "",          TRUE)
        ;
}

# 5. Brightness
if (isset($fhem_defines['brightness']) ) {
   $ds_name[] = 'brightness';
   $opt[] = $defopt . "--title \"Brightness\"";
   $def[] = ""
        . fhem_area("brightness",   "ffb90f", "Brightness", "%%",  FALSE)
        . fhem_line("brightness_on","551a8b", "Brightness_on", "%%",  FALSE)
        ;
}


# 6. Color temperature (ct)
if (isset($fhem_defines['ct']) ) {
   $ds_name[] = 'ct';
   $opt[] = $defopt . "--title \"Color temperature (ct)\"";
   $def[] = ""
        . fhem_curve("LINE2", "ct", "ff4500", "Color temperature (ct)", "K",  FALSE)
        ;
}

# 7. Speedtest (down-/upload)
if (isset($fhem_defines['download']) ) {
   $ds_name[] = 'speedtest';
   $opt[] = $defopt . "--title \"Speedtest\"";
   $def[] = ""
        . fhem_area("download",         "00ffc0", "Download",       "Mbit/s",  FALSE)
        . fhem_area("upload",           "00c0ff", "Upload",         "Mbit/s",  FALSE)
        ;
}

# 8. Speedtest (ping)
if (isset($fhem_defines['ping']) ) {
   $ds_name[] = 'speedtest_ping';
   $opt[] = $defopt . "--title \"Speedtest Ping\"";
   $def[] = ""
        . fhem_area("ping",             "2b85c8", "Ping",           "ms",      FALSE)
        ;
}

# 9. Traffic (duration)
if (isset($fhem_defines['duration']) ) {
   $ds_name[] = 'duration';
   $opt[] = $defopt . "--title \"Traffic duration\"";
   $def[] = ""
        . fhem_area("duration", "00bfff", "Duration", "min", FALSE)
        . fhem_area("delay", "f78181", "Delay", "min", TRUE)
        . fhem_curve("LINE2", "duration_in_traffic", "B40404", "Duration in traffic", "min", FALSE)
        ;
}   


# 9. Traffic (duration)
if (isset($fhem_defines['presence']) ) {
   $ds_name[] = 'presence';
   $opt[] = $defopt . "--title \"Presence\"";
   $def[] = ""
        . fhem_area("presence", "00bfff", "Presence", "", FALSE)
        ;
}



# 10. LUXTRONIK2 (ambientTemperature)
if (isset($fhem_defines['ambientTemperature']) ) {
   $ds_name[] = 'ambientTemperature';
   $opt[] = $defopt . "--title \"Ambient temperature\"";
   $def[] = ""
        . fhem_area("ambientTemperature",      "80ff40", "ambientTemperature",    "°C",  FALSE)
        . fhem_curve("LINE2", "averageAmbientTemperature",      "408f20", "averageAmbientTemperature",   "°C",  FALSE)
        ;
}


# 11. LUXTRONIK2 (hotWaterTemperature)
if (isset($fhem_defines['hotWaterTemperature']) ) {
   $ds_name[] = 'hotWaterTemperature';
   $opt[] = $defopt . "--title \"hot wasser temperature\"";
   $def[] = ""
        . fhem_area("hotWaterTemperature",      "00bfff", "hotWaterTemperature",         "°C",  FALSE)
        . fhem_curve("LINE2", "hotWaterTemperatureTarget","00008B", "hotWaterTemperatureTarget",   "°C",  FALSE)
        ;
}


# 12. LUXTRONIK2 (returnTemperature)
if (isset($fhem_defines['returnTemperature']) ) {
   $ds_name[] = 'returnTemperature';
   $opt[] = $defopt . "--title \"return temperature + flow temperature\"";
   $def[] = ""
        . fhem_area("returnTemperature", "ffd700", "returnTemperature", "°C",  FALSE)
        . fhem_curve("LINE2", "flowTemperature", "00bfff", "flowTemperature", "°C",  FALSE)
        . fhem_curve("LINE2", "returnTemperatureTarget","ee0000", "returnTemperatureTarget",   "°C",  FALSE)
        ;
}


# 13. LUXTRONIK2 (counterHoursHeatPump)
if (isset($fhem_defines['counterHoursHeatPump']) ) {
   $ds_name[] = 'counterHoursHeatPump';
   $opt[] = $defopt . "--title \"counter Hours Heating\"";
   $def[] = ""
        . fhem_area("counterHoursHeatPump", "00EE76", "counterHoursHeatPump", "h",  FALSE)
#        . fhem_curve("LINE2", "counterHoursHeating", "00bfff", "counterHoursHeating", "h",  FALSE)
#        . fhem_area("counterHoursHotWater","ee0000", "counterHoursHotWater",   "h",  FALSE)
#        . fhem_curve("LINE3", "counterHoursHeating", "00bfff", "counterHoursHeating", "h",  FALSE)


        ;
}

# 14. LUXTRONIK2 (counterHoursHeating)
if (isset($fhem_defines['counterHoursHeating']) or isset($fhem_defines['counterHoursHotWater'])) {
   $ds_name[] = 'counterHoursHeating';
   $opt[] = $defopt . "--title \"counterHoursHotWater + counterHoursHeating\"";
   $def[] = ""
        . fhem_area("counterHoursHotWater","ffd700", "counterHoursHotWater",   "h",  FALSE)
        . fhem_area("counterHoursHeating", "ee0000", "counterHoursHeating", "h",  FALSE)
        ;
}


# 15. XiaomiFlowerSens (fertility)
if (isset($fhem_defines['fertility']) or isset($fhem_defines['lux'])) {
   $ds_name[] = '';
   $opt[] = $defopt . "--title \"fertility\"";
   $def[] = ""
        . fhem_area("fertility","ffd700", "fertility",   "",  FALSE)
        . fhem_curve("LINE2", "lux", "ee0000", "lux", "lx",  FALSE)
        . fhem_curve("LINE2", "moisture", "00bfff", "moisture", "%%",  FALSE)
        ;
}

?>
