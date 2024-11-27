from tkinter import *

import requests


def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
    requisicao_dic = requisicao.json()
    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']
    
    texto_resposta['text'] = f'''
    DÓLAR: {cotacao_dolar}
    EURO: {cotacao_euro}
    BTC: {cotacao_btc}
    '''

# Interface gráfica
janela = Tk()
janela.title("Cotações de Moedas")
janela.geometry("400x400")
janela.configure(bg="#0f0f3d")

# Título
titulo = Label(
    janela,
    text="COTAÇÕES DE MOEDAS",
    font=("Arial", 16, "bold"),
    fg="#00ffff",
    bg="#0f0f3d"
)
titulo.pack(pady=20)

# Botão para buscar cotações
botao = Button(
    janela,
    text="Atualizar Cotações",
    command=pegar_cotacoes,
    font=("Arial", 12, "bold"),
    bg="#1f1f5c",
    fg="#00ffff",
    activebackground="#00ffff",
    activeforeground="#1f1f5c",
    relief="raised"
)
botao.pack(pady=20)

# Espaço para exibir os resultados
texto_resposta = Label(
    janela,
    text="Clique no botão para obter as cotações.",
    font=("Arial", 12),
    fg="#ffffff",
    bg="#0f0f3d",
    justify="left"
)
texto_resposta.pack(pady=20)

# Inicia o loop da interface
janela.mainloop()
