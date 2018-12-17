
//Libraries
#include <DHT.h>;
#include <ESP8266WiFi.h>

//Constants
const char* ssid     = "Coffman";         // The SSID (name) of the Wi-Fi network you want to connect to
const char* password = "rem35621";     // The password of the Wi-Fi network
#define DHTPIN  4
#define DHTTYPE DHT22

DHT dht(DHTPIN, DHTTYPE);

//Variables
float temp;
//int rooms[] = {"Kitchen", "Living Room", "Master Bedroom", "Man Cave", "Guest Bedroom"};

void setup() {
  Serial.begin(115200);
  dht.begin();
  WiFi.begin(ssid,password);
  Serial.print("Connecting...");

  int i = 0;
  while (WiFi.status() != WL_CONNECTED) { // Wait for the Wi-Fi to connect
    delay(1000);
    Serial.print(++i); Serial.print(' ');
  }
  
  Serial.println('\n');
  Serial.println("Connection established!");
  Serial.print("IP address:\t");
  Serial.println(WiFi.localIP());
}

void loop() {
  temp = dht.readTemperature(true);
  commit_temperature(temp);
  delay(2000);
}

void commit_temperature(float t) {
  Serial.print('\n');
  Serial.print("Temperature: ");
  Serial.print(temp);
  Serial.print(" F");
  
  //Send data to API
}
