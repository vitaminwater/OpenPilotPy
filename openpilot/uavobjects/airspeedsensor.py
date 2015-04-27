##
##############################################################################
#
# @file       airspeedsensor.py
# @author     The OpenPilot Team, http://www.openpilot.org Copyright (C) 2010.
# @brief      Implementation of the AirspeedSensor object. This file has been
#             automatically generated by the UAVObjectGenerator. For use with
#             the PyMite VM of the FlightPlan module.
#
# @note       Object definition file: airspeedsensor.xml.
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

# Field DifferentialPressure definition
class DifferentialPressureField(UAVObjectField):
    def __init__(self):
    	UAVObjectField.__init__(self, 6, 1)

# Field Temperature definition
class TemperatureField(UAVObjectField):
    def __init__(self):
    	UAVObjectField.__init__(self, 6, 1)

# Field CalibratedAirspeed definition
class CalibratedAirspeedField(UAVObjectField):
    def __init__(self):
    	UAVObjectField.__init__(self, 6, 1)

# Field TrueAirspeed definition
class TrueAirspeedField(UAVObjectField):
    def __init__(self):
    	UAVObjectField.__init__(self, 6, 1)

# Field SensorValue definition
class SensorValueField(UAVObjectField):
    def __init__(self):
    	UAVObjectField.__init__(self, 4, 1)

# Field SensorValueTemperature definition
class SensorValueTemperatureField(UAVObjectField):
    def __init__(self):
    	UAVObjectField.__init__(self, 4, 1)

# Field SensorConnected definition
class SensorConnectedField(UAVObjectField):
    # Enumeration options
    FALSE = 0
    TRUE = 1
    def __init__(self):
    	UAVObjectField.__init__(self, 7, 1)



# Object AirspeedSensor definition
class AirspeedSensor(UAVObject):
    # Object constants
    OBJID = 1133338522

    # Constructor
    def __init__(self):
        UAVObject.__init__(self, AirspeedSensor.OBJID)

        # Create object fields
    	self.DifferentialPressure = DifferentialPressureField()
    	self.addField(self.DifferentialPressure)
    	self.Temperature = TemperatureField()
    	self.addField(self.Temperature)
    	self.CalibratedAirspeed = CalibratedAirspeedField()
    	self.addField(self.CalibratedAirspeed)
    	self.TrueAirspeed = TrueAirspeedField()
    	self.addField(self.TrueAirspeed)
    	self.SensorValue = SensorValueField()
    	self.addField(self.SensorValue)
    	self.SensorValueTemperature = SensorValueTemperatureField()
    	self.addField(self.SensorValueTemperature)
    	self.SensorConnected = SensorConnectedField()
    	self.addField(self.SensorConnected)

        # Read field data
        self.read()
        self.metadata.read()
