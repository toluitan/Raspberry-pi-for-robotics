import serial
arduino = serial.Serial('/dev/ttyUSB0', 9600)
while True:
    
    data = arduino.readline().decode('ascii') #the last bit gets rid of the new-line
    
    if data:
        data = data.split()
        data = int(data[0])
        print("distance to obstacle is: ",data)
        
        if data < 20:
            
            arduino.write(b'H')
            
        else:
            
            arduino.write(b'L')
