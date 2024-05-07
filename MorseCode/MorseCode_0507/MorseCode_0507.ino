unsigned long myTime;

long interval = 0, exmoment = 0, nowtime, HoldingTime, hold, tem[5];
int avg, world[5];


void setup() {
  pinMode(7, INPUT);
  Serial.begin(9600);
  Serial.println("=====start=====");
  delay(500);
}

void loop() {
  for (int i = 0; i != 5; i++) {
    nowtime = millis();
    while (digitalRead(7) == 0) {}//等待直到開關被放開
    if (digitalRead(7) == 1) {
      interval = exmoment - nowtime;
      Serial.print("間隔時間:"); Serial.println(abs(interval));
      exmoment = nowtime;
    }
    hold = millis();
    while (digitalRead(7) == 1) {}
    HoldingTime = abs(hold - millis());
    Serial.print("持續時間"); Serial.println(abs(HoldingTime));
    tem[i] = abs(HoldingTime);
    Serial.println("=======================");
  }
  int sum;
  for (int i = 0; i != 5; i++) {
    sum = sum + tem[i];
  }
  avg = sum / 5;
  Serial.println("");
  for (int i = 0; i != 5; i++) {
    /*
      if (tem[i] > avg) {
      world[i] = 1;
    */
    if (tem[i] > 300) {
      world[i] = 1;
    } else {
      world[i] = 0;
    }
  }
  Serial.print("----> world:"); for (int i = 0; i != 5; i++) {
    Serial.print(world[i]); Serial.print(",");
  }
  while (1) {}
}

