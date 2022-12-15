import pyautogui as pg
import time
import os
import pandas as pd

lista = pd.read_excel('lista_wpp.xlsx')
mensagens = lista[['contato', 'mensagem']]


def max() :
    pg.hotkey('win', 'up')

def close() :
    pg.hotkey('alt', 'f4') 

def carregar_msg() :
    open_wpp()
    time.sleep(120)
    close()
        

def open_wpp() :
    os.system("start Chrome.exe")
    time.sleep(1)
    max()
    time.sleep(4)
    pg.write('https://web.whatsapp.com/')
    time.sleep(1)
    pg.press('enter')
    time.sleep(25)

def varias() :
    open_wpp()
    for i in lista.index :
        to = lista.loc[i, "contato"]
        msg = lista.loc[i, "mensagem"]
        pg.click(160, 187)
        time.sleep(1)
        pg.write(to)
        time.sleep(1)
        pg.click(206, 310)
        time.sleep(1.5)
        pg.click(620, 707)
        time.sleep(1)
        pg.write(msg)
        pg.press('enter')
        time.sleep(2)
        #pg.hotkey('ctrl', 't')
        #time.sleep(1)
        #pg.write('https://web.whatsapp.com/')



def mensagem() :
    to = input("Para: ")
    msg = input("Digite a mensagem: ")
    open_wpp()
    pg.click(160, 187)
    time.sleep(1)
    pg.write(to)
    time.sleep(1)
    pg.click(206, 310)
    time.sleep(1.5)
    pg.click(620, 707)
    time.sleep(1)
    pg.write(msg)
    pg.press('enter')


def funn() :
    to = input("Nome")
    open_wpp()
    msg = "oi"
    pg.click(160, 187)
    time.sleep(1)
    pg.write(to)
    time.sleep(1)
    pg.click(206, 310)
    time.sleep(1.5)
    pg.click(620, 707)
    time.sleep(1)
    while True :
        pg.write(msg)
        pg.press('enter')
        time.sleep(2)   

  


