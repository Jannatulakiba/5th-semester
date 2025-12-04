#include <WiFi.h>           // use <ESP8266WiFi.h> for ESP8266
#include <HTTPClient.h>

const char* ssid = "YOUR_SSID";
const char* password = "YOUR_PASS";

const char* serverUrl = "http://192.168.0.105:5000/update-sensor-data"; // তোমার PC IP

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nWiFi connected");
}

void loop() {
  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;
    http.begin(serverUrl);
    http.addHeader("Content-Type", "application/json");

    // Example sensor values (তুমি এখানে সত্যিকারের সেন্সর থেকে নেবে)
    String payload = "{\"N\":50, \"P\":40, \"K\":30, \"temperature\":26.5, \"humidity\":70, \"ph\":6.8, \"rainfall\":120.0}";

    int httpResponseCode = http.POST(payload);

    Serial.print("POST code: ");
    Serial.println(httpResponseCode);
    if (httpResponseCode > 0) {
      String response = http.getString();
      Serial.println(response);
    } else {
      Serial.println("Error on sending POST");
    }
    http.end();
  } else {
    Serial.println("WiFi disconnected");
  }

  delay(60 * 1000); // প্রতি 60 সেকেন্ডে একবার পাঠাবে (পছন্দমতো কম-বেশি করো)
}
