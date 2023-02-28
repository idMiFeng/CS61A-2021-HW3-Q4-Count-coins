def descending_coin(coin):
    if coin == 25:
        return 10
    elif coin == 10:
        return 5
    elif coin == 5:
        return 1

def count_coins(change):
    def f(n,m):
        if n<0:
            return 0
        elif n==0:
            return 1
        elif m==1:
            return 1
        else:
            return f(n,descending_coin(m))+f(n-m,m)
    return f(change,25)

print(f"count_coins(15)'s value is {count_coins(15)}")