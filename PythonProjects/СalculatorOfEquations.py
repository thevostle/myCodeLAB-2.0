import math
import matplotlib.pyplot as plt
countX = int(input())
countY = int(input())
Ans = int(input())
rX = []
rY = []
answer = {}
for x in range(Ans):  # все возможные варианты ответа
    rX.append(x)
    rY.append(x)
for r in range((Ans) ** 2):  # решение
    for X in rX:
        for Y in rY:
            if countX * X + countY * Y == Ans:
                answer[X] = Y
x = list(answer.keys())
y = list(answer.values())
print('X: Y' + str(answer))
print("Количество решений: " + str(len(answer)))
print(x)
print(y)
line = plt.plot(x, y)
plt.ylabel("Количество целочисленных решений: " + str(len(answer)))
plt.show() # Покажем окно с нарисованным графиком
