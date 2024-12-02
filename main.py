# cook your dish here
import random
import numpy as np

# Входные параметры
num_cashiers = 3  # Количество работающих касс
processing_time = 5  # Время обработки заказа одного покупателя (в минутах)
average_arrival_time = 2  # Среднее время появления следующего покупателя (в минутах)
simulation_duration = 1000  # Время моделирования (в минутах)

# Выходные величины
customers_served = [0] * num_cashiers
lost_customers = 0

# Функция для генерации времени появления следующего покупателя
def generate_interarrival_time(average_arrival_time):
    return np.random.exponential(average_arrival_time)

# Основная функция моделирования
def simulate_cashier_service(num_cashiers, processing_time, average_arrival_time, simulation_duration):
    global customers_served, lost_customers
    customers_served = [0] * num_cashiers
    lost_customers = 0
    current_time = 0
    next_arrival_time = generate_interarrival_time(average_arrival_time)
    cashier_busy_until = [0] * num_cashiers

    while current_time < simulation_duration:
        if next_arrival_time <= current_time:
            # Появление нового покупателя
            next_arrival_time += generate_interarrival_time(average_arrival_time)
            # Найти свободную кассу
            free_cashier = -1
            for i in range(num_cashiers):
                if cashier_busy_until[i] <= current_time:
                    free_cashier = i
                    break
            if free_cashier != -1:
                # Обслуживание покупателя
                cashier_busy_until[free_cashier] = current_time + processing_time
                customers_served[free_cashier] += 1
            else:
                # Покупатель потерян
                lost_customers += 1
        else:
            # Обновление времени
            current_time += 1

    return customers_served, lost_customers

# Проведение моделирования несколько раз для усреднения результатов
num_simulations = 1000
total_customers_served = [0] * num_cashiers
total_lost_customers = 0

for _ in range(num_simulations):
    served, lost = simulate_cashier_service(num_cashiers, processing_time, average_arrival_time, simulation_duration)
    total_customers_served = [x + y for x, y in zip(total_customers_served, served)]
    total_lost_customers += lost

# Усреднение результатов
average_customers_served = [int(x / num_simulations) for x in total_customers_served]  # Преобразование в целые
average_lost_customers = int(total_lost_customers / num_simulations)  # Преобразование в целое

# Вывод результатов
print("Среднее количество обслуженных покупателей на каждой кассе:", average_customers_served)
print("Среднее количество потерянных покупателей:", average_lost_customers)

# Моделирование различных ситуаций
situations = [
    {"num_cashiers": num_cashiers, "processing_time": 5, "average_arrival_time": 2, "simulation_duration": 1000},
    {"num_cashiers": num_cashiers + 1, "processing_time": 4, "average_arrival_time": 3, "simulation_duration": 1000},
    {"num_cashiers": num_cashiers + 2, "processing_time": 6, "average_arrival_time": 2, "simulation_duration": 1000},
    {"num_cashiers": num_cashiers + 3, "processing_time": 3, "average_arrival_time": 1, "simulation_duration": 1000},
]

for i, situation in enumerate(situations):
    print(f"\nСитуация {i + 1}:")
    num_cashiers = situation["num_cashiers"]
    processing_time = situation["processing_time"]
    average_arrival_time = situation["average_arrival_time"]
    simulation_duration = situation["simulation_duration"]

    total_customers_served = [0] * num_cashiers
    total_lost_customers = 0

    for _ in range(num_simulations):
        served, lost = simulate_cashier_service(num_cashiers, processing_time, average_arrival_time, simulation_duration)
        total_customers_served = [x + y for x, y in zip(total_customers_served, served)]
        total_lost_customers += lost

    average_customers_served = [int(x / num_simulations) for x in total_customers_served]  # Преобразование в целые
    average_lost_customers = int(total_lost_customers / num_simulations)  # Преобразование в целое

    print("Среднее количество обслуженных покупателей на каждой кассе:", average_customers_served)
    print("Среднее количество потерянных покупателей:", average_lost_customers)
