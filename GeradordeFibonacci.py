#Gerador de Fibonacci
def fibonacci(n):
    """Um gerador que produz a sequência de Fibonacci"""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

#Usando o gerador de Fibonacci
for num in fibonacci(10):
    print(num)