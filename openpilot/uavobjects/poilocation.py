##
##############################################################################
#
# @file       poilocation.py
# @author     The OpenPilot Team, http://www.openpilot.org Copyright (C) 2010.
# @brief      Implementation of the PoiLocation object. This file has been
#             automatically generated by the UAVObjectGenerator. For use with
#             the PyMite VM of the FlightPlan module.
#
# @note       Object definition file: poilocation.xml.
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

# Field North definition
class NorthField(UAVObjectField):
    def __init__(self):
    	UAVObjectField.__init__(self, 6, 1)

# Field East definition
class EastField(UAVObjectField):
    def __init__(self):
    	UAVObjectField.__init__(self, 6, 1)

# Field Down definition
class DownField(UAVObjectField):
    def __init__(self):
    	UAVObjectField.__init__(self, 6, 1)



# Object PoiLocation definition
class PoiLocation(UAVObject):
    # Object constants
    OBJID = 401091000

    # Constructor
    def __init__(self):
        UAVObject.__init__(self, PoiLocation.OBJID)

        # Create object fields
    	self.North = NorthField()
    	self.addField(self.North)
    	self.East = EastField()
    	self.addField(self.East)
    	self.Down = DownField()
    	self.addField(self.Down)

        # Read field data
        self.read()
        self.metadata.read()
