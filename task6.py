def greedy_algorithm(items, budget):
    items_ratio = {item: (value['calories'] / value['cost'])
                   for item, value in items.items()}

    sorted_items = sorted(items_ratio.items(),
                          key=lambda x: x[1], reverse=True)

    total_cost = 0
    total_calories = 0
    selected_items = []

    for item, ratio in sorted_items:
        if total_cost + items[item]['cost'] <= budget:
            total_cost += items[item]['cost']
            total_calories += items[item]['calories']
            selected_items.append(item)

    return selected_items, total_calories


def dynamic_programming(items, budget):
    item_list = list(items.keys())
    n = len(item_list)
    dp = [[0 for x in range(budget + 1)] for x in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, budget + 1):
            if items[item_list[i-1]]['cost'] <= w:
                dp[i][w] = max(dp[i-1][w],
                               dp[i-1][w - items[item_list[i-1]]['cost']] +
                               items[item_list[i-1]]['calories'])
            else:
                dp[i][w] = dp[i-1][w]

    w = budget
    selected_items = []

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            selected_items.append(item_list[i-1])
            w -= items[item_list[i-1]]['cost']

    total_calories = dp[n][budget]
    return selected_items[::-1], total_calories


if __name__ == "__main__":
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350}
    }

    budget = 75
    greedy_result = greedy_algorithm(items, budget)
    dp_result = dynamic_programming(items, budget)

    print(f'{"budget":20} : {budget}')
    print(f'{"greedy_result":20} : {greedy_result}')
    print(f'{"dp_result":20} : {dp_result}')
