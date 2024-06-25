from RelatoriosEstoque.older.library import *

filtered_calendar = get_filtered_calendar()
if filtered_calendar:
    last_working_day = filtered_calendar[-1]
    formatted_date = format_date(last_working_day)
    browser = initialize_browser()
    login(browser)
    switch_to_window(
        browser,
        "http://192.168.1.50/sicomnet4/newcotrasa/sicomweb.gen.gen.pag.Principal.cls?CSPToken=1IOnKO0MKhZzf5Ki5xZ_YdQN5GcavAe_Ydn5bwpEEYUvAm3bTgVbn7MF7n7DHD5V&CSPCHD=012006060000RyCjI5MShmUHJzzsZhjcIc5qswZdZI9rTz0EfU&",
    )

    # Aguarde até que o elemento de login esteja visível antes de interagir com ele
    wait = WebDriverWait(browser, 20)

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

    time.sleep(10)
    # Clique em um elemento específico para começar a executar o trafego de "tabs" na tela
    browser.find_element("xpath", '//*[@id="zenLayoutTableCell_6"]').click()

    time.sleep(10)

    # Simule o pressionamento da tecla Enter
    pyautogui.press("enter")

    time.sleep(0.5)

    # Seleciona Filial
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

    date = get_last_working_day()

    if date:
        formatted_date = format_date(date)
        pyautogui.typewrite(formatted_date)

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

    pyautogui.press("space")

    pyautogui.press("tab")

    pyautogui.press("enter")

time.sleep(1000)

browser.quit()
