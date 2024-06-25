from ..Library.library import *

@app.route("/orcamento", methods=["POST"])
def run_codeorcamento():
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
        browser.find_element(
            "xpath", '//*[@id="m60"]/td'
        ).click()

        # Clique no elemento "Oficina"
        time.sleep(0.5)
        browser.find_element(
            "xpath", '//*[@id="g231"]/td'
        ).click()

        # Clique no elemento "Relatorio"
        time.sleep(0.5)
        browser.find_element(
            "xpath", '//*[@id="rotina"]/table[1]/tbody/tr[5]/td/a'
        ).click()

        # Aguarde até que um elemento esteja presente antes de interagir com ele
        element = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="zenLayoutTableCell_7"]')
            )
        )

        element.click()
        
        time.sleep(0.5)

        # Seleciona Data Inicial
        for _ in range(num_tabs14):
            time.sleep(0.2)
            pyautogui.press("tab")

        time.sleep(0.3)

        # Preenche datas
        # Formata as datas para o formato brasileiro (dia/mês/ano)

        date = get_last_working_day()

        if date:
            formatted_date = format_date(date)
            

        # Preenche o campo com a data de ontem
        pyautogui.typewrite(formatted_date)
        pyautogui.press("tab")
        time.sleep(0.5)

        # Preenche o campo com a data de ontem
        pyautogui.typewrite(formatted_date)
        time.sleep(0.5)

        # Seleciona Tipo de Venda "Opçao de listagem"
        for _ in range(num_tabs4):
            time.sleep(0.2)
            pyautogui.press("tab")

        time.sleep(0.3)

        # Selciona "XML"
        for _ in range(num_downs3):
            time.sleep(0.2)
            pyautogui.press("down")

        time.sleep(0.3)

        pyautogui.press("enter")

        time.sleep(0.3)

        # Seleciona "Armazenar para download"

        pyautogui.press("tab")

        time.sleep(0.3)

        pyautogui.press("space")

        time.sleep(0.3)

        # Seleciona "Processar"

        pyautogui.press("tab")

        time.sleep(0.3)

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

        time.sleep(5)

        downloads_path = os.path.expanduser("~") + "/Downloads/"
        source_file_path = downloads_path + "RelatorioGerencial.xml"
        destination_file_path = downloads_path + "Orcamento.xml"

        if os.path.exists(source_file_path):
            os.rename(source_file_path, destination_file_path)

        time.sleep(8)

        browser.quit()

        return render_template(
            "interface.html",
            resultado="Executado com Sucesso",
            error_message=None,
        )

    if __name__ == "__main__":
        app.run(debug=False)