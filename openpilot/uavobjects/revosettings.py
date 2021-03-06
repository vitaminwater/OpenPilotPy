##
##############################################################################
#
# @file       revosettings.py
# @author     The OpenPilot Team, http://www.openpilot.org Copyright (C) 2010.
# @brief      Implementation of the RevoSettings object. This file has been
#             automatically generated by the UAVObjectGenerator. For use with
#             the PyMite VM of the FlightPlan module.
#
# @note       Object definition file: revosettings.xml.
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

# Field BaroGPSOffsetCorrectionAlpha definition
class BaroGPSOffsetCorrectionAlphaField(UAVObjectField):
    def __init__(self):
    	UAVObjectField.__init__(self, 6, 1)

# Field MagnetometerMaxDeviation definition
class MagnetometerMaxDeviationField(UAVObjectField):
    # Array element names
    WARNING = 0
    ERROR = 1
    def __init__(self):
    	UAVObjectField.__init__(self, 6, 2)

# Field BaroTempCorrectionPolynomial definition
class BaroTempCorrectionPolynomialField(UAVObjectField):
    # Array element names
    A = 0
    B = 1
    C = 2
    D = 3
    def __init__(self):
    	UAVObjectField.__init__(self, 6, 4)

# Field BaroTempCorrectionExtent definition
class BaroTempCorrectionExtentField(UAVObjectField):
    # Array element names
    MIN = 0
    MAX = 1
    def __init__(self):
    	UAVObjectField.__init__(self, 6, 2)

# Field VelocityPostProcessingLowPassAlpha definition
class VelocityPostProcessingLowPassAlphaField(UAVObjectField):
    def __init__(self):
    	UAVObjectField.__init__(self, 6, 1)

# Field FusionAlgorithm definition
class FusionAlgorithmField(UAVObjectField):
    # Enumeration options
    NONE = 0
    BASICCOMPLEMENTARY = 1
    COMPLEMENTARYMAG = 2
    COMPLEMENTARYMAGGPSOUTDOOR = 3
    INS13INDOOR = 4
    GPSNAVIGATIONINS13 = 5
    def __init__(self):
    	UAVObjectField.__init__(self, 7, 1)



# Object RevoSettings definition
class RevoSettings(UAVObject):
    # Object constants
    OBJID = -1000936550

    # Constructor
    def __init__(self):
        UAVObject.__init__(self, RevoSettings.OBJID)

        # Create object fields
    	self.BaroGPSOffsetCorrectionAlpha = BaroGPSOffsetCorrectionAlphaField()
    	self.addField(self.BaroGPSOffsetCorrectionAlpha)
    	self.MagnetometerMaxDeviation = MagnetometerMaxDeviationField()
    	self.addField(self.MagnetometerMaxDeviation)
    	self.BaroTempCorrectionPolynomial = BaroTempCorrectionPolynomialField()
    	self.addField(self.BaroTempCorrectionPolynomial)
    	self.BaroTempCorrectionExtent = BaroTempCorrectionExtentField()
    	self.addField(self.BaroTempCorrectionExtent)
    	self.VelocityPostProcessingLowPassAlpha = VelocityPostProcessingLowPassAlphaField()
    	self.addField(self.VelocityPostProcessingLowPassAlpha)
    	self.FusionAlgorithm = FusionAlgorithmField()
    	self.addField(self.FusionAlgorithm)

        # Read field data
        self.read()
        self.metadata.read()
