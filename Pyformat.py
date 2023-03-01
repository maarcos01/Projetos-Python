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


def get_dominio():
    ad = str(prompt("Dominio: "))
    if (ad == 'ho.local'):
        return 1
    elif (ad == 'skauto.corp'):
        return 2
    else:
        alert("Digite uma opção válida.")
        return False


valorDominio = False
while not valorDominio:
    valorDominio = get_dominio()
if valorDominio == 1:
    dominio = ('ho.local')
else:
    dominio = ('skauto.corp')

ativo = str(prompt('Hostname').replace(" ", "").upper())


def u():
    user = str(prompt("Usuario: "))
    if (user == 'lucas.candeias'):
        return 1
    elif (user == 'marcos.floriano'):
        return 2
    elif (user == 'hiago.alonso'):
        return 3
    elif (user == 'enzo.araujo'):
        return 4
    elif (user == 'felipe.lublanski'):
        return 5
    else:
        alert("Digite uma opção válida.")
        return False


valor = False
while not valor:
    valor = u()
if valor == 1:
    print('Usuario valido')
    user = ('lucas.candeias')
if valor == 2:
    print('Usuario valido')
    user = ('marcos.floriano')
if valor == 3:
    print('Usuario valido')
    user = ('hiago.alonso')
if valor == 4:
    print('Usuario valido')
    user = ('enzo.araujo')
if valor == 5:
    print('Usuario Valido')
    user = ('felipe.lublanski')

senha = str(password(text='Senha', title='',
            default='', mask='*').replace(" ", ""))
check = confirm(text='Continuar', title='ultima ação',
                buttons=['OK', 'Cancel'])
while (check != 'OK'):
    print("Senha errada! Tente novamente!")
    senha = str(password(text='Senha', title='',
                default='', mask='*').replace(" ", ""))
    check = confirm(text='Continuar', title='ultima ação',
                    buttons=['OK', 'Cancel'])

if check == 'OK':
    print('seguir')
else:
    print('Parar')
print('Carregando...')
sleep(3)

# Pausa Global de 1segundo e meio
pyautogui.PAUSE = 1.5

# Trocar nome e add AD
hotkey('win', 'd')
sleep(1)
hotkey('win', 'r')
sleep(1)
write('sysdm.cpl')
sleep(0.5)
press('enter')
sleep(1.5)
press(['tab', 'tab'])
sleep(0.5)
press('enter')
sleep(0.5)
write(ativo)
sleep(1)
press(['tab', 'tab', 'up', 'tab'])
sleep(0.5)
write(dominio)
sleep(0.1)
sistema = getActiveWindow()
click(sistema.left + 166, sistema.top + 370)
sleep(6)
write(user)
sleep(0.5)
press('tab')
write(senha)
sleep(0.5)
press('enter')
sleep(3)
press('enter')
sleep(1.5)
press('enter')
hotkey('alt', 'f4')
press('tab')
sleep(0.5)
press('enter')
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
