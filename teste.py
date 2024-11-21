import pytest
from jabotron import json_umidade, relatorio_html

def test_json_umidade():
    # Sucesso
    lista_de_valores = [45, 55, 60]
    resultado = json_umidade(lista_de_valores)
    assert resultado == {"umidade": lista_de_valores}
    
    # Erro: lista vazia
    with pytest.raises(ValueError, match="A lista de valores de umidade não pode ser vazia."):
        json_umidade([])

def test_relatorio_html():
    # Sucesso
    dados = {"umidade": [45, 55, 60]}
    resultado = relatorio_html(dados)
    assert "<html>" in resultado
    assert "<h1>Relatório de Umidade</h1>" in resultado
    assert "<li><strong>Umidade:</strong> 45, 55, 60</li>" in resultado
    assert "</html>" in resultado

    # Erro: dados inválidos
    with pytest.raises(ValueError, match="Os dados fornecidos devem ser um dicionário não vazio."):
        relatorio_html({}) # json vazio
    with pytest.raises(ValueError, match="Os dados fornecidos devem ser um dicionário não vazio."):
        relatorio_html(None) # json inexistente
