import serial
arduino = serial.Serial('/dev/ttyUSB1', 9600)
while True:
    data = arduino.readline().decode('ascii') #the last bit gets rid of the new-line
    if data:
        data = data.split("\r")
        data = int(data[0])
        if data:
            print(data)
        if data < 15:
            
            arduino.write(b'H')
            
        else:
            
            arduino.write(b'L')