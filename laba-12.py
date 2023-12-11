#30. Вычислить сумму знакопеременного ряда |х*2n!|/(2n)!,
# где х-матрица размера к (к и матрица задаются случайным образом), n - номер слагаемого.
# #Сумма считается вычисленной, если точность вычислений будет не меньше t знаков после запятой.
# У алгоритма д.б. линейная сложность. Знак первого слагаемого  -.

import numpy as np

def result_sum(det_x, t):
    n = 1  # Начальное значение
    fact_chislitel = 1 # Начальный факториал
    fact_znamenatel = 1
    current_sum = 0  # Инициализация текущей суммы
    det_x_times_fact = det_x * (2 * (fact_chislitel*n))
    # Добавляем первый элемент с отрицательным знаком
    first_term = (-1) * det_x_times_fact / fact_znamenatel * (2*n)
    current_sum += first_term

    while True:
        n += 1
        fact_znamenatel = fact_znamenatel * (2*n) # Вычисляем факториал в знаменателе
        fact_chislitel = fact_chislitel*n # Вычисляем факториал в числителе
        term = det_x_times_fact / fact_znamenatel # Вычисляем очередное слагаемое
        if n % 2 == 0:
            current_sum += term  # Добавляем слагаемое с положительным знаком
        else:
            current_sum -= term  # Добавляем слагаемое с отрицательным знаком

        if abs(term) < t:  # Проверяем точность
            break

    return current_sum

while True:
    t = input("Введите желаемую точность вычислений (не равную нулю): ")
    try:
        t = int(t)
        if t == 0:
            print("Ошибка: значение точности не может быть равным нулю. Пожалуйста, введите другое значение.")
        else:
            break
    except ValueError:
        print("Ошибка: введите число")

k = np.random.randint(2, 6)
random_matrix = np.random.uniform(-1, 1, (k, k))
print("Сгенерирована матрица:\n", random_matrix)

det_x = np.linalg.det(random_matrix)
result = result_sum(det_x, t)

precision_format = "{:." + str(int(t)) + "f}"
print(f"Сумма знакопеременного ряда: {precision_format.format(result)}")