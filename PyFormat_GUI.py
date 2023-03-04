from time import sleep
from pyautogui import hotkey
from pyautogui import press
from pyautogui import click
from pyautogui import write
from pyautogui import prompt
from pyautogui import alert
from pyautogui import password
from pyautogui import confirm
import pyautogui
from pyautogui import getActiveWindow
import os
import shutil
import PySimpleGUI as sg

usuarios = ['Enzo', 'Felipe', 'Hiago', 'Lucas', 'Marcos']
dominios = ['ho.local', 'skauto.corp']

sg.theme('reddit')

estilo = [
    [sg.Text('Insira as informações do computador')],
    [sg.Text('Hostname:'), sg.Input(key='ativo', size = (20,1))],
    [sg.Text('Dominio:   '), sg.Combo(dominios, key='dominio', size = (18,1))],
    [sg.Text('Users:      '),sg.Combo(usuarios, key='user', size= (18,1))],
    [sg.Text('Senha:     '),sg.Input(key='senha', password_char='*', size = (20,1))],
    [sg.Button('Continuar'), sg.Button('Sair')],
]

janela = sg.Window('Informações', layout=estilo)

while True:
    event, values = janela.read()

    if event == sg.WIN_CLOSED or event == 'Sair':
        break
    if event == 'Continuar' and values['user'] == 'Enzo':
        user = 'enzo.araujo'
        senha = values['senha']
    if event == 'Continuar' and values['user'] == 'Lucas':
        user = 'lucas.candeias'
        senha = values['senha']
    if event == 'Continuar' and values['user'] == 'Marcos':
        user = 'marcos.floriano'
        senha = values['senha']
    if event == 'Continuar' and values['user'] == 'Hiago':
        user = 'hiago.alonso'
        senha = values['senha']
    if event == 'Continuar' and values['user'] == 'Felipe':
        user = 'felipe.lublanski'
        senha = values['senha']
    if event == 'Continuar':
        dominio = values['dominio']
        ativo = values['ativo']

    pyautogui.PAUSE = 1.5

    hotkey('win', 'd')
    sleep(1)
    hotkey('win', 'r')
    sleep(1)
    write('powershell')
    sleep(0.5)
    press('enter')
    sleep(4)
    write(f"Add-Computer –DomainName {dominio} -NewName {ativo}")
    sleep(1)
    press('enter')
    sleep(0.5)
    write(user)
    sleep(0.5)
    press('tab')
    write(senha)
    sleep(0.5)
    press('enter')
    sleep(3)
    hotkey('win', 'd')

    # Buscar arquivos

    # Install
    hotkey('win', 'r')
    sleep(0.5)
    write(r'''C:\Util\Necessario''')
    sleep(0.5)
    press('enter')
    sleep(1)
    explorer = getActiveWindow()
    sleep(0.5)
    pyautogui.getWindowsWithTitle("Necessario")[0].maximize()
    sleep(0.5)
    click(800, 400)
    press('c')
    sleep(0.5)
    hotkey('ctrl', 'c')
    sleep(0.5)
    hotkey('win', 'r')
    sleep(0.5)
    write(r'''C:''')
    sleep(0.5)
    press('enter')
    sleep(1)
    hotkey('ctrl', 'v')
    sleep(5)
    hotkey('win', 'r')
    sleep(0.5)
    write('cmd')
    sleep(0.5)
    press('enter')
    sleep(2)
    write(r'''cd\
    cd Cisco
    FOR %F IN (vpn-cisco.msi) DO START %F /quiet
    ''')
    sleep(0.5)
    press('enter')
    sleep(8)
    hotkey('win', 'r')
    sleep(0.5)
    write('cmd')
    sleep(0.5)
    press('enter')
    sleep(1)
    write(r'''cd\
    cd Cisco
    FOR %F IN (umbrella-cisco.msi) DO START %F /quiet
    ''')
    sleep(1)
    press('enter')
    sleep(8)
    hotkey('win', 'r')
    sleep(0.5)
    write(r'C:\Util\Necessario')
    sleep(1)
    press('enter')
    sleep(1)
    if dominio == 'ho.local':
        press('k')
        sleep(0.5)
        press('enter')
        sleep(3)
        kasper = getActiveWindow()
        click(kasper.left + 99, kasper.top + 350)
        sleep(60)
    else:
        press('s')
        sleep(0.5)
        press('enter')
        sleep(3)
        kaspersk = getActiveWindow()
        click(kaspersk.left + 169, kaspersk.top + 325)
        sleep(60)
        click(kaspersk.left + 169, kaspersk.top + 325)
        sleep(1)
    hotkey('win', 'r')
    sleep(0.5)
    write('cmd')
    sleep(0.5)
    press('enter')
    sleep(1)
    write(r'''cd "C:\Program Files (x86)\Kaspersky Lab\NetworkAgent"
    ''')
    sleep(1)
    press('enter')
    sleep(0.5)
    write('klnagchk.exe -sendhb')
    sleep(0.5)
    press('enter')
    sleep(7)
    hotkey('win', 'd')
    sleep(2)
    os.chdir(r"C:\Util\Necessario\Cisco\profiles\umbrella")
    os.listdir()
    for file in os.listdir():
        print(file)
        shutil.copy2(
            file, r'C:\programdata\Cisco\Cisco AnyConnect Secure Mobility Client\umbrella\\')
    sleep(1)
    pyautogui.alert('Maquina padronizada')