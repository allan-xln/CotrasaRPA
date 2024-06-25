import pyautogui
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from datetime import datetime, timedelta


# Função para verificar se uma data é um final de semana (sábado ou domingo)
def is_weekend(date):
    return date.weekday() >= 5  # 5 representa sábado, 6 representa domingo


# Função para verificar se uma data é um feriado (você precisa fornecer a lista de feriados)
def is_holiday(date, holidays):
    return date in holidays


# Obter a data atual
data_atual = datetime.now()

# Gerar o intervalo de datas a partir de hoje até uma data no passado
start_date = data_atual - timedelta(days=365)  # Um ano atrás
end_date = data_atual - timedelta(days=1)  # Ontem

calendar = pd.bdate_range(start=start_date, end=end_date)

# Lista de feriados (substitua com seus feriados específicos)
holidays = [
    datetime(2023, 1, 1),
    (2023, 2, 20),
    (2023, 2, 21),
    (2023, 4, 7),
    (2023, 4, 21),
    (2023, 5, 1),
    (2023, 6, 19),
    (2023, 9, 7),
    (2023, 10, 12),
    (2023, 11, 2),
    (2023, 11, 15),
    (2023, 12, 25),
    (2024, 1, 1),
    (2024, 2, 12),
    (2024, 2, 13),
    (2024, 3, 29),
    (2024, 4, 21),
    (2024, 5, 1),
    (2024, 5, 30),
    (2024, 9, 7),
    (2024, 10, 12),
    (2024, 11, 2),
    (2024, 11, 15),
    (2024, 12, 25),
    (2025, 1, 1),
    (2025, 3, 3),
    (2025, 3, 4),
    (2025, 4, 18),
    (2025, 4, 21),
    (2025, 5, 1),
    (2025, 6, 19),
    (2025, 9, 7),
    (2025, 10, 12),
    (2025, 11, 2),
    (2025, 11, 15),
    (2025, 12, 25),
    (2026, 1, 1),
    (2026, 2, 16),
    (2026, 2, 17),
    (2026, 4, 3),
    (2026, 4, 21),
    (2026, 5, 1),
    (2026, 6, 4),
    (2026, 9, 7),
    (2026, 10, 12),
    (2026, 11, 2),
    (2026, 11, 15),
    (2026, 12, 25),
    (2027, 1, 1),
    (2027, 2, 8),
    (2027, 2, 9),
    (2027, 3, 26),
    (2027, 4, 21),
    (2027, 5, 1),
    (2027, 5, 27),
    (2027, 9, 7),
    (2027, 10, 12),
    (2027, 11, 2),
    (2027, 11, 15),
    (2027, 12, 25),
    (2028, 1, 1),
    (2028, 2, 28),
    (2028, 2, 29),
    (2028, 4, 14),
    (2028, 4, 21),
    (2028, 5, 1),
    (2028, 6, 15),
    (2028, 9, 7),
    (2028, 10, 12),
    (2028, 11, 2),
    (2028, 11, 15),
    (2028, 12, 25),
    (2029, 1, 1),
    (2029, 2, 12),
    (2029, 2, 13),
    (2029, 3, 30),
    (2029, 4, 21),
    (2029, 5, 1),
    (2029, 5, 31),
    (2029, 9, 7),
    (2029, 10, 12),
    (2029, 11, 2),
    (2029, 11, 15),
    (2029, 12, 25),
    (2030, 1, 1),
    (2030, 3, 4),
    (2030, 3, 5),
    (2030, 4, 19),
    (2030, 4, 21),
    (2030, 5, 1),
    (2030, 6, 20),
    (2030, 9, 7),
    (2030, 10, 12),
    (2030, 11, 2),
    (2030, 11, 15),
    (2030, 12, 25),
    (2031, 1, 1),
    (2031, 2, 24),
    (2031, 2, 25),
    (2031, 4, 11),
    (2031, 4, 21),
    (2031, 5, 1),
    (2031, 6, 12),
    (2031, 9, 7),
    (2031, 10, 12),
    (2031, 11, 2),
    (2031, 11, 15),
    (2031, 12, 25),
    (2032, 1, 1),
    (2032, 2, 9),
    (2032, 2, 10),
    (2032, 3, 26),
    (2032, 4, 21),
    (2032, 5, 1),
    (2032, 5, 27),
    (2032, 9, 7),
    (2032, 10, 12),
    (2032, 11, 2),
    (2032, 11, 15),
    (2032, 12, 25),
    (2033, 1, 1),
    (2033, 2, 28),
    (2033, 3, 1),
    (2033, 4, 15),
    (2033, 4, 21),
    (2033, 5, 1),
    (2033, 6, 16),
    (2033, 9, 7),
    (2033, 10, 12),
    (2033, 11, 2),
    (2033, 11, 15),
    (2033, 12, 25),
    (2034, 1, 1),
    (2034, 2, 20),
    (2034, 2, 21),
    (2034, 4, 7),
    (2034, 4, 21),
    (2034, 5, 1),
    (2034, 6, 8),
    (2034, 9, 7),
    (2034, 10, 12),
    (2034, 11, 2),
    (2034, 11, 15),
    (2034, 12, 25),
    (2035, 1, 1),
    (2035, 2, 5),
    (2035, 2, 6),
    (2035, 3, 23),
    (2035, 4, 21),
    (2035, 5, 1),
    (2035, 5, 24),
    (2035, 9, 7),
    (2035, 10, 12),
    (2035, 11, 2),
    (2035, 11, 15),
    (2035, 12, 25),
    (2036, 1, 1),
    (2036, 2, 25),
    (2036, 2, 26),
    (2036, 4, 11),
    (2036, 4, 21),
    (2036, 5, 1),
    (2036, 6, 12),
    (2036, 9, 7),
    (2036, 10, 12),
    (2036, 11, 2),
    (2036, 11, 15),
    (2036, 12, 25),
    (2037, 1, 1),
    (2037, 2, 16),
    (2037, 2, 17),
    (2037, 4, 3),
    (2037, 4, 21),
    (2037, 5, 1),
    (2037, 6, 4),
    (2037, 9, 7),
    (2037, 10, 12),
    (2037, 11, 2),
    (2037, 11, 15),
    (2037, 12, 25),
    (2038, 1, 1),
    (2038, 3, 8),
    (2038, 3, 9),
    (2038, 4, 21),
    (2038, 4, 23),
    (2038, 5, 1),
    (2038, 6, 24),
    (2038, 9, 7),
    (2038, 10, 12),
    (2038, 11, 2),
    (2038, 11, 15),
    (2038, 12, 25),
    (2039, 1, 1),
    (2039, 2, 21),
    (2039, 2, 22),
    (2039, 4, 8),
    (2039, 4, 21),
    (2039, 5, 1),
    (2039, 6, 9),
    (2039, 9, 7),
    (2039, 10, 12),
    (2039, 11, 2),
    (2039, 11, 15),
    (2039, 12, 25),
    (2040, 1, 1),
    (2040, 2, 13),
    (2040, 2, 14),
    (2040, 3, 30),
    (2040, 4, 21),
    (2040, 5, 1),
    (2040, 5, 31),
    (2040, 9, 7),
    (2040, 10, 12),
    (2040, 11, 2),
    (2040, 11, 15),
    (2040, 12, 25),
]

# Filtrar as datas removendo feriados e finais de semana
filtered_calendar = [
    date for date in calendar if not is_holiday(date, holidays) and not is_weekend(date)
]

# Verificar se existem datas disponíveis após a filtragem
if filtered_calendar:
    # Obter a última data do intervalo filtrado (dia útil anterior a hoje)
    data_ultimo_dia_util = filtered_calendar[-1]

    # Inicializa o driver do Chrome
    downloadBrowser = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=downloadBrowser)
    browser.maximize_window()

    # Navega para o site desejado
    browser.get(
        "http://192.168.1.50/sicomnet4/newcotrasa/sicomweb.gen.gen.apl.Sicomweb.cls"
    )

    # Aguarde até que o elemento de login esteja visível antes de interagir com ele
    wait = WebDriverWait(browser, 20)
    element = wait.until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="control_11"]'))
    )

    # Preencha o campo de login com o valor desejado
    element.send_keys("CTSLFG")

    # Preencha o campo de senha com o valor desejado
    browser.find_element("xpath", '//*[@id="control_15"]').send_keys("abcDefgh1!")

    # Clique no botão de login
    browser.find_element("xpath", '//*[@id="botaoLogin"]').click()

    # Obtenha as alças das janelas abertas
    browser.current_window_handle
    wids = browser.window_handles

    # Função para encontrar uma janela específica
    def find_window(url: str):
        for window in wids:
            browser.switch_to.window(window)
            if url in browser.current_url == url:
                break

    # Encontre a janela desejada
    find_window(
        "http://192.168.1.50/sicomnet4/newcotrasa/sicomweb.gen.gen.pag.Principal.cls?CSPToken=1IOnKO0MKhZzf5Ki5xZ_YdQN5GcavAe_Ydn5bwpEEYUvAm3bTgVbn7MF7n7DHD5V&CSPCHD=012006060000RyCjI5MShmUHJzzsZhjcIc5qswZdZI9rTz0EfU&"
    )

    # Clique no elemento "Comercial"
    date = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="a9"]')))
    date.click()

    time.sleep(0.2)

    # Seleciona a Rotina desejada
    browser.find_element("xpath", '//*[@id="m50"]/td').click()
    time.sleep(0.2)
    browser.find_element("xpath", '//*[@id="g134"]/td').click()
    time.sleep(0.2)
    browser.find_element(
        "xpath", '//*[@id="rotina"]/table[1]/tbody/tr[12]/td/a'
    ).click()
    time.sleep(0.5)

    # Encontre a janela desejada
    # find_window("http://192.168.1.50/sicomnet4/newcotrasa/sicomweb.gen.gen.pag.Principal.cls?CSPToken=A46LH92YaO5asG5ka_J$IR1dKGpIUiof0wgbp50rhlGtwSYVGWN32jYZxIcLN6ta&CSPCHD=014007060000FADj2N3S3mriA$HTWQDcLC8MipkiRHEuuDEFCB&")

    # Clique em um elemento específico para começar a executar o trafego de "tabs" na tela
    browser.find_element("xpath", '//*[@id="zenLayoutTableCell_6"]').click()

    # Aguarde até que um elemento esteja presente antes de interagir com ele
    element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="zenLayoutTableCell_4"]'))
    )

    element.click()

    # Simule o pressionamento da tecla Enter
    pyautogui.press("enter")

    time.sleep(0.5)

    # Seleciona Data de Referencia dos dias úteis
    num_tabs1 = 5
    for _ in range(num_tabs1):
        pyautogui.press("tab")

    num_downs1 = 2
    for _ in range(num_downs1):
        pyautogui.press("down")

    pyautogui.press("enter")

    num_tabs2 = 2
    for _ in range(num_tabs2):
        pyautogui.press("tab")

    time.sleep(0.5)
    
    pyautogui.typewrite(data_ultimo_dia_util("%d%m%Y"))

    time.sleep(0.2)

    # Seleciona Opção de Seleção - "Por Linha"
    num_tabs3 = 1
    for _ in range(num_tabs3):
        pyautogui.press("tab")

    num_downs3 = 4
    for _ in range(num_downs3):
        pyautogui.press("down")

    pyautogui.press("enter")

    time.sleep(0.2)

    # Prenche Valores das linhas
    pyautogui.press("tab")
    pyautogui.typewrite("1,2,3,4,5,7,8,9,10,12,13,16,17,18,19,42,45,47,49,53,55,56")

    time.sleep(0.2)

    # Prenche Valores das linhas
    pyautogui.press("tab")
    pyautogui.typewrite("E")

    time.sleep(0.2)

    # Prenche Valores de Tipo de Estoque
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.typewrite("B,C,D,G,O,P,R,T")

    time.sleep(0.2)

    # Seleciona informações finais
    num_tabs4 = 3
    for _ in range(num_tabs4):
        pyautogui.press("tab")

    num_downs4 = 3
    for _ in range(num_downs4):
        pyautogui.press("down")

    pyautogui.press("enter")

    pyautogui.press("tab")

    pyautogui.press("spacebar")

    pyautogui.press("tab")

    pyautogui.press("enter")

time.sleep(1000)

browser.quit()
