void setup()
{
  Serial.begin(9600);
}
String str;
void loop()
{
 str=Serial.readStringUntil('\n');
 Serial.write(str);
}
