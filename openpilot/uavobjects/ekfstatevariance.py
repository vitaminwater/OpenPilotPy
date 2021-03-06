##
##############################################################################
#
# @file       ekfstatevariance.py
# @author     The OpenPilot Team, http://www.openpilot.org Copyright (C) 2010.
# @brief      Implementation of the EKFStateVariance object. This file has been
#             automatically generated by the UAVObjectGenerator. For use with
#             the PyMite VM of the FlightPlan module.
#
# @note       Object definition file: ekfstatevariance.xml.
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

# Field P definition
class PField(UAVObjectField):
    # Array element names
    POSITIONNORTH = 0
    POSITIONEAST = 1
    POSITIONDOWN = 2
    VELOCITYNORTH = 3
    VELOCITYEAST = 4
    VELOCITYDOWN = 5
    ATTITUDEQ1 = 6
    ATTITUDEQ2 = 7
    ATTITUDEQ3 = 8
    ATTITUDEQ4 = 9
    GYRODRIFTX = 10
    GYRODRIFTY = 11
    GYRODRIFTZ = 12
    def __init__(self):
    	UAVObjectField.__init__(self, 6, 13)



# Object EKFStateVariance definition
class EKFStateVariance(UAVObject):
    # Object constants
    OBJID = 515081700

    # Constructor
    def __init__(self):
        UAVObject.__init__(self, EKFStateVariance.OBJID)

        # Create object fields
    	self.P = PField()
    	self.addField(self.P)

        # Read field data
        self.read()
        self.metadata.read()
