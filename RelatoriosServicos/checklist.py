from ..Library.library import *

@app.route("/checklist", methods=["POST"])
def run_codechecklist():
    filtered_calendar = get_filtered_calendar()
    base_filename = "Checklist"
    downloads_path = os.path.expanduser("~") + "/Downloads/"
    source_file_path = downloads_path + "RelatorioGerencial.xml"
    filiais = ["9", "10", "11", "12", "13", "14", "17"]

    if filtered_calendar:
        last_working_day_initial = filtered_calendar[-1]  # Salva o valor inicial de last_working_day
        formatted_date_initial = format_date(last_working_day_initial)
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
        for _ in range(num_tabs12):
            time.sleep(0.2)
            pyautogui.press("tab")

        time.sleep(0.5)

        # Seleciona Tipo de Relatório
        for _ in range(num_downs3):
            time.sleep(0.2)
            pyautogui.press("down")

        pyautogui.press("enter")

        time.sleep(0.5)

        for _ in range(num_tabs5):
            time.sleep(0.2)
            pyautogui.press("tab")

        time.sleep(0.3)

        # Seleciona "XML"    
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

        # --------------final da organização dos campos padrões------------------#

        for filial in filiais:
            last_working_day = last_working_day_initial  # Reinicia last_working_day para o valor inicial
            formatted_date = formatted_date_initial  # Reinicia formatted_date para o valor inicial
            
            time.sleep(3)

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

            time.sleep(0.5)

            pyautogui.typewrite(filial)  # Campo Filial

            time.sleep(0.5)

            for _ in range(num_tabs2):
                    time.sleep(0.2)
                    pyautogui.press("tab")


                # Formata as datas para o formato brasileiro (dia/mês/ano)
            formatted_date = format_date(last_working_day)
            # Preenche o campo com a data atual
            pyautogui.typewrite(formatted_date)

            time.sleep(0.5)
            pyautogui.press("tab")
            time.sleep(0.5)

            # Preenche o campo com a data de ontem
            pyautogui.typewrite(formatted_date)
            time.sleep(0.5)

            for _ in range(num_tabs5):
                time.sleep(0.2)
                pyautogui.press("tab")

            pyautogui.press("enter")

            time.sleep(8)

            # Chama a função que aguarda e tenta alternar para a nova janela
            switch_to_window_with_retry(browser, "https://siconnet.scania.com.br/sicomnet4/newcotrasa/sicomweb.gen.gen.pag.RelatorioArmazenado.cls")

            # Baixar Arquivo
            element = WebDriverWait(browser, 30).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="tr_0_24"]/td[10]/span'))
            )

            # Atualiza last_working_day para o dia anterior
            #last_working_day -= timedelta(days=1)

            element.click()
            element.click()

            time.sleep(2)

            # Renomeia o arquivo
            destination_file_path = f"{downloads_path}{base_filename}{filial}.xml"
            os.rename(source_file_path, destination_file_path)

            time.sleep(3)
            
            pyautogui.hotkey('ctrl', 'w')

            time.sleep(0.5)

            pyautogui.hotkey('ctrl', 'w')

            time.sleep(0.5)

            switch_to_window_with_retry(browser, "https://siconnet.scania.com.br/sicomnet4/newcotrasa/sicomweb.gen.gen.pag.Principal.cls")

            
            time.sleep(1)
            

            # #---------------INICIA LOOP PARA PUXAR TODOS OS DIAS------------#

            # while last_working_day.date() >= datetime(2024, 1, 1).date():
                
            #     # Aguarde até que um elemento esteja presente antes de interagir com ele
            #     element = WebDriverWait(browser, 10).until(
            #         EC.presence_of_element_located(
            #             (By.XPATH, '//*[@id="zenLayoutTableCell_7"]')
            #         )
            #     )

            #     element.click()

            #     time.sleep(0.5)

            #     for _ in range(num_tabs13):
            #         time.sleep(0.2)
            #         pyautogui.press("tab")


            #      # Formata as datas para o formato brasileiro (dia/mês/ano)
            #     formatted_date = format_date(last_working_day)
            #     # Preenche o campo com a data atual
            #     pyautogui.typewrite(formatted_date)

            #     time.sleep(0.5)
            #     pyautogui.press("tab")
            #     time.sleep(0.5)

            #     # Preenche o campo com a data de ontem
            #     pyautogui.typewrite(formatted_date)
            #     time.sleep(0.5)

            #     for _ in range(num_tabs5):
            #         time.sleep(0.2)
            #         pyautogui.press("tab")

            #     pyautogui.press("enter")

            #     time.sleep(8)

            #     # Acessa a Janela
            #     url_esperado = "https://siconnet.scania.com.br/sicomnet4/newcotrasa/sicomweb.gen.gen.pag.RelatorioArmazenado.cls?"

            #     # Chama a função que aguarda e tenta alternar para a nova janela
            #     switch_to_window_with_retry(browser, url_esperado)

            #     # Baixar Arquivo
            #     element = WebDriverWait(browser, 30).until(
            #             EC.presence_of_element_located((By.XPATH, '//*[@id="tr_0_24"]/td[10]/span'))
            #     )

            #     # Atualiza last_working_day para o dia anterior
            #     last_working_day -= timedelta(days=1)

            #     element.click()
            #     element.click()

            #     time.sleep(3)
                
            #     pyautogui.hotkey('ctrl', 'w')

            #     time.sleep(2)

            #     pyautogui.hotkey('ctrl', 'w')

            #     time.sleep(5)

            #     switch_to_window_with_retry(browser, "https://siconnet.scania.com.br/sicomnet4/newcotrasa/sicomweb.gen.gen.pag.Principal.cls")

            #      # Renomeia o arquivo
            #     data_referencia = formatted_date.replace(".", "-")
            #     destination_file_path = f"{downloads_path}{base_filename}{filial}-{data_referencia}.xml"
            #     os.rename(source_file_path, destination_file_path)

        time.sleep(5)

        browser.quit()

        return render_template(
            "interface.html",
            resultado="Executado com Sucesso",
            error_message=None,
        )

    if __name__ == "__main__":
        app.run(debug=False)
