import random
from typing import TypeAlias

from src.banco_dados import Estado

#dados_missao = [
# [temperatura, comunicacao, bateria, oxigenio, estabilidade],
# [temperatura, comunicacao, bateria, oxigenio, estabilidade],
# [temperatura, comunicacao, bateria, oxigenio, estabilidade],
# [temperatura, comunicacao, bateria, oxigenio, estabilidade],
# [temperatura, comunicacao, bateria, oxigenio, estabilidade],
# [temperatura, comunicacao, bateria, oxigenio, estabilidade]
# ]

tempo = 10

temperatura = random.randint(0, 50)
comunicacao = random.randint(0, 100)
bateria = random.uniform(0.0, 100.0)
oxigenio = random.randint(0, 100)
estabilidade = random.randint(0, 100)
integridade_modulo = random.randint(80, 100)
Dados_Atuais: TypeAlias = list[int|float]
dados_atuais: Dados_Atuais = [temperatura, comunicacao, bateria, oxigenio, estabilidade, integridade_modulo]
dados_missao = [[temperatura, comunicacao, bateria, oxigenio, estabilidade, integridade_modulo]]
historico_tendencias: list[list[Estado]] = []