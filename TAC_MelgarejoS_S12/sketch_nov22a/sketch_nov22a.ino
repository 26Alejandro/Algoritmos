// Añadir librerías
#include <WiFi.h>
#include "SPIFFS.h"
#include <WiFiClientSecure.h>
#include <PubSubClient.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

// Credenciales de la red WiFi
const char* ssid = "UNI_LIBRE_H";
const char* password = "123456789";

// Configuración del servidor MQTT
const char* mqtt_server = "d02853903v0mqxoo9t9cd-ats.iot.us-east-2.amazonaws.com";
const int mqtt_port = 1883;  // Cambia a 8883 si usas TLS y configura los certificados
const char* mqtt_topic = "test/connection";

// Crear clientes WiFi y MQTT
WiFiClient espClient;
PubSubClient client(espClient);

void setup_wifi() {
  delay(10);
  Serial.println();
  Serial.print("Conectando a ");
  Serial.println(ssid);

  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("");
  Serial.println("WiFi conectado");
  Serial.println("Dirección IP: ");
  Serial.println(WiFi.localIP());
}

// Función para manejar la conexión al servidor MQTT
void reconnect() {
  // Intenta conectarse hasta que tenga éxito
  while (!client.connected()) {
    Serial.print("Intentando conectar a MQTT...");
    
    // ID de cliente único para evitar colisiones
    String clientId = "ESP32Client-";
    clientId += String(random(0xffff), HEX);

    // Intenta conectarse
    if (client.connect(clientId.c_str())) {
      Serial.println("Conectado al servidor MQTT");

      // Publica un mensaje de prueba al conectarse
      client.publish(mqtt_topic, "Prueba de conexión exitosa");
      Serial.println("Mensaje de prueba publicado en el tema: " + String(mqtt_topic));
    } else {
      Serial.print("Falló, rc=");
      Serial.print(client.state());
      Serial.println(" Intentando de nuevo en 5 segundos");
      delay(5000);
    }
  }
}

void setup() {
  Serial.begin(115200);
  setup_wifi();
  
  // Configura el servidor MQTT y la función de callback
  client.setServer(mqtt_server, mqtt_port);
}

void loop() {
  if (!client.connected()) {
    reconnect();
  }
  client.loop();
}
