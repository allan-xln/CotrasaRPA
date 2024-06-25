# Bibliotecas para automação e interação com páginas da web
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Bibliotecas para manipulação de dados
import pandas as pd
import os
import xml.etree.ElementTree as ET
import requests

# Bibliotecas para manipulação de data e hora
from datetime import datetime, timedelta
import time
from holidays import *

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

app = Flask(__name__, template_folder="templates", static_folder="static")


def get_first_last_days_of_month():
    data_atual = datetime.now()
    first_day = data_atual.replace(day=1)
    last_day = first_day + pd.offsets.MonthEnd(0)

    return first_day, last_day


def is_weekend(date):
    return date.weekday() >= 5


def is_holiday(date, holidays):
    return date in holidays


def get_filtered_calendar():
    data_atual = datetime.now()
    start_date = data_atual - timedelta(days=365)
    end_date = data_atual - timedelta(days=1)
    calendar = pd.bdate_range(start=start_date, end=end_date)

    filtered_calendar = [
        date
        for date in calendar
        if not is_holiday(date, holidays) and not is_weekend(date)
    ]
    return filtered_calendar


def get_last_working_day():
    filtered_calendar = get_filtered_calendar()
    if filtered_calendar:
        return filtered_calendar[-1]
    return None


def format_date(date):
    return date.strftime("%d%m%Y")


def initialize_browser():
    downloadBrowser = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=downloadBrowser)
    browser.maximize_window()
    return browser


def login(browser):
    browser.get(
        "https://siconnet.scania.com.br/sicomnet4/newcotrasa/sicomweb.gen.gen.apl.Sicomweb.cls"
    )
    wait = WebDriverWait(browser, 20)
    element = wait.until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="control_11"]'))
    )
    element.send_keys("CTSAUT")
    browser.find_element("xpath", '//*[@id="control_15"]').send_keys("Cotrasa@2022")
    browser.find_element("xpath", '//*[@id="botaoLogin"]').click()


def switch_to_window(browser, url):
    browser.current_window_handle
    wids = browser.window_handles

    for window in wids:
        browser.switch_to.window(window)
        if url in browser.current_url == url:
            break


def find_window(browser, url):
    wids = browser.window_handles

    for window in wids:
        browser.switch_to.window(window)
        if url in browser.current_url == url:
            break
