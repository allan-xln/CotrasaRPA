from ..Library.library import *


# --------------código inicial (funcional filial 9)------------------#

@app.route("/rankingclientes", methods=["POST"])
def run_coderankingclientes():
    filtered_calendar = get_filtered_calendar()
    first_day, last_day = get_first_last_days_of_month()
    if filtered_calendar:
        first_day, last_day = get_first_last_days_of_month()
        browser = initialize_browser()
        login(browser)
        time.sleep(2)
        switch_to_window(
            browser,
            "https://siconnet.scania.com.br/sicomnet4/newcotrasa/sicomweb.gen.gen.pag.Principal.cls",
        )

        switch_to_window(
            browser,
            "https://siconnet.scania.com.br/sicomnet4/newcotrasa/sicomweb.gen.gen.pag.Principal.cls",
        )

        wait = WebDriverWait(browser, 20)

        time.sleep(0.5)

        date = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="a9"]')))
        date.click()

        time.sleep(0.5)

        browser.find_element(By.XPATH, '//*[@id="m66"]/td').click() #Clicar no Vendas
        time.sleep(0.5)
        browser.find_element(By.XPATH, '//*[@id="g216"]/td').click()  #Clicar no Relatório
        time.sleep(0.5)
        browser.find_element(
            By.XPATH, '//*[@id="rotina"]/table/tbody/tr[11]/td/a').click() #Clicar no Ranking de Clientes

        time.sleep(0.5)

        # Aguarde até que um elemento esteja presente antes de interagir com ele
        element = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="zenLayoutTableCell_7"]')
            )
        )

        element.click()
        
        time.sleep(0.5)

        for _ in range(num_tabs13):
            time.sleep(0.2)
            pyautogui.press("tab")

        time.sleep(0.3)

        pyautogui.typewrite("9") #Campo Filial

        time.sleep(0.3)

        pyautogui.press("tab")

        #Campo Data Inical
        # Formata as datas para o formato brasileiro (dia/mês/ano)
        formatted_first_day = first_day.strftime("%d%m%Y")
        formatted_last_day = last_day.strftime("%d%m%Y")

        pyautogui.typewrite(formatted_first_day)
        pyautogui.press("tab")
        time.sleep(0.5)

        #Campo Data Final
        pyautogui.typewrite(formatted_last_day)
        pyautogui.press("tab")
        time.sleep(0.5)

        for _ in range(num_tabs7):
            time.sleep(0.2)
            pyautogui.press("tab")
        time.sleep(0.3)

        pyautogui.typewrite("3") #Campo Tipo De Venda

        time.sleep(0.3)

        pyautogui.press("tab")

        time.sleep(0.3)
        
        pyautogui.typewrite("150") #Campo Departamento

        time.sleep(0.3)

        for _ in range(num_tabs2):
            time.sleep(0.2)
            pyautogui.press("tab")
            
            time.sleep(0.5)
            
        for _ in range(num_downs3):
            time.sleep(0.2)
            pyautogui.press("down")

            time.sleep(0.3)

        pyautogui.press("enter") #Selecionar XML

        time.sleep(0.5)

        pyautogui.press("tab")

        time.sleep(0.5)

        pyautogui.press("space") #Selecionar p/ Download

        time.sleep(0.5)

        pyautogui.press("tab") #Selecionar Processar

        time.sleep(0.5)

        pyautogui.press("enter") #Selecionar Processar

        time.sleep(10)

        # Acessa a Janela
        url_esperado = "https://siconnet.scania.com.br/sicomnet4/newcotrasa/sicomweb.gen.gen.pag.RelatorioArmazenado.cls?"

        # Chama a função que aguarda e tenta alternar para a nova janela
        switch_to_window_with_retry(browser, url_esperado)

        time.sleep(5)

        # Baixa o Relatório mais atual
        element2 = WebDriverWait(browser, 30).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="tr_0_24"]/td[10]/span'))
        )

        element2.click()
        element2.click()

        time.sleep(2)

        downloads_path = os.path.expanduser("~") + "/Downloads/"
        source_file_path = downloads_path + "RankingClientes.xml"
        destination_file_path = downloads_path + "RankingClientes09.xml"

        if os.path.exists(source_file_path):
            os.rename(source_file_path, destination_file_path)

        time.sleep(5)

        # --------------final código inicial (funcional filial 9)------------------#
        
        base_filename = "RankingClientes"
        downloads_path = os.path.expanduser("~") + "/Downloads/"
        source_file_path = downloads_path + "RankingClientes.xml"

        filiais = ["10", "11", "12", "13", "14", "17"]

        for filial in filiais:
            time.sleep(3)

            pyautogui.hotkey('ctrl', 'w')

            time.sleep(2)

            pyautogui.hotkey('ctrl', 'w')

            time.sleep(5)

            switch_to_window_with_retry(browser, "https://siconnet.scania.com.br/sicomnet4/newcotrasa/sicomweb.gen.gen.pag.Principal.cls")

            time.sleep(3)

            # Aguarde até que um elemento esteja presente antes de interagir com ele
            element = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="zenLayoutTableCell_7"]')
                )
            )

            element.click()

            time.sleep(0.5)

            num_tabs4 = 13
            for _ in range(num_tabs4):
                time.sleep(0.2)
                pyautogui.press("tab")

            pyautogui.typewrite(filial)  # Campo Filial

            num_tabs5 = 15
            for _ in range(num_tabs5):
                time.sleep(0.2)
                pyautogui.press("tab")

            pyautogui.press("enter")

            time.sleep(5)

            switch_to_window_with_retry(browser, "https://siconnet.scania.com.br/sicomnet4/newcotrasa/sicomweb.gen.gen.pag.RelatorioArmazenado.cls?")

            # Baixar Arquivo
            element = WebDriverWait(browser, 30).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="tr_0_24"]/td[10]/span'))
            )

            element.click()
            element.click()

            time.sleep(8)

            if os.path.exists(source_file_path):
        
                destination_file_path = downloads_path + f"{base_filename}{filial}.xml"
                
                # Substitui o arquivo de destino se já existir
                shutil.move(source_file_path, destination_file_path)


        browser.quit()

        return render_template(
            "interface.html",
            resultado="Executado com Sucesso",
        )

if __name__ == "__main__":
    app.run(debug=False)