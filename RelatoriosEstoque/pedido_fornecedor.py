from ..Library.library import *

@app.route("/pedidofornecedor", methods=["POST"])
def run_codepedidofornecedor():
    filtered_calendar = get_filtered_calendar()
    first_day, last_day = get_first_last_days_of_month()
    base_filename = "PedidoPorFornecedor"
    downloads_path = os.path.expanduser("~") + "/Downloads/"
    source_file_path = downloads_path + "PedidoPorFornecedor.xml"
    filiais = ["9", "10", "11", "12", "13", "14", "15", "17"]
    primeiro_loop = True

    if filtered_calendar:
        try:
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

            browser.find_element(By.XPATH, '//*[@id="m61"]/td').click() #Clicar no Pedidos
            time.sleep(0.5)
            browser.find_element(By.XPATH, '//*[@id="g191"]/td').click()  #Clicar no Relatório
            time.sleep(0.5)
            browser.find_element(
                By.XPATH, '//*[@id="rotina"]/table/tbody/tr[7]/td/a').click() #Clicar Pedidos Por Fornecedor

            time.sleep(0.5)

            # Aguarde até que um elemento esteja presente antes de interagir com ele
            element = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="zenLayoutTableCell_7"]')
                )
            )

            element.click()
            
            time.sleep(0.5)

            for _ in range(num_tabs15):
                time.sleep(0.2)
                pyautogui.press("tab")

            # Preenche datas
            date = get_last_working_day()

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
            
            time.sleep(0.3)
            
            for _ in range(num_tabs3):
                time.sleep(0.2)
                pyautogui.press("tab")

            time.sleep(0.5)

            for _ in range(num_downs3):
                time.sleep(0.2)
                pyautogui.press("down")

            time.sleep(0.3)

            pyautogui.press("enter") #Seleciona XML

            time.sleep(0.5)

            pyautogui.press("tab")

            time.sleep(0.5)

            pyautogui.press("space") 

            time.sleep(0.5)

            pyautogui.press("tab")

            time.sleep(0.5)

        # ------------------------LOOP PARA PREENCHIMENTO DA FILIAL------------------------#

            for indice, filial_numero in enumerate(filiais):
                while True:
                    try:
                        # Define o valor de num_downloop de acordo com o primeiro_loop
                        if primeiro_loop:
                            num_downloop = 1
                            primeiro_loop = False
                        else:
                            num_downloop = 2

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

                        # Loop para down
                        for _ in range(num_downloop):
                            time.sleep(1)
                            pyautogui.press("down")

                        filial = filial_numero  # Usando o número da filial atual

                        time.sleep(1)

                        pyautogui.press("enter")

                        time.sleep(1)

                        for _ in range(num_tabs10):
                            time.sleep(0.2)
                            pyautogui.press("tab")

                        time.sleep(0.5)

                        pyautogui.press("enter")  # Seleciona Processar

                        time.sleep(3)

                        try:
                            # Tentar mudar para o alerta
                            alert = browser.switch_to.alert
                            alert.accept()  # Clicar em OK no alerta
                            # Se o alerta for encontrado e aceito, voltar ao início do loop para a mesma filial
                            continue

                        except:
    
                            time.sleep(2)

                        # Chama a função que aguarda e tenta alternar para a nova janela
                        switch_to_window_with_retry(browser, "https://siconnet.scania.com.br/sicomnet4/newcotrasa/sicomweb.gen.gen.pag.RelatorioArmazenado.cls?")
                        
                        # Baixar Arquivo
                        element = WebDriverWait(browser, 30).until(
                                EC.presence_of_element_located((By.XPATH, '//*[@id="tr_0_24"]/td[10]/span'))
                        )

                        element.click()
                        element.click()

                        time.sleep(2)

                        # ------------------------LÓGICA PARA VERIFICAR E RENOMEAR ARQUIVO------------------------#

                        # Renomeia o arquivo
                        destination_file_path = f"{downloads_path}{base_filename}{filial}.xml"
                        os.rename(source_file_path, destination_file_path)

                        # ----------------------------------------------------------------------------------------#

                        time.sleep(3)
                        
                        pyautogui.hotkey('ctrl', 'w')

                        time.sleep(0.5)

                        pyautogui.hotkey('ctrl', 'w')

                        time.sleep(0.5)

                        switch_to_window_with_retry(browser, "https://siconnet.scania.com.br/sicomnet4/newcotrasa/sicomweb.gen.gen.pag.Principal.cls")

                        time.sleep(1)
                        break  # Sai do loop while e continua para a próxima filial

                    except Exception as e:
                        print(f"Erro ao processar filial {filial_numero}: {e}")
                        continue  # Pula para a próxima filial em caso de erro
                
                #------------------------------------FIM DO LOOP FILIAL------------------------------------#

        except Exception as e:
            print(f"Erro durante a execução: {e}")
        finally:
            browser.quit()

    return render_template(
        "interface.html",
        resultado="Executado com Sucesso",
    )

if __name__ == "__main__":
    app.run(debug=False)
