
//Libraries
#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>

//Constants
const char* ssid     = "Coffman";         // The SSID (name) of the Wi-Fi network you want to connect to
const char* password = "rem35621";     // The password of the Wi-Fi network
const char server[] = "www.rcoff.me";
const int upload_minutes = 60;
const String room = "Basement";
const String connector = "http://www.rcoff.me/upload/waterdetected/"; //Port must be in URL

int analogpin = A0;

WiFiClient client;
HTTPClient http;

//Variables

void setup() {
  Serial.begin(115200);
  Serial.println("Device started");
}

void loop() {
  if(analogRead(analogpin) > 10){
    wifi_connect();

    if(WiFi.status()==WL_CONNECTED) {
      server_connect();

      //client.close();
    } else {
      Serial.println("WiFi not connected");
    }
  } else { Serial.println("Water not detected"); }
  delay(15000);  //upload_minutes * 60 * 1000);
}

void wifi_connect() {
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid,password);
  Serial.print("Connecting...");

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

void server_connect() {
  Serial.println('\n');
  Serial.println("Attempting to connect to server...");
  if (client.connect(server, 80)){
    Serial.println("Connected to server!");
    POST_status();
  } else{
    Serial.println("Failed to connect :(");
    return;
  }
}

void POST_status() {
  Serial.print('\n');

  //Send data to API
  String PostData;
  if (http.begin(connector)) {
    PostData = "{\"Level\": \"" + String(analogRead(analogpin)) + "\"}";
    Serial.println(PostData);


    http.addHeader("Content-Type", "application/json");
    http.POST(PostData);
    Serial.println("Sending data to server...");
    Serial.println(http.getString());
    } else {
      Serial.println("Failed to send data...");
      }
}
