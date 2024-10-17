def eh_primo(num):
    """Verifica se um número é primo."""
    if num < 2:
        return False
    for divisor in range(2, int(num ** 0.5) + 1):
        if num % divisor == 0:
            return False
    return True

# Gerador de números primos até 50
primos = (num for num in range(2, 51) if eh_primo(num))

# Usando o gerador
for primo in primos:
    print(primo)