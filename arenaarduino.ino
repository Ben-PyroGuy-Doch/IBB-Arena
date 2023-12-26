#include <Adafruit_NeoPixel.h>

#define PIN            6  // Pin number to which the data input of the NeoPixel strip is connected
#define NUMPIXELS      30 // Number of LEDs in the strip
#define START_PIN     2  // Pin number to which the button is connected
#define MID_PIN     3  // Pin number to which the button is connected
#define END_PIN     4  // Pin number to which the button is connected

Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUMPIXELS, PIN, NEO_GRB + NEO_KHZ800);

int buttonState = 0;
int lastButtonState = 0;

void setup() {
  strip.begin();
  strip.show(); // Initialize all pixels to 'off'
  pinMode(START_PIN, INPUT);
  pinMode(MID_PIN, INPUT);
  pinMode(END_PIN, INPUT);
}

void loop() {
  startbuttonState = digitalRead(START_PIN);
  midbuttonState = digitalRead(MID_PIN);
  endbuttonState = digitalRead(END_PIN);


  if (startbuttonState == HIGH) {
    // Button was pressed
    Start();
  }
  else if (midbuttonState == HIGH) {
    // Button was pressed
    FlashRed();
  }
  else if (endbuttonState == HIGH) {
    // Button was pressed
    Endred();
  }
}

void Start() {
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

void flashRed(int duration) {
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

void EndredRed(int duration) {
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