#include <Wire.h>
#include <Servo.h>
Servo servo_test1;
Servo servo_test2;
const byte numChars = 32; //character limit
char receivedChars[numChars]; // an array to store the received data
boolean newData = false;
String wheelstring; //string for sending wheel values
String case_i; //wheel cases
String wheelstring2;
String case_i2;

String readString;
int angle1 = 90;//Servo1
int angle2 =90;//Servo2
boolean move_servo_logic=false;

char tmp_str[7]; // temporary variable used in convert function

char* convert_int16_to_str(int16_t i) { // converts int16 to string. Moreover, resulting strings will have the same length in the debug monitor.
  sprintf(tmp_str, "%6d", i);
  return tmp_str;
}  

String convertToString(char* a, int size)
{
    int i;
    String s = "";
    for (i = 0; i < size; i++) {
        s = s + a[i];
    }
    return s;
}

void setup() {
  // put your setup code here, to run once:

  Serial.begin(115200);

  // Servos
  servo_test1.attach(11); //Servo1
  servo_test2.attach(12); //Servo2

}
void recvWithEndMarker() {
 static byte ndx = 0;
 char endMarker = '\n';
 char rc;
 // if (Serial.available() > 0) {
           while (Serial.available() > 0 && newData == false) {
 rc = Serial.read();

 if (rc != endMarker) {
 receivedChars[ndx] = rc;
 ndx++;
 if (ndx >= numChars) {
 ndx = numChars - 1;
 }
 }
 else {
 receivedChars[ndx] = '\0'; // terminate the string
 ndx = 0;
 newData = true;
 }
 }
}
void move_servo(){
 char str_array[case_i2.length()];
      case_i2.toCharArray(str_array, case_i2.length());
      
      // Read each command pair 
      //i.e. serv1&30: 
      // the above would make Servo1 go to 30 degrees
      char* command = strtok(str_array, "&");
      while (command != 0)
      {
          String command_s=convertToString(command,1+sizeof(str_array));
          Serial.println(command_s);
          Serial.println(command);
          // Split the command in two values
          char* separator = strchr(command, ':');
          if (separator != 0)
          {
              // Actually split the string in 2: replace ':' with 0
              *separator = 0;
              int servoId = atoi(command);
              Serial.print("command_s: ");
              Serial.println(command_s);
              Serial.print("This just in");
              if(case_i2.indexOf("serv1")>=0 and command_s.indexOf("serv")!=-1){
                delay(10);
                angle1=servoId; //Servo1
                Serial.println(angle1);
                Serial.print("ANGLE1; The command_s.indexOf('serv')");
                Serial.println(command_s.indexOf("serv"));
                delay(10);

              }
              if(case_i2.indexOf("serv2")>=0 and command_s.indexOf("serv")==-1){
                delay(10);
                angle2=servoId; //Servo2
                Serial.println(angle2);
                Serial.print("ANGLE2; The command_s.indexOf('serv')");
                Serial.println(command_s.indexOf("serv"));
                delay(10);

              }

              ++separator;
              int position = atoi(separator);
      
              // Do something with servoId and position
          }
          // Find the next command in input string
          command = strtok(0, "&");
      }}
void showNewData() {
 delay(10);
 if (newData == true) {
 Serial.print("This just in ... ");
 Serial.println(receivedChars);
case_i2=String(receivedChars);
//////////////////////
    if(case_i2.indexOf("grip")>=0)
    {
      wheelstring2="gr";}
    if(case_i2.indexOf("serv") >=0) //
    {

    move_servo();
    move_servo_logic=true;
    }
    if(case_i2.indexOf("stop")>=0)
    {
      move_servo_logic=false;
    }

    case_i2="";
 newData = false;
}}



void loop() {
   //Serial.println(forward_d);
   recvWithEndMarker();
   showNewData();
   //servo_test1.write(angle1);
   if (move_servo_logic==true){
     delay(100);
     servo_test1.write(angle1);
     servo_test2.write(angle2);
     delay(200);
     Serial.print("angle1: ");
     Serial.println(angle1);
     Serial.print("angle2: ");
     Serial.println(angle2);}
   if (move_servo_logic==false){
     //Serial.println("waiting");
   }
}
