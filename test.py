
def fib():
    fibo = [0, 1, 1]
    while True:
        yield fibo[2]
        fibo[1] = fibo[2]
        fibo[2] = fibo[1] + fibo[0]
        fibo[0] = fibo[1]



'''


0 1 1 2 3 5

1 1 2 3 5 8

0 -> 1

1 -> 1 

1 -> 2

2 -> 3
'''
fibs = fib()

for i in fibs:
    print(i)