import serial
import sys

#Definicion del objeto para utilzar el puerto serie
class SerialOb():
    def __init__(self, comPort, baud = 9600):
        #Inicialziar Objeto Serie
        self.ser = serial.Serial(
            port=comPort,\
            baudrate=baud,\
            # parity=serial.PARITY_NONE,\
            # stopbits=serial.STOPBITS_ONE,\
            # bytesize=serial.EIGHTBITS,\
            # timeout=0
            )
        #Mensaje de bienvenida 
        print("Connectado: " + self.ser.portstr)

    
    def close(self):
        self.ser.close()