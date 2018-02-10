/*
 Name:		GameBones.ino
 Created:	05.06.2017 19:06:40
 Author:	m0ln1a
*/

#include "LiquidCrystal.h"
LiquidCrystal lcd(4, 5, 10, 11, 12, 13);

void setup()
{
	lcd.begin(16, 2); // Инициализация экрана
	lcd.print("BONES!");  // Пишем название игры в первой строке
}

void loop()
{
	lcd.setCursor(0, 1);
	lcd.print(random(1, 6));
	lcd.print("    ");
	lcd.print(random(1, 6));
}
