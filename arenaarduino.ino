#include <Adafruit_NeoPixel.h>

#define PIN            6  // Pin number to which the data input of the NeoPixel strip is connected
#define NUMPIXELS      30 // Number of LEDs in the strip
#define START_PIN     2  // Pin number to which the button is connected
#define MID_PIN     3  // Pin number to which the button is connected
#define END_PIN     4  // Pin number to which the button is connected

Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUMPIXELS, PIN, NEO_GRB + NEO_KHZ800);

int buttonState = 0;
int startbuttonState = 0;
int midbuttonState = 0;
int endbuttonState = 0;
int lastButtonState = 0;

void setup() {
  Serial.begin(9600);
  strip.begin();
  strip.show(); // Initialize all pixels to 'off'
  pinMode(START_PIN, INPUT_PULLUP);
  pinMode(MID_PIN, INPUT_PULLUP);
  pinMode(END_PIN, INPUT_PULLUP);
  Serial.println("setup compleate");
}

void loop() {
  // Serial.println("looping");
  
  startbuttonState = digitalRead(START_PIN);
  midbuttonState = digitalRead(MID_PIN);
  endbuttonState = digitalRead(END_PIN);


  if (startbuttonState == LOW) {
     Serial.print("match start pressed");
    // Button was pressed
    // start();
  }
  else if (midbuttonState == LOW) {
      Serial.print("match mid pressed"); 

    // Button was pressed
    // flashred(3);
  }
  else if (endbuttonState == LOW) {
    Serial.print("match end pressed");

    // Button was pressed
    // endred(3);
  }
}

void start() {
  for (int i = 0; i < NUMPIXELS; i++) {
    // Flash pattern: 1-2-3
    strip.setPixelColor(i, 255, 0, 0); // Red
    strip.show();
    delay(500);

    strip.setPixelColor(i, 0, 0, 0); // Turn off
    strip.show();
    delay(250);

    strip.setPixelColor(i, 255, 255, 255); // White
    strip.show();
    delay(500);

    strip.setPixelColor(i, 0, 0, 0); // Turn off
    strip.show();
    delay(250);
  }

  // Turn all LEDs white at the end
  for (int i = 0; i < NUMPIXELS; i++) {
    strip.setPixelColor(i, 255, 255, 255); // Turn off
  }
  strip.show();
}

void flashred(int duration) {
  unsigned long startTime = millis();

  while (millis() - startTime < duration) {
    strip.fill(strip.Color(255, 0, 0)); // Set all pixels to red
    strip.show();
    delay(100); // Adjust the delay to control the flashing speed

    strip.fill(strip.Color(0, 0, 0)); // Turn off all pixels
    strip.show();
    delay(100); // Adjust the delay to control the flashing speed
  }
}

void endred(int duration) {
  unsigned long startTime = millis();

  while (millis() - startTime < duration) {
    strip.fill(strip.Color(255, 0, 0)); // Set all pixels to red
    strip.show();
    delay(100); // Adjust the delay to control the flashing speed

    strip.fill(strip.Color(0, 0, 0)); // Turn off all pixels
    strip.show();
    delay(100); // Adjust the delay to control the flashing speed
  }
}