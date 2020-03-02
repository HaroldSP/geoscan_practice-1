import serial
import time
import check_code


def WIFI_BTN():
    
    package = (0xCC, 0x01, 0x00)
    code = check_code.calc(package)
    package += (code,)
    
    return package


#in photo mode takes a picture, in video mode starts/stops recording
def POWER_BTN():
    
    package = (0xCC, 0x01, 0x01)
    code = check_code.calc(package)
    package += (code,)
    
    return package


#switching camera modes (see your camera manual for a description)
def CHANGE_MODE():
    
    package = (0xCC, 0x01, 0x02)
    code = check_code.calc(package)
    package += (code,)
    
    return package


def START_RECORDING():
    
    package = (0xCC, 0x01, 0x03)
    code = check_code.calc(package)
    package += (code,)
    
    return package


def STOP_RECORDING():
    
    package = (0xCC, 0x01, 0x04)
    code = check_code.calc(package)
    package += (code,)
    
    return package


if __name__=="__main__":
    
    ser = serial.Serial("/dev/ttyS0", baudrate = 115200, timeout = 2)

    if ser.isOpen():
        while(1):
            print(' 0 - wi-fi btn\n','1 - power btn\n', '2 - change mode\n', '3 - start recording\n', '4 - stop recording\n') 
            a = input()
            if a == '0':
                ser.write(WIFI_BTN())
            elif a == '1':
                ser.write(POWER_BTN())
            elif a == '2':
                ser.write(CHANGE_MODE())
            elif a == '3':
                ser.write(START_RECORDING())
            elif a == '4':
                ser.write(STOP_RECORDING())
            elif a == 'exit':
                break
        


