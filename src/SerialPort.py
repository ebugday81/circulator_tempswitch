'''
Created on 13.06.2019


@author: Ekrem Bugday
'''

#import serial
import serial.tools.list_ports
import time

ports = serial.tools.list_ports.comports()
for port in ports :
    break

obj = serial.Serial( #Serial COM configuration
    port=port.device,
    baudrate=4800,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    rtscts=True,
    timeout=3,
    writeTimeout=5)

obj.flushInput()
obj.flushOutput()

contents = None

# fixed values of S - f3
def read_fixed_Temperature_of_specific_f(digit):
    appendedString = "R S"+str(digit)+"\r"
    obj.write(appendedString.encode())
    contents = float(obj.readline().decode("utf-8")[3:10])
    return contents

def read_fixed_Temperature():
    obj.write(b'R SW\r')
    contents = obj.readline().decode("utf-8")
    return contents

def read_current_Temperature():
    obj.write(b'R I\r')
    contents = float(obj.readline().decode("utf-8")[3:10])
    return contents

def startHeat():
    obj.write(b'W GO\r')
    contents = obj.readline().decode("utf-8") # unused, but useful to flush the line.

def stopHeat():
    obj.write(b'W ST\r')
    contents = obj.readline().decode("utf-8") # unused, but useful to flush the line.
    return contents

def setTemperature(number):
    obj.write(('W S1 '+str(number)+'\r').encode())
    contents = obj.readline().decode("utf-8")
    return contents
    
def incTemperature(temperature):
    float(temperature)
    tempCurrentTemperature = read_current_Temperature()
    while(True):
        if(round(tempCurrentTemperature,1) < 42):
            tempCurrentTemperature = read_current_Temperature()
            temp = read_fixed_Temperature_of_specific_f(1)
            print('Fixed Temperatur: ',temp)
            print('Aktuelle Temperatur',tempCurrentTemperature)
            
            if(round(tempCurrentTemperature,1) >= 42):
                break
        
            if(round(tempCurrentTemperature,1) == temp):
    
                temp = round(temp + temperature,1)
                setTemperature(temp)
                print('Erhoehe um 0.1 Grad bis 42 Grad')
                #print(temp)
                time.sleep(30)
        else: break

def closePort():
    obj.close()

def objStatus():
    print(obj)
    
ports = serial.tools.list_ports.comports()

print(ports[0])
