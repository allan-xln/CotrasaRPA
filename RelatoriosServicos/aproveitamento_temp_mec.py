from ..Library.library import *

@app.route("/tempomec", methods=["POST"])
def run_codetempomec():
    filtered_calendar = get_filtered_calendar()
    first_day, last_day = get_first_last_days_of_month()
    if filtered_calendar:
        last_working_day = filtered_calendar[-1]
        formatted_date = format_date(last_working_day)
        browser = initialize_browser()
        login(browser)
        time.sleep(2)
        switch_to_window(
            browser,
            "https://siconnet.scania.com.br/sicomnet4/newcotrasa/sicomweb.gen.gen.pag.Principal.cls",
        )

    wait = WebDriverWait(browser, 20)

    time.sleep(0.5)

    date = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="a9"]')))
    date.click()

    time.sleep(0.5)

    browser.find_element(By.XPATH, '//*[@id="m60"]/td').click()
    time.sleep(0.5)
    browser.find_element(By.XPATH, '//*[@id="g187"]/td').click()
    time.sleep(0.5)
    browser.find_element(
        By.XPATH, '//*[@id="rotina"]/table[1]/tbody/tr[3]/td/a'
    ).click()

    time.sleep(0.5)

    # Aguarde até que um elemento esteja presente antes de interagir com ele
    element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[@id="zenLayoutTableCell_7"]')
        )
    )

    element.click()

    time.sleep(0.5)

    for _ in range(num_tabs11):
        time.sleep(0.2)
        pyautogui.press("tab")

    time.sleep(0.3)

    pyautogui.typewrite("9,10,11,12,13,14,17")

    time.sleep(0.3)

    pyautogui.press("tab")

    for _ in range(num_downs2):
        time.sleep(0.2)
        pyautogui.press("down")

    time.sleep(0.3)

    pyautogui.press("enter")  # Selecionar "Total por mecânico (sintético)”

    pyautogui.press("tab")

    for _ in range(num_downs2):
        time.sleep(0.2)
        pyautogui.press("down")

    time.sleep(0.3)

    pyautogui.press("enter")  # Selecionar  “Hora decimal. Ex: 10.25”

    pyautogui.press("tab")

    for _ in range(num_downs2):
        time.sleep(0.2)
        pyautogui.press("down")

    time.sleep(0.3)

    pyautogui.press("enter")

    pyautogui.press("tab")

    time.sleep(0.3)

    pyautogui.press("left")

    time.sleep(0.3)

    for _ in range(num_tabs4):
        time.sleep(0.2)
        pyautogui.press("tab")  # Selecionar  “Data Inicial”

    time.sleep(0.3)

    formatted_first_day = first_day.strftime("%d%m%Y")

    time.sleep(0.3)

    formatted_last_day = last_day.strftime("%d%m%Y")

    time.sleep(0.3)

    pyautogui.typewrite(formatted_first_day)
    pyautogui.press("tab")
    time.sleep(0.5)

    pyautogui.typewrite(formatted_last_day)
    time.sleep(0.5)
 
    for _ in range(num_tabs3):
        time.sleep(0.2)
        pyautogui.press("tab")

    for _ in range(num_downs3):
        time.sleep(0.2)
        pyautogui.press("down")

    time.sleep(0.3)

    pyautogui.press("enter")

    time.sleep(0.5)

    pyautogui.press("tab")

    time.sleep(0.5)

    pyautogui.press("space")

    time.sleep(0.5)

    pyautogui.press("tab")

    time.sleep(0.5)

    pyautogui.press("enter")

    time.sleep(120)

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

    time.sleep(10)

    browser.quit()

    return render_template(
        "interface.html",
        resultado="Executado com Sucesso",
        error_message=None,
    )

if __name__ == "__main__":
    app.run(debug=False)