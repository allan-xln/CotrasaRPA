from ..Library.library import *

@app.route("/osabertanumperiodosint", methods=["POST"])
def run_codeosabertanumperiodosint():
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

        time.sleep(0.5)

        pyautogui.hotkey('ctrl', '-')

        time.sleep(0.5)

        pyautogui.hotkey('ctrl', '-')

        time.sleep(0.5)

        # Aguarde até que o elemento de login esteja visível antes de interagir com ele
        wait = WebDriverWait(browser, 20)

        time.sleep(0.5)

        # Clique no elemento "Comercial"
        date = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="a9"]')))

        date.click()

        time.sleep(0.5)

        # Clique no elemento "Oficina"
        browser.find_element(
            "xpath", '//*[@id="m60"]/td'
        ).click()

        #Clique no elemento "Relatorio"
        time.sleep(0.5)
        browser.find_element(
            "xpath", '//*[@id="g187"]/td'
        ).click()

        # Clique no elemento "Relação de Ordens de Serviços"
        time.sleep(0.5)
        browser.find_element(
            "xpath", '//*[@id="rotina"]/table[1]/tbody/tr[20]/td/a'
        ).click()  

        time.sleep(0.5)

        time.sleep(0.5)

        pyautogui.hotkey('ctrl', '+')

        time.sleep(0.5)

        pyautogui.hotkey('ctrl', '+')

        time.sleep(1)

        # Aguarde até que um elemento esteja presente antes de interagir com ele
        element = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="zenLayoutTableCell_7"]')
            )
        )

        element.click()

        time.sleep(0.5)

        # Campo tipo de Relatório
        for _ in range(num_tabs12):
            time.sleep(0.2)
            pyautogui.press("tab")

        time.sleep(0.2)

        # Seleciona Tipo de Relatório “Relatório Analítico de Ordens de Serviço” 
        for _ in range(num_downs3):
            time.sleep(0.2)
            pyautogui.press("down")

        time.sleep(0.2)

        pyautogui.press("enter")

        time.sleep(0.2)

        pyautogui.press("tab")

        # Campo “Tipo de Layout” 
        for _ in range(num_downs3):
            time.sleep(0.2)
            pyautogui.press("down")

        time.sleep(0.2)

        pyautogui.press("enter")

        time.sleep(0.2)

        pyautogui.press("tab")

        time.sleep(0.2)

        # Campo “Opção de Seleção” 
        num_down3 = 2
        for _ in range(num_down3):
            time.sleep(0.2)
            pyautogui.press("down")

        time.sleep(0.2)

        pyautogui.press("enter")

        time.sleep(0.2)

        pyautogui.press("tab")

        time.sleep(0.2)

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

        # Campo “Classificação Principal/Secundária”
        for _ in range(num_tabs3):
            time.sleep(0.2)
            pyautogui.press("tab")

        time.sleep(0.2)

        # Selecionar opção “Por Consultor Técnico” 
        for _ in range(num_downs8):
            time.sleep(0.2)
            pyautogui.press("down")

        time.sleep(0.2)

        pyautogui.press("enter")

        time.sleep(0.2)

        # Campo “Opção de Seleção Adicional”  
        pyautogui.press("tab")

        time.sleep(0.2)

        # Selecionar opção “Consultor Técnico”   
        for _ in range(num_downs5):
            time.sleep(0.2)
            pyautogui.press("down")

        time.sleep(0.2)

        pyautogui.press("enter")

        time.sleep(0.2)

        # Campo “Valores”  
        for _ in range(num_tabs3):
            time.sleep(0.2)
            pyautogui.press("tab")

        time.sleep(0.2)

        # Selecionar opção “Valores da Negociação (Cliente)”   
        for _ in range(num_downs3):
            time.sleep(0.2)
            pyautogui.press("down")

        time.sleep(0.2)

        pyautogui.press("enter")

        time.sleep(0.2)

        pyautogui.press("tab")
        pyautogui.press("tab")

        pyautogui.press("down")

        # Campo “Formato de Saída do Relatório” 
        for _ in range(num_tabs2):
            time.sleep(0.2)
            pyautogui.press("tab")

        # Selciona "XML"

        time.sleep(0.2)

        for _ in range(num_downs3):
            time.sleep(0.2)
            pyautogui.press("down")

        time.sleep(0.2)

        pyautogui.press("enter")

        time.sleep(0.2)

        # Seleciona "Armazenar para download"

        pyautogui.press("tab")

        time.sleep(0.2)

        pyautogui.press("space")

        time.sleep(0.2)

        # Seleciona "Processar"

        pyautogui.press("tab")

        time.sleep(0.2)

        pyautogui.press("enter")

        time.sleep(70)

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
        source_file_path = downloads_path + "OrdemServico.xml"
        destination_file_path = downloads_path + "OSemAbertoO_Sintetico.xml"

        if os.path.exists(source_file_path):
            os.rename(source_file_path, destination_file_path)

        time.sleep(5)

        browser.quit()

        return render_template(
            "interface.html",
            resultado="Executado com Sucesso",
            error_message=None,
        )

if __name__ == "__main__":
    app.run(debug=False)