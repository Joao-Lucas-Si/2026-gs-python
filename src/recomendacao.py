
from src.banco_dados import Estado
from utils.tui.render.elementos import Coluna, Texto

def estado_temperatura(temperatura):
    if temperatura < 18 or (temperatura > 30 and temperatura < 35):
        estado_temperatura = Estado.ATENCAO
    elif temperatura > 18 and temperatura < 30:
        estado_temperatura = Estado.ESTAVEL
    elif temperatura < -20 or temperatura > 50:
        estado_temperatura = Estado.MORTIFERO
    else:
        estado_temperatura = Estado.CRITICO
    return estado_temperatura

def estado_comunicacao(comunicacao):
    if comunicacao > 30 and comunicacao < 59:
        estado_comunicacao = Estado.ATENCAO
    elif comunicacao > 60:
        estado_comunicacao = Estado.ESTAVEL
    elif comunicacao < 0:
        estado_comunicacao = Estado.MORTIFERO
    else:
        estado_comunicacao = Estado.CRITICO
    return estado_comunicacao

def estado_bateria(bateria):
    if bateria > 20.0 and bateria < 49.0:
        estado_bateria = Estado.ATENCAO
    elif bateria < 0.00 or bateria > 100:
        estado_bateria = Estado.MORTIFERO
    elif bateria > 50.0:
        estado_bateria = Estado.ESTAVEL
    else:
        estado_bateria = Estado.CRITICO
    return estado_bateria

def estado_oxigenio(oxigenio):
    if oxigenio > 70 and oxigenio < 79:
        estado_oxigenio = Estado.ATENCAO
    elif oxigenio > 80:
        estado_oxigenio = Estado.ESTAVEL
    elif oxigenio < 0:
        estado_oxigenio = Estado.MORTIFERO
    else:
        estado_oxigenio = Estado.CRITICO
    return estado_oxigenio

def estado_estabilidade(estabilidade):
    if estabilidade > 40 and estabilidade < 69:
        estado_estabilidade = Estado.ATENCAO
    elif estabilidade < 0:
        estado_estabilidade = Estado.MORTIFERO
    elif estabilidade > 70:
        estado_estabilidade = Estado.ESTAVEL
    else:
        estado_estabilidade = Estado.CRITICO
    return estado_estabilidade

def estado_integridade(integridade):
    if integridade > 80 and integridade < 85:
        estado_integridade = Estado.ATENCAO
    elif integridade > 85:
        estado_integridade = Estado.ESTAVEL
    elif integridade <= 50:
        estado_integridade = Estado.MORTIFERO
    else:
        
        estado_integridade = Estado.CRITICO
    return estado_integridade

# def estado_motor(temperatura_motor):
#     if temperatura_motor > 3600 and temperatura_motor < 4000 :
#         estado_motor = Estado.ATENCAO
#     elif temperatura_motor > 1000 and temperatura_motor < 3600:
#         estado_motor = Estado.ESTAVEL
#     elif temperatura_motor <= 500 or temperatura_motor > 4000:
#         estado_motor = Estado.MORTIFERO
#     else:
#         estado_motor = Estado.CRITICO
#     return estado_motor


def recomendacao_temperatura(estado_temperatura):
    if estado_temperatura == Estado.ATENCAO:
       "Atenção: Temperatura esta fora dos parametros normais."
    elif estado_temperatura == Estado.CRITICO:
       "Critico: A temperatura esta alem dos parametros, ligar resfrigerador."
    else:
        "Temperatura esta dentro dos parametros normais."

def recomendacao_comunicacao(estado_comunicacao):
    if estado_comunicacao == Estado.ATENCAO:
       "Atenção: Comunicação esta fora dos parametros normais."
    elif estado_comunicacao == Estado.CRITICO:
       "Critico: A comunicação esta em niveis de risco altos , verificar frequencia de radio!."
    else:
        "Comunicação esta dentro dos parametros normais."

def recomendacao_bateria(estado_bateria):
    if estado_bateria == Estado.ATENCAO:
       "Atenção: Bateria esta fora dos parametros normais,usar combustivel de reserva/ligar geraradores."
    elif estado_bateria == Estado.CRITICO:
       "Critico: A bateria esta em niveis de risco altos , ativar modo economia!."
    else:
        "Bateria esta dentro dos parametros normais."

def recomendacao_oxigenio(estado_oxigenio):
    if estado_oxigenio == Estado.ATENCAO:
       "Atenção: Oxigenio esta fora dos parametros normais."
    elif estado_oxigenio == Estado.CRITICO:
       "Critico: O Oxigenio esta em niveis criticos , ativar gerador oxigenio."
    else:
         "Oxigenio esta dentro dos parametros normais."

def recomendacao_estabilidade(estado_estabilidade):
    if estado_estabilidade == Estado.ATENCAO:
       "Atenção: A Estabilidade esta fora dos parametros normais."
    elif estado_estabilidade == Estado.CRITICO:
       "Critico: A Estabilidade esta baixa, é necessario reduzir operações não essenciais."
    else:
         "A Estabilidade esta dentro dos parametros normais."

def recomendacao_integridade(estado_integridade):
    if estado_integridade == Estado.ATENCAO:
       "Atenção: A Integridade esta fora dos parametros normais."
    elif estado_integridade == Estado.CRITICO:
       "Critico: A Integridade esta baixa, é necessario reparar nave."
    else:
        "A Integridade esta dentro dos parametros normais."

def recomendacao_motor(estado_motor):
    if estado_motor == Estado.ATENCAO:
       return "Atenção: A Temperatura do Motor esta fora dos parametros normais."
    elif estado_motor == Estado.CRITICO:
       return "Critico: A Temperatura do Motor esta alta, é necessario reduzir operações não essenciais."
    else:
        return "A Temperatura do Motor esta dentro dos parametros normais."


