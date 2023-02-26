import PySimpleGUI as sg
import re

#POO para validar IP varias vezes durante meu codigo

class IPValidator:
    def __init__(self, ip):
        self.ip = ip
        self.ip_pattern = re.compile(r'^(\d{1,3}\.){3}\d{1,3}$')

    def is_valid(self):
        if not self.ip_pattern.match(self.ip):
            return False
        first_octet = int(self.ip.split('.')[0])
        if first_octet >= 1 and first_octet <= 127:
            return True
        return False

# ip = input('Digite o endereço IP: ')
# validator = IPValidator(ip)
# if validator.is_valid():
#     print('Endereço IP de classe A válido')
# else:
#     print('Endereço IP inválido: não é um endereço de classe A')


# Primeira janela, onde a pessoa vai colocar as informações necessarias parar falar com ela

def janela_info():
    # Tema da janela
    sg.theme('Darkblue15')
    # layout da janela, como ela deve ser
    layout = [
        [sg.Text('E-mail')],
        [sg.Input(key='email')],
        [sg.Text('Ramal')],
        [sg.Input(key='ramal')],
        [sg.Button('Continuar')],
    ]
    # o que esse função deve retornar, no caso seria uma janela aberta, com nome "dados para contato" e usando o Layout definido a cima
    return sg.Window('Dados para contato', layout, finalize=True)

# Segunda tela, onde ja iremos solicitar o TIPO do chamado


def janela_tipo():
    sg.theme('Darkblue15')

    layout = [
        [sg.Text('Tipo')],
        [sg.Radio('Incidente', 'RADIO01'), sg.Radio('Requisição', 'RADIO01')],
        [sg.Text('Categoria')],
        [sg.Radio('Infraestrutrura', 'RADIO02',  default=False, key='infra'), sg.Radio(
            'Sistemas Corporativos', 'RADIO02', default=False, key='sistemas')],
        [sg.Text('Titulo')],
        [sg.Input(key='titulo')],
        [sg.Button('Continuar'), sg.Button('Voltar')],
    ]
    # Sobre os botões em RADIO
    # O primeiro parâmetro é o título do botão de opção.
    # O segundo parâmetro é o grupo do botão de opção. (Apenas um botão no mesmo grupo pode ser selecionado)
    # O terceiro parâmetro é seu estado padrão. ()
    return sg.Window('Tipo do chamado', layout, finalize=True)


def janela_infra():
    sg.theme('Darkblue15')

    layout = [
        [sg.Text('Categoria')],
        [sg.Radio('Informatica', 'RADIO02', default=True, key='informatica')],
        [sg.Radio('Redes', 'RADIO02', default=False, key='redes')],
        [sg.Radio('Telefonia', 'RADIO02', default=False, key='telefonia')],
        [sg.Button('Continuar'), sg.Button('Voltar')],
    ]

    return sg.Window('Categoria Infra', layout=layout, finalize=True)


def janela_sistemas():
    sg.theme('Darkblue15')

    layout = [
        [sg.Text('Categoria')],
        [sg.Radio('Intranet', 'RADIO01', key='intranet')],
        [sg.Radio('Protheus', 'RADIO01', key='protheus')],
        [sg.Radio('QlickView', 'RADIO01', key='qlick')],
        [sg.Button('Continuar'), sg.Button('Voltar')]
    ]

    return sg.Window('Categoria Sistema', layout=layout, finalize=True)


def janela_informatica():
    sg.theme('Darkblue15')

    layout = [
        [sg.Radio('Wifi', 'RADIO1', key='wifi')],
        [sg.Radio('Impressora', 'RADIO1', key='impressora')],
        [sg.Radio('Instalar Aplicativo', 'RADIO1', key='install_app')],
        [sg.Radio('Acessos novo colaborador', 'RADIO1', key='acessos')],
        [sg.Radio('Lentidão', 'RADIO1', key='lentidao')],
        [sg.Text('Outros')],
        [sg.Input(key='problemas_gerais')],
        [sg.Button('Continuar'), sg.Button('Voltar')]
    ]
    return sg.Window('Informatica', layout=layout, finalize=True)

def janela_acessos():
    sg.theme('Darkblue15')

    layout = [
        [sg.Text('Informar nome completo do colaborador que precisa\ndos acessos')],
        [sg.Input(key='novo_colaborador')],
        [sg.Text('Setor: ')],
        [sg.Input(key='setor')],
        [sg.Text('Quais acessos são necessarios: ')],
        [sg.Checkbox('Intranet', default=False, key='intranet')],
        [sg.Checkbox('Protheus', default=False, key='protheus')],
        [sg.Checkbox('Computador', default=False, key='computador')],
        [sg.Checkbox('Qlickview', default=False, key='qlickview')],
        [sg.Checkbox('E-mail', default=False, key='email')],
        [sg.Checkbox('Pasta da Rede', key='pasta_rede')],
        [sg.Text('Informe usuario para espelho')],
        [sg.Input(key='user_espelho')],
        [sg.Button('Continuar'), sg.Button('Voltar')]
    ]
    return sg.Window('Acessos', layout=layout, finalize=True)

def janela_lentidao():
    sg.theme('Darkblue15')

    layout = [
        [],
        [],
        [],
        [],
    ]


janela1, janela2, janela3, janela4, janela5, janela6 = janela_info(), None, None, None, None, None

while True:
    window, event, values = sg.read_all_windows()

    # Fechar janela 1
    if window == janela1 and event == sg.WIN_CLOSED:
        break

    # Minimizar janela 1 e abrir janela 2
    if window == janela1 and event == 'Continuar':
        janela2 = janela_tipo()
        janela1.hide()

    # Fechar janela 2
    if window == janela2 and event == sg.WIN_CLOSED:
        break

    # Sair da janlea 2 e voltar para janela 1
    if window == janela2 and event == 'Voltar':
        janela2.hide()
        janela1.un_hide()

    # Se a escolha for Infra na janela 2, abrir janela 3
    if window == janela2 and values['infra'] == True and event == 'Continuar':
        janela2.hide()
        janela3 = janela_infra()

    # Fechar janela 3
    if window == janela3 and event == sg.WIN_CLOSED:
        break

    # Minimizar janela 3 e voltar janela 2
    if window == janela3 and event == 'Voltar':
        janela3.hide()
        janela2.un_hide()

    # Fechar janela 4
    if window == janela4 and event == sg.WIN_CLOSED:
        break

    # Se a escolha da janela 2 for sistemas, abrir janela 4
    if window == janela2 and values['sistemas'] == True and event == 'Continuar':
        janela2.hide()
        janela4 = janela_sistemas()

    # Minimizar 4 e voltar janela 2
    if window == janela4 and event == 'Voltar':
        janela4.hide()
        janela2.un_hide()

    #======janela_informatica======
    if window == janela3 and values['informatica'] == True and event == 'Continuar':
        janela3.hide()
        janela5 = janela_informatica()
    if window == janela5 and event == sg.WIN_CLOSED:
        break
    if window == janela5 and event == 'Voltar':
        janela5.hide()
        janela3.un_hide()
    if window == janela5 and values['acessos'] == True and event == 'Continuar':
        janela6=janela_acessos()
        janela5.hide()
    if window ==  janela6 and event == sg.WIN_CLOSED:
        break
    if window == janela6 and event ==  'Voltar':
        janela6.hide()
        janela5.un_hide()
    #======janela_informatica======#
    acessos=[]
    #======acessos======#
    if window == janela6 and values['intranet'] == True and event == 'Continuar':
        acessos.append('intranet')
    if window == janela6 and values['protheus'] == True and event == 'Continuar':
        acessos.append('protheus')
    if window == janela6 and values['qlickview'] == True and event == 'Continuar':
        acessos.append('QlickView')
    if window == janela6 and values['computador'] == True and event == 'Continuar':
        acessos.append('Computador')
    if window == janela6 and values['email'] == True and event == 'Continuar':
        acessos.append('E-mail')
    if window == janela6 and values['pasta_rede'] == True and event == 'Continuar':
        acessos.append('Pasta na rede')
    if window == janela6 and event == 'Continuar':
        print(f'Os acessos requeridos são: {acessos}') 
