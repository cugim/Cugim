from PySimpleGUI import  PySimpleGUI as sg
#layou
sg.theme('Reddit')
layout = [
    [sg.Text('Usuário'),sg.Input(key='usuario', size=(20,0))],
    [sg.Text('Senha'), sg.Input(key='senha', password_char='*', size=(20,0))],
    [sg.Checkbox('Salvar o login?')],
    [sg.Button('Entrar')]
]
#janela
janela = sg.Window('Tela de login', layout)
#ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WIN_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'jhonatam' and valores['senha'] == '123456':
            print('Bem vindo, seu bosta')
