import random
import math

# Генерируем последовательность из 5 случайных целых чисел и случайное число с плавающей запятой
int_seq = [random.randint(0, 100) for _ in range(5)]
float_random = random.uniform(0, 1)

# Выводим сгенерированные переменные
print("Сгенерированная последовательность:", int_seq)
print("Сгенерированное число с плавающей запятой:", float_random)

# Находим максимальный элемент и выполняем операции с ним
int_seq_max = max(int_seq)
floor_div_result = int(int_seq_max // float_random)
factorial_result = math.factorial(floor_div_result)

# Выводим результаты
print("Максимальный элемент:", int_seq_max)
print("Результат целочисленного деления:", floor_div_result)
print("Факториал результата:", factorial_result)
