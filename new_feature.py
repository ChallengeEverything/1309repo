# Количество корзин с овощами, шт.
baskets = 462
# Средний вес овощей в одной корзине, кг.
average_weight = 25
# Стоимость одного килограмма урожая, в монетах.
price_per_kg = 175


# Допишите функции, которая рассчитывает вес и стоимость урожая.
def calc(baskets, average_weight, price_per_kg):
    total_weight = baskets * average_weight
    total_cost = total_weight * price_per_kg
    return total_weight, total_cost

# Вызовите функцию calc() и обработайте вернувшееся значение.
print_total_weight, print_total_cost = calc(baskets, average_weight, price_per_kg)
# Составьте f-строку и напечатайте её.
print(f'Общий вес урожая: {print_total_weight} кг. Оценённая стоимость урожая: {print_total_cost}.')
