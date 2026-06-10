from enum import Enum
import random
from typing import Optional, Tuple

from src.tipos import Asteroide
from utils.arquivos import Database


class Estado(Enum):
    CRITICO = 2
    ATENCAO = 1
    ESTAVEL = 0


class Tendencia:
    intervalo: Tuple[int, int]
    estado: Estado
    recomendacao: str
    duracao = 0
    atividade = 0

    def __init__(
        self, intervalo: Tuple[int, int], estado: Estado, recomendacao: str
    ) -> None:
        self.intervalo = intervalo
        self.estado = estado
        self.recomendacao = recomendacao


class Parametro:
    nome: str
    
    tendencia_atual: Tendencia
    tendencias: list[Tendencia]
    
     
    @property
    def valor(self):
        tendencia = self.tendencia_atual
        intervalo = tendencia.intervalo
        return  random.randint(intervalo[0], intervalo[1])

    def __init__(self, nome: str, tendencias: list[Tendencia]):
        self.nome = nome
        self.tendencias = tendencias
        self.definir_tendencia(Estado.ESTAVEL)

    
    def gerar_tendencia(self):
        if self.tendencia_atual.atividade >= self.tendencia_atual.duracao:
            i = random.randint(0, 10)
            estado: Estado = Estado.ESTAVEL
            if i > 8:
                estado = Estado.CRITICO
            elif i > 5:
                estado = Estado.ATENCAO
            self.definir_tendencia(estado)
            self.tendencia_atual.duracao = random.randint(2, 5)

    def definir_tendencia(self, estado: Estado):
        validos = [
            tendencia for tendencia in self.tendencias if tendencia.estado == estado
        ]

        atual = validos[random.randint(0, len(validos) - 1)]
        atual.atividade = 0
        self.tendencia_atual = atual


class Rodada:
    tempo_inicial: int = 0
    tempo_final: int = 0
    tempo_atual: int = 1
    tendencias: list[list[Estado]] = []
    morte: Optional[str] = None
        

    @property
    def tendencias_atuais(self):
        return self.tendencias[self.tempo_atual - 1]

    @property
    def dados_atuais(self):
        return self.dados[self.tempo_atual - 1]

    dados: list[list[int]] = []
    asteroide: Asteroide
    parametros: list[Parametro] = [
        Parametro(
            "Temperatura",
            [
                Tendencia((18, 30), Estado.ESTAVEL, "temperatura segura"),
                Tendencia(
                    (30, 35),
                    Estado.ATENCAO,
                    "a temperatura está começando a esquentar, ligue o resfrigerador se necessário",
                ),
                Tendencia(
                    (0, 18),
                    Estado.ATENCAO,
                    "a temperatura está começando a esfriar, ligue o aquecedor se necessário",
                ),
                Tendencia(
                    (-40, -20),
                    Estado.CRITICO,
                    "a temperatura está muito fria, ligue o aquecedor rapidamente",
                ),
                Tendencia(
                    (50, 90), Estado.CRITICO, "superaquecimento, ligue o refrigerador"
                ),
            ],
        ),
        Parametro(
            "Comunicação",
            [
                Tendencia((60, 100), Estado.ESTAVEL, "Comunicação funcional"),
                Tendencia(
                    (30, 60),
                    Estado.ATENCAO,
                    "Comunicação falha, tente achar um frequencia de radio estavel",
                ),
                Tendencia(
                    (0, 30),
                    Estado.CRITICO,
                    "quase há perda total da conexão com a base, ache uma frequencia funcional rapidamente",
                ),
            ],
        ),
        Parametro(
            "Bateria",
            [
                Tendencia((50, 100), Estado.ESTAVEL, "Bateria suficiente"),
                Tendencia((20, 50), Estado.ATENCAO, "Bateria fraca, ative o gerador"),
                Tendencia(
                    (0, 20), Estado.CRITICO, "Bateria escassa, ativa o modo economia"
                ),
            ],
        ),
        Parametro(
            "Oxigenio",
            [
                Tendencia((80, 100), Estado.ESTAVEL, "abundacia de Oxigenio"),
                Tendencia((60, 80), Estado.ATENCAO, "Oxigenio em escotamento"),
                Tendencia(
                    (0, 60), Estado.CRITICO, "Oxigenio acabando, ligue o gerador"
                ),
            ],
        ),
        Parametro(
            "Estabilidae",
            [
                Tendencia((70, 100), Estado.ESTAVEL, "Estavel"),
                Tendencia((40, 70), Estado.ATENCAO, "Estabilidade baixa"),
                Tendencia(
                    (10, 40), Estado.CRITICO, "Instavel, tente estabilizar a nave"
                ),
            ],
        ),
        Parametro(
            "Integridade",
            [
                Tendencia((85, 100), Estado.ESTAVEL, "Nave inteira"),
                Tendencia(
                    (70, 85),
                    Estado.ATENCAO,
                    "Nave com defeito, alguns reparos podem ser necessários",
                ),
                Tendencia(
                    (50, 70),
                    Estado.CRITICO,
                    "Nave parcialmente destruida, tente reparar",
                ),
            ],
        ),
    ]


class Banco(Database):
    pontos: int = 0

    # asteroide: Asteroide
    rodada: Rodada = Rodada()

    @property
    def caminho(self) -> str:
        return "recursos/db/dados.json"

    def padrao(self) -> None:
        # self.tempo = 10
        self.pontos = 0
        return super().padrao()

    def instanciar(self, json: dict) -> None:
        return super().instanciar(json)

    @property
    def json(self) -> dict:

        return {}


banco_dados = Banco()
