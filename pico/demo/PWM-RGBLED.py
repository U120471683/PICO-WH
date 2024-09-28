#define I_RED_PIN A0  // 紅色輸入腳位
#define I_GREEN_PIN A1  // 綠色輸入腳位
#define I_BLUE_PIN A2  // 藍色輸入腳位
#define O_RED_PIN 2 // 紅色輸出腳位
#define O_GREEN_PIN 3 // 綠色輸出腳位
#define O_BLUE_PIN 5  // 藍色輸出腳位

byte rPin;
byte gPin;
byte bPin;

void setup() {
  // 初始化序列通訊
  Serial.begin(9600);
  // 設定輸出腳位
  pinMode(O_RED_PIN, OUTPUT);
  pinMode(O_GREEN_PIN, OUTPUT);
  pinMode(O_BLUE_PIN, OUTPUT);
}

void loop() {
  // 重複執行主要程式碼
  readSensor();
  outputSensor();
  delay(100);
}

void readSensor() {
  // 讀取紅色輸入值並映射到0-255範圍
  int r = analogRead(I_RED_PIN);
  rPin = map(r, 0, 1023, 0, 255);
  Serial.println(rPin);
  
  // 讀取綠色輸入值並映射到0-255範圍
  int g = analogRead(I_GREEN_PIN);
  gPin = map(g, 0, 1023, 0, 255);
  Serial.println(gPin);
  
  // 讀取藍色輸入值並映射到0-255範圍
  int b = analogRead(I_BLUE_PIN);
  bPin = map(b, 0, 1023, 0, 255);
  Serial.println(bPin);
}

void outputSensor() {
  // 將映射後的值輸出到對應的腳位
  analogWrite(O_RED_PIN, rPin);
  analogWrite(O_GREEN_PIN, gPin);
  analogWrite(O_BLUE_PIN, bPin);
}