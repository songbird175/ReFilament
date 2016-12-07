// Set up global variables
const byte EXT_PIN = 9;
const byte SPL_PIN = 10;
const byte HTR_PIN = 11;

// Serial input parameter editing for PID
boolean input_complete = false;
float input_param = 0;
String input = "";

// Extruder motor globals
boolean extruder_active = 1;
byte ex_power = 80;

long start_millis = 0;

// Heater control globals
long over_temp_mv = 2480;
long temp_mv = 0;
long temp_deg = 87;
byte temp_hi_limit = 210;
byte temp_lo_limit = 190;
boolean heater_activated = true;

// Spooling control globals
byte spl_kp = 0;
byte spl_ki = 0;
byte spl_kd = 0;
long filament_diameter_mm = 3;

// Serial variables
int desiredTemp;
byte serialBuffer[256];
int heater_on = 0;
int motors_on = 0;

/*
 * ##################################################################
 * Digital caliper code to read the value off of a cheap set of digital calipers
 * By Making Stuff Youtube channel https://www.youtube.com/c/makingstuff
 */
const byte clockPin = 2;  //attach to clock pin on calipers
const byte dataPin = 3; //attach to data pin on calipers

//Milliseconds to wait until starting a new value
//This can be a different value depending on which flavor caliper you are using.
const int cycleTime = 32; 

unsigned volatile int clockFlag = 0; 

long now = 0;
long lastInterrupt = 0;
long value = 0;

float finalValue = 0;
float previousValue = 0;

int newValue = 0;
int sign = 1;
int currentBit = 1;

// End caliper code setup
// ##################################################################
 

void setup() {
  // put your setup code here, to run once:
  pinMode(EXT_PIN, OUTPUT); // Extrusion Motor  
  pinMode(SPL_PIN, OUTPUT); // Spooling Motor
  pinMode(HTR_PIN, OUTPUT); // Heater
  pinMode(clockPin, INPUT);  
  pinMode(dataPin, INPUT); 
  
  
  //We have to take the value on the RISING edge instead of FALLING
  //because it is possible that the first bit will be missed and this
  //causes the value to be off by .01mm.
  attachInterrupt(digitalPinToInterrupt(clockPin), clockISR, FALLING);

  //write all control pins low
  digitalWrite(EXT_PIN, LOW);
  digitalWrite(SPL_PIN, LOW);
  digitalWrite(HTR_PIN, LOW);

  Serial.begin(9600);
  start_millis = millis();

}

void loop() {
  //Serial communication: blocking read first to avoid swamping 
  
  // Deal with temperature
  temp_mv = analogRead(0) / 1024.0 * 5000;
  if (temp_mv >= over_temp_mv) {
    heater_shutdown();
  }
  long temp_deg = temp_mv / 0.9181 - 2483;
  if (heater_activated) {
    update_temp();
  }
  
  analogWrite(SPL_PIN, 3);
  analogWrite(EXT_PIN, 0);
  delay(10);

  printSerialData();
  readSerialData();
  
}

void heater_shutdown() {
  digitalWrite(HTR_PIN, LOW);
  heater_activated = false;
}

void update_temp() {
  if (temp_deg <= 180) {
    digitalWrite(HTR_PIN, HIGH);
    heater_on = true;
  } else if (temp_deg >= 220) {
    digitalWrite(HTR_PIN, LOW);
    heater_on = false;
  } 
}

void update_ex_power()
{
  if (!extruder_active) {
    analogWrite(9, 0);
  } else {
    analogWrite(9, ex_power);
  }
}

void clockISR(){
 clockFlag = 1; 
}

void printSerialData()
{
  // printSerialData prints the
  Serial.print(temp_deg); // 
  Serial.print(",");
  Serial.print(17); // 
  Serial.print(",");
  Serial.println(filament_diameter_mm * 5);
}

void readSerialData()
{
  if (Serial.available() > 1)
  {
    Serial.readBytes(serialBuffer, 256); // read 256 bytes from serial
    heater_on = int(serialBuffer[0]); // The values for the desiredTemp should be between 0 - 255 (size of byte)
    motors_on = int(serialBuffer[1]); // The values for the on (1) or off (0) state
  }
}

