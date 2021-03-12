#include <Arduino.h>

#define OUT_LED_ONBOARD 2
#define DEBUG_ANALOG_PIN 34
#define DELAY_REPEAT_LOOP 1000

unsigned long MAX_TIEMPO_ESPERA_REGISTRO_DB = DELAY_REPEAT_LOOP * 2;
unsigned long ultimoTiempoRegDb = 0;

/*==============================================
  SETUP DEL MICRO
==============================================*/
void setup() {
    Serial.begin(115200);
    //Pines Auxiliares
    pinMode(OUT_LED_ONBOARD, OUTPUT);//Led onboard

    digitalWrite(OUT_LED_ONBOARD, LOW);

    ultimoTiempoRegDb = millis();
    Serial.println("Inciio de Conexion");
}

/*==============================================
  LOOP DEL MICRO
==============================================*/
void loop() {
    float temp=0;
    
    temp = analogRead(DEBUG_ANALOG_PIN);
    
    //Enviar registro a DB de la temperatura
    if((millis() - ultimoTiempoRegDb) >=  MAX_TIEMPO_ESPERA_REGISTRO_DB){
      Serial.println("Registro de Datos en DB");
      ultimoTiempoRegDb = millis();
    }

    //------------------------------------------
    //Impresion de datos en el monitor serie
    Serial.print(temp, 0);

    Serial.print(",");
    Serial.print(temp, 0);

    Serial.print(",");
    Serial.print(temp,2);

    Serial.println();
    // Delay para repetir ciclo
    delay(DELAY_REPEAT_LOOP);

}