char datas[100];
int i = 0;
unsigned long currentMicros   = 0;
unsigned long previousMicros  = 0; 
const long period   = 5000;

void setup() {
  Serial.begin(115200);
}
void loop() {
  currentMicros = micros();
  if(currentMicros - previousMicros >= period){
    previousMicros = currentMicros;
    int sensor = analogRead(A0);
    sprintf(datas,"%04d",sensor);
    Serial.println(datas);
    Serial.flush();
  }
}
