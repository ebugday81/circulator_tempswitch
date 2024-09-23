'''
Created on 27.06.2019

@author: SYSADMIN
'''

import ctypes

testlib = ctypes.CDLL("C:\\Users\\Sysadmin\\Downloads\\sdk\\iowkit api\\x64 dll\\iowkit.dll")
HANDLE = testlib.IowKitOpenDevice()
NUM_DEV = testlib.IowKitGetNumDevs()
DEVICE_HANDLE = testlib.IowKitGetDeviceHandle(1)
#testRead = testlib.IowKitReadImmediate()

testBuffer = ctypes.c_buffer(9)
serial = testlib.IowKitGetRevision(DEVICE_HANDLE)

print(DEVICE_HANDLE)
print(testlib)
print(HANDLE)
print(NUM_DEV)
#print(testRead)
print(serial)


testlib.IowKitCloseDevice()