"""
Teste do programa de pesquisa de opinião com uma amostra reduzida
de 10 entrevistados, para validar o funcionamento antes de rodar
a pesquisa completa com 50 pessoas (pesquisa_opiniao.py).
"""

from pesquisa_opiniao import coletar_pesquisa, exibir_resultado

QUANTIDADE_TESTE = 10

if __name__ == "__main__":
    total_excelente, total_bom, total_ruim = coletar_pesquisa(QUANTIDADE_TESTE)
    exibir_resultado(QUANTIDADE_TESTE, total_excelente, total_bom, total_ruim)
