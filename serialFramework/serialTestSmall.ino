byte serialBuffer[256];
byte heater_on = 0;
byte motors_on = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  printSerialData();
  readSerialData();
}

void printSerialData()
{
  // printSerialData prints the
  Serial.print(heater_on); // 
  Serial.print(",");
  Serial.println(motors_on);
}

void readSerialData()
{
  if (Serial.available() > 0)
  {
    Serial.readBytes(serialBuffer, 256); // read 256 bytes from serial
    heater_on = byte(serialBuffer[0]); // The values for the desiredTemp should be between 0 - 255 (size of byte)
    motors_on = byte(serialBuffer[1]); // The values for the on (1) or off (0) state
  }
}
