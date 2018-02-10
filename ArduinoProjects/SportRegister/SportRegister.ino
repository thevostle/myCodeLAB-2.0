/*
 Name:		SportRegister.ino
 Created:	05.06.2017 18:30:46
 Author:	m0ln1a
*/

///////////  1 ðåæèì áåñêîíå÷íûé 
///////////  2 ðåæèì 9 î÷êîâ
///////////  3 ðåæèì 21 î÷êî

#include "OneButton.h"
#include <LiquidCrystal.h>                // Áèáëèîòåêà LCD
LiquidCrystal lcd(13, 12, 11, 10, 9, 8);

OneButton button1(14, true);
OneButton button2(15, true);
OneButton button3(16, true);    // Êíîïêà ðåæèìîâ

#define  LED1  6                // ñâåòèê ïîáåäèòåëÿ 1
#define  LED2  7               // ñâåòèê ïîáåäèòåëÿ 2
#define  BUZZ  8                // äèíàìèê

int  P1 = 0;                    // Ñ÷¸ò ïåðâîãî èãðîêà
int  P2 = 0;                    // Ñ÷åò âòîðîãî èãðîêà
int backLight = 3;
byte regim = 1;

void setup()
{
	button1.attachClick(Click1);
	button2.attachClick(Click2);
	button3.attachClick(Click3);
	button3.attachLongPressStart(LongPressStart3);  // äëèòåëüíîå íàæàòèå
	pinMode(backLight, OUTPUT);
	pinMode(LED1, OUTPUT);
	pinMode(LED2, OUTPUT);
	pinMode(BUZZ, OUTPUT);
	digitalWrite(backLight, HIGH);
	lcd.begin(16, 2);
	lcd.clear(); //  î÷èùàåì äèñïëåé
	lcd.setCursor(0, 0);
	lcd.print("R  P1");
	lcd.setCursor(3, 1);
	lcd.print("P2");
}

void loop()
{
	button1.tick();
	button2.tick();
	button3.tick();

	lcd.setCursor(6, 0);                      // Ïå÷àòü ñ÷åòà 1 èãðîêà
	lcd.print(P1);
	lcd.print(" ");
	lcd.setCursor(0, 1);                    // êàêîé ñåé÷àñ ðåæèì
	lcd.print(regim);
	lcd.setCursor(6, 1);
	lcd.print(P2);                          // Ïå÷àòü ñ÷åòà 2 èãðîêà
	lcd.print(" ");
}

void Click1()
{
	P1 = P1 + 1;
	if (P1 >= 9 && regim == 2 && P1 > P2)
	{
		END1();
	}
	if (P1 >= 21 && regim == 3 && P1 > P2)
	{
		END1();
	}
}

void Click2()
{
	P2 = P2 + 1;
	if (P2 >= 9 && regim == 2 && P2 > P1)
	{
		END2();
	}
	if (P2 >= 21 && regim == 3 && P2 > P1)
	{
		END2();
	}
}

void Click3()
{
	regim++;
	if (regim > 3)
	{
		regim = 1;
	}
}
void LongPressStart3()
{
	P1 = 0;
	P2 = 0;
}

void END1()
{
	lcd.setCursor(10, 0);
	lcd.print("Game");
	lcd.setCursor(10, 1);
	lcd.print("Over");
	digitalWrite(LED2, HIGH);
	digitalWrite(LED1, LOW);
	digitalWrite(BUZZ, HIGH);
	delay(1000);
	lcd.setCursor(10, 0);
	lcd.print("    ");
	lcd.setCursor(10, 1);
	lcd.print("    ");
	digitalWrite(LED1, LOW);
	digitalWrite(LED2, LOW);
	digitalWrite(BUZZ, LOW);
	delay(1000);
	lcd.setCursor(10, 0);
	lcd.print("Game");
	lcd.setCursor(10, 1);
	lcd.print("Over");
	digitalWrite(LED2, HIGH);
	digitalWrite(LED1, LOW);
	digitalWrite(BUZZ, HIGH);
	delay(1000);
	lcd.setCursor(10, 0);
	lcd.print("    ");
	lcd.setCursor(10, 1);
	lcd.print("    ");
	digitalWrite(LED1, LOW);
	digitalWrite(LED2, LOW);
	digitalWrite(BUZZ, LOW);
	delay(1000);
	lcd.setCursor(10, 0);
	lcd.print("Game");
	lcd.setCursor(10, 1);
	lcd.print("Over");
	digitalWrite(LED2, HIGH);
	digitalWrite(LED1, LOW);
	digitalWrite(BUZZ, HIGH);
	delay(1000);
	lcd.setCursor(10, 0);
	lcd.print("    ");
	lcd.setCursor(10, 1);
	lcd.print("    ");
	digitalWrite(LED1, LOW);
	digitalWrite(LED2, LOW);
	digitalWrite(BUZZ, LOW);
	P1 = 0;
	P2 = 0;
}
void END2()
{
	lcd.setCursor(10, 0);
	lcd.print("Game");
	lcd.setCursor(10, 1);
	lcd.print("Over");
	digitalWrite(LED2, HIGH);
	digitalWrite(LED1, LOW);
	digitalWrite(BUZZ, HIGH);
	delay(1000);
	lcd.setCursor(10, 0);
	lcd.print("    ");
	lcd.setCursor(10, 1);
	lcd.print("    ");
	digitalWrite(LED1, LOW);
	digitalWrite(LED2, LOW);
	digitalWrite(BUZZ, LOW);
	delay(1000);
	lcd.setCursor(10, 0);
	lcd.print("Game");
	lcd.setCursor(10, 1);
	lcd.print("Over");
	digitalWrite(LED2, HIGH);
	digitalWrite(LED1, LOW);
	digitalWrite(BUZZ, HIGH);
	delay(1000);
	lcd.setCursor(10, 0);
	lcd.print("    ");
	lcd.setCursor(10, 1);
	lcd.print("    ");
	digitalWrite(LED1, LOW);
	digitalWrite(LED2, LOW);
	digitalWrite(BUZZ, LOW);
	delay(1000);
	lcd.setCursor(10, 0);
	lcd.print("Game");
	lcd.setCursor(10, 1);
	lcd.print("Over");
	digitalWrite(LED2, HIGH);
	digitalWrite(LED1, LOW);
	digitalWrite(BUZZ, HIGH);
	delay(1000);
	lcd.setCursor(10, 0);
	lcd.print("    ");
	lcd.setCursor(10, 1);
	lcd.print("    ");
	digitalWrite(LED1, LOW);
	digitalWrite(LED2, LOW);
	digitalWrite(BUZZ, LOW);
	P1 = 0;
	P2 = 0;
}
