from ..Library.library import *

@app.route("/garantia", methods=["POST"])
def run_codegarantia():
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
            "https://siconnet.scania.com.br/sicomnet4/newcotrasa/sicomweb.gen.gen.pag.Principal.cls?CSPToken=1IOnKO0MKhZzf5Ki5xZ_YdQN5GcavAe_Ydn5bwpEEYUvAm3bTgVbn7MF7n7DHD5V&CSPCHD=012006060000RyCjI5MShmUHJzzsZhjcIc5qswZdZI9rTz0EfU&",
        )
        

        # Aguarde até que o elemento de login esteja visível antes de interagir com ele
        wait = WebDriverWait(browser, 20)

        time.sleep(0.5)

        # Clique no elemento "Comercial"
        date = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="a9"]')))
        date.click()

        time.sleep(0.5)

        # Seleciona a Rotina desejada
        browser.find_element("xpath", '//*[@id="m63"]/td').click()  # Clique no elemento "Garantia"
        time.sleep(0.5)
        browser.find_element("xpath", '//*[@id="g198"]/td').click()  # Clique no elemento "Relartorio/Arquivo"
        time.sleep(0.5)
        browser.find_element("xpath", '//*[@id="rotina"]/table/tbody/tr[10]/td/a').click()  # Clique no elemento "Relartorio de Garantia"
        time.sleep(0.5)

         # Aguarde até que um elemento esteja presente antes de interagir com ele
        element = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="zenLayoutTableCell_7"]')
            )
        )

        element.click()

        #Campo Opção de Seleção
        for _ in range(num_tabs12):
            time.sleep(0.2)
            pyautogui.press("tab")

        pyautogui.press("tab")

        time.sleep(0.3)

        for _ in range(num_downs4):
            time.sleep(0.2)
            pyautogui.press("down")

        time.sleep(0.5)

        pyautogui.press("enter")  # Seleciona 3 - Em aberto em dado periodo

        time.sleep(0.5)

        pyautogui.press("tab")

        time.sleep(0.5)

        # Campo Opção de Classificação
        for _ in range(num_tabs3):
            time.sleep(0.2)
            pyautogui.press("tab")

        time.sleep(0.3)

        for _ in range(num_downs2):
            time.sleep(0.2)
            pyautogui.press("down")

        time.sleep(0.5)

        pyautogui.press("enter")  # Seleciona 2-por data de abertura

        # Campo Lista Itens

        pyautogui.press("tab")

        time.sleep(0.3)

        for _ in range(num_downs2):
            time.sleep(0.2)
            pyautogui.press("down")

        time.sleep(0.5)

        pyautogui.press("enter")  # Seleciona Não

        time.sleep(0.5)

        # Campo Formato De Saida do Relarorio
        for _ in range(num_tabs2):
            time.sleep(0.2)
            pyautogui.press("tab")

        time.sleep(0.5)

        for _ in range(num_downs3):
            time.sleep(0.2)
            pyautogui.press("down")

        time.sleep(0.5)

        pyautogui.press("enter")  # Seleciona XML

        time.sleep(0.3)

        pyautogui.press("tab")

        time.sleep(0.3)

        pyautogui.press("space")  # Seleciona Armazenar p Download

        time.sleep(0.3)

        pyautogui.press("tab")

        time.sleep(0.3)

        pyautogui.press("enter")  # Seleciona Processar

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
    )

if __name__ == "__main__":
    app.run(debug=True)
