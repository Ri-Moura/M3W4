import pytest
from main import calcular_total_pedido

def test_calcular_total_pedido_somente_um_produto():
    # Teste com apenas um produto pedido
    assert calcular_total_pedido([100]) == 9.0

def test_calcular_total_pedido_com_varios_produtos():
    # Teste com vários produtos pedidos
    assert calcular_total_pedido([100, 101, 105, 201]) == 41.0

def test_calcular_total_pedido_produto_invalido():
    # Teste com um produto inválido
    assert calcular_total_pedido([200, 300, 104]) == 19.0

def test_calcular_total_pedido_sem_produto():
    # Teste com uma lista vazia
    assert calcular_total_pedido([]) == 0.0

def test_calcular_total_pedido_produtos_repetidos():
    # Teste com produtos repetidos
    assert calcular_total_pedido([100, 100, 105, 200, 201, 201]) == 48.0

def test_calcular_total_pedido_todos_produtos():
    # Teste com todos os produtos do cardápio
    assert calcular_total_pedido([100, 101, 102, 103, 104, 105, 200, 201]) == 84.0

def test_calcular_total_pedido_produto_inexistente():
    # Teste com um produto inexistente no cardápio
    calcular_total_pedido([300]) == 0.0
