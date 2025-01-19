print("Bem-vindo a copiadora do Vitor Filipe!")


def escolha_servico():
    while True:
        print("\nEscolha o tipo serviço desejado:")
        print("DIG - Digitalização")
        print("ICO - Impressão Colorida")
        print("IPB - Impressão Preto e Branco")
        print("FOT - Fotocópia")
        servico = input("Digite a opção de serviço: ").upper()


        if servico == "DIG":
            return 1.10
        elif servico == "ICO":
            return 1.00
        elif servico == "IPB":
            return 0.40
        elif servico == "FOT":
            return 0.20
        else:
            print("Escolha invalida, entre com o tipo de serviço novamente")


def num_pagina():
    while True:
        try:
            paginas = int(input("\nEntre com o numero de páginas: "))
            if paginas >= 20000:
                print("Não aceitamos tantas páginas de uma vez.")
                print("Por favor entre com o numero de páginas novamente.")
            elif paginas < 20:
                return paginas
            elif 20 <= paginas < 200:
                return paginas * 0.85
            elif 200 <= paginas < 2000:
                return paginas * 0.80
            elif 2000 <= paginas < 20000:
                return paginas * 0.75
        except ValueError:
            print("Valor não numérico. Tente novamente.")


def servico_extra():
    while True:
        print("\n Deseja adicionar algum serviço? ")
        print("1 - Encadernação simples - R$ 15,00")
        print("2 - Encadernação capa dura - R$ 40,00")
        print("0 - Não desejo mais nada")
        extra = input("Digite a opção de serviço extra: ")


        if extra == "1":
            return 15.00
        elif extra == "2":
            return 40.00
        elif extra == "0":
            return 0.00
        else:
            print("Opção inválida. Tente novamente.")


servico_valor = escolha_servico()
paginas = num_pagina()
extra_valor = servico_extra()
total = (servico_valor * paginas) + extra_valor


print(f"Total: R$ {total:.2f} Serviço: {servico_valor:.2f} * {paginas} páginas + "
   f"R$ {extra_valor:.2f} serviço extra")