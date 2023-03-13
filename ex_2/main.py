def calcular_total_pedido(codigos_pedidos):
    """
    Calcula o valor total de um pedido, dado uma lista de códigos de produtos.

    Args:
        codigos_pedidos (List[int]): Lista contendo os códigos dos produtos pedidos.

    Returns:
        float: Valor total do pedido.
    """
    # Dicionário contendo as informações sobre os produtos disponíveis no cardápio
    cardapio = {
        100: ('Cachorro Quente', 9.0),
        101: ('Cachorro Quente Duplo', 11.0),
        102: ('X-Egg', 12.0),
        103: ('X-Salada', 12.0),
        104: ('X-Bacon', 14.0),
        105: ('X-Tudo', 17.0),
        200: ('Refrigerante Lata', 5.0),
        201: ('Chá Gelado', 4.0),
    }

    # Variável que armazenará o valor total do pedido
    total = 0.0

    # Percorre a lista de códigos de produtos pedidos
    for codigo in codigos_pedidos:
        # Verifica se o código de produto é válido (se consta no cardápio)
        if codigo in cardapio:
            # Recupera as informações do produto a partir do cardápio e adiciona o valor do produto ao total
            produto, valor = cardapio[codigo]
            print(f'Você pediu um {produto} no valor de {valor:.2f}')
            total += valor
        else:
            print('Opção inválida')

    return total

if __name__ == '__main__':
    
    # Mostra o cardápio
    cardapio = """
    *******************Cardápio*******************
    ----------------------------------------------
    | Código |        Descrição        |  Valor  |
    |   100  |     Cachorro Quente     |   9,00  |
    |   101  |  Cachorro Quente Duplo  |  11,00  |
    |   102  |           X-Egg         |  12,00  |
    |   103  |         X-Salada        |  12,00  |
    |   104  |          X-Bacon        |  14,00  |
    |   105  |           X-Tudo        |  17,00  |
    |   200  |    Refrigerante Lata    |   5,00  |
    |   201  |         Chá Gelado      |   4,00  |
    ----------------------------------------------
    """
    print(cardapio)

    # Lista que armazenará os códigos dos produtos pedidos
    codigos = []

    # Recebe o primeiro código de produto do usuário
    codigo = int(input('Entre com o código desejado: '))
    
    while True:
        # Verifica se o código de produto é válido (se consta no cardápio) e adiciona à lista de códigos
        if codigo in [100, 101, 102, 103, 104, 105, 200, 201]:
            codigos.append(codigo)
        else:
            print('Opção inválida')

        print('Deseja pedir mais alguma coisa?')
        print('1 - Sim')
        print('2 - Não')
        pedir_mais = int(input())

        if pedir_mais == 2:
            break

        codigo = int(input('Entre com o código desejado: '))

    total = calcular_total_pedido(codigos)
    print(f'O total a ser pago é: {total:.2f} R$')