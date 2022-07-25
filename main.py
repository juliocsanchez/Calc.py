import math

import PySimpleGUI as janela

janela.theme('DarkBlue1')

layout_calculadora = [
    [janela.Text('Simple Calculator to one digit numbers', key='resultado')],
    [janela.Button('+'), janela.Button('-'), janela.Button('x'),janela.Button('/'),],
    [janela.Button('1'), janela.Button('2'),janela.Button('3'),janela.Button('4'),janela.Button('5')],
    [janela.Button('6'), janela.Button('7'),janela.Button('8'),janela.Button('9'),janela.Button('0'), janela.Button('=')]

]

window = janela.Window('Calculadora', layout_calculadora, resizable=True)

resultado = 0
botoes_clicados = []
operacao_atual = None
limpar = 0

while True:
    event, values = window.read()

    botao_atual = window[event].get_text()

    if event != janela.WINDOW_CLOSED:

        if botao_atual == "1":
            botoes_clicados.append(1)

        elif botao_atual == "2":
            botoes_clicados.append(2)

        elif botao_atual == "3":
            botoes_clicados.append(3)

        elif botao_atual == "4":
            botoes_clicados.append(4)

        elif botao_atual == "5":
            botoes_clicados.append(5)

        elif botao_atual == "6":
            botoes_clicados.append(6)

        elif botao_atual == "7":
            botoes_clicados.append(7)

        elif botao_atual == "8":
            botoes_clicados.append(8)

        elif botao_atual == "9":
            botoes_clicados.append(9)

        elif botao_atual == "0":
            botoes_clicados.append(0)

        elif botao_atual == "+":
            operacao_atual = "+"

        elif botao_atual == "C":
            operacao_atual = "C"

        ##########################

        elif botao_atual == "-":
            operacao_atual = "-"

        elif botao_atual == "x":
            operacao_atual = "x"

        elif botao_atual == "/":
            operacao_atual = "/"

        elif botao_atual == "=":
            resultado = 0

            for i in range(len(botoes_clicados) - 1):
                x = botoes_clicados[i]

                if operacao_atual == '+':
                    resultado = x + botoes_clicados[i + 1]

                if operacao_atual == "-":
                    resultado = x - botoes_clicados[i + 1]

                if operacao_atual == "x":
                    resultado = x * botoes_clicados[i + 1]

                if operacao_atual == "/":
                    resultado = x / botoes_clicados[i + 1]


            window['resultado'].update(value=resultado)
            botoes_clicados = []
            resultado = 0
            operacao_atual = None
