#18/Дано ціле число N (> 0). Використовуючи операції ділення без остачі і взяття залишку від
#ділення, вивести всі його цифри, починаючи з самої правої (розряду одиниць).


import math
print('введите любое число:  ' )
N = int(input())
while 0< int(N):
    print(int(math.fmod(N, 10)))
    N /= 10
