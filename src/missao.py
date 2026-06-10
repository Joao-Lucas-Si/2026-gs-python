import enum
from random import Random
import random

from src.banco_dados import Rodada, banco_dados
from src.ciclo import gerenciar_ciclo
from src.tipos import Asteroide, Materiais
from utils.menu import Opcao, menu
from utils.sistema import limpar
from utils.tui.render.elementos import Ascii, Centralizado, Coluna, Tabela, Texto


def menuMissao():
    def criarAsteroide() -> Asteroide:
        chars = ["A", "B", "C", "D","E"]
        ints = [59,27,19,11,31]
        
        nome = chars[random.randint(0, len(chars) - 1)] + str(ints[random.randint(0, len(ints)-1)])
        
        lenM = random.randint(1, 4)        
        materiais = [e for e in Materiais]
        materiais_finais: list[Materiais] = []
        for i in range(lenM):
            materiais_finais.append(materiais[random.randint(0, len(materiais)-1)])
        return Asteroide(materiais_finais, nome, random.randint(6, 15))
            
    while True:
        limpar()    
        asteroides = [criarAsteroide() for i in range(random.randint(2, 8))]
            
        
        def mostrarAsteroide(asteroide: Asteroide) -> Coluna:
            # recursos/ascii/asteroide_grande.txt
            #recursos/ascii/asteroide.txt
            return Coluna([
                Ascii("recursos/ascii/asteroide_grande.txt"),
                Texto(asteroide.nome),
                Texto(f"tempo estimado: {asteroide.tempo}"),
                Texto("Materiais:"+ ", ".join(map(lambda x: x.value.nome, asteroide.materiais)))
            ])
        
        
        def escolher_missao(i : int):
            def comecar_missao():
                rodada = Rodada()
                rodada.tempo_final = asteroides[i].tempo
                rodada.asteroide = asteroides[i]
                rodada.tempo_inicial = asteroides[i].tempo
                rodada.tempo_atual = 1
                banco_dados.rodada = rodada
                gerenciar_ciclo()
            return comecar_missao
        opcoes: list[Opcao] = list(map(lambda x: Opcao(mostrarAsteroide(x[1]), escolher_missao(x[0])), enumerate(asteroides)))
        menu("Escolha de Missão", opcoes, 4)
    