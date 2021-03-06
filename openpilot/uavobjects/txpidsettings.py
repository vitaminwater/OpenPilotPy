##
##############################################################################
#
# @file       txpidsettings.py
# @author     The OpenPilot Team, http://www.openpilot.org Copyright (C) 2010.
# @brief      Implementation of the TxPIDSettings object. This file has been
#             automatically generated by the UAVObjectGenerator. For use with
#             the PyMite VM of the FlightPlan module.
#
# @note       Object definition file: txpidsettings.xml.
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

# Field ThrottleRange definition
class ThrottleRangeField(UAVObjectField):
    # Array element names
    MIN = 0
    MAX = 1
    def __init__(self):
    	UAVObjectField.__init__(self, 6, 2)

# Field MinPID definition
class MinPIDField(UAVObjectField):
    # Array element names
    INSTANCE1 = 0
    INSTANCE2 = 1
    INSTANCE3 = 2
    def __init__(self):
    	UAVObjectField.__init__(self, 6, 3)

# Field MaxPID definition
class MaxPIDField(UAVObjectField):
    # Array element names
    INSTANCE1 = 0
    INSTANCE2 = 1
    INSTANCE3 = 2
    def __init__(self):
    	UAVObjectField.__init__(self, 6, 3)

# Field UpdateMode definition
class UpdateModeField(UAVObjectField):
    # Enumeration options
    NEVER = 0
    WHENARMED = 1
    ALWAYS = 2
    def __init__(self):
    	UAVObjectField.__init__(self, 7, 1)

# Field BankNumber definition
class BankNumberField(UAVObjectField):
    # Enumeration options
    BANK1 = 0
    BANK2 = 1
    BANK3 = 2
    def __init__(self):
    	UAVObjectField.__init__(self, 7, 1)

# Field Inputs definition
class InputsField(UAVObjectField):
    # Enumeration options
    THROTTLE = 0
    ACCESSORY0 = 1
    ACCESSORY1 = 2
    ACCESSORY2 = 3
    ACCESSORY3 = 4
    ACCESSORY4 = 5
    ACCESSORY5 = 6
    # Array element names
    INSTANCE1 = 0
    INSTANCE2 = 1
    INSTANCE3 = 2
    def __init__(self):
    	UAVObjectField.__init__(self, 7, 3)

# Field PIDs definition
class PIDsField(UAVObjectField):
    # Enumeration options
    DISABLED = 0
    ROLLRATEKP = 1
    ROLLRATEKI = 2
    ROLLRATEKD = 3
    ROLLRATEILIMIT = 4
    ROLLRATERESP = 5
    PITCHRATEKP = 6
    PITCHRATEKI = 7
    PITCHRATEKD = 8
    PITCHRATEILIMIT = 9
    PITCHRATERESP = 10
    ROLLPITCHRATEKP = 11
    ROLLPITCHRATEKI = 12
    ROLLPITCHRATEKD = 13
    ROLLPITCHRATEILIMIT = 14
    ROLLPITCHRATERESP = 15
    YAWRATEKP = 16
    YAWRATEKI = 17
    YAWRATEKD = 18
    YAWRATEILIMIT = 19
    YAWRATERESP = 20
    ROLLATTITUDEKP = 21
    ROLLATTITUDEKI = 22
    ROLLATTITUDEILIMIT = 23
    ROLLATTITUDERESP = 24
    PITCHATTITUDEKP = 25
    PITCHATTITUDEKI = 26
    PITCHATTITUDEILIMIT = 27
    PITCHATTITUDERESP = 28
    ROLLPITCHATTITUDEKP = 29
    ROLLPITCHATTITUDEKI = 30
    ROLLPITCHATTITUDEILIMIT = 31
    ROLLPITCHATTITUDERESP = 32
    YAWATTITUDEKP = 33
    YAWATTITUDEKI = 34
    YAWATTITUDEILIMIT = 35
    YAWATTITUDERESP = 36
    ROLLEXPO = 37
    PITCHEXPO = 38
    ROLLPITCHEXPO = 39
    YAWEXPO = 40
    GYROTAU = 41
    ACROPLUSFACTOR = 42
    # Array element names
    INSTANCE1 = 0
    INSTANCE2 = 1
    INSTANCE3 = 2
    def __init__(self):
    	UAVObjectField.__init__(self, 7, 3)



# Object TxPIDSettings definition
class TxPIDSettings(UAVObject):
    # Object constants
    OBJID = -2055515662

    # Constructor
    def __init__(self):
        UAVObject.__init__(self, TxPIDSettings.OBJID)

        # Create object fields
    	self.ThrottleRange = ThrottleRangeField()
    	self.addField(self.ThrottleRange)
    	self.MinPID = MinPIDField()
    	self.addField(self.MinPID)
    	self.MaxPID = MaxPIDField()
    	self.addField(self.MaxPID)
    	self.UpdateMode = UpdateModeField()
    	self.addField(self.UpdateMode)
    	self.BankNumber = BankNumberField()
    	self.addField(self.BankNumber)
    	self.Inputs = InputsField()
    	self.addField(self.Inputs)
    	self.PIDs = PIDsField()
    	self.addField(self.PIDs)

        # Read field data
        self.read()
        self.metadata.read()
