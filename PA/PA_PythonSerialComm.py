import serial
ser=serial.Serial('/dev/tty.usbmodem1421',9600,timeout=0)
ser.write('pos')
