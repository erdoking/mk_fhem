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
if (isset($fhem_defines['temperature']) ) {
   $ds_name[] = 'temperature';
   $opt[] = $defopt . "--title \"Temperature\"";
   $def[] = ""
        . fhem_area("temperature",      "80ff40", "Temperature",    "°C",  FALSE)
        . fhem_line("desiredtemp",      "408f20", "Desired temp",   "°C",  FALSE)
        . fhem_area("dewpoint",         "B40404", "Dewpoint",       "°C",  FALSE)  
        . fhem_line("valveposition",    "00bfff", "Valve position", "%% ",  FALSE)
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



?>
