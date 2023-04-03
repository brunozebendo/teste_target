def fibonacci(n):
    if n <= 1:
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))

num = int(input("Digite um número inteiro positivo: "))

if num <= 0:
    print("Por favor, digite um número maior que zero.")
else:
    print("Sequência de Fibonacci:")
    for i in range(num):
        print(fibonacci(i), end=" ")
        if fibonacci(i) == num:
            print("\nO número pertence à sequência de Fibonacci.")
            break
    else:
        print("\nO número não pertence à sequência de Fibonacci.")


