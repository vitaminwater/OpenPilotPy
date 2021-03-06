##
##############################################################################
#
# @file       oplinksettings.py
# @author     The OpenPilot Team, http://www.openpilot.org Copyright (C) 2010.
# @brief      Implementation of the OPLinkSettings object. This file has been
#             automatically generated by the UAVObjectGenerator. For use with
#             the PyMite VM of the FlightPlan module.
#
# @note       Object definition file: oplinksettings.xml.
#             This is an automatically generated file.
#             DO NOT modify manually.
#
# @see        The GNU Public License (GPL) Version 3
#
#############################################################################/
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
# or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License
# for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
#

from openpilot.uavtalk.uavobject import *

# Field CoordID definition
class CoordIDField(UAVObjectField):
    def __init__(self):
    	UAVObjectField.__init__(self, 5, 1)

# Field Coordinator definition
class CoordinatorField(UAVObjectField):
    # Enumeration options
    FALSE = 0
    TRUE = 1
    def __init__(self):
    	UAVObjectField.__init__(self, 7, 1)

# Field OneWay definition
class OneWayField(UAVObjectField):
    # Enumeration options
    FALSE = 0
    TRUE = 1
    def __init__(self):
    	UAVObjectField.__init__(self, 7, 1)

# Field PPM definition
class PPMField(UAVObjectField):
    # Enumeration options
    FALSE = 0
    TRUE = 1
    def __init__(self):
    	UAVObjectField.__init__(self, 7, 1)

# Field PPMOnly definition
class PPMOnlyField(UAVObjectField):
    # Enumeration options
    FALSE = 0
    TRUE = 1
    def __init__(self):
    	UAVObjectField.__init__(self, 7, 1)

# Field MainPort definition
class MainPortField(UAVObjectField):
    # Enumeration options
    DISABLED = 0
    TELEMETRY = 1
    SERIAL = 2
    PPM = 3
    PWM = 4
    def __init__(self):
    	UAVObjectField.__init__(self, 7, 1)

# Field FlexiPort definition
class FlexiPortField(UAVObjectField):
    # Enumeration options
    DISABLED = 0
    TELEMETRY = 1
    SERIAL = 2
    PPM = 3
    PWM = 4
    def __init__(self):
    	UAVObjectField.__init__(self, 7, 1)

# Field VCPPort definition
class VCPPortField(UAVObjectField):
    # Enumeration options
    DISABLED = 0
    SERIAL = 1
    def __init__(self):
    	UAVObjectField.__init__(self, 7, 1)

# Field ComSpeed definition
class ComSpeedField(UAVObjectField):
    # Enumeration options
    N4800 = 0
    N9600 = 1
    N19200 = 2
    N38400 = 3
    N57600 = 4
    N115200 = 5
    def __init__(self):
    	UAVObjectField.__init__(self, 7, 1)

# Field MaxRFPower definition
class MaxRFPowerField(UAVObjectField):
    # Enumeration options
    N0 = 0
    N125 = 1
    N16 = 2
    N316 = 3
    N63 = 4
    N126 = 5
    N25 = 6
    N50 = 7
    N100 = 8
    def __init__(self):
    	UAVObjectField.__init__(self, 7, 1)

# Field MinChannel definition
class MinChannelField(UAVObjectField):
    def __init__(self):
    	UAVObjectField.__init__(self, 3, 1)

# Field MaxChannel definition
class MaxChannelField(UAVObjectField):
    def __init__(self):
    	UAVObjectField.__init__(self, 3, 1)



# Object OPLinkSettings definition
class OPLinkSettings(UAVObject):
    # Object constants
    OBJID = -2004486126

    # Constructor
    def __init__(self):
        UAVObject.__init__(self, OPLinkSettings.OBJID)

        # Create object fields
    	self.CoordID = CoordIDField()
    	self.addField(self.CoordID)
    	self.Coordinator = CoordinatorField()
    	self.addField(self.Coordinator)
    	self.OneWay = OneWayField()
    	self.addField(self.OneWay)
    	self.PPM = PPMField()
    	self.addField(self.PPM)
    	self.PPMOnly = PPMOnlyField()
    	self.addField(self.PPMOnly)
    	self.MainPort = MainPortField()
    	self.addField(self.MainPort)
    	self.FlexiPort = FlexiPortField()
    	self.addField(self.FlexiPort)
    	self.VCPPort = VCPPortField()
    	self.addField(self.VCPPort)
    	self.ComSpeed = ComSpeedField()
    	self.addField(self.ComSpeed)
    	self.MaxRFPower = MaxRFPowerField()
    	self.addField(self.MaxRFPower)
    	self.MinChannel = MinChannelField()
    	self.addField(self.MinChannel)
    	self.MaxChannel = MaxChannelField()
    	self.addField(self.MaxChannel)

        # Read field data
        self.read()
        self.metadata.read()
