# 금액
n = 1260
count = 0

# 동전 종류
coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n // coin # 동전 개수 카운팅
    n %= coin
    
print(count)
