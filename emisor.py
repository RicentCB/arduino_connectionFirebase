from serialOb import SerialOb
from firebase import firebase


#Variable con la url de la base de adtos
serverDb = "https://arduinointernet-1697e-default-rtdb.firebaseio.com/"

#Conexion con las base de datos
firebaseApp = firebase.FirebaseApplication(serverDb, None)

#Crear objeto serie
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
                data = {
                   "sensor1": arrayPartsMessage[0],
                   "sensor2": arrayPartsMessage[1],
                   "sensor3": arrayPartsMessage[2]
                }   
                # Solicitud a firebase
                insData = firebaseApp.post('/',data)
                print(insData)        
                # print('S1:'+arrayPartsMessage[0]+' S2:'+arrayPartsMessage[1]+' S3:'+arrayPartsMessage[2])
            # Proceso de Mensaje
            strMessage = ""

arduino.close()

# #Leer DB por metodo GET
readData = firebaseApp.get('/test/postEx/', '')
print(readData)