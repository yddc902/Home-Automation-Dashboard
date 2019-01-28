
//Libraries
#include <DHT.h>;
#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>

//Constants
const char* ssid     = "Coffman";                                               // The SSID (name) of the Wi-Fi network you want to connect to
const char* password = "rem35621";                                              // The password of the Wi-Fi network
const char server[] = "www.rcoff.me";
const int upload_seconds = 30;
const String room = "Kitchen";                                                  //Change this value for each room, must match the model field
const String connector = "http://www.rcoff.me/upload/temp/";                     //Port must be in URL

#define DHTPIN  4
#define DHTTYPE DHT22

//Initialize libraries as variables
DHT dht(DHTPIN, DHTTYPE);
WiFiClient client;
HTTPClient http;

//Variables
float temp;
float hum;
char payload;

void setup() {
  Serial.begin(115200);
  dht.begin();
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid,password);
  Serial.print("Connecting...");

  open_connection();

  Serial.println('\n');
  Serial.println("Attempting to connect to server...");
  if (client.connect(server, 80)){
    Serial.println("Connected to server!");
  } else{
    Serial.println("Failed to connect :(");
    Serial.println("");
    return;
  }
}

void loop() {
  temp = dht.readTemperature(true);                                             //True for fahrenheit, blank or false for Celsius
  hum  = dht.readHumidity();

  // Print out temperature data
  Serial.print("Temperature: ");
  Serial.print(temp);
  Serial.println(" F");

  // Print out humidity data
  Serial.print("Humidity: ");
  Serial.print(hum);
  Serial.println("%");

  if(WiFi.status()==WL_CONNECTED) {
    if( (temp > 0 ) && (hum > 0) ) {
      commit_temperature();
    } else {
      Serial.println("No readings from sensor...");
      Serial.println("Trying again...");
      Serial.println("");
    }
  } else {
    Serial.println("WiFi not connected");
  }
  delay(upload_seconds * 1000);
}

void open_connection() {
  int i = 0;
  while (WiFi.status() != WL_CONNECTED) { // Wait for the Wi-Fi to connect
    delay(1000);
    Serial.print(++i); Serial.print(' ');
  }

  Serial.println('\n');
  Serial.println(" WiFi Connection established!");
  Serial.print("IP address:\t");
  Serial.println(WiFi.localIP());
}

void commit_temperature() {
  Serial.print('\n');

  //Send data to API
  String PostData;
  if (http.begin(connector)) {
    PostData = "{\"Room\":\"" + room + "\",\"Temp\":\"" + String(temp) + "\",\"Humidity\": \"" + String(hum) + "\"}";

    http.addHeader("Content-Type", "application/json");
    http.POST(PostData);
    Serial.println("Sending data to server...");
    //Serial.println(PostData);

    if(String(Serial.println(http.getString())) == String("")) {
      Serial.println("Failed to send data...");
    }
    } else {
      Serial.println("Failed to send data...");
      }

}
