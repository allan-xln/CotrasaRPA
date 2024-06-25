from ..Library.library import *

@app.route("/servicepack", methods=["POST"])
def run_codeservicepack():
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

        # Aguarde até que o elemento de login esteja visível antes de interagir com ele
        wait = WebDriverWait(browser, 20)

        time.sleep(0.5)

        # Clique no elemento "Comercial"
        date = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="a9"]')))
        date.click()

        time.sleep(0.5)

        # Seleciona a Rotina desejada

        # Seleciona a Oficina
        browser.find_element("xpath", '//*[@id="m60"]/td').click()
        time.sleep(0.5)

        # Seleciona a Arquivo
        browser.find_element("xpath", '//*[@id="g181"]/td').click()
        time.sleep(0.5)

        # Seleciona a Serviço Packs
        browser.find_element("xpath", '//*[@id="rotina"]/table/tbody/tr[3]/td/a').click()

        time.sleep(0.5)


        # Aguarde até que um elemento esteja presente antes de interagir com ele
        element = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="zenLayoutTableCell_7"]')
            )
        )

        element.click()

        # Seleciona Filial
        for _ in range(num_tabs13):
            time.sleep(0.2)
            pyautogui.press("tab")

        time.sleep(0.5)

        pyautogui.press("space")

        time.sleep(0.5)

        pyautogui.press("tab")

        time.sleep(0.5)

        # Preenche datas
        # Formata as datas para o formato brasileiro (dia/mês/ano)
        formatted_first_day = first_day.strftime("%d%m%Y")
        formatted_last_day = last_day.strftime("%d%m%Y")

        # Preenche o campo com o primeiro dia do mês
        pyautogui.typewrite(formatted_first_day)
        pyautogui.press("tab")
        time.sleep(0.5)

        # Preenche o campo com o último dia do mês
        pyautogui.typewrite(formatted_last_day)
        time.sleep(0.5)

        for _ in range(num_tabs2):
            time.sleep(0.2)
            pyautogui.press("tab")

        time.sleep(0.5)

        pyautogui.press("space")

        time.sleep(0.5)

        for _ in range(num_tabs2):
            time.sleep(0.2)
            pyautogui.press("tab")

        time.sleep(0.5)

        pyautogui.press("space")

        time.sleep(0.5)

        pyautogui.press("tab")

        time.sleep(0.5)

        pyautogui.press("enter")

        time.sleep(0.5)

        for _ in range(num_downs2):
            time.sleep(0.2)
            pyautogui.press("down")

        time.sleep(0.5)

        pyautogui.press("enter")

        time.sleep(0.5)

        pyautogui.press("tab")

        for _ in range(num_downs2):
            time.sleep(0.2)
            pyautogui.press("down")

        time.sleep(0.5)

        pyautogui.press("enter")

        time.sleep(0.5)

        pyautogui.press("tab")

        time.sleep(0.5)

        pyautogui.press("enter")

        time.sleep(30)

        # Acessa a Janela
        url_esperado = "https://siconnet.scania.com.br/sicomnet4/newcotrasa/sicomweb.gen.gen.pag.DownloadArquivo.cls?"

        # Chama a função que aguarda e tenta alternar para a nova janela
        switch_to_window_with_retry(browser, url_esperado)

        # Listas de XPATH (Filiais) a serem clicadas (logica para ignorar a falta de um xpath e continuar)
        element_xpaths = {
        'SJP': '//*[@id="tr_0_16"]/td[3]/a',
        'PTB': '//*[@id="tr_1_16"]/td[3]/a',
        'PGO': '//*[@id="tr_2_16"]/td[3]/a',
        'CSV': '//*[@id="tr_3_16"]/td[3]/a',
        'GPV': '//*[@id="tr_4_16"]/td[3]/a',
        'UNV': '//*[@id="tr_5_16"]/td[3]/a',
        'IMB': '//*[@id="tr_6_16"]/td[3]/a'
    }

        # Iterar sobre os elementos XPath e seus nomes de filial correspondentes
        for filial, xpath in element_xpaths.items():
            try:
                # Tenta clicar no elemento
                browser.find_element("xpath", xpath).click()
                time.sleep(2)
                
            except NoSuchElementException:
                # Se o elemento não for encontrado, imprime uma mensagem de aviso com o nome da filial correspondente
                print("Xpath não encontrado para a filial:", filial)

                continue

        time.sleep(8)

        browser.quit()

        return render_template(
            "interface.html",
            resultado="Executado com Sucesso",
        )


if __name__ == "__main__":
    app.run(debug=True)
