volatile int desiredTemp;
volatile float desiredSpeed;
volatile int onOff;
volatile int P;
volatile float I;


byte serialBuffer[256];

void setup()
{
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop()
{
  // put your main code here, to run repeatedly:
  readSerialData();

  printSerialData();
}

void printSerialData()
{
  // printSerialData prints the
  Serial.print(desiredTemp); //
  Serial.print(",");
  Serial.print(desiredSpeed); //
  Serial.print(",");
  Serial.print(onOff); //
  Serial.print(",");
  Serial.print(P); //
  Serial.print(",");
  Serial.println(I); //
}

void readSerialData()
{
  Serial.readBytes(serialBuffer, 256); // read 256 bytes from serial
  desiredTemp = int(serialBuffer[0]); // The values for the desiredTemp should be between 0 - 255 (size of byte)
  desiredSpeed = float(serialBuffer[1]) / 256; // The values for the desiredSpeed should
  onOff = int(serialBuffer[2]); // The values for the desiredSpeed should
  P = int(serialBuffer[3]); // The values for the desiredSpeed should
  I = float(serialBuffer[4]) / 256; // The values for the desiredSpeed should
}
