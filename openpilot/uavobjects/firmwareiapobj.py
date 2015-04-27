##
##############################################################################
#
# @file       firmwareiapobj.py
# @author     The OpenPilot Team, http://www.openpilot.org Copyright (C) 2010.
# @brief      Implementation of the FirmwareIAPObj object. This file has been
#             automatically generated by the UAVObjectGenerator. For use with
#             the PyMite VM of the FlightPlan module.
#
# @note       Object definition file: firmwareiapobj.xml.
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

# Field crc definition
class crcField(UAVObjectField):
    def __init__(self):
    	UAVObjectField.__init__(self, 5, 1)

# Field Command definition
class CommandField(UAVObjectField):
    def __init__(self):
    	UAVObjectField.__init__(self, 4, 1)

# Field BoardRevision definition
class BoardRevisionField(UAVObjectField):
    def __init__(self):
    	UAVObjectField.__init__(self, 4, 1)

# Field Description definition
class DescriptionField(UAVObjectField):
    def __init__(self):
    	UAVObjectField.__init__(self, 3, 100)

# Field CPUSerial definition
class CPUSerialField(UAVObjectField):
    def __init__(self):
    	UAVObjectField.__init__(self, 3, 12)

# Field BoardType definition
class BoardTypeField(UAVObjectField):
    def __init__(self):
    	UAVObjectField.__init__(self, 3, 1)

# Field BootloaderRevision definition
class BootloaderRevisionField(UAVObjectField):
    def __init__(self):
    	UAVObjectField.__init__(self, 3, 1)

# Field ArmReset definition
class ArmResetField(UAVObjectField):
    def __init__(self):
    	UAVObjectField.__init__(self, 3, 1)



# Object FirmwareIAPObj definition
class FirmwareIAPObj(UAVObject):
    # Object constants
    OBJID = -2094468526

    # Constructor
    def __init__(self):
        UAVObject.__init__(self, FirmwareIAPObj.OBJID)

        # Create object fields
    	self.crc = crcField()
    	self.addField(self.crc)
    	self.Command = CommandField()
    	self.addField(self.Command)
    	self.BoardRevision = BoardRevisionField()
    	self.addField(self.BoardRevision)
    	self.Description = DescriptionField()
    	self.addField(self.Description)
    	self.CPUSerial = CPUSerialField()
    	self.addField(self.CPUSerial)
    	self.BoardType = BoardTypeField()
    	self.addField(self.BoardType)
    	self.BootloaderRevision = BootloaderRevisionField()
    	self.addField(self.BootloaderRevision)
    	self.ArmReset = ArmResetField()
    	self.addField(self.ArmReset)

        # Read field data
        self.read()
        self.metadata.read()