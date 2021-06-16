"""
Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um
link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
"""


def calcular_download():
    """
    Função que calcula tempo aproximado para download do arquivo em minutos
    :return: tempo (em minutos) para download de arquivo em mb a partir da velocidade de conexão do usuário.
    """
    while True:
        try:
            tamanho_arquivo_download = int(input('Qual tamanho arquivo? Em (MB): '))
            velocidade_internet = int(input('Quantos Mbps a sua conexão de internet? '))
            tempo_aproximado = (tamanho_arquivo_download / velocidade_internet) * 60

        except Exception as error:
            print(f'Não consegui calcular. Erro: {error}\nTente novamente')

        else:
            print(f'Tempo aproximado para baixar um arquivo de {tamanho_arquivo_download}mb, '
                  f'é de {tempo_aproximado:.0f}min.')
            break


# programa principal
calcular_download()
