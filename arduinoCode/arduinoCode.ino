# include <Servo.h>
String cmd;
String theta1;
String theta2;
float angle_1 ;
float angle_2;

Servo servo1;
Servo servo2;
void setup() {
  // put your setup code here, to run once:
servo1.attach(5);
servo2.attach(6);
Serial.begin(115200);
}

void loop() {
  // put your main code here, to run repeatedly:
  while(Serial.available()==0){
  }
  cmd=Serial.readStringUntil('\r');
  if (cmd==theta1){
    cmd=theta1; 
  }
  if (cmd==theta2){
    cmd=theta2; 
  }
  angle_1=theta1.toFloat();
  angle_2=theta2.toFloat();

  servo1.write(angle_1);
  servo2.write(angle_2);
}
