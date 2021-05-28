import PySimpleGUI as sg

class TelaPython:
    def __init__(self):
        #leyout
        layout = [
            [sg.Text('Nome', size=(5,0)), sg.Input(size=(15,0), key=('Nome'))],
            [sg.Text('Idade', size=(5,0)), sg.Input(size=(15,0),key=('Idade'))],
            [sg.Text('Uqias provedores de Email são aceitos?')],
            [sg.Checkbox('Gmail', key='Gmail'), sg.Checkbox('Outlook', key='outlook'), sg.Checkbox('Yahoo', key='Yahoo')],
            [sg.Button('Eenviar dados')]
        ]
        #janela
        janela = sg.Window("Dados do usuário").layout(layout)
        #extrair dadados da tela
        self.button, self.values = janela.Read()

    def Iniciar(self):
        nome = self.values['Nome']
        idade = self.values['Idade']
        aceita_gmail = self.values['Gmail']
        aceita_outlook = self.values['outlook']
        aceita_yahoo = self.values['Yahoo']
        print(f'nome: {nome}')
        print(f'Idade: {idade}')
        print(f'Aceita Gmail {aceita_gmail}')
        print(f'Aceita Outlook {aceita_outlook}')
        print(f'Aceita Yahoo {aceita_yahoo}')
tela = TelaPython()
tela.Iniciar()