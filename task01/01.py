
def find_coins_greedy(amount, coins):
    result = {}
    for coin in sorted(coins, reverse=True):
        if amount >= coin:
            count = amount // coin
            result[coin] = count
            amount -= count * coin
    return result

# Приклад використання
coins = [50, 25, 10, 5, 2, 1]
amount = 113
result_greedy = find_coins_greedy(amount, coins)
print("Жадібний алгоритм:", result_greedy)  # Виведе: {50: 2, 10: 1, 2: 1, 1: 1}


def find_min_coins(amount, coins):
    # Ініціалізуємо таблицю мінімальної кількості монет для кожної суми
    min_coins = [float('inf')] * (amount + 1)
    min_coins[0] = 0

    # Ініціалізуємо таблицю для збереження номіналів монет
    coin_used = [None] * (amount + 1)

    # Заповнюємо таблицю мінімальної кількості монет
    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin and min_coins[i - coin] + 1 < min_coins[i]:
                min_coins[i] = min_coins[i - coin] + 1
                coin_used[i] = coin

    # Визначаємо, які монети було використано
    result = {}
    remaining_amount = amount
    while remaining_amount > 0:
        coin = coin_used[remaining_amount]
        if coin is None:
            return {}  # Немає рішення
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        remaining_amount -= coin

    return dict(sorted(result.items()))

# Приклад використання
result_dp = find_min_coins(amount, coins)
print("Динамічне програмування:", result_dp)  # Виведе: {1: 1, 2: 1, 10: 1, 50: 2}


import timeit

# Функції для тестування
def test_greedy():
    find_coins_greedy(amount_large, coins)

def test_dp():
    find_min_coins(amount_large, coins)

# Великі суми для тестування
amount_large = 1000000  # Сума в 1 мільйон

# Тестування продуктивності
time_greedy = timeit.timeit(test_greedy, number=1)
time_dp = timeit.timeit(test_dp, number=1)

print(f"Час виконання жадібного алгоритму: {time_greedy:.5f} секунд")
print(f"Час виконання алгоритму динамічного програмування: {time_dp:.5f} секунд")
