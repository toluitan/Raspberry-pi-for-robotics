int echoPin = 6;

int trigPin = 7;

int LED_pin = 8;

int duration;

double distance;

void setup(){
  
  pinMode(echoPin, INPUT);
  
  pinMode(trigPin, OUTPUT);
  
  Serial.begin(9600);

}

void loop(){
  
  digitalWrite(trigPin, HIGH);
  
  digitalWrite(trigPin, LOW);
  
  duration = pulseIn(echoPin, HIGH);
  
  distance = duration * 0.017;
  
  Serial.println(distance);










}

