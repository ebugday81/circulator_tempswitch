'''
Created on 21.06.2019

@author: SYSADMIN
'''
from src import SerialPort as ser

ser.objStatus()
#ser.startHeat()

#print("Timeout in Sekunden: ",ser.obj.timeout)
ser.stopHeat()
'''ser.setTemperature(41.7)
ser.incTemperature(0.1) '''
ser.closePort()
ser.objStatus()


#print()
#contents = setTemperature()
#contents = incTemperature(0.1)
'''obj.write(b'W NS 1\r') ## eine oder zwei Dezimalstellen
contents = obj.readline().decode("utf-8")
print(contents)
print("Temperatur erfolgreich gesetzt:",contents)

obj.write(b'R SW\r')
contents = obj.readline().decode("utf-8")
print(contents)

startHeat()
setTemperature(41.8)
contents = incTemperature(0.1)
print(contents)

#stopHeat()
 # init stop

#test loop
while(i <= 3): 
    contents = read_fixed_Temperature_of_specific_f(str(i))
    print("Fixer Wert von "+str(i)+":")
#   contents = obj.readline()
    print(contents)
    i = i + 1

stopHeat()

print(obj) '''


'''print(obj.is_open)
obj.set


ports = list(serial.tools.list_ports.comports())
for p in ports:
    print(p)
'''
