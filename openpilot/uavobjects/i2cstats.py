##
##############################################################################
#
# @file       i2cstats.py
# @author     The OpenPilot Team, http://www.openpilot.org Copyright (C) 2010.
# @brief      Implementation of the I2CStats object. This file has been
#             automatically generated by the UAVObjectGenerator. For use with
#             the PyMite VM of the FlightPlan module.
#
# @note       Object definition file: i2cstats.xml.
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

# Field evirq_log definition
class evirq_logField(UAVObjectField):
    def __init__(self):
    	UAVObjectField.__init__(self, 5, 5)

# Field erirq_log definition
class erirq_logField(UAVObjectField):
    def __init__(self):
    	UAVObjectField.__init__(self, 5, 5)

# Field event_errors definition
class event_errorsField(UAVObjectField):
    def __init__(self):
    	UAVObjectField.__init__(self, 3, 1)

# Field fsm_errors definition
class fsm_errorsField(UAVObjectField):
    def __init__(self):
    	UAVObjectField.__init__(self, 3, 1)

# Field irq_errors definition
class irq_errorsField(UAVObjectField):
    def __init__(self):
    	UAVObjectField.__init__(self, 3, 1)

# Field nacks definition
class nacksField(UAVObjectField):
    def __init__(self):
    	UAVObjectField.__init__(self, 3, 1)

# Field timeouts definition
class timeoutsField(UAVObjectField):
    def __init__(self):
    	UAVObjectField.__init__(self, 3, 1)

# Field last_error_type definition
class last_error_typeField(UAVObjectField):
    # Enumeration options
    EVENT = 0
    FSM = 1
    INTERRUPT = 2
    def __init__(self):
    	UAVObjectField.__init__(self, 7, 1)

# Field event_log definition
class event_logField(UAVObjectField):
    # Enumeration options
    I2C_EVENT_BUS_ERROR = 0
    I2C_EVENT_START = 1
    I2C_EVENT_STARTED_MORE_TXN_READ = 2
    I2C_EVENT_STARTED_MORE_TXN_WRITE = 3
    I2C_EVENT_STARTED_LAST_TXN_READ = 4
    I2C_EVENT_STARTED_LAST_TXN_WRITE = 5
    I2C_EVENT_ADDR_SENT_LEN_EQ_0 = 6
    I2C_EVENT_ADDR_SENT_LEN_EQ_1 = 7
    I2C_EVENT_ADDR_SENT_LEN_EQ_2 = 8
    I2C_EVENT_ADDR_SENT_LEN_GT_2 = 9
    I2C_EVENT_TRANSFER_DONE_LEN_EQ_0 = 10
    I2C_EVENT_TRANSFER_DONE_LEN_EQ_1 = 11
    I2C_EVENT_TRANSFER_DONE_LEN_EQ_2 = 12
    I2C_EVENT_TRANSFER_DONE_LEN_GT_2 = 13
    I2C_EVENT_NACK = 14
    I2C_EVENT_STOPPED = 15
    I2C_EVENT_AUTO = 16
    def __init__(self):
    	UAVObjectField.__init__(self, 7, 5)

# Field state_log definition
class state_logField(UAVObjectField):
    # Enumeration options
    I2C_STATE_FSM_FAULT = 0
    I2C_STATE_BUS_ERROR = 1
    I2C_STATE_STOPPED = 2
    I2C_STATE_STOPPING = 3
    I2C_STATE_STARTING = 4
    I2C_STATE_R_MORE_TXN_ADDR = 5
    I2C_STATE_R_MORE_TXN_PRE_ONE = 6
    I2C_STATE_R_MORE_TXN_PRE_FIRST = 7
    I2C_STATE_R_MORE_TXN_PRE_MIDDLE = 8
    I2C_STATE_R_MORE_TXN_LAST = 9
    I2C_STATE_R_MORE_TXN_POST_LAST = 10
    R_LAST_TXN_ADDR = 11
    I2C_STATE_R_LAST_TXN_PRE_ONE = 12
    I2C_STATE_R_LAST_TXN_PRE_FIRST = 13
    I2C_STATE_R_LAST_TXN_PRE_MIDDLE = 14
    I2C_STATE_R_LAST_TXN_PRE_LAST = 15
    I2C_STATE_R_LAST_TXN_POST_LAST = 16
    I2C_STATE_W_MORE_TXN_ADDR = 17
    I2C_STATE_W_MORE_TXN_MIDDLE = 18
    I2C_STATE_W_MORE_TXN_LAST = 19
    I2C_STATE_W_LAST_TXN_ADDR = 20
    I2C_STATE_W_LAST_TXN_MIDDLE = 21
    I2C_STATE_W_LAST_TXN_LAST = 22
    I2C_STATE_NACK = 23
    def __init__(self):
    	UAVObjectField.__init__(self, 7, 5)



# Object I2CStats definition
class I2CStats(UAVObject):
    # Object constants
    OBJID = -1223392706

    # Constructor
    def __init__(self):
        UAVObject.__init__(self, I2CStats.OBJID)

        # Create object fields
    	self.evirq_log = evirq_logField()
    	self.addField(self.evirq_log)
    	self.erirq_log = erirq_logField()
    	self.addField(self.erirq_log)
    	self.event_errors = event_errorsField()
    	self.addField(self.event_errors)
    	self.fsm_errors = fsm_errorsField()
    	self.addField(self.fsm_errors)
    	self.irq_errors = irq_errorsField()
    	self.addField(self.irq_errors)
    	self.nacks = nacksField()
    	self.addField(self.nacks)
    	self.timeouts = timeoutsField()
    	self.addField(self.timeouts)
    	self.last_error_type = last_error_typeField()
    	self.addField(self.last_error_type)
    	self.event_log = event_logField()
    	self.addField(self.event_log)
    	self.state_log = state_logField()
    	self.addField(self.state_log)

        # Read field data
        self.read()
        self.metadata.read()