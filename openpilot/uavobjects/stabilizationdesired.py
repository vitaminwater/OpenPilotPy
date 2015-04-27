##
##############################################################################
#
# @file       stabilizationdesired.py
# @author     The OpenPilot Team, http://www.openpilot.org Copyright (C) 2010.
# @brief      Implementation of the StabilizationDesired object. This file has been
#             automatically generated by the UAVObjectGenerator. For use with
#             the PyMite VM of the FlightPlan module.
#
# @note       Object definition file: stabilizationdesired.xml.
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

# Field Roll definition
class RollField(UAVObjectField):
    def __init__(self):
    	UAVObjectField.__init__(self, 6, 1)

# Field Pitch definition
class PitchField(UAVObjectField):
    def __init__(self):
    	UAVObjectField.__init__(self, 6, 1)

# Field Yaw definition
class YawField(UAVObjectField):
    def __init__(self):
    	UAVObjectField.__init__(self, 6, 1)

# Field Thrust definition
class ThrustField(UAVObjectField):
    def __init__(self):
    	UAVObjectField.__init__(self, 6, 1)

# Field StabilizationMode definition
class StabilizationModeField(UAVObjectField):
    # Enumeration options
    MANUAL = 0
    RATE = 1
    ATTITUDE = 2
    AXISLOCK = 3
    WEAKLEVELING = 4
    VIRTUALBAR = 5
    ACRO = 6
    RATTITUDE = 7
    ALTITUDEHOLD = 8
    ALTITUDEVARIO = 9
    CRUISECONTROL = 10
    # Array element names
    ROLL = 0
    PITCH = 1
    YAW = 2
    THRUST = 3
    def __init__(self):
    	UAVObjectField.__init__(self, 7, 4)



# Object StabilizationDesired definition
class StabilizationDesired(UAVObject):
    # Object constants
    OBJID = -1976957908

    # Constructor
    def __init__(self):
        UAVObject.__init__(self, StabilizationDesired.OBJID)

        # Create object fields
    	self.Roll = RollField()
    	self.addField(self.Roll)
    	self.Pitch = PitchField()
    	self.addField(self.Pitch)
    	self.Yaw = YawField()
    	self.addField(self.Yaw)
    	self.Thrust = ThrustField()
    	self.addField(self.Thrust)
    	self.StabilizationMode = StabilizationModeField()
    	self.addField(self.StabilizationMode)

        # Read field data
        self.read()
        self.metadata.read()
