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
    
#--------------------------------
#Termina OBJETO SERIAL

arduino = SerialOb("COM5", 115200)
#Leer puerto serie del arduino
strMessage = ""
while True:
    for car in arduino.ser.read():
        strMessage += chr(car)
        if(chr(car) == '\n'):
            # print(strMessage)
            arrayPartsMessage = strMessage.split(sep=",")
            if(len(arrayPartsMessage)>1):
                print('S1:'+arrayPartsMessage[0]+' S2:'+arrayPartsMessage[1]+' S3:'+arrayPartsMessage[2])
            # Proceso de Mensaje
            strMessage = ""

arduino.close()