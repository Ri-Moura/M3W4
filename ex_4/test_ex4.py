from main import gerar_codigo, cadastrar_peca, imprimir_peca

def test_gerar_codigo():
    global pecas
    pecas = []
    assert gerar_codigo() == 1
    pecas.append({'codigo': 1})
    assert gerar_codigo() == 1

def test_cadastrar_peca(monkeypatch, capsys):
    global pecas
    pecas = []
    nome = 'Peça 1'
    fabricante = 'Fabricante 1'
    valor = '50'
    entradas = [nome, fabricante, valor]
    monkeypatch.setattr('builtins.input', lambda _: entradas.pop(0))
    cadastrar_peca()
    assert len(pecas) == 0

def test_imprimir_peca(capsys):
    global pecas
    pecas = [{'codigo': 1, 'nome': 'Peça 1', 'fabricante': 'Fabricante 1', 'valor': 50.0}]
    imprimir_peca(pecas[0])
    out, _ = capsys.readouterr()
    assert 'Código: 001\n' in out
    assert 'Fabricante: Fabricante 1\n' in out
    assert 'Valor: 50.00 R$\n' in out