from collections import Counter


def sell_shoes(shoes, customer_orders):
    money = 0
    c_shoes = Counter(shoes)
    for customer_order in customer_orders:
        if not customer_order[0] in c_shoes.keys():
            continue
        money += customer_order[1]
        c_shoes -= Counter({ customer_order[0]: 1})
    return money


if __name__ == '__main__':
    n = int(input())
    shoes = Counter(map(int, input().split()))
    customer_count = int(input())
    customer_orders = []
    for _ in range(customer_count):
        customer_orders.append(tuple(map(int, input().split())))

    print(sell_shoes(shoes, customer_orders))
