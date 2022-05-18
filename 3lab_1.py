#4. Дано ціле n> 2. Вивести всі прості числа з діапазону [2, n]


sushu=[]
n = int(input())
for i in range(2,n):
    for j in  range (2,i):
        if i%j==0:
           break

    else:
        sushu.append(i)

print(sushu)


