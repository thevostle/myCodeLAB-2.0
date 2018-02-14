import time
input("\nЗдрасьте, я решатель сложных примеров 2000! Для начала работы нажмите Enter...")
while True:
    x = float(input("\nВведите первое число: "))
    y = float(input("Введите второе число: "))
    znak = str(input("Введите операцию (+, -, *, /): "))
    ans = 0
    if znak == "+":
        ans = x + y
    if znak == "-":
        ans = x - y
    if znak == "*":
        ans = x * y
    if znak == "/":
        ans = x / y
    print("Ответ: " + str(ans))
    m = str(input())
    if m == " ":
        break
    
x = float(input("\nВведите первое число: "))
y = float(input("Введите второе число: "))
znak = str(input("Введите операцию (+, -, *, /): "))
time.sleep(4)
if znak == "/" and y == 0:
    print("\nНЕЛЬЗЯ НА НОЛЬ ДЕЛИТЬ!")
else:
    print("\nСАМ ТАКИЕ ПРИМЕРЫ РЕШАЙ!")
