##
##############################################################################
#
# @file       connectionManager.py
# @author     The OpenPilot Team, http://www.openpilot.org Copyright (C) 2011.
# @brief      Base classes for python UAVObject
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



import logging
import serial
import sys

import objectManager
import uavobject
import time

class ConnectionTimeoutException(Exception): 
    pass 
    
    
class ConnectionManager(object):
    
    def __init__(self, uavTalk, objMan):
        self.uavTalk = uavTalk
        self.objMan = objMan
        self.connected = False
        
        
        
        self.ftsObj = self.objMan.FlightTelemetryStats
        self.gcsObj = self.objMan.GCSTelemetryStats
        
        import flighttelemetrystats
        self.statusFieldClss = flighttelemetrystats.StatusField
        
    def requestObjUpdate(self, obj, requestor=None):
        logging.debug("Requesting %s" % obj)
        self.uavTalk.sendObjReq(obj)
    
    def waitObjUpdate(self, obj, request=True, timeout=.5):
        logging.debug("Waiting for %s " % obj)
        cnt = obj.updateCnt
        if request:
            self.requestObjUpdate(obj)
        obj.updateEvent.acquire()
        obj.updateEvent.wait(timeout)
        obj.updateEvent.release()
        timeout = (cnt == obj.updateCnt)
        logging.debug("-> Waiting for %s Done. " % (obj))
        if timeout:
            s = "Timeout waiting for %s" % obj
            logging.debug(s)
            raise ConnectionTimeoutException(s)
            
    def requestAllObjUpdate(self):
        for objId, obj in self.objs.items():
            if not obj.isMetaData():
                #print "GetMeta %s" % obj
                try:
                    logging.debug("Getting %s" % obj)
                    self.waitObjUpdate(obj, request=True, timeout=.1)
                    logging.debug("  Getting %s" % obj.metadata)
                    self.waitObjUpdate(obj.metadata, request=True, timeout=.1)
                except ConnectionTimeoutException:
                    logging.debug("  TIMEOUT")
                    pass
                    
    def disableAllAutomaticUpdates(self):
        objsToExclude = [self.getObjByName("GCSTelemetryStats"), self.getObjByName("FlightTelemetryStats"), self.getObjByName("ObjectPersistence")]
        for i in xrange(len(objsToExclude)):
            objsToExclude[i] = objsToExclude[i].metadata.objId
            
        for objId, obj in self.objs.items():
            if obj.isMetaData() and obj.updateCnt>0:
                if obj.objId not in objsToExclude:
                    #print "Disabling automatic updates for %s" % (obj)
                    #print obj.telemetryUpdateMode.value
                    obj.telemetryUpdateMode.value = UAVMetaDataObject.UpdateMode.MANUAL
                    self.uavTalk.sendObject(obj)
                    
    def objLocallyUpdated(self, obj):
        # TODO: should check meta-data what to do
        self.uavTalk.sendObject(obj)
        raise
        
    def connect(self):
        timeout = True
        logging.debug("Connecting")
        startTime = time.clock()
        while not self.connected:
            try:
                self.waitObjUpdate(self.ftsObj.metadata, request=timeout, timeout=5)
                timeout = False
                self._onFtsChange()
                if self.connected:
                    self.waitObjUpdate(self.ftsObj.metadata)
                    self.ftsObj.metadata.telemetryUpdateMode.value = uavobject.UAVMetaDataObject.UpdateMode.PERIODIC
                    self.ftsObj.metadata.telemetryUpdatePeriod.value = 1000
                    self.ftsObj.metadata.updated()
                    raise
                    self.regObjectObserver(self.ftsObj, self, "_onFtsChange")
                else:
                    pass
            except ConnectionTimeoutException:
                timeout = True
                self.connected = False
                logging.warning("Connecting TO")
                pass
        logging.debug("Connected in %.1fs" % (time.clock()-startTime))   
        
    def _onFtsChange(self, args=None):
        connected = False
        logging.debug("FTS State=%d TxFail=%3d RxFail=%3d TxRetry=%3d" % \
                     (self.ftsObj.Status.value, self.ftsObj.TxFailures.value, self.ftsObj.RxFailures.value, self.ftsObj.TxRetries.value))
        
        if self.ftsObj.Status.value == self.statusFieldClss.DISCONNECTED:  
            logging.debug(" Handshake REQ")
            self.gcsObj.Status.value = self.statusFieldClss.HANDSHAKEREQ
            self.gcsObj.updated()
            
        elif self.ftsObj.Status.value == self.statusFieldClss.HANDSHAKEACK:
            logging.debug(" Got Handshake ACK")
            self.gcsObj.Status.value = self.statusFieldClss.CONNECTED
            self.gcsObj.updated()
        
        elif self.ftsObj.Status.value == self.statusFieldClss.CONNECTED:
            connected = True
            
        if self.connected:
            if not connected:
                logging.warning("DISCONNECTED")
        else:
            if connected:
                logging.debug("CONNECTED")
        
        self.connected = connected
