
def calcular_valor_total(valor_unitario: float, quantidade: int) -> float:
    """
    Calcula o valor total de um produto com base em seu valor unitário e quantidade, considerando
    os descontos aplicáveis.

    Args:
        valor_unitario (float): Valor unitário do produto.
        quantidade (int): Quantidade desejada do produto.

    Returns:
        Tuple[float, float]: Tupla contendo os valores sem desconto e com desconto, respectivamente.
    """
    # No desconto o completo de até 1 é o valor do desconto.
    # Ex: 0,85 tem 15% de desconto. -> 1 - 0,85 = 0.15
    desconto = 1

    # Calcula o desconto com base na quantidade de produtos comprados
    if quantidade >= 10 and quantidade <= 99:
        desconto = 0.95
    elif quantidade >= 100 and quantidade <= 999:
        desconto = 0.90
    elif quantidade >= 1000:
        desconto = 0.85

    # Calcula o valor total com e sem desconto
    valor_com_desconto = valor_unitario * desconto * quantidade
    valor_sem_desconto = valor_unitario * quantidade

    # Retorna uma tupla contendo os valores com e sem desconto
    return valor_sem_desconto, valor_com_desconto

if __name__ == '__main__':
    valor_unitario = float(input('Valor unitário do produto: '))
    quantidade = int(input('Quantidade: '))

    valor_sem_desconto, valor_com_desconto = calcular_valor_total(valor_unitario, quantidade)

    print(f'Valor total sem desconto: {valor_sem_desconto:.2f} R$')
    print(f'Valor total com desconto: {valor_com_desconto:.2f} R$')