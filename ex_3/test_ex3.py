from main import validar_medida, \
                calcular_preco_volume, \
                calcular_multiplicador_peso, \
                calcular_multiplicador_rota, \
                calcular_frete                    
import pytest


# Teste da função validar_medida para entrada numérica
def test_validar_medida_numero():
    assert validar_medida('5') == 5

# Teste da função validar_medida para entrada não numérica
def test_validar_medida_nao_numero():
    assert validar_medida('abc') == -1

# Teste da função calcular_preco_volume com volume menor que 1000
def test_calcular_preco_volume_menor_1000():
    assert calcular_preco_volume(500) == 10.0

# Teste da função calcular_preco_volume com volume entre 1000 e 10000
def test_calcular_preco_volume_1000_10000():
    assert calcular_preco_volume(5000) == 20.0

# Teste da função calcular_preco_volume com volume entre 10000 e 30000
def test_calcular_preco_volume_10000_30000():
    assert calcular_preco_volume(15000) == 30.0

# Teste da função calcular_preco_volume com volume entre 30000 e 100000
def test_calcular_preco_volume_30000_100000():
    assert calcular_preco_volume(50000) == 20.0

# Teste da função calcular_preco_volume com volume maior que 100000
def test_calcular_preco_volume_maior_100000():
    assert calcular_preco_volume(150000) == 0.0

def test_calcular_multiplicador_peso_50g():
    # Testa para um objeto com peso de 0.05kg
    assert calcular_multiplicador_peso(0.05) == 1.0
    
def test_calcular_multiplicador_peso_500g():
    # Testa para um objeto com peso de 0.5kg
    assert calcular_multiplicador_peso(0.5) == 1.5
    
def test_calcular_multiplicador_peso_5kg():
    # Testa para um objeto com peso de 5kg
    assert calcular_multiplicador_peso(5) == 2.0
    
def test_calcular_multiplicador_peso_20kg():
    # Testa para um objeto com peso de 20kg
    assert calcular_multiplicador_peso(20) == 3.0
    
def test_calcular_multiplicador_peso_31kg():
    # Testa para um objeto com peso de 31kg, que é maior que o limite aceitável
    assert calcular_multiplicador_peso(31) == 0

def test_calcular_multiplicador_rota_br():
    #Verifica se a função retorna o valor esperado quando é passada a sigla 'br'
    assert calcular_multiplicador_rota('br') == 1.5
    
def test_calcular_multiplicador_rota_rs():
    #Verifica se a função retorna o valor esperado quando é passada a sigla 'rs'
    assert calcular_multiplicador_rota('rs') == 1.0

def test_calcular_multiplicador_rota_SB():
    #Verifica se a função retorna o valor esperado quando é passada a sigla 'SB'
    assert calcular_multiplicador_rota('SB') == 1.2

def test_calcular_multiplicador_rota_zz():
    #Verifica se a função retorna o valor esperado quando é passada a sigla 'zz'
    assert calcular_multiplicador_rota('zz') == 0

def test_calcular_frete():
    assert calcular_frete(1000, 1.5, 1.0) == 1500
    assert calcular_frete(2000, 2.0, 1.2) == 4800
    assert calcular_frete(5000, 3.0, 1.5) == 22500

#def test_ler_dimensoes_objeto(monkeypatch):
#    # Teste com entrada válida
#    monkeypatch.setattr('builtins.input', lambda _: '10\n20\n30\n')
#    assert ler_dimensoes_objeto() == 6000
#
#    # Teste com altura inválida
#    monkeypatch.setattr('builtins.input', lambda _: 'a\n20\n30\n')
#    assert ler_dimensoes_objeto() == None
#
#    # Teste com comprimento inválido
#    monkeypatch.setattr('builtins.input', lambda _: '10\na\n30\n')
#    assert ler_dimensoes_objeto() == None
#
#    # Teste com largura inválida
#    monkeypatch.setattr('builtins.input', lambda _: '10\n20\na\n')
#    assert ler_dimensoes_objeto() == None
#
#    # Teste com volume muito grande
#    monkeypatch.setattr('builtins.input', lambda _: '1000\n1000\n1000\n')
#    assert ler_dimensoes_objeto() == None
#
#    # Teste com volume zero
#    monkeypatch.setattr('builtins.input', lambda _: '0\n0\n0\n')
#    assert ler_dimensoes_objeto() == None
