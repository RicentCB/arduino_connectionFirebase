from serialOb import SerialOb
from firebase import firebase
import time

#Variable con la url de la base de adtos
serverDb = "https://arduinointernet-1697e-default-rtdb.firebaseio.com/"

#Conexion con las base de datos
firebaseApp = firebase.FirebaseApplication(serverDb, None)

# Crear objeto serie
arduino = SerialOb("COM5", 115200)

while True:
    #Leer DB por metodo GET
    readData = firebaseApp.get('/', '')
    values = list(readData.values())
    lastValue = values[-1]['pot']
    print(lastValue)
    
    #Escribir en monitor serie
    print("Enviando dato")
    arduino.ser.write(255)
# arduino.close()
# time.sleep(6)
