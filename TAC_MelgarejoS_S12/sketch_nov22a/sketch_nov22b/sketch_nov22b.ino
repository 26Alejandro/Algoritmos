#include "SPIFFS.h"

void setup() {
  Serial.begin(115200);
  delay(1000);

  // Iniciar SPIFFS
  if (!SPIFFS.begin(true)) {
    Serial.println("Error al montar SPIFFS");
    return;
  }
  
  // Listar todos los archivos en el sistema de archivos
  Serial.println("Archivos en el sistema SPIFFS:");
  File root = SPIFFS.open("/");
  File file = root.openNextFile();

  while (file) {
    Serial.print("Nombre de archivo: ");
    Serial.println(file.name());
    file = root.openNextFile();
  }
  
  // Verificar archivos específicos
  verificarArchivo("/AmazonRootCA1.pem");         // Cambia al nombre de tu archivo Root CA
  verificarArchivo("/854-certificate.pem.crt");   // Cambia al nombre de tu archivo de certificado
  verificarArchivo("/854-private.pem.key");       // Cambia al nombre de tu archivo de clave privada
  
  SPIFFS.end(); // Opcional: cerrar SPIFFS al finalizar
}

void loop() {
  // Vacío, el loop no es necesario en este caso
}

void verificarArchivo(const char* nombreArchivo) {
  File archivo = SPIFFS.open(nombreArchivo, "r");

  if (!archivo) {
    Serial.print("Error: No se encontró el archivo ");
    Serial.println(nombreArchivo);
    return;
  }

  Serial.print("Contenido del archivo ");
  Serial.println(nombreArchivo);
  while (archivo.available()) {
    Serial.write(archivo.read());
  }
  Serial.println(); // Salto de línea al final del contenido del archivo
  archivo.close();
}
