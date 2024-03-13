const int buzzerPin = 9;
const int ledPin = 13;

void setup() {
  pinMode(buzzerPin, OUTPUT); 
  pinMode(ledPin, OUTPUT); 
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) { 
    char receivedChar = Serial.read();

    if (receivedChar == 'Y' || receivedChar == 'y') {
      tone(buzzerPin, 6000); 
      digitalWrite(ledPin, HIGH);
      delay(100);      
      noTone(buzzerPin);   
      digitalWrite(ledPin, LOW);
      delay(100);   
    }
  }
}
