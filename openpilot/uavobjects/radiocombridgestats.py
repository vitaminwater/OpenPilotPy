##
##############################################################################
#
# @file       radiocombridgestats.py
# @author     The OpenPilot Team, http://www.openpilot.org Copyright (C) 2010.
# @brief      Implementation of the RadioComBridgeStats object. This file has been
#             automatically generated by the UAVObjectGenerator. For use with
#             the PyMite VM of the FlightPlan module.
#
# @note       Object definition file: radiocombridgestats.xml.
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

# Field TelemetryTxBytes definition
class TelemetryTxBytesField(UAVObjectField):
    def __init__(self):
    	UAVObjectField.__init__(self, 5, 1)

# Field TelemetryTxFailures definition
class TelemetryTxFailuresField(UAVObjectField):
    def __init__(self):
    	UAVObjectField.__init__(self, 5, 1)

# Field TelemetryTxRetries definition
class TelemetryTxRetriesField(UAVObjectField):
    def __init__(self):
    	UAVObjectField.__init__(self, 5, 1)

# Field TelemetryRxBytes definition
class TelemetryRxBytesField(UAVObjectField):
    def __init__(self):
    	UAVObjectField.__init__(self, 5, 1)

# Field TelemetryRxFailures definition
class TelemetryRxFailuresField(UAVObjectField):
    def __init__(self):
    	UAVObjectField.__init__(self, 5, 1)

# Field TelemetryRxSyncErrors definition
class TelemetryRxSyncErrorsField(UAVObjectField):
    def __init__(self):
    	UAVObjectField.__init__(self, 5, 1)

# Field TelemetryRxCrcErrors definition
class TelemetryRxCrcErrorsField(UAVObjectField):
    def __init__(self):
    	UAVObjectField.__init__(self, 5, 1)

# Field RadioTxBytes definition
class RadioTxBytesField(UAVObjectField):
    def __init__(self):
    	UAVObjectField.__init__(self, 5, 1)

# Field RadioTxFailures definition
class RadioTxFailuresField(UAVObjectField):
    def __init__(self):
    	UAVObjectField.__init__(self, 5, 1)

# Field RadioTxRetries definition
class RadioTxRetriesField(UAVObjectField):
    def __init__(self):
    	UAVObjectField.__init__(self, 5, 1)

# Field RadioRxBytes definition
class RadioRxBytesField(UAVObjectField):
    def __init__(self):
    	UAVObjectField.__init__(self, 5, 1)

# Field RadioRxFailures definition
class RadioRxFailuresField(UAVObjectField):
    def __init__(self):
    	UAVObjectField.__init__(self, 5, 1)

# Field RadioRxSyncErrors definition
class RadioRxSyncErrorsField(UAVObjectField):
    def __init__(self):
    	UAVObjectField.__init__(self, 5, 1)

# Field RadioRxCrcErrors definition
class RadioRxCrcErrorsField(UAVObjectField):
    def __init__(self):
    	UAVObjectField.__init__(self, 5, 1)



# Object RadioComBridgeStats definition
class RadioComBridgeStats(UAVObject):
    # Object constants
    OBJID = 614051416

    # Constructor
    def __init__(self):
        UAVObject.__init__(self, RadioComBridgeStats.OBJID)

        # Create object fields
    	self.TelemetryTxBytes = TelemetryTxBytesField()
    	self.addField(self.TelemetryTxBytes)
    	self.TelemetryTxFailures = TelemetryTxFailuresField()
    	self.addField(self.TelemetryTxFailures)
    	self.TelemetryTxRetries = TelemetryTxRetriesField()
    	self.addField(self.TelemetryTxRetries)
    	self.TelemetryRxBytes = TelemetryRxBytesField()
    	self.addField(self.TelemetryRxBytes)
    	self.TelemetryRxFailures = TelemetryRxFailuresField()
    	self.addField(self.TelemetryRxFailures)
    	self.TelemetryRxSyncErrors = TelemetryRxSyncErrorsField()
    	self.addField(self.TelemetryRxSyncErrors)
    	self.TelemetryRxCrcErrors = TelemetryRxCrcErrorsField()
    	self.addField(self.TelemetryRxCrcErrors)
    	self.RadioTxBytes = RadioTxBytesField()
    	self.addField(self.RadioTxBytes)
    	self.RadioTxFailures = RadioTxFailuresField()
    	self.addField(self.RadioTxFailures)
    	self.RadioTxRetries = RadioTxRetriesField()
    	self.addField(self.RadioTxRetries)
    	self.RadioRxBytes = RadioRxBytesField()
    	self.addField(self.RadioRxBytes)
    	self.RadioRxFailures = RadioRxFailuresField()
    	self.addField(self.RadioRxFailures)
    	self.RadioRxSyncErrors = RadioRxSyncErrorsField()
    	self.addField(self.RadioRxSyncErrors)
    	self.RadioRxCrcErrors = RadioRxCrcErrorsField()
    	self.addField(self.RadioRxCrcErrors)

        # Read field data
        self.read()
        self.metadata.read()
