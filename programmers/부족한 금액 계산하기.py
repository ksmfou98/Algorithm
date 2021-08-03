def solution(price, money, count):
    store = sum([price*i for i in range(1, count+1)])
    return 0 if store <= money else store-money