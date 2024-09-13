def assess_yield(number_of_plants, average_weight):
    # Ваш код здесь
    total_weight_in_gramms = number_of_plants * average_weight
    total_weight_in_kilos = total_weight_in_gramms / 1000

    if total_weight_in_kilos > 100:
        message = 'Ожидается отличный урожай.'
    elif total_weight_in_kilos > 50:
        message = 'Ожидается хороший урожай.'
    elif total_weight_in_kilos > 0:
        message = 'Урожай будет так себе.'
    else:
        message = 'Урожая не будет.'

    return total_weight_in_kilos, message

# Пример вызова функции
# Вызываем функцию и распаковываем кортеж:
total_weight, rating = assess_yield(50, 200)

# Печатаем результат:
print(total_weight, 'кг.', rating)
