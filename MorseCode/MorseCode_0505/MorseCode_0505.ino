unsigned long myTime;

long interval = 0, exmoment = 0, nowtime, HoldingTime, hold;

void setup() {
  pinMode(7, INPUT);
  Serial.begin(9600);
}

void loop() {
  nowtime = millis();
  if (digitalRead(7) == 1) {
    interval = exmoment - nowtime;
    Serial.print("間隔時間:"); Serial.println(abs(interval));
    exmoment = nowtime;
  }
  hold = millis();
  while (digitalRead(7) == 1) {}
  HoldingTime = abs(hold - millis());
  Serial.print("持續時間"); Serial.println(abs(HoldingTime));
  Serial.println("=======================");
  while (digitalRead(7) == 0) {}//等待直到開關被放開
}
