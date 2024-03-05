import pyautogui
import time 
import pandas

pyautogui.PAUSE = 0.5

pyautogui.press("win")
pyautogui.write("Chrome")
pyautogui.press("enter")

link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
pyautogui.write(link)
pyautogui.press("enter")

time.sleep(2)

pyautogui.click(x=675, y=614)
pyautogui.write("jgmalafaia04@gmail.com")
pyautogui.click(x=621, y=765)
pyautogui.write('vascodagama')
pyautogui.click(x=967, y=846)

time.sleep(2)
tabela = pandas.read_csv('produtos.csv')
print(tabela)

for linha in tabela.index:
    
    pyautogui.click(x=843, y=432)
    
    codigo=(str(tabela.loc[linha, "codigo"]))
    pyautogui.write(codigo)
    pyautogui.press('tab')
    
    marca=(str(tabela.loc[linha, "marca"]))
    pyautogui.write(marca)
    pyautogui.press('tab')
    
    tipo=(str(tabela.loc[linha, "tipo"]))
    pyautogui.write(tipo)
    pyautogui.press('tab')
    
    categoria=(str(tabela.loc[linha, "categoria"]))
    pyautogui.write(categoria)
    pyautogui.press('tab')
    
    pyautogui.write((str(tabela.loc[linha, "preco_unitario"])))
    pyautogui.press('tab')
    
    custo=(str(tabela.loc[linha, "custo"]))
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press('tab')
    
    obs=(str(tabela.loc[linha, "obs"]))
    if not pandas.isna:
        pyautogui.write(obs)    
    pyautogui.press('tab')
    pyautogui.press("enter")
    
    pyautogui.scroll(9999)
    