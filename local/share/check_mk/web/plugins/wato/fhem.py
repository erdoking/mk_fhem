#!/usr/bin/python
# -*- encoding: utf-8; py-indent-offset: 4 -*-

# Rules for configuring parameters of check fhem

#subgroup_networking =   _("Networking")

register_check_parameters(
    subgroup_environment,
    "fhem",
    _("FHEM"),
    Transform(
        Dictionary(
            elements = [
                ( "level_temperature_max",
                  Tuple(
		      help = _("You can adjust the levels before this service goes into warning/critical. Set to 1000 to disable."),
                      title = _("Upper Temperature Levels"),
                      elements = [
                          Integer(title = _("Warning at"), unit = u"°C", default_value = 26),
                          Integer(title = _("Critical at"), unit = u"°C", default_value = 30),
                      ]
                )),
                ( "level_temperature_min",
                  Tuple(
                      title = _("Lower Temperature Levels"),
		      help = _("You can adjust the levels before this service goes into warning/critical. Set to -1000 to disable."),
                      elements = [
                          Integer(title = _("Warning below"), unit = u"°C", default_value = 0),
                          Integer(title = _("Critical below"), unit = u"°C", default_value = -10),
                      ]
                )),
#                ( "output_unit",
#                  DropdownChoice(
#                      title = _("Display values in "),
#                      choices = [
#                        ( "c", _("Celsius") ),
#                        ( "f", _("Fahrenheit") ),
#                        ( "k", _("Kelvin") ),
#                      ]
#                )),
                ( "level_humidity_max",
                  Tuple(
                      help = _("You can adjust the levels before this service goes into warning/critical. Set to 1000 to disable."),
                      title = _("Upper huminity levels"),
                      elements = [
                          Integer(title = _("Warning at"), unit = u"%", default_value = 70),
                          Integer(title = _("Critical at"), unit = u"%", default_value = 80),
                      ]
                )),
                ( "level_humidity_min",
                  Tuple(
                      title = _("Lower huminity levels"),
                      help = _("You can adjust the levels before this service goes into warning/critical. Set to -1000 to disable."),
                      elements = [
                          Integer(title = _("Warning below"), unit = u"%", default_value = 50),
                          Integer(title = _("Critical below"), unit = u"%", default_value = 45),
                      ]
                )),
                ( "level_data_age",
                  Tuple(
                      title = _("Time left until data becoming obsolet."),
		      help = _("Time before data becoming obsolete. Set to 0 to disable."),
                      elements = [
                          Integer(title = _("Warning older than"), unit = "minutes", default_value = 30),
                          Integer(title = _("Critical older than"), unit = "minutes", default_value = 90),
                      ]
                )),
                ( "level_batteryLevel_min",
                  Tuple(
                      title = _("Level for batterie voltage"),
                      help = _("You can adjust the levels before this service goes into warning/critical. Set to 0 to disable."),
                      elements = [
                          Percentage(title = _("Warning at"), unit = "V", default_value = 2.3),
                          Percentage(title = _("Critical at"), unit = "V", default_value = 2.1),
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
		("var_alive",
		 Alternative(
                    title = _('Alive state'),
                    style = "dropdown",
                    allow_empty = False,
                    help = _("Check state of reading 'alive' on HomeMatic devices (default: ignore) "),
                    elements = [
                        FixedValue(
                            'alive',
                            totext = "alive",
                            title = _("alive"),
                        ),
                        FixedValue(
                            'dead',
                            totext = "dead",
                            title = _("dead"),
                        ),
                        TextAscii(
                            title = _("custom"),
                            label = _("custom:"),
                            size = 50,
                        ),
                   ]
                )),
                ("var_contact",
                 Alternative(
                    title = _('Contact state'),
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
                    help = _("Check state of reading 'globalBtnLock' (default: ignore) "),
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
                    help = _("Check state of reading 'modusBtnLock' (default: ignore) "),
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

	    ],
#                optional_keys = False,
        ),
        forth = lambda v: type(v) == tuple and { "levels" : v } or v,
    ),
    TextAscii(
        title = _("fhem device"),
        help = _("Specify the name of the FHEM device, i.e. <tt>eg.bad.heizung</tt>"),
    ),
    "dict",
)
