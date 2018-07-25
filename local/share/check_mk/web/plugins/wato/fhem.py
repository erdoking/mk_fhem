#!/usr/bin/python
# -*- encoding: utf-8; py-indent-offset: 4 -*-

# Rules for configuring parameters of check fhem

#subgroup_networking =   _("Networking")

register_check_parameters(
    subgroup_environment,
    "fhem",
    _("FHEM"),
    Dictionary(
        title = _('FHEM parameters'),
        help = _('configure FHEM devices'),
        elements = [
            ## ####################################################
            ## Category common
            ## ####################################################
            ('common_params', Dictionary(
             title = "Common",
             required_keys = [],
             elements = [
              ## ----------------------------------------------------
              ## Sub-category Temperatur
              ## ----------------------------------------------------
              ('state_params', Dictionary(
               title = "Device state",
               required_keys = [],
               elements = [
                       ## Device state (reading)
                       ("var_state",
                         Alternative(
                            title = _('Decice state (r: state)'),
                            style = "dropdown",
                            allow_empty = False,
                            help = _("Check state of reading 'state' (default: ignore) "),
                            elements = [
                                FixedValue(
                                    'ok',
                                    totext = "ok",
                                    title = _("ok"),
                                ),
                                TextAscii(
                                    title = _("custom"),
                                    label = _("custom:"),
                                    size = 50,
                                ),
                           ]

                        )),
                       ## Device presence (reading)
                       ## maybe Sonoff specified?
                       ("var_presence",
                         Alternative(
                            title = _('Decice presence (r: presence)'),
                            style = "dropdown",
                            allow_empty = False,
                            help = _("Check state of reading 'presence' (default: present) "),
                            elements = [
                                FixedValue(
                                    'ignore',
#                                    totext = "ignore",
                                    title = _("ignore"),
                                ),
                                FixedValue(
                                    'present',
                                    totext = "present",
                                    title = _("present"),
                                ),
                                FixedValue(
                                    'absent',
                                    totext = "absent",
                                    title = _("absent"),
                                ),

                                TextAscii(
                                    title = _("custom"),
                                    label = _("custom:"),
                                    size = 50,
                                ),
                           ]

                        )),
               ],
              )),
              ## ----------------------------------------------------
              ## Sub-category Battery
              ## ----------------------------------------------------
              ('battery_params', Dictionary(
               title = "Battery state",
               required_keys = [],
               elements = [
                       ## Battery state
                       ("var_battery",
                         Alternative(
                            title = _('State of battery (r: battery'),
                            style = "dropdown",
                            allow_empty = False,
                            help = _("Check state of reading 'battery' (default: ok) "),
                            elements = [
                                FixedValue(
                                    'ignore',
                                    totext = "ignore",
                                    title = _("ignore"),
                                ),
                                TextAscii(
                                    title = _("custom"),
                                    label = _("custom:"),
                                    size = 50,
                                ),
                           ]

                        )),
                        ## Battery voltage
                        ( "level_batteryLevel_min",
                          Tuple(
                              title = _("Level for batterie voltage (r: batteryLevel)"),
                              help = _("You can adjust the levels before this service goes into warning/critical. Set to 0 to disable."),
                              elements = [
                                  Percentage(title = _("Warning at"), unit = "V", default_value = 2.3),
                                  Percentage(title = _("Critical at"), unit = "V", default_value = 2.1),
                              ]
                        )),

               ],
              )),

             ]
            )),

            ## ####################################################
            ## Category Climate
            ## ####################################################
            ('climate_params', Dictionary(
             title = "Climate",
             required_keys = [],
             elements = [
              ## ----------------------------------------------------
              ## Sub-category Temperature
              ## ----------------------------------------------------
              ('temperature_params', Dictionary(
               title = "Temperature",
               required_keys = [],
               elements = [
                       ## Temperature upper level
                       ( "level_temperature_max",
                          Tuple(
                              help = _("You can adjust the levels before this service goes into warning/critical. Set to 1000 to disable."),
                              title = _("Upper Levels (r: temperature)"),
                              elements = [
                                  Integer(title = _("Warning at"), unit = u"°C", default_value = 26),
                                  Integer(title = _("Critical at"), unit = u"°C", default_value = 30),
                              ]
                        )),
                        ## Temperature lower level
                        ( "level_temperature_min",
                          Tuple(
                              title = _("Lower Levels (r: temperature)"),
                              help = _("You can adjust the levels before this service goes into warning/critical. Set to -1000 to disable."),
                              elements = [
                                  Integer(title = _("Warning below"), unit = u"°C", default_value = 0),
                                  Integer(title = _("Critical below"), unit = u"°C", default_value = -10),
                              ]
                        )),
               ]
              )),
              ## ----------------------------------------------------
              ## Sub-category Humidity 
              ## ----------------------------------------------------
              ('humidity_params', Dictionary(
               title = "Humidity",
               required_keys = [],
               elements = [
                        ## Humidity upper level
                        ( "level_humidity_max",
                          Tuple(
                              help = _("You can adjust the levels before this service goes into warning/critical. Set to 1000 to disable."),
                              title = _("Upper levels (r: humidity)"),
                              elements = [
                                  Integer(title = _("Warning at"), unit = u"%", default_value = 70),
                                  Integer(title = _("Critical at"), unit = u"%", default_value = 80),
                              ]
                        )),
                        ## Humidity lower level
                        ( "level_humidity_min",
                          Tuple(
                              title = _("Lower levels (r: humidity)"),
                              help = _("You can adjust the levels before this service goes into warning/critical. Set to -1000 to disable."),
                              elements = [
                                  Integer(title = _("Warning below"), unit = u"%", default_value = 50),
                                  Integer(title = _("Critical below"), unit = u"%", default_value = 45),
                              ]
                        )),
               ]
              )),
              ## ----------------------------------------------------
              ## Sub-category dewpoint
              ## ----------------------------------------------------
              ('dewpoint_params', Dictionary(
               title = "Dewpoint",
               required_keys = [],
               elements = [
                        ## Dewpoint upper level
                        ( "level_dewpoint_max",
                          Tuple(
                              title = _("diff to temperatur"),
                              help = _("exp. 17°C [dewp] vs 20°C [temp] (r: dewpoint) "),
                              elements = [
                                  Integer(title = _("Warning below"), unit = u"°C", default_value = 3),
                                  Integer(title = _("Critical below"), unit = u"°C", default_value = 1),
                              ]
                        )),
                        ## ignore humidity
                        ("var_dewpoint_override",
                         Alternative(
                            title = _('ignore humidity (r: humidity+dewpoint)'),
                            style = "dropdown",
                            allow_empty = False,
                            help = _("don't alert humidity if dewpoint given. (default: true)"),
                            elements = [
                                FixedValue(
                                    'true',
                                    totext = "true",
                                    title = _("true"),
                                ),
                                FixedValue(
                                    'false',
                                    totext = "false",
                                    title = _("false"),
                                ),
                           ]
                        )),
               ]
              )),
             ],
            )),
            ## ####################################################
            ## Category Various 
            ## ####################################################
            ('various_params', Dictionary(
             title = "Various",
             help = _("everything else ..."),
             elements = [
              ## ----------------------------------------------------
              ## Sub-category Speedtest 
              ## ----------------------------------------------------
              ('speedtest_params', Dictionary(
               title = "Speedtest",
               required_keys = [],
               elements = [
                        ## speedtest download
                        ( "level_download_min",
                          Tuple(
                              title = _("Level for speedtest download "),
                              help = _("You can adjust the levels before this service goes into warning/critical. Set to 0 to disable. (r: download)"),
                              elements = [
                                  Percentage(title = _("Warning at"), unit = "Mbit/s", default_value = 10.0),
                                  Percentage(title = _("Critical at"), unit = "Mbit/s", default_value = 8.0),
                              ]
                        )),
                        ## speedtest upload
                        ( "level_upload_min",
                          Tuple(
                              title = _("Level for speedtest upload"),
                              help = _("You can adjust the levels before this service goes into warning/critical. Set to 0 to disable. (r: upload)"),
                              elements = [
                                  Percentage(title = _("Warning at"), unit = "Mbit/s", default_value = 1.5),
                                  Percentage(title = _("Critical at"), unit = "Mbit/s", default_value = 1.0),
                              ]
                        )),
                        ## speedtest ping
                        ( "level_ping_max",
                          Tuple(
                              title = _("Level for speedtest ping"),
                              help = _("You can adjust the levels before this service goes into warning/critical. Set to 0 to disable. (r: ping)"),
                              elements = [
                                  Integer(title = _("Warning at"), unit = "ms", default_value = 100),
                                  Integer(title = _("Critical at"), unit = "ms", default_value = 150),
                              ]
                        )),
               ]
              )),
             ],
            )),
            ## ####################################################
            ## Category Device types
            ## ####################################################
            ('devicetypes_params', Dictionary(
             title = "Device types",
             required_keys = [],
             elements = [
              ## ----------------------------------------------------
              ## Sub-category Light 
              ## ----------------------------------------------------
              ('light_params', Dictionary(
               title = "Light",
               required_keys = [],
               elements = [
                       ("var_RGB_color",
                         Alternative(
                            title = _('RGB color (r: RGB)'),
                            style = "dropdown",
                            allow_empty = False,
                            help = _("Check state of reading 'RGB' (without #)"),
                            elements = [
                                FixedValue(
                                    'FFFFFF',
                                    totext = "white",
                                    title = _("white"),
                                ),
                                TextAscii(
                                    title = _("custom"),
                                    label = _("custom:"),
                                    size = 6,
                                ),
                           ]

                        )),
                       ("var_brightness",
                         Alternative(
                            title = _('light brightness (r: brightness)'),
                            style = "dropdown",
                            allow_empty = False,
                            help = _("Check state of reading 'brightness' (default: ignore) "),
                            elements = [
                                FixedValue(
                                    '100',
                                    totext = "100%",
                                    title = _("100%"),
                                ),
                                FixedValue(
                                    '0',
                                    totext = "0%",
                                    title = _("0%"),
                                ),
                                TextAscii(
                                    title = _("custom"),
                                    label = _("custom:"),
                                    size = 3,
                                ),
                           ]

                        )),

               ]
              )),
              ## ----------------------------------------------------
              ## Sub-category Contact sensor
              ## ----------------------------------------------------
              ('contactsensor_params', Dictionary(
               title = "Contact sensor",
               required_keys = [],
               elements = [
                        ("var_contact",
                         Alternative(
                            title = _('Contact state (r: contact)'),
                            style = "dropdown",
                            allow_empty = False,
                            help = _("Check state of reading 'contact' (default: ignore) "),
                            elements = [
                                FixedValue(
                                    'open',
                                    totext = "open",
                                    title = _("open"),
                                ),
                                FixedValue(
                                    'closed',
                                    totext = "closed",
                                    title = _("closed"),
                                ),
                                TextAscii(
                                    title = _("custom"),
                                    label = _("custom:"),
                                    size = 50,
                                ),
                           ]
                       )),

               ]
              )),           

             ],
            )),
            ## ####################################################
            ## Category Manufacturer
            ## ####################################################
            ('manufacturer_params', Dictionary(
             title = "Manufacturer",
             help = _("Manufacturer specific parameter"),
             elements = [
              ## ----------------------------------------------------
              ## Sub-category HomeMatic
              ## ----------------------------------------------------
              ('homematic_params', Dictionary(
               title = "HomeMatic",
               help = _("HomeMatic specific parameter"),
               allow_empty = False,
               elements = [
               ("var_btnLock",
                 Alternative(
                    title = _('btnLock state'),
                    style = "dropdown",
                    allow_empty = False,
                    help = _("Check state of reading 'btnLock' (default: ignore) "),
                    elements = [
                        FixedValue(
                            'on',
                            totext = "on",
                            title = _("on"),
                        ),
                        FixedValue(
                            'off',
                            totext = "off",
                            title = _("off"),
                        ),
                        TextAscii(
                            title = _("custom"),
                            label = _("custom:"),
                            size = 50,
                        ),
                   ]

                )),
               ("var_globalBtnLock",
                 Alternative(
                    title = _('globalBtnLock state'),
                    style = "dropdown",
                    allow_empty = False,
                    help = _("Check state of reading 'globalBtnLock' [default: ignore] (r: globalBtnLock) "),
                    elements = [
                        FixedValue(
                            'on',
                            totext = "on",
                            title = _("on"),
                        ),
                        FixedValue(
                            'off',
                            totext = "off",
                            title = _("off"),
                        ),
                        TextAscii(
                            title = _("custom"),
                            label = _("custom:"),
                            size = 50,
                        ),
                   ]

                )),
               ("var_modusBtnLock",
                 Alternative(
                    title = _('modusBtnLock state'),
                    style = "dropdown",
                    allow_empty = False,
                    help = _("Check state of reading 'modusBtnLock' [default: ignore] (r: modusBtnLock) "),
                    elements = [
                        FixedValue(
                            'on',
                            totext = "on",
                            title = _("on"),
                        ),
                        FixedValue(
                            'off',
                            totext = "off",
                            title = _("off"),
                        ),
                        TextAscii(
                            title = _("custom"),
                            label = _("custom:"),
                            size = 50,
                        ),
                   ]

                )),
                ("var_controlMode",
                 Alternative(
                    title = _('Control Mode'),
                    style = "dropdown",
                    allow_empty = False,
                    help = _("Check current control mode. (default: ignore)"),
                    elements = [
                        FixedValue(
                            'auto',
                            totext = "auto",
                            title = _("auto"),
                        ),
                        FixedValue(
                            'manual',
                            totext = "manual",
                            title = _("manual"),
                        ),
                        FixedValue(
                            'boost',
                            totext = "boost",
                            title = _("boost"),
                        ),
                        FixedValue(
                            'day',
                            totext = "day",
                            title = _("day"),
                        ),
                        FixedValue(
                            'night',
                            totext = "night",
                            title = _("night"),
                        ),

                        TextAscii(
                            title = _("custom"),
                            label = _("custom:"),
                            size = 50,
                        ),
                   ]
                )),
                       ## Device activity (reading)
                       ("var_activity",
                         Alternative(
                            title = _('Decice activity (r: activity)'),
                            style = "dropdown",
                            allow_empty = False,
                            help = _("Check state of reading 'activity' (default: alive) "),
                            elements = [
                                FixedValue(
                                    'alive',
                                    totext = "alive",
                                    title = _("alive"),
                                ), 
                                FixedValue(
                                    'ignore',
                                    title = _("ignore"),
                                ),
                                FixedValue(
                                    'dead',
                                    totext = "dead",
                                    title = _("dead"),
                                ),
                                FixedValue(
                                    'switchedOff',
                                    totext = "switchedOff",
                                    title = _("switchedOff"),
                                ),
                                TextAscii(
                                    title = _("custom"),
                                    label = _("custom:"),
                                    size = 50,
                                ),
                           ]

                        )),

               ]
              )),
              ## ----------------------------------------------------
              ## Sub-category MAX!
              ## ----------------------------------------------------
              ('max_params', Dictionary(
               title = "MAX!",
               help = _("MAX! specific parameter"),
               allow_empty = False,
               elements = [
                        ("var_mode",
                         Alternative(
                            title = _('Control Mode'),
                            style = "dropdown",
                            allow_empty = False,
                            help = _("Check current control mode. (default: ignore)"),
                            elements = [
                                FixedValue(
                                    'auto',
                                    totext = "auto",
                                    title = _("auto"),
                                ),
                                FixedValue(
                                    'manual',
                                    totext = "manual",
                                    title = _("manual"),
                                ),
                                FixedValue(
                                    'temporary',
                                    totext = "temporary",
                                    title = _("temporary"),
                                ),
                                FixedValue(
                                    'boost',
                                    totext = "boost",
                                    title = _("boost"),
                                ),
                                TextAscii(
                                    title = _("custom"),
                                    label = _("custom:"),
                                    size = 50,
                                ),
                           ]
                        )),
                        ("var_window",
                         Alternative(
                            title = _('window state (r: window)'),
                            style = "dropdown",
                            allow_empty = False,
                            help = _("Check state of reading 'window' (default: ignore) "),
                            elements = [
                                FixedValue(
                                    'open',
                                    totext = "open",
                                    title = _("open"),
                                ),
                                FixedValue(
                                    'closed',
                                    totext = "closed",
                                    title = _("closed"),
                                ),
                                TextAscii(
                                    title = _("custom"),
                                    label = _("custom:"),
                                    size = 50,
                                ),
                           ]
                       )),
               ]
              )),

              ## ----------------------------------------------------
              ## Sub-category Luxtronik
              ## ----------------------------------------------------
              ('luxtronik2_params', Dictionary(
               title = "Luxtronik",
               help = _("Luxtronik specific parameter"),
               allow_empty = False,
               elements = [
                       ## ambientTemperature upper level
                       ( "level_ambientTemperature_max",
                          Tuple(
                              help = _("You can adjust the levels before this service goes into warning/critical. Set to 1000 to disable."),
                              title = _("Ambient temperature upper Levels (r: ambientTemperature)"),
                              elements = [
                                  Integer(title = _("Warning at"), unit = u"°C", default_value = 26),
                                  Integer(title = _("Critical at"), unit = u"°C", default_value = 30),
                              ]
                        )),
                        ## ambientTemperature lower level
                        ( "level_ambientTemperature_min",
                          Tuple(
                              title = _("Ambient temperature lower Levels (r: ambientTemperature)"),
                              help = _("You can adjust the levels before this service goes into warning/critical. Set to -1000 to disable."),
                              elements = [
                                  Integer(title = _("Warning below"), unit = u"°C", default_value = 15),
                                  Integer(title = _("Critical below"), unit = u"°C", default_value = 12),
                              ]
                        )),
                       ## hotWaterTemperature upper level
                       ( "level_hotWaterTemperature_max",
                          Tuple(
                              help = _("You can adjust the levels before this service goes into warning/critical. Set to 1000 to disable."),
                              title = _("Water temperature upper Levels (r: hotWaterTemperature)"),
                              elements = [
                                  Integer(title = _("Warning at"), unit = u"°C", default_value = 60),
                                  Integer(title = _("Critical at"), unit = u"°C", default_value = 65),
                              ]
                        )),
                        ## hotWaterTemperature lower level
                        ( "level_hotWaterTemperature_min",
                          Tuple(
                              title = _("Water temperature lower Levels (r: hotWaterTemperature)"),
                              help = _("You can adjust the levels before this service goes into warning/critical. Set to -1000 to disable."),
                              elements = [
                                  Integer(title = _("Warning below"), unit = u"°C", default_value = 40),
                                  Integer(title = _("Critical below"), unit = u"°C", default_value = 37),
                              ]
                        )),
                       ## hotGasTemperature upper level
                       ( "level_hotGasTemperature_max",
                          Tuple(
                              help = _("You can adjust the levels before this service goes into warning/critical. Set to 1000 to disable."),
                              title = _("Gas temperature upper Levels (r: hotGasTemperature)"),
                              elements = [
                                  Integer(title = _("Warning at"), unit = u"°C", default_value = 0),
                                  Integer(title = _("Critical at"), unit = u"°C", default_value = 0),
                              ]
                        )),
                        ## hotGasTemperature lower level
                        ( "level_hotGasTemperature_min",
                          Tuple(
                              title = _("Gas temperature lower Levels (r: hotGasTemperature)"),
                              help = _("You can adjust the levels before this service goes into warning/critical. Set to -1000 to disable."),
                              elements = [
                                  Integer(title = _("Warning below"), unit = u"°C", default_value = 0),
                                  Integer(title = _("Critical below"), unit = u"°C", default_value = 0),
                              ]
                        )),
                       ## returnTemperature upper level
                       ( "level_returnTemperature_max",
                          Tuple(
                              help = _("You can adjust the levels before this service goes into warning/critical. Set to 1000 to disable."),
                              title = _("Return temperature upper Levels (r: returnTemperature)"),
                              elements = [
                                  Integer(title = _("Warning at"), unit = u"°C", default_value = 0),
                                  Integer(title = _("Critical at"), unit = u"°C", default_value = 0),
                              ]
                        )),
                        ## returnTemperature lower level
                        ( "level_returnTemperature_min",
                          Tuple(
                              title = _("Return temperature lower Levels (r: returnTemperature)"),
                              help = _("You can adjust the levels before this service goes into warning/critical. Set to -1000 to disable."),
                              elements = [
                                  Integer(title = _("Warning below"), unit = u"°C", default_value = 0),
                                  Integer(title = _("Critical below"), unit = u"°C", default_value = 0),
                              ]
                        )),
                        ## opModeHeating
                        ("var_opModeHeating",
                         Alternative(
                            title = _('Operation mode heating (r: opModeHeating)'),
                            style = "dropdown",
                            allow_empty = False,
                            help = _("opModeHeating (default: Automatik)"),
                            elements = [
                                FixedValue(
                                    'Automatik',
                                    totext = "Automatik",
                                    title = _("Automatik"),
                                ),
                                TextAscii(
                                    title = _("custom"),
                                    label = _("custom:"),
                                    size = 50,
                                ),
                           ]
                        )),
                        ## opModeHotWater
                        ("var_opModeHotWater",
                         Alternative(
                            title = _('Operation mode heating (r: opModeHotWater)'),
                            style = "dropdown",
                            allow_empty = False,
                            help = _("opModeHotWater (default: Automatik)"),
                            elements = [ 
                                FixedValue(
                                    'Automatik',
                                    totext = "Automatik",
                                    title = _("Automatik"),
                                ),
                                TextAscii(
                                    title = _("custom"),
                                    label = _("custom:"),
                                    size = 50,
                                ),
                           ]
                        )),
                        ## heatingSystemCircPump
                        ("var_heatingSystemCircPump",
                         Alternative(
                            title = _('Heating system cirle pump (r: heatingSystemCircPump)'),
                            style = "dropdown",
                            allow_empty = False,
                            help = _("heatingSystemCircPump (default: ignore)"),
                            elements = [  
                                FixedValue(
                                    'on',
                                    totext = "on",
                                    title = _("on"),
                                ),
                                FixedValue(
                                    'off',
                                    totext = "off",
                                    title = _("off"),
                                ),
                                TextAscii(
                                    title = _("custom"),
                                    label = _("custom:"),
                                    size = 50,
                                ),
                           ]
                        )),
                        ## opStateHeatPump1
                        ("var_opStateHeatPump1",
                         Alternative(
                            title = _('Operation mode heating (r: opStateHeatPump1)'),
                            style = "dropdown",
                            allow_empty = False,
                            help = _("opStateHeatPump1 (default: ignore)"),
                            elements = [  
                                TextAscii(
                                    title = _("custom"),
                                    label = _("custom:"),
                                    size = 50,
                                ),
                           ]
                        )),




               ]
              )),




             ],
            )),


        ],
#        required_keys = [ 'service_description', 'imap_parameters' ]
    ),
    TextAscii(
        title = _("fhem device"),
        help = _("Specify the name of the FHEM device, i.e. <tt>eg.bad.heizung</tt>"),
        allow_empty = False,
        default_value = 0,
    ),
    "dict",
)


