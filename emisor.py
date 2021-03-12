from firebase import firebase

#Variable con la url de la base de adtos
serverDb = "https://arduinointernet-1697e-default-rtdb.firebaseio.com/"

#Conexion con las base de datos
firebaseApp = firebase.FirebaseApplication(serverDb, None)
#Datos a enviar
data = {
    "id": "2",
    "sensor1": "1024",
    "sensor2": "520"
}

#Llenar DB por metodo POST
# insData = firebaseApp.post('/test/postEx',data)
# print(insData)

#Leer DB por metodo GET
readData = firebaseApp.get('/test/postEx', '')
print(readData)