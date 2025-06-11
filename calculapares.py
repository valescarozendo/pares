inicio = int(input("Digite o número inicial do intervalo: "))
fim = int(input("Digite o número final do intervalo: "))

soma_pares = 0
tem_pares = False  # Variável para verificar se há números pares no intervalo

for numero in range(inicio, fim + 1):
    if numero % 2 == 0:
        soma_pares += numero
        tem_pares = True

if tem_pares:
    print(f"A soma dos números pares no intervalo é: {soma_pares}")
else:
    print("Não há números pares no intervalo.")