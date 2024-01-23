#include <FastLED.h>


#define DATA_PIN 23
#define CLOCK_PIN 22

// #define PIN            6  // Pin number to which the data input of the NeoPixel strip is connected
#define NUM_LEDS     30 // Number of LEDs in the strip
#define START_PIN     2  // Pin number to which the button is connected
#define MID_PIN     3  // Pin number to which the button is connected
#define END_PIN     4  // Pin number to which the button is connected

Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUMPIXELS, PIN, NEO_GRB + NEO_KHZ800);

int buttonState = 0;
int startbuttonState = 0;
int midbuttonState = 0;
int endbuttonState = 0;
int lastButtonState = 0;

// Define the array of leds
CRGB leds[NUM_LEDS];


void setup() {
  Serial.begin(9600);
  strip.begin();
  strip.show(); // Initialize all pixels to 'off'
  pinMode(START_PIN, INPUT_PULLUP);
  pinMode(MID_PIN, INPUT_PULLUP);
  pinMode(END_PIN, INPUT_PULLUP);
  FastLED.addLeds<APA102, DATA_PIN, CLOCK_PIN, BGR>(leds, NUM_LEDS);
  Serial.println("setup compleate");

  for(int i=0;i<NUM_LEDS;i++){
    leds[i] = CRGB::Red;
  }
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
    // flashred();
  }
  else if (endbuttonState == LOW) {
    Serial.print("match end pressed");

    // Button was pressed
    // endred();
  }
}

void start() {
  for(int i=0;i<NUM_LEDS;i++){
    leds[i] = CRGB::Red;
  }
    FastLED.show();
    delay(500);
  for(int i=0;i<NUM_LEDS;i++){
    leds[i] = CRGB::White;
  }
    FastLED.show();
    delay(500);
  for(int i=0;i<NUM_LEDS;i++){
    leds[i] = CRGB::Red;
  }
    FastLED.show();
    delay(500);
  for(int i=0;i<NUM_LEDS;i++){
    leds[i] = CRGB::White;
  }
    FastLED.show();
    delay(500);
  for(int i=0;i<NUM_LEDS;i++){
    leds[i] = CRGB::Red;
  }
  FastLED.show();
  delay(500)
  for(int i=0;i<NUM_LEDS;i++){
    leds[i] = CRGB::Green;
  }
    FastLED.show();
    delay(1000);
  for(int i=0;i<NUM_LEDS;i++){
    leds[i] = CRGB::White;
  }
  FastLED.show();
  }


void flashred() {
  red();
  white();
   delay(30);
  red();
  white();
   delay(30);
  red();
  white();
   delay(30);
  red();
  white();
  
}

void endred() {
  red();
   delay(30);
  red();
   delay(30);
  red();
   delay(30);
  red();
   delay(30);
  red();
 
}

void red(){
   for(int i=0;i<NUM_LEDS;i++){
    leds[i] = CRGB::Red;
  }
  FastLED.show();
}

void green(){
   for(int i=0;i<NUM_LEDS;i++){
    leds[i] = CRGB::Green;
  }
  FastLED.show();
}

void white(){
   for(int i=0;i<NUM_LEDS;i++){
    leds[i] = CRGB::White;
  }
  FastLED.show();
}