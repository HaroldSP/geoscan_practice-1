import serial
import time

ser = serial.Serial("/dev/ttyS0", baudrate = 115200, timeout = 2)

if (ser.isOpen()):
    while True:
        ser.write(b'1234')
        time.sleep(1)
        recieved = ser.read(5)
        print('Recieved: ', recieved)
