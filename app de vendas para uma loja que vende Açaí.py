print("Bem-vindo à Loja de Gelatos do Vitor Filipe")

print("---------------Cardápio----------------")
print("---------------------------------------")
print("--| Tamanho | Cupuaçu(CP) | Açai(AC)|--")
print("--|    P    |   R$ 9,00   | R$ 11,00|--")
print("--|    M    |   R$ 14,00  | R$ 16,00|--")
print("--|    G    |   R$ 18,00  | R$ 20,00|--")
print("---------------------------------------")

total = 0

while True:
    while True:
        sabor = input("\nEntre com o sabor desejado (CP/AC): ").upper()
        if sabor in ['CP', 'AC']:
            break
        print("Sabor inválido. Tente novamente.")

    while True:
        tamanho = input("Entre com o tamanho desejado (P, M, G): ").upper()
        if tamanho in ['P', 'M', 'G']:
            break
        print("Tamanho inválido. Tente novamente.")

    if sabor == 'CP':
        if tamanho == 'P':
            valor_pedido = 9
            descricao = "Cupuaçu tamanho P"
        elif tamanho == 'M':
            valor_pedido = 14
            descricao = "Cupuaçu tamanho M"
        elif tamanho == 'G':
            valor_pedido = 18
            descricao = "Cupuaçu tamanho G"
    elif sabor == 'AC':
        if tamanho == 'P':
            valor_pedido = 11
            descricao = "Açaí tamanho P"
        elif tamanho == 'M':
            valor_pedido = 16
            descricao = "Açaí tamanho M"
        elif tamanho == 'G':
            valor_pedido = 20
            descricao = "Açaí tamanho G"

    total += valor_pedido

    print(f"Você pediu um {descricao}: R$ {valor_pedido:.2f}")

    mais_pedidos = input("\nDeseja mais alguma coisa? (S/N): ").upper()
    if mais_pedidos != 'S':
        break

print(f"Valor total dos pedidos: R${total:.2f}")