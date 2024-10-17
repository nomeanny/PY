def gerador_primos(n):
    """Um gerador que produz números primos até n."""
    for num in range(2, n):
        eh_primo = True
        for divisor in range(2, int(num ** 0.5) + 1):
            if num % divisor == 0:
                eh_primo = False
                break
        if eh_primo:
            yield num  # Produz o número primo encontrado

# Usando o gerador
for primo in gerador_primos(20):
    print(primo)