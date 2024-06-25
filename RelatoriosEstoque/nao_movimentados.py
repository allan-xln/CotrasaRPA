from ..Library.library import *


@app.route("/itensnaomov", methods=["POST"])
def run_codeitensnaomov():
    filtered_calendar = get_filtered_calendar()
    if filtered_calendar:
        """last_working_day = filtered_calendar[-1]"""
        """ formatted_date = format_date(last_working_day) """
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
        date = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="a9"]')))
        date.click()

        time.sleep(0.5)

        # Seleciona a Rotina desejada

        # Controle de estoque
        browser.find_element("xpath", '//*[@id="m50"]/td').click()
        time.sleep(0.5)

        # Relatórios/Arquivo
        browser.find_element("xpath", '//*[@id="g134"]/td').click()
        time.sleep(0.5)

        # Rel. Itens não Movtos
        browser.find_element(
            "xpath", '//*[@id="rotina"]/table/tbody/tr[15]/td/a'
        ).click()

        time.sleep(0.5)

        # Aguarde até que um elemento esteja presente antes de interagir com ele
        element = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="zenLayoutTableCell_7"]')
            )
        )

        time.sleep(0.5)

        element.click()

        # Seleciona Data de Referencia dos dias úteis
        for _ in range(num_tabs11):
            time.sleep(0.2)
            pyautogui.press("tab")

        # Seleciona "Filial"
        pyautogui.press("down")

        time.sleep(0.5)

        pyautogui.press("down")

        time.sleep(0.5)

        pyautogui.press("enter")

        # Preenche Linha
        for _ in range(num_tabs3):
            time.sleep(0.2)
            pyautogui.press("tab")

        time.sleep(0.5)

        pyautogui.typewrite("1,2,3,4,5,7,8,9,10,12,13,16,17,18,19,42,45,47,49,53,55,56")

        time.sleep(0.5)

        pyautogui.press("tab")

        time.sleep(0.5)

        # Preenche "Nº de dias a considerar"
        pyautogui.typewrite("180")

        time.sleep(0.5)

        # Seleciona Custo Médio
        for _ in range(num_tabs5):
            time.sleep(0.2)
            pyautogui.press("tab")

        for _ in range(num_downs3):
            time.sleep(0.2)
            pyautogui.press("down")

        time.sleep(0.5)

        pyautogui.press("enter")

        time.sleep(0.5)

        # Seleciona XML
        for _ in range(num_tabs2):
            time.sleep(0.2)
            pyautogui.press("tab")

        for _ in range(num_downs3):
            time.sleep(0.2)
            pyautogui.press("down")

        pyautogui.press("enter")

        time.sleep(0.5)

        # Armazena para download
        pyautogui.press("tab")

        time.sleep(0.5)

        pyautogui.press("space")

        # Processa
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