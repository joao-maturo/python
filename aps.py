import pandas as pd
import numpy as np 
import plotly.express  as px

# Lê o CSV:
x = pd.read_csv("C:\\Users\\joaop\Desktop\\aps\\TA_PRECO_MEDICAMENTO.CSV", encoding="latin-1", sep = ";",low_memory=False)

# Formata o arquivo pra melhor exibição:
pd.get_option('display.max_rows')
pd.options.display.max_rows = 276940
pd.options.display.max_columns = 40

# Exibe a quantidade de medicamentos por tarja:

tarjas = x['TARJA'].value_counts()
# O value_counts acima printa a tarja seguida do número de medicamentos naquela tarja.
# Algumas no entanto são repetidas. Por isso, soma:

tarja_vermelha = tarjas[0] + tarjas[1] + tarjas[2]
sem_tarja = tarjas[3] + tarjas[4]
tarja_preta = tarjas[5] + tarjas[6]

# Exibe a quantidade de medicamentos por laboratório:
labs = x['LABORATÓRIO'].value_counts()

# Exibe a classificação do medicamento:
status = x['TIPO DE PRODUTO (STATUS DO PRODUTO)'].value_counts()

# Exibe o preço de cada medicamento:
precosord = x[["SUBSTÂNCIA", "PF Sem Impostos"]]

# Exibe quantos medicamentos tem por regimento:
regpreco = x['REGIME DE PREÇO'].value_counts()

#INDO DO MENOR PRO MAIOR 
a= x.sort_values(by=['PF Sem Impostos']).reset_index(drop = True)
print(a)

grafico = px.bar(x, x='LABORATÓRIO', y='PF Sem Impostos')

def menu():
    escolha = input(f'Digite um número para obter as informações desejadas. Digite qualquer outra coisa para sair.\nDigite 0 para saber a quantidade de medicamentos por tarja.\nDigite 1 para saber a quantidade de medicamentos por laboratório.\nDigite 2 para saber a classificação de cada medicamento;\nDigite 3 para saber o preço de cada medicamento;\nDigite 4 para saber quantos medicamentos tem por regimento;\nDigite 5 para ver os medicamentos do menor pro maior PF;\nEscolha: ')
    match escolha:
        case '0':
            print(f'O número de medicamentos por tarja é:\nTarja vermelha: {tarja_vermelha};\nTarja preta: {tarja_preta};\nSem tarja (livre): {sem_tarja}.')
            menu()
        case '1':
            print(labs)
            menu()
        case '2':
            print(status)
            menu()
        case '3':
            print(precosord)
            menu()
        case '4':
            print(regpreco)
            menu()
        case '5':
            #aqui vcs poem o print
            menu()
        case _:
            exit()

menu()