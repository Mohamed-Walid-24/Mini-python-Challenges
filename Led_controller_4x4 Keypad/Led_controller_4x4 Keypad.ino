#include <Keypad.h>

const byte ROWS = 4; //four rows
const byte COLS = 4; //four columns


/* 
C1-->9
C2-->8
C3-->7
C4-->6
R1-->5
R2-->4
R3-->3
R4-->2
*/

//define the cymbols on the buttons of the keypads

char hexaKeys[ROWS][COLS] = {
  {'1','2','3','A'},
  {'4','5','6','B'},
  {'7','8','9','c'},
  {'M','0','N','D'}
};
byte rowPins[ROWS] = {5, 4, 3, 2}; //connect to the row pinouts of the keypad
byte colPins[COLS] = {9, 8, 7, 6}; //connect to the column pinouts of the keypad

Keypad customKeypad = Keypad( makeKeymap(hexaKeys), rowPins, colPins, ROWS, COLS); 

#define led 10  //pwm


void setup(){

  Serial.begin(9600);
  pinMode(led,OUTPUT);

}
  
void loop(){

  int customKey = customKeypad.getKey(); //using int will make its ASCII character = its Decimal number

   
  
  // if (customKey){
  //   Serial.println(customKey);}
    switch (customKey) {

      case 57://key 9
        analogWrite(led,255);
        break;
      case 56://key 8
        analogWrite(led,229.5);
        break;
      case 55://key 7
        analogWrite(led,204);
        break;
      case 54://key 6
        analogWrite(led,178.5);
        break;
      case 53://key 5
        analogWrite(led,153);
        break;  
      case 52://key 4
        analogWrite(led,127.5);
        break;
      case 51://key 3
        analogWrite(led,102);
        break;
      case 50://key 2
        analogWrite(led,76.5);
        break;    
      case 49://key 1
        analogWrite(led,25.5);
        break;      
      case 48://key 0
        analogWrite(led,0);
        break;      
       
  }
}