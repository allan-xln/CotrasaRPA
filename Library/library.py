# Bibliotecas para automação e interação com páginas da web
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from flask_apscheduler import APScheduler

# Bibliotecas para manipulação de dados
import pandas as pd
import os
import xml.etree.ElementTree as ET
import requests

# Bibliotecas para manipulação de data e hora
from datetime import datetime, timedelta
import time
import holidays as hdays
import schedule

# Bibliotecas para criação de aplicativos web
from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, send
from webdriver_manager.chrome import ChromeDriverManager

# Bibliotecas para monitoramento de arquivos e diretórios
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Biblioteca para manipulação de sockets e rede
import socket

# Biblioteca para execução de código em threads
from threading import Thread

# Biblioteca para ambiente de producao
from waitress import serve

# Inicialização do aplicativo Flask
app = Flask(__name__, template_folder="templates", static_folder="static")

# Função para obter o primeiro e o último dia do mês
def get_first_last_days_of_month():
    data_atual = datetime.now()

    # Calcula o dia anterior
    data_anterior = data_atual - timedelta(days=1)

    # Verifica se o dia anterior é feriado ou final de semana
    while is_holiday(data_anterior, hdays.Brazil()) or data_anterior.weekday() >= 5:
        data_anterior -= timedelta(days=1)

    # Verifica se o dia anterior é o primeiro dia do mês e não é um feriado ou final de semana
    if data_anterior.day == 1 and not (is_holiday(data_anterior, hdays.Brazil()) or data_anterior.weekday() >= 5):
        first_day_month = data_anterior.replace(day=1)
        last_day_month = first_day_month + pd.offsets.MonthEnd(0)
    else:
        # Se o dia anterior não for o primeiro dia do mês e não é um feriado ou final de semana, considera o mês atual
        first_day_month = data_atual.replace(day=1)
        last_day_month = first_day_month + pd.offsets.MonthEnd(0)

    return first_day_month, last_day_month

# Função para verificar se uma data é fim de semana
def is_weekend(date):
    return date.weekday() >= 5

# Função para verificar se uma data é feriado
def is_holiday(date, holidays_instance):
    return date in holidays_instance

# Função para obter o calendário filtrado sem fins de semana e feriados brasileiros
def get_filtered_calendar():
    data_atual = datetime.now()
    start_date = data_atual - timedelta(days=365)
    end_date = data_atual - timedelta(days=1)
    
    holidays_instance = hdays.Brazil()
    
    filtered_calendar = pd.bdate_range(start=start_date, end=end_date, freq='B')
    filtered_calendar = [date for date in filtered_calendar if date not in holidays_instance]
    
    return filtered_calendar

# Função para obter o último dia útil
def get_last_working_day():
    filtered_calendar = get_filtered_calendar()
    if filtered_calendar:
        return filtered_calendar[-1]
    return None

# Função para formatar uma data no formato "ddMMyyyy"
def format_date(date):
    return date.strftime("%d%m%Y")

# Função para inicializar o navegador Chrome
def initialize_browser():
    # Configura as opções do Chrome
    chrome_options = Options()
    chrome_options.add_argument("user-data-dir=C:\\Users\\Automação\\AppData\\Local\\Google\\User Data\\Default")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")

    # Configura preferências para downloads
    prefs = {"safebrowsing.enabled": "false"}
    chrome_options.add_experimental_option("prefs", prefs)

    # Inicia o serviço do Chrome
    downloadBrowser = Service(ChromeDriverManager().install())

    # Inicia o navegador Chrome com as opções configuradas
    browser = webdriver.Chrome(service=downloadBrowser, options=chrome_options)

    browser.maximize_window()
    return browser

# Função para fazer login em uma página da web
def login(browser):
    browser.get("https://siconnet.scania.com.br/sicomnet4/newcotrasa/sicomweb.gen.gen.apl.Sicomweb.cls")
    wait = WebDriverWait(browser, 20)

    try:
        element = wait.until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="control_11"]'))
        )

        element.send_keys("CTSAUT")
        #element.send_keys("CTSBOT")
        #element.send_keys("CTSASP")

    except TimeoutException:
        error_message = "Não foi possível acessar o SiconNet"
        return render_template(
            "interface.html",
            resultado_geralestoque="Erro na Execução",
            error_message=error_message,
        )

    browser.find_element(By.XPATH, '//*[@id="control_15"]').send_keys("Cotrasa@2023*")
    #browser.find_element(By.XPATH, '//*[@id="control_15"]').send_keys("Cotrasa2024**")
    #browser.find_element(By.XPATH, '//*[@id="control_15"]').send_keys("Xlncs2023**")

    browser.find_element(By.ID, 'botaoLogin').click()

# Função para alternar para uma janela específica do navegador
def switch_to_window(browser, url):
    browser.current_window_handle
    wids = browser.window_handles

    for window in wids:
        browser.switch_to.window(window)
        if url in browser.current_url == url:
            break

# Função para alternar para uma janela específica do navegador com tentativas de retry
def switch_to_window_with_retry(browser, url_esperado):
    while True:
        try:
            janelas = browser.window_handles
            for janela in janelas:
                browser.switch_to.window(janela)  
                if url_esperado in browser.current_url:
                    return
            time.sleep(10)
        except Exception as e:
            print("Erro:", e)
            time.sleep(10)

# Função para encontrar uma janela específica do navegador
def find_window(browser, url):
    wids = browser.window_handles

    for window in wids:
        browser.switch_to.window(window)
        if url in browser.current_url == url:
            break

# Definindo num_downs
num_downs1 = 1
num_downs2 = 2
num_downs3 = 3
num_downs4 = 4
num_downs5 = 5
num_downs6 = 6
num_downs7 = 7
num_downs8 = 8
num_downs9 = 9
num_downs10 = 10
num_downs11 = 11
num_downs12 = 12
num_downs13 = 13
num_downs14 = 14
num_downs15 = 15
num_downs16 = 16
num_downs17 = 17
num_downs18 = 18
num_downs19 = 19
num_downs20 = 20

# Definindo num_tabs
num_tabs1 = 1
num_tabs2 = 2
num_tabs3 = 3
num_tabs4 = 4
num_tabs5 = 5
num_tabs6 = 6
num_tabs7 = 7
num_tabs8 = 8
num_tabs9 = 9
num_tabs10 = 10
num_tabs11 = 11
num_tabs12 = 12
num_tabs13 = 13
num_tabs14 = 14
num_tabs15 = 15
num_tabs16 = 16
num_tabs17 = 17
num_tabs18 = 18
num_tabs19 = 19
num_tabs20 = 20
