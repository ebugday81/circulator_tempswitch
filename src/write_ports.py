import ctypes
from ctypes import *
import time, os
import sys
import random

#####
#####
# Sample for IO-Port communication based on IO-Warrior40
#####
#####

# Available Pipes
IOW_PIPE_IO_PINS = ctypes.c_ulong(0)
IOW_PIPE_SPECIAL_MODE = ctypes.c_ulong(1)

# Product IDs
IOWKIT_PRODUCT_ID_IOW40 = 0x1500
IOWKIT_PRODUCT_ID_IOW24 = 0x1501
IOWKIT_PRODUCT_ID_IOW56 = 0x1503

# Defines
IOWKIT_MAX_PIPES = ctypes.c_ulong(2)
IOWKIT_MAX_DEVICES = ctypes.c_ulong(16)

# Count of BYTES 
IOWKIT24_IO_REPORT = ctypes.c_ubyte * 3
IOWKIT40_IO_REPORT = ctypes.c_ubyte * 5
IOWKIT_SPECIAL_REPORT = ctypes.c_ubyte * 9

IOWKIT56_IO_REPORT = ctypes.c_ubyte * 9
IOWKIT56_SPECIAL_REPORT = ctypes.c_ubyte * 64

SERIAL_NUMBER_BUFFER = ctypes.c_ubyte * 9


# Load iowkit.dll
try:
    iowkit = ctypes.WinDLL("C:\\Users\\Sysadmin\\eclipse-workspace\\CirculatorSerial\\src")
except:
    try:
        iowkit = ctypes.WinDLL(os.path.join(os.curdir, 'iowkit'))
    except:
        iowkit = ctypes.WinDLL('iowkit')


# Open iowkit.dll
ioHandle = c_ulong(iowkit.IowKitOpenDevice())

print (sys.version)

if ioHandle != 0:
    
    serial = create_unicode_buffer("xxxxxxxx")

    # Get number of IO-Warrior
    numdevs = iowkit.IowKitGetNumDevs()
    
    # For this script only one IO-Warrior
    if numdevs > 1: 
        iowkit.IowKitCloseDevice(ioHandle)
        print("Only one single IO-warrior allowed")
        exit(1)


    # Get ProductID
    pid = iowkit.IowKitGetProductId(ioHandle)  

    if pid == IOWKIT_PRODUCT_ID_IOW40: 
        
        # Get Serialnumber
        windll.Iowkit.IowKitGetSerialNumber(ioHandle, serial)
        print ("Device Type: IO-Warrior40 - Serial: ", str(serial.value))

    else:
        iowkit.IowKitCloseDevice(ioHandle)
        print ("Only IO-Warrior40 support for these script")
        exit(1)

    # Get a random Integer 
    output = random.randint(0, 255)

    print("Random Value: ", output)

    # Fill the Buffer
    report = IOWKIT40_IO_REPORT(
                                0x00,  # ReportID
                                0x00,  # IO-Port 0
                                0x00,  # IO-Port 1
                                0x00,  # IO-Port 2
                                output # IO-Port 3 -> On IOW40 Starterkit LED output
                                )

        # Write to IO-Warrior
    iowkit.IowKitWrite(
                       ioHandle,                   # Device Handle
                       IOW_PIPE_IO_PINS,           # Endpoint 0 -> for I/O Pins / Ports
                       ctypes.byref(report),       # Buffer of data
                       sizeof(IOWKIT40_IO_REPORT)  # Buffersize
                       )

else:
    print('No Device')

# Don't forget to close !
iowkit.IowKitCloseDevice(ioHandle)
print ("Close iowkit, Exit")