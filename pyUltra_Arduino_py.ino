int echoPin = 6;
int trigPin = 7;
long int duration;
float distance;

void setup(){
 pinMode(echoPin, INPUT);
 pinMode(trigPin, OUTPUT);
 Serial.begin(9600);
 
}

void loop(){
digitalWrite(trigPin, HIGH);
delay(3);
digitalWrite(trigPin, LOW);
delay(2);
duration = pulseIn(echoPin,HIGH);
distance = duration * 0.017;
Serial.println(distance);
delay(1);









}
