"""
módulo que implementa os métodos necessários para a conversão de unidades de distância.

:Date: nov, 2020
:Version: 1.0
:Authors: pcardoso
"""

fator = {
    "mm": 0.001,
    "cm": 0.01,
    "dm": 0.1,
    "m": 1,
    "dam": 10,
    "hm": 100,
    "km": 1000,
    "mi": 1609.344,    # milhas
    "pe": 0.3048      # pés
    }
"""
fator de conversão de cada unidade para metros
"""


def converte_distancia(comprimento, de_unidade, para_unidade):
    """
    Conversor de distancia.
    Recebe o valor da distancia e correspondente unidade e devolve a distancia na unidade pretendida.

    :param comprimento: distancia originial
    :param de_unidade: unidade da distancia original
    :param para_unidade: unidade da distancia pretendida
    :return: comprimento na unidade pretendida
    """

    return comprimento * fator[de_unidade] / fator[para_unidade]


def menu_distancia():
    """
    Função para gerir o menu dos conversores de distância.
    Apresenta um menu e de acordo com as opcao escolhida pelo utilizador chamas as funções de conversão
    """

    while True:
        print(f"""
             -----------------------------  converte distâncias ------------------------------
             Unidades possíveis: {list(fator.keys())}
             exemplo: 
               de = 10 m    # colocar espaco a seguir ao número
               para = km

               km = 10000 m 
             (S)air
             """)

        try:
            de_str = input("de?").lower()
            if de_str == "s":
                break
            comprimento, de_unidade = de_str.split()
            if de_unidade not in fator.keys():
                print("Unidade inválida")
            comprimento = float(comprimento)

            para_unidade = input("para?").lower()
            if para_unidade not in fator.keys():
                print("Unidade inválida")

            print(f"{de_str} = {converte_distancia(comprimento, de_unidade, para_unidade)} {para_unidade}")
        except Exception as e:
            print(f"Erro: {e}")
