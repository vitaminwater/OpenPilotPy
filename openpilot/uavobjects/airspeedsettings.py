##
##############################################################################
#
# @file       airspeedsettings.py
# @author     The OpenPilot Team, http://www.openpilot.org Copyright (C) 2010.
# @brief      Implementation of the AirspeedSettings object. This file has been
#             automatically generated by the UAVObjectGenerator. For use with
#             the PyMite VM of the FlightPlan module.
#
# @note       Object definition file: airspeedsettings.xml.
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

# Field Scale definition
class ScaleField(UAVObjectField):
    def __init__(self):
    	UAVObjectField.__init__(self, 6, 1)

# Field IMUBasedEstimationLowPassPeriod1 definition
class IMUBasedEstimationLowPassPeriod1Field(UAVObjectField):
    def __init__(self):
    	UAVObjectField.__init__(self, 6, 1)

# Field IMUBasedEstimationLowPassPeriod2 definition
class IMUBasedEstimationLowPassPeriod2Field(UAVObjectField):
    def __init__(self):
    	UAVObjectField.__init__(self, 6, 1)

# Field ZeroPoint definition
class ZeroPointField(UAVObjectField):
    def __init__(self):
    	UAVObjectField.__init__(self, 4, 1)

# Field SamplePeriod definition
class SamplePeriodField(UAVObjectField):
    def __init__(self):
    	UAVObjectField.__init__(self, 3, 1)

# Field AirspeedSensorType definition
class AirspeedSensorTypeField(UAVObjectField):
    # Enumeration options
    PIXHAWKAIRSPEEDMS4525DO = 0
    EAGLETREEAIRSPEEDV3 = 1
    DIYDRONESMPXV5004 = 2
    DIYDRONESMPXV7002 = 3
    GROUNDSPEEDBASEDWINDESTIMATION = 4
    NONE = 5
    def __init__(self):
    	UAVObjectField.__init__(self, 7, 1)



# Object AirspeedSettings definition
class AirspeedSettings(UAVObject):
    # Object constants
    OBJID = 1777642874

    # Constructor
    def __init__(self):
        UAVObject.__init__(self, AirspeedSettings.OBJID)

        # Create object fields
    	self.Scale = ScaleField()
    	self.addField(self.Scale)
    	self.IMUBasedEstimationLowPassPeriod1 = IMUBasedEstimationLowPassPeriod1Field()
    	self.addField(self.IMUBasedEstimationLowPassPeriod1)
    	self.IMUBasedEstimationLowPassPeriod2 = IMUBasedEstimationLowPassPeriod2Field()
    	self.addField(self.IMUBasedEstimationLowPassPeriod2)
    	self.ZeroPoint = ZeroPointField()
    	self.addField(self.ZeroPoint)
    	self.SamplePeriod = SamplePeriodField()
    	self.addField(self.SamplePeriod)
    	self.AirspeedSensorType = AirspeedSensorTypeField()
    	self.addField(self.AirspeedSensorType)

        # Read field data
        self.read()
        self.metadata.read()
