from src.tipos import Asteroide
from utils.arquivos import Database


class Banco(Database):
    pontos: int = 0
    tempo: int = 0
    asteroide: Asteroide
    @property
    def caminho(self) -> str:
        return "recursos/db/dados.json"

    def padrao(self) -> None:
        self.tempo = 10
        self.pontos = 0 
        return super().padrao()

    def instanciar(self, json: dict) -> None:
        return super().instanciar(json)

    @property
    def json(self) -> dict:

        return {}


banco_dados = Banco()
