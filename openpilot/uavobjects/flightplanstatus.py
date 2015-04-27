##
##############################################################################
#
# @file       flightplanstatus.py
# @author     The OpenPilot Team, http://www.openpilot.org Copyright (C) 2010.
# @brief      Implementation of the FlightPlanStatus object. This file has been
#             automatically generated by the UAVObjectGenerator. For use with
#             the PyMite VM of the FlightPlan module.
#
# @note       Object definition file: flightplanstatus.xml.
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

# Field ErrorFileID definition
class ErrorFileIDField(UAVObjectField):
    def __init__(self):
    	UAVObjectField.__init__(self, 5, 1)

# Field ErrorLineNum definition
class ErrorLineNumField(UAVObjectField):
    def __init__(self):
    	UAVObjectField.__init__(self, 5, 1)

# Field Debug definition
class DebugField(UAVObjectField):
    def __init__(self):
    	UAVObjectField.__init__(self, 6, 2)

# Field Status definition
class StatusField(UAVObjectField):
    # Enumeration options
    STOPPED = 0
    RUNNING = 1
    ERROR = 2
    def __init__(self):
    	UAVObjectField.__init__(self, 7, 1)

# Field ErrorType definition
class ErrorTypeField(UAVObjectField):
    # Enumeration options
    NONE = 0
    VMINITERROR = 1
    EXCEPTION = 2
    IOERROR = 3
    DIVBYZERO = 4
    ASSERTERROR = 5
    ATTRIBUTEERROR = 6
    IMPORTERROR = 7
    INDEXERROR = 8
    KEYERROR = 9
    MEMORYERROR = 10
    NAMEERROR = 11
    SYNTAXERROR = 12
    SYSTEMERROR = 13
    TYPEERROR = 14
    VALUEERROR = 15
    STOPITERATION = 16
    WARNING = 17
    UNKNOWNERROR = 18
    def __init__(self):
    	UAVObjectField.__init__(self, 7, 1)



# Object FlightPlanStatus definition
class FlightPlanStatus(UAVObject):
    # Object constants
    OBJID = 570879558

    # Constructor
    def __init__(self):
        UAVObject.__init__(self, FlightPlanStatus.OBJID)

        # Create object fields
    	self.ErrorFileID = ErrorFileIDField()
    	self.addField(self.ErrorFileID)
    	self.ErrorLineNum = ErrorLineNumField()
    	self.addField(self.ErrorLineNum)
    	self.Debug = DebugField()
    	self.addField(self.Debug)
    	self.Status = StatusField()
    	self.addField(self.Status)
    	self.ErrorType = ErrorTypeField()
    	self.addField(self.ErrorType)

        # Read field data
        self.read()
        self.metadata.read()
