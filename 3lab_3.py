#14. Дано ціле число N (> 0). Знайти добуток N! = 1 • 2 • ... • N (N-факторіал). Щоб уникнути
#цілочисельного переповнення, обчислювати цей добуток за допомогою дійсної змінної і вивести його
#як дійсне число.


N = int(input("Введите N >>>>>>>>" ))
factorial = 1
summ = 0
for i in range(1, N+1):
    factorial *= i
    summ += factorial
print(summ)