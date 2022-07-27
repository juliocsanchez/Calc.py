import math

import PySimpleGUI as janela

janela.theme('DarkBlue1')

layout_calculadora = [
    [janela.Text('Simple Calculator to one digit numbers', key='resultado')],
    [janela.Button('+'), janela.Button('-'), janela.Button('x'), janela.Button('/'), ],
    [janela.Button('1'), janela.Button('2'), janela.Button('3'), janela.Button('4'), janela.Button('5')],
    [janela.Button('6'), janela.Button('7'), janela.Button('8'), janela.Button('9'), janela.Button('0'),
     janela.Button('=')]

]

window = janela.Window('Calculadora', layout_calculadora, resizable=True)

# values started in 0
resultado = 0
texto_digitado = ''

while True:  # When the 'janela' is open...

    event, values = window.read()  # Declared variables for manipulation

    botao_atual = window[event].get_text()  # Capture the Strings in the visor of the calculator

    if event == janela.WINDOW_CLOSED:  # If the 'janela' is close, the operation is down
        break

    botao_clicado = window[event].get_text()  # Method for separate the number of '='

    if botao_clicado != '=':  # If the 'botao_clicado' it´s different of '=', he go add the task below
        texto_digitado = texto_digitado + botao_clicado
    else:
        pass

    window['resultado'].update(texto_digitado) # Will type the numbers placed on the calculator display

    if window[event].get_text() == '=':

        for caracter in texto_digitado:  # Will get the String characters to get their value

            if caracter == '+':
                arrays = texto_digitado.split('+')  # The method 'split()' broken the string to half the values. ['1','2']
                x = arrays[0]
                y = arrays[1]

                resultado = int(x) + int(y) # Forces String array to be Int

            if caracter == '-':
                arrays = texto_digitado.split('-')
                x = arrays[0]
                y = arrays[1]

                resultado = int(x) - int(y)

            if caracter == 'x':
                arrays = texto_digitado.split('x')
                x = arrays[0]
                y = arrays[1]

                resultado = int(x) * int(y)

            if caracter == '/':
                arrays = texto_digitado.split('/')
                x = arrays[0]
                y = arrays[1]

                resultado = int(x) / int(y)

        window['resultado'].update(resultado) # After the operation, put the result on the calculator display
        texto_digitado = '' # After the result, resets the 'texto_digitado'

window.close()
