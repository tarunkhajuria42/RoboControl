#include <math.h>
int mot1p=3, mot1d=22, mot2p=4, mot2d=23,cam1d=24, cam1p=5, cam2d=25, cam2p=6, pld=26, plp=7, act1p=8, act1d=27, act2p=9, act2d=28, dgLp=10, 
dgLd=29, dgRp=11, dgRd=30, effp=12, effd=31;
void setup()
{
  pinMode( mot1p, OUTPUT);
  pinMode( mot1d, OUTPUT);
  pinMode( mot2p, OUTPUT);
  pinMode( mot2d, OUTPUT);
  pinMode( cam1d, OUTPUT);
  pinMode( cam1p, OUTPUT);
  pinMode( cam2d, OUTPUT);
  pinMode( cam2p, OUTPUT);
  pinMode( plp, OUTPUT);
  pinMode( pld, OUTPUT);
  pinMode( act1p, OUTPUT);
  pinMode( act1d, OUTPUT);
  pinMode( act2p, OUTPUT);
  pinMode( act2d, OUTPUT);
  pinMode( dgLp, OUTPUT);
  pinMode( dgLd, OUTPUT);
  pinMode( dgRp, OUTPUT);
  pinMode( dgRd, OUTPUT);
  pinMode( effp, OUTPUT);
  pinMode( effd, OUTPUT);
  
  digitalWrite( mot1p, LOW);
  digitalWrite( mot1d, LOW);
  digitalWrite( mot2p, LOW);
  digitalWrite( mot2d, LOW);
  digitalWrite( cam1d, LOW);
  digitalWrite( cam1p, LOW);
  digitalWrite( cam2d, LOW);
  digitalWrite( cam2p, LOW);
  digitalWrite( plp, LOW);
  digitalWrite( pld, LOW);
  digitalWrite( act1p, LOW);
  digitalWrite( act1d, LOW);
  digitalWrite( act2p, LOW);
  digitalWrite( act2d, LOW);
  digitalWrite( dgLp, LOW);
  digitalWrite( dgLd, LOW);
  digitalWrite( dgRp, LOW);
  digitalWrite( dgRd, LOW);
  digitalWrite( effp, LOW);
  digitalWrite( effd, LOW);
}



void loop()
{
  
  char a;
  a=Serial.read();
 if(a==8)
   left();
   else if(a==9)
   right();
   else if(a==10)
   lrstop();
   else if(a==14)
   camleft();
   else if(a==17)
   camright();
   else if(a==20)
   camlrstop();
   else if(a==23)
   camlrstop();
   else if(a==15)
   camup();
   else if(a==16)
   camdown();
   else if(a==21)
   camudstop();
   else if(a==22)
   camudstop();
   else if(a==37)
   plleft();
   else if(a==38)
   plright();
   else if(a==39)
   pllrstop();
   else if(a==47)
   act1up();
   else if(a==46)
   act1down();
   else if(a==53)
   act1stop();
   else if(a==52)
   act1stop();
   else if(a==48)
   act2up();
   else if(a==49)
   act2down();
   else if(a==55)
   act2stop();
   else if(a==54)
   act2stop();
   else if(a==43)
   dgup();
   else if(a==44)
   dgdown();
   else if(a==45)
   dgudstop();
   else if(a==41)
   dgCW();
   else if(a==40)
   dgACW();
   else if(a==42)
   dgCWACWstop();
   else if(a==51)
   effopen();
   else if(a==50)
   effclose();
   else if(a==57)
   effstop();
   else if(a==56)
   effstop();
   else if(a>57 && a<156)
   {
     sig=a-57
     sig=round(sig*255/(155-57));
     //analogWrite(PinNO,sig) write your pinno here for forward signal
     //Make the opposite one low
   }
   else if(a>156 && a<255)
   {
     sig=a-156
     sig=round(sig*255/(254-156));  
     //analogWrite(PinNO,sig) write your pinno here for back signal
     //Make the opposite one low
   }
}
void left()
{ digitalWrite(mot1d, LOW);
  analogWrite(mot1p, 255);
  digitalWrite(mot2d, HIGH);
  analogWrite(mot2p, 255);
}
void right()
{ digitalWrite(mot2d, LOW);
  analogWrite(mot2p, 255);
  digitalWrite(mot1d, HIGH);
  analogWrite(mot1p, 255);
}
void lrstop()
{ digitalWrite(mot1d, LOW);
  analogWrite(mot1p, 0);
  digitalWrite(mot2d, LOW);
  analogWrite(mot2p, 0);
}
void camleft()
{
  digitalWrite( cam1d, LOW);
  analogWrite( cam1p, 255);
}
void camright()
{
  digitalWrite( cam1d, HIGH);
  analogWrite( cam1p, 255);
}
void camlrstop()
{
  digitalWrite( cam1d, LOW);
  analogWrite( cam1p, 0);
}
void camup()
   {
  digitalWrite( cam2d, HIGH);
  analogWrite( cam2p, 255);
}

void camdown()
   {
  digitalWrite( cam2d, LOW);
  analogWrite( cam2p, 255);
}
void camudstop()
   {
  digitalWrite( cam2d, HIGH);
  analogWrite( cam2p, 0);
}

void plleft()
{
  digitalWrite(pld, LOW);
  analogWrite( plp, 255);
}  
void plright()
{
  digitalWrite(pld, HIGH);
  analogWrite( plp, 255);
}  
void pllrstop()
{
  digitalWrite(pld, LOW);
  analogWrite( plp, 0);
}
void act1up()
{
  digitalWrite(act1d, HIGH);
  analogWrite( act1p, 255);
}
void act1down()
{
  digitalWrite(act1d, LOW);
  analogWrite( act1p, 255);
}
void act1stop()
{
  digitalWrite(act1d, HIGH);
  analogWrite( act1p, 0);
}
void act2up()
{
  digitalWrite(act2d, HIGH);
  analogWrite( act2p, 255);
}
void act2down()
{
  digitalWrite(act2d, LOW);
  analogWrite( act2p, 255);
}
void act2stop()
{
  digitalWrite(act2d, HIGH);
  analogWrite( act2p, 0);
}

void dgup()
{ 
  digitalWrite(dgLd, HIGH);
  analogWrite( dgLp, 255);
  digitalWrite(dgRd, HIGH);
  analogWrite( dgRp, 255);
}
void dgdown()
{ 
  digitalWrite(dgLd, LOW);
  analogWrite( dgLp, 255);
  digitalWrite(dgRd, LOW);
  analogWrite( dgRp, 255);
}
void dgudstop()
{ 
 digitalWrite(dgLd, HIGH);
  analogWrite( dgLp, 0);
  digitalWrite(dgRd, HIGH);
  analogWrite( dgRp, 0);
}

void dgCW()
{ 
  digitalWrite(dgLd, LOW);
  analogWrite( dgLp, 255);
  digitalWrite(dgRd, HIGH);
  analogWrite( dgRp, 255);
}
void dgACW()
{ 
  digitalWrite(dgLd, HIGH);
  analogWrite( dgLp, 255);
  digitalWrite(dgRd, LOW);
  analogWrite( dgRp, 255);
}
void dgCWACWstop()
{ 
  digitalWrite(dgLd, LOW);
  analogWrite( dgLp, 0);
  digitalWrite(dgRd, HIGH);
  analogWrite( dgRp, 0);
}
void effopen()
{
 digitalWrite(effd, HIGH);
 analogWrite( effp, 255);
}
void effclose()
{
 digitalWrite(effd, LOW);
 analogWrite( effp, 255);
}
void effstop()
{
 digitalWrite(effd, HIGH);
 analogWrite( effp, 0);
}

