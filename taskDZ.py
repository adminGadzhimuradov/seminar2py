# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
# а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть,
#  чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, 
# которые нужно перевернуть

n = int(input())
count1 = 0
count2 = 0
for i in range(n):
  x = int(input())
  if x == 0:
   count1 += 1
else:   
    count2 += 1
if count2 > count1:
  print(count1)
else:
  print(count2)
