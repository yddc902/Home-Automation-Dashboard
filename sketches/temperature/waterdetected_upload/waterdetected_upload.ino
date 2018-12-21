
//Libraries
#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>

//Constants
const char* ssid     = "Coffman";         // The SSID (name) of the Wi-Fi network you want to connect to
const char* password = "rem35621";     // The password of the Wi-Fi network
const char server[] = "192.168.0.113";
const int upload_minutes = 60;
const String room = "Basement";
const String connector = "http://192.168.0.113/upload/water/";

int analogpin = A0;

WiFiClient client;
HTTPClient http;

//Variables

void setup() {
  Serial.begin(115200);
}

void loop() {
  if(analogread(analogpin) > 10){
    wifi_connect();

    if(WiFi.status()==WL_CONNECTED) {
      server_connect();
      POST_status();

      client.close();
    } else {
      Serial.println("WiFi not connected");
    }
  }
  delay(upload_minutes * 60 * 1000);
}

void wifi_connect() {
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid,password);
  Serial.print("Connecting...");

  Serial.println('\n');
  Serial.println("Attempting to connect to server...");
  if (client.connect(server, 8000)){
    Serial.println("Connected to server!");
  } else{
    Serial.println("Failed to connect :(");
    return;
  }
}

void server_connect() {
  int i = 0;
  while (WiFi.status() != WL_CONNECTED) { // Wait for the Wi-Fi to connect
    delay(1000);
    Serial.print(++i); Serial.print(' ');
  }

  Serial.println('\n');
  Serial.println("WiFi Connection established!");
  Serial.print("IP address:\t");
  Serial.println(WiFi.localIP());
}

void POST_status() {
  Serial.print('\n');

  //Send data to API
  String PostData;
  if (http.begin(connector)) {
    //PostData = "{\"Room\": \"" + room + "\",\"Temp\": \"" + String(temp) + "\",\"Humidity\": \"" + String(hum) + "\"}";
    PostData = "{\"Level\": \"" + analogread(analogpin) + "\"}";

    http.addHeader("Content-Type", "application/json");
    http.POST(PostData);
    Serial.println("Sending data to server...");
    Serial.println(http.getString());
    } else {
      Serial.println("Failed to send data...");
      }
}
