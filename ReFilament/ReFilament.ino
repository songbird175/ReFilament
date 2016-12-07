#define EXT_PIN 6
#define SPL_PIN 5
#define HTR_PIN 3

// Set up global variables
boolean input_complete = false;
float input_param = 0;
String input = "";
boolean active = true;
int shaft_speed = 80;
long start_millis = 0;
long over_temp_mv = 2480;
long temp_mv = 0;
long temp_deg = 0;
boolean heater_activated = true;
boolean heater_on = false;

void setup() {
  // put your setup code here, to run once:
  pinMode(EXT_PIN, OUTPUT); // Extrusion Motor  
  pinMode(SPL_PIN, OUTPUT); // Spooling Motor
  pinMode(HTR_PIN, OUTPUT); // Heater

  //write all control pins low
  digitalWrite(EXT_PIN, LOW);
  digitalWrite(SPL_PIN, LOW);
  digitalWrite(HTR_PIN, LOW);

  Serial.begin(9600);
  Serial.println("Initiating vehicle...");
  start_millis = millis();

}

void loop() {
  // put your main code here, to run repeatedly:
  temp_mv = analogRead(0) / 1024.0 * 5000;
  if (temp_mv >= over_temp_mv) {
    heater_shutdown();
  }
  long temp_deg = temp_mv / 0.9181 - 2483;
  Serial.print(String(temp_mv) + "/");
  Serial.print(String(temp_deg) + "/");
  Serial.println(heater_activated);
  
  // get serial input here, change global variables
  get_serial();
  if (heater_activated) {
    update_temp();
  }
  analogWrite(SPL_PIN, 3);
  analogWrite(EXT_PIN, 0);
  delay(10);
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

void get_serial(){
  if (input_complete) {
    Serial.println(input);
    Serial.println(input_param);
    if (input.indexOf("speed")) {
      shaft_speed = input_param;
    } else if (input.indexOf("stop") > -1) {
      active = false;
    } else if (input.indexOf("go") > -1) {
      active = true;
    }
    input_complete = false;
    input = "";
    input_param = 0;
  }
}

void update_speed()
{
  if (!active) {
    analogWrite(9, 0);
  } else {
    analogWrite(9, shaft_speed);
  }
}

void serialEvent()
{
  while (Serial.available()) {
    char input_char = (char)Serial.read();
    if (input_char == ':') {
      input_param = Serial.parseFloat();
      input_complete = true;
    }
    else {
      input += input_char;
    }
  }
}
