"""
Pesquisa de Opinião - TudoWeb
Coleta, por meio de estrutura de repetição, o nome, a idade e a opinião
de vários entrevistados sobre o atendimento prestado, e exibe ao final
a quantidade de respostas EXCELENTE e RUIM.

Opções de opinião:
    1 - EXCELENTE
    2 - BOM
    3 - RUIM
"""

TOTAL_ENTREVISTADOS = 50  # quantidade de pessoas que devem responder a pesquisa


def obter_idade(nome):
    """
    Solicita a idade do entrevistado e garante que o valor digitado
    seja um número inteiro válido e não negativo.
    """
    while True:
        entrada = input(f"Idade de {nome}: ")
        if entrada.isdigit():
            return int(entrada)
        print("Idade inválida. Digite apenas números inteiros.")


def obter_opiniao(nome):
    """
    Exibe o menu de opções e solicita a opinião do entrevistado,
    garantindo que apenas 1, 2 ou 3 sejam aceitos.
    """
    while True:
        print("Opinião sobre o atendimento:")
        print("  1 - EXCELENTE")
        print("  2 - BOM")
        print("  3 - RUIM")
        opcao = input(f"Digite a opção de {nome}: ")

        if opcao in ("1", "2", "3"):
            return int(opcao)
        print("Opção inválida. Digite 1, 2 ou 3.\n")


def coletar_pesquisa(quantidade):
    """
    Executa a coleta da pesquisa com a quantidade de entrevistados
    informada, utilizando um laço de repetição (for), e devolve os
    totais de respostas EXCELENTE e RUIM.
    """
    total_excelente = 0
    total_bom = 0
    total_ruim = 0

    for pessoa in range(1, quantidade + 1):
        print(f"\n----- Entrevistado {pessoa}/{quantidade} -----")
        nome = input("Nome: ")
        idade = obter_idade(nome)
        opiniao = obter_opiniao(nome)

        # Estrutura de decisão para contabilizar a opinião do entrevistado
        if opiniao == 1:
            total_excelente += 1
        elif opiniao == 2:
            total_bom += 1
        else:  # opiniao == 3
            total_ruim += 1

    return total_excelente, total_bom, total_ruim


def exibir_resultado(quantidade, total_excelente, total_bom, total_ruim):
    """Exibe o resultado final da pesquisa de forma organizada."""
    print("\n========== RESULTADO DA PESQUISA ==========")
    print(f"Total de entrevistados: {quantidade}")
    print(f"Respostas EXCELENTE:    {total_excelente}")
    print(f"Respostas BOM:          {total_bom}")
    print(f"Respostas RUIM:         {total_ruim}")
    print("=============================================\n")


def main():
    """Função principal: coordena a coleta e a exibição do resultado da pesquisa."""
    total_excelente, total_bom, total_ruim = coletar_pesquisa(TOTAL_ENTREVISTADOS)
    exibir_resultado(TOTAL_ENTREVISTADOS, total_excelente, total_bom, total_ruim)


if __name__ == "__main__":
    main()
