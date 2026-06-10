# Operação CosmosMiner - Equipe: AstroTec

## integrantes

- João Lucas Silva Lopes – RM:  573875
- Alan Otalvaro – RM: 571794
- João Pedro Evangelista – RM: 573899


## como rodar

basta executar o arquivo mission_control_ai.py usando o comando "python mission_control_ai.py" no terminal

## Funcionamento do sistema e geração de dados

O sistema funciona atráves de um padrão de têndencia individual de cada parâmetro, após o primeiro ciclo, cada parâmetro recebe uma têndencia que ditará qual será seu valor e estado por uma quantidade limitada de ciclos, podendo ser estavel, atenção ou critico.

essas têndencias individuais podem ser modificadas atráves da ação do usuário, mas além disso, há um terceiro sistema de controle de têndencia, o evento, que aleatóriamente pode acontecer, levando alguns parâmetros a têndencias criticas automaticamente.

no fim de cada ciclo, é apresentado uma têndencia geral do sistema derivado das individuais, além disso, os dados referentes a essas têndencia são salvos em mátrizes para apresentação no fim do código. 

### ações

ações são escolhas do usuário que mudam uma têndencia alvo de forma motiva, mas que como consequência afetam têndencias de outros parâmetros negativamente.

uma mudança positiva sempre resultará em estado estavel, mas uma negativa pode variar dependendo do contexto, caso já seja um estado Atenção, há a chance de se tornar um Critico, mas na maioria das vezes resulta em uma duração maior do estado de atenção, caso esteja em nivel critico, sua longividade aumenta, em parâmetros estaveis, sempre se tornam tendencias de atenção.

algumas ações mudam o tempo da missão invés dos parâmetros.

#### ligar controlador de temperatura

positivo: temperatura
negativo: energia

### verificar frequencia de radio

positivo: comunicacao

#### ligar gerador

positivo energia
negativo: tempo(+2 ciclos)

#### gerar oxigênio

positivo: oxigênio
negativo: energia

#### reparar nave

positivo: integridade
negativo: oxigênio, temperatura


#### estabilizar

positivo: estabilidade
negativo: comunicação

## Parâmetros e limites

todos os parâmetros funcionam em um intervalo principal de 0 a 100, com exceção de temperatura, que consegue valores negativos de -100, qualquer valor dentro desse intervalo principal, mas não abordado nas tabelas abaixo representa valor mortifero, então são omitidos.

### Temperatura

| intervalo | Têndencia |
| --------- | --------- |
| 18 a 30   | Estavel   |
| 30 a 35   | ATENÇÃO   |
| 0 a 18    | ATENÇÃo   |
| -40 a -20 | CRITICO   |
| 50 a 90   | CRITICO   |

### Comunicação

| intervalo | Têndencia |
| --------- | --------- |
| 60 a 100  | Estavel   |
| 30 a 60   | ATENÇÃO   |
| 0 a 30    | CRITICO   |

### Bateria 

| intervalo | Têndencia |
| --------- | --------- |
| 50 a 100  | Estavel   |
| 20 a 50   | ATENÇÃO   |
| 0 a 30    | CRITICO   |

### Oxigênio

| intervalo | Têndencia |
| --------- | --------- |
| 80 a 100  | Estavel   |
| 60 a 80   | ATENÇÃO   |
| 0 a 60    | CRITICO   |

### Estabilidade

| intervalo | Têndencia |
| --------- | --------- |
| 70 a 100  | Estavel   |
| 40 a 80   | ATENÇÃO   |
| 10 a 40   | CRITICO   |

### Integridade

| intervalo | Têndencia |
| --------- | --------- |
| 85 a 100  | Estavel   |
| 70 a 85   | ATENÇÃO   |
| 50 a 40   | CRITICO   |