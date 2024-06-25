from ..Library.library import *

@app.route("/geralestoque", methods=["POST"])
def run_codeestoque():
    filtered_calendar = get_filtered_calendar()
    if filtered_calendar:
        last_working_day = filtered_calendar[-1]
        formatted_date = format_date(last_working_day)
        browser = initialize_browser()
        login(browser)
        time.sleep(2)
        switch_to_window(
            browser,
            "https://siconnet.scania.com.br/sicomnet4/newcotrasa/sicomweb.gen.gen.pag.Principal.cls?CSPToken=1IOnKO0MKhZzf5Ki5xZ_YdQN5GcavAe_Ydn5bwpEEYUvAm3bTgVbn7MF7n7DHD5V&CSPCHD=012006060000RyCjI5MShmUHJzzsZhjcIc5qswZdZI9rTz0EfU&",
        )

    # Aguarde até que o elemento de login esteja visível antes de interagir com ele
    wait = WebDriverWait(browser, 30)
    time.sleep(0.5)

    # Clique no elemento "Comercial"
    try:
        date = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="a9"]')))
        date.click()
    except Exception as e:
        # Handle the case when switching to the window fails
        error_message = "Não foi possível acessar o Sicon"
        return render_template(
            "interface.html",
            resultado_geralestoque="Erro na Execução",
            error_message=error_message,
        )

    time.sleep(0.5)

    # Seleciona a Rotina desejada

    # Controle estoque
    browser.find_element("xpath", '//*[@id="m50"]/td').click()
    time.sleep(0.5)

    # Relatorio Arquivo
    browser.find_element("xpath", '//*[@id="g134"]/td').click()
    time.sleep(0.5)

    # Geral Estoque
    browser.find_element(
        "xpath", '//*[@id="rotina"]/table[1]/tbody/tr[12]/td/a'
    ).click()
    time.sleep(0.5)

    # Aguarde até que um elemento esteja presente antes de interagir com ele
    element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[@id="zenLayoutTableCell_7"]')
        )
    )

    element.click()

    # Simule o pressionamento da tecla Enter
    pyautogui.press("enter")

    time.sleep(0.5)

    # Seleciona Data de Referencia dos dias úteis
    for _ in range(num_tabs11):
        time.sleep(0.2)
        pyautogui.press("tab")

    for _ in range(num_downs2):
        time.sleep(0.2)
        pyautogui.press("down")

    pyautogui.press("enter")

    time.sleep(0.5)

    for _ in range(num_tabs2):
        time.sleep(0.2)
        pyautogui.press("tab")

    time.sleep(0.5)

    date = get_last_working_day()

    if date:
        formatted_date = format_date(date)
        pyautogui.typewrite(formatted_date)

    time.sleep(0.2)

    # Seleciona Opção de Seleção - "Por Linha"
    for _ in range(num_tabs1):
        time.sleep(0.2)
        pyautogui.press("tab")

    for _ in range(num_downs4):
        time.sleep(0.2)
        pyautogui.press("down")

    pyautogui.press("enter")

    time.sleep(1.5)

    # Prenche Valores das linhas
    pyautogui.press("tab")
    pyautogui.typewrite("1,2,3,4,5,7,8,9,10,12,13,16,17,18,19,42,45,47,49,53,55,56")

    time.sleep(0.5)

    # Prenche Opção de Seleção
    pyautogui.press("tab")

    time.sleep(0.5)

    pyautogui.typewrite("E")

    time.sleep(0.5)

    # Prenche Valores de Tipo de Estoque
    pyautogui.press("tab")

    time.sleep(0.5)

    pyautogui.press("tab")

    time.sleep(0.5)

    pyautogui.typewrite("B,C,D,G,O,P,R,T")

    time.sleep(0.5)

    # Seleciona informações finais
    for _ in range(num_tabs3):
        time.sleep(0.2)
        pyautogui.press("tab")

    for _ in range(num_downs3):
        time.sleep(0.2)
        pyautogui.press("down")

    pyautogui.press("enter")

    time.sleep(0.5)

    pyautogui.press("tab")

    time.sleep(0.5)

    pyautogui.press("space")

    time.sleep(0.5)

    pyautogui.press("tab")

    time.sleep(0.5)

    pyautogui.press("enter")

    time.sleep(30)

    # Acessa a Janela
    url_esperado = "https://siconnet.scania.com.br/sicomnet4/newcotrasa/sicomweb.gen.gen.pag.RelatorioArmazenado.cls?"

    # Chama a função que aguarda e tenta alternar para a nova janela
    switch_to_window_with_retry(browser, url_esperado)

    # Baixar Arquivo
    element = WebDriverWait(browser, 30).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="tr_0_24"]/td[10]/span'))
    )

    element.click()
    element.click()

    time.sleep(8)

    browser.quit()

    return render_template(
        "interface.html",
        resultado="Executado com Sucesso",
        error_message=None,
    )

if __name__ == "__main__":
    app.run(debug=False)
