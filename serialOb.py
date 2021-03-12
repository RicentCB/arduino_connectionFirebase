import serial
import sys
#Definicion del objeto para utilzar el puerto serie
class SerialOb():
    def __init__(self, port, baud = 9600):
        #Inicialziar Objeto Serie
        self.ser = serial.Serial(
            port=self.port,\
            baudrate=self.baud,\
            parity=serial.PARITY_NONE,\
            stopbits=serial.STOPBITS_ONE,\
            bytesize=serial.EIGHTBITS,\
            timeout=0)
        #Mensaje de bienvenida 
        print("Connectado: " + self.ser.portstr)

    
    def close():
        self.ser.close()
        
# count=1
# strMessage = ""
# while True:
#     for car in ser.read():
#         strMessage += chr(car)
#         if(chr(car) == '\n'):
#             # print(strMessage)
#             arrayPartsMessage = strMessage.split(sep=",")
#             if(len(arrayPartsMessage)>1):
#                 print(arrayPartsMessage[0]+','+arrayPartsMessage[1])
#             # Proceso de Mensaje
#             strMessage = ""

def __main__():
    print ("hello")