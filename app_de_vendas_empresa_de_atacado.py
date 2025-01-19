print("Bem-vindo a Loja do Vitor Filipe! ")

valor_unitario = float(input("\nEntre com o Valor do Produto:"))
quantidade = int(input("Entre com a Quantidade do Produto:" ))

valor_sem_desconto = valor_unitario * quantidade

if valor_sem_desconto < 2500:
    desconto = 0
elif 2500 <= valor_sem_desconto < 6000:  
    desconto = 0.04
elif 6000 <= valor_sem_desconto < 10000:
    desconto = 0.07
else:
    desconto = 0.11

valor_do_desconto = valor_sem_desconto * desconto
valor_total = valor_sem_desconto - valor_do_desconto

print(f"\nValor total sem desconto: R${valor_sem_desconto:.2f}")
print(f"Valor total com desconto: R${valor_total:.2f}")