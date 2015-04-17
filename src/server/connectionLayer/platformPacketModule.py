#!/usr/bin/python
#----------------------------------------------------------------------#

## IMPORTS ##
import os
import sys

### PANDA Imports ###
# from pandac.PandaModules import *
from panda3d.core import Datagram
from panda3d.core import DatagramIterator
from direct.task.Task import Task

## Server Imports ##
from opcodes import *

########################################################################
# The Connection Manager should handle reliable stuff with some custom udp /tcp mix,
# but for now it will handle/use basic tcp stuff


class PlatformPacketModule():
    
    def __init__(self, _connectionManager):
    	print "Loaded Platform Packet Module"

    	# ConnectionManager ref
    	self.connectionManager = _connectionManager


        # TCP Listener Task
    def tcpListenerTask(self, task):
        """
        Accept new incoming connection from clients, related to TCP
        """
        # Handle new connection
        if self.connectionManager.tcpListener.newConnectionAvailable():
        	rendezvous = PointerToConnection()
        	netAddress = NetAddress()
        	newConnection = PointerToConnection()

	        if self.connectionManager.tcpListener.getNewConnection(rendezvous, netAddress, newConnection):
	            newConnection = newConnection.p()
	            self.connectionManager.tcpReader.addConnection(newConnection)
	            self.connectionManager.activeConnections.append(newConnection)
	            
	            print "Server: New Connection from -", str(netAddress.getIpString())
	        else:
	            print "Server: Connection Failed from -", str(netAddress.getIpString())

        return Task.cont


    # TCP Reader Task
    def tcpReaderTask(self, task):
        """
        Handle any data from clients by sending it to the Handlers.
        """
        while 1:
            (datagram, data, opcode, managerCode) = self.tcpNonBlockingRead(self.connectionManager.tcpReader)
            if opcode is MSG_NONE:
                # Do nothing or use it as some 'keep_alive' thing.
                break 
            else:
                # Handle it
                self.connectionManager.passPacketToStreamMgr(data, opcode, managerCode, datagram.getConnection(), datagram.getLength())
                
        return Task.cont


    # TCP NonBlockingRead
    def tcpNonBlockingRead(self, qcr):
        """
        Return a datagram collection and type if data is available on
        the queued connection tcpReader
        
        @param qcr: self.tcpReader
        """
        if self.connectionManager.tcpReader.dataAvailable():
            datagram = NetDatagram()
            if self.connectionManager.tcpReader.getData(datagram):
                data = DatagramIterator(datagram)
                opcode = data.getUint8()
                managerCode = data.getUint8()
                
            else:
                data = None
                opcode = MSG_NONE
                managerCode = None
            
        else:
            datagram = None
            data = None
            opcode = MSG_NONE
            managerCode = None
            
        # Return the datagram to keep a handle on the data
        return (datagram, data, opcode, managerCode)

