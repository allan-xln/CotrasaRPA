from ..Library.library import *

# ------------------------------------- SUPER ------------------------------------- #

class MyHandler(FileSystemEventHandler):
    def __init__(self, src_folder, dest_folder):
        super().__init__()
        self.src_folder = src_folder
        self.dest_folder = dest_folder
        self.log_file = os.path.join(dest_folder, "log", "log.txt")  # Caminho do arquivo de log
        self.last_working_day = get_last_working_day()  # Obter o último dia útil

        # Criar a pasta de log, se não existir
        log_folder = os.path.join(dest_folder, "log")
        if not os.path.exists(log_folder):
            os.makedirs(log_folder)

    def _log(self, message):
        # Função para registrar mensagens no arquivo de log
        with open(self.log_file, "a") as f:
            f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {message}\n")

    def process_all_files(self):
        # Função para processar todos os arquivos na pasta de downloads
        for filename in os.listdir(self.src_folder):
            time.sleep(5)  # Delay de 5 segundos antes de processar o arquivo (obrigatório)
            if filename.lower().startswith("service") and filename.lower().endswith(".txt"):
                self._process_service(filename)
            elif filename.lower().startswith("rankingclientes") and filename.lower().endswith(".xml"):
                self._process_ranking_clientes(filename)
            elif filename.lower().startswith("aproveittempomecanico") and filename.lower().endswith(".xml"):
                self._process_aproveittempomec(filename)
            elif filename.lower().startswith("checklist") and filename.lower().endswith(".xml"):
                self._process_checklist(filename)
            elif filename.lower().startswith("pedidoporfornecedor") and filename.lower().endswith(".xml"):
                self._process_pedido_fornecedor(filename)
            elif filename.lower().startswith("osemaberto_sintetico") and filename.lower().endswith(".xml"):
                self._process_os_em_aberto_s(filename)
            elif filename.lower().startswith("tempoveiculooficina") and filename.lower().endswith(".xml"):
                self._process_tempoveiculooficina(filename)
            elif filename.lower().startswith("origemservaplicado") and filename.lower().endswith(".xml"):
                self._process_origemservaplicado(filename)
            elif filename.lower().startswith("osemaberto") and filename.lower().endswith(".xml"):
                self._process_os_em_aberto(filename)
            elif filename.lower().startswith("garantia") and filename.lower().endswith(".xml"):
                self._process_garantia(filename)
            elif filename.lower().startswith("apurdebitointerno") and filename.lower().endswith(".xml"):
                self._process_debito_interno(filename)
            else:
                self._process_generic(filename)

    def on_modified(self, event):
        # Função que é chamada quando há uma modificação na pasta observada
        if not event.is_directory:
            self.process_all_files()

    # Funções para renomear os arquivos com base em suas nomenclaturas específicas

    def _rename_service_pack(self, filename):
        service_file_number = ''.join(filter(str.isdigit, filename))
        return f"service{service_file_number} - {self.last_working_day.strftime('%m.%Y')}{os.path.splitext(filename)[1]}"

    def _rename_ranking_clientes(self, filename):
        ranking_file_number = ''.join(filter(str.isdigit, filename))
        return f"RankingClientes{ranking_file_number} - {self.last_working_day.strftime('%m.%Y')}{os.path.splitext(filename)[1]}"
    
    def _rename_checklist(self, filename):
        checklist_file_number = ''.join(filter(str.isdigit, filename))
        return f"Checklist{checklist_file_number} - {self.last_working_day.strftime('%d.%m.%Y')}{os.path.splitext(filename)[1]}"

    def _rename_aproveittempomec(self, filename):
        return f"AproveitTempoMecanico - {self.last_working_day.strftime('%m.%Y')}{os.path.splitext(filename)[1]}"

    def _rename_debito_interno(self, filename):
        return f"DebitoInterno - {self.last_working_day.strftime('%m.%Y')}{os.path.splitext(filename)[1]}"
    
    def _rename_tempoveiculooficina(self, filename):
        return f"TempoVeiculoOficina - {self.last_working_day.strftime('%m.%Y')}{os.path.splitext(filename)[1]}"
    
    def _rename_origemservaplicado(self, filename):
        return f"OrigemServAplicados - {self.last_working_day.strftime('%m.%Y')}{os.path.splitext(filename)[1]}"
    
    def _rename_os_em_aberto(self, filename):
        return "OSemAberto"
    
    def _rename_garantia(self, filename):
        return "Garantia"
    
    def _rename_os_em_aberto_s(self, filename):
        return "OSemAberto_Sintetico"

    def _rename_pedido_fornecedor_pack(self, filename):
        pedido_fornecedor_file_number = ''.join(filter(str.isdigit, filename))
        return f"PedidoPorFornecedor{pedido_fornecedor_file_number} - {self.last_working_day.strftime('%m.%Y')}{os.path.splitext(filename)[1]}"


    # Funções para processar arquivos específicos

    def _process_service(self, filename):
        new_filename = self._rename_service_pack(filename)
        new_file_path = os.path.join(self.dest_folder, "ServicePack", new_filename)

        try:
            shutil.move(os.path.join(self.src_folder, filename), new_file_path)
            print(f"Arquivo {filename} movido para a pasta ServicePack e renomeado para {new_filename}")
            self._log(f"Arquivo {filename} movido para a pasta ServicePack e renomeado para {new_filename}")
        except (PermissionError, FileNotFoundError) as e:
            print(f"Erro ao processar arquivo {filename}: {e}")
        except Exception as e:
            print(f"Ocorreu um erro ao mover o arquivo {filename}: {e}")

    def _process_ranking_clientes(self, filename):
        new_filename = self._rename_ranking_clientes(filename)
        new_file_path = os.path.join(self.dest_folder, "RankingClientes", new_filename)

        try:
            shutil.move(os.path.join(self.src_folder, filename), new_file_path)
            print(f"Arquivo {filename} movido para a pasta RankingClientes e renomeado para {new_filename}")
            self._log(f"Arquivo {filename} movido para a pasta RankingClientes e renomeado para {new_filename}")
        except (PermissionError, FileNotFoundError) as e:
            print(f"Erro ao processar arquivo {filename}: {e}")
        except Exception as e:
            print(f"Ocorreu um erro ao mover o arquivo {filename}: {e}")

    def _process_aproveittempomec(self, filename):
        aproveit_tempo_mec_folder = os.path.join(self.dest_folder, "AproveitTempoMecanico")
        new_filename = self._rename_aproveittempomec(filename)
        new_file_path = os.path.join(aproveit_tempo_mec_folder, new_filename)

        if not os.path.exists(aproveit_tempo_mec_folder):
            os.makedirs(aproveit_tempo_mec_folder)

        try:
            shutil.move(os.path.join(self.src_folder, filename), new_file_path)
            print(f"Arquivo {filename} movido para {aproveit_tempo_mec_folder} e renomeado para {new_filename}")
            self._log(f"Arquivo {filename} movido para {aproveit_tempo_mec_folder} e renomeado para {new_filename}")
        except (PermissionError, FileNotFoundError) as e:
            print(f"Erro ao processar arquivo {filename}: {e}")
        except Exception as e:
            print(f"Ocorreu um erro ao mover o arquivo {filename}: {e}")

    def _process_debito_interno(self, filename):
        debito_interno_folder = os.path.join(self.dest_folder, "AproveitTempoMecanico")
        new_filename = self._rename_debito_interno(filename)
        new_file_path = os.path.join(debito_interno_folder, new_filename)

        if not os.path.exists(debito_interno_folder):
            os.makedirs(debito_interno_folder)

        try:
            shutil.move(os.path.join(self.src_folder, filename), new_file_path)
            print(f"Arquivo {filename} movido para {debito_interno_folder} e renomeado para {new_filename}")
            self._log(f"Arquivo {filename} movido para {debito_interno_folder} e renomeado para {new_filename}")
        except (PermissionError, FileNotFoundError) as e:
            print(f"Erro ao processar arquivo {filename}: {e}")
        except Exception as e:
            print(f"Ocorreu um erro ao mover o arquivo {filename}: {e}")

    def _process_origemservaplicado(self, filename):
        origem_serv_aplicado_folder = os.path.join(self.dest_folder, "OrigemServAplicado")
        new_filename = self._rename_origemservaplicado(filename)
        new_file_path = os.path.join(origem_serv_aplicado_folder, new_filename)

        if not os.path.exists(origem_serv_aplicado_folder):
            os.makedirs(origem_serv_aplicado_folder)

        try:
            shutil.move(os.path.join(self.src_folder, filename), new_file_path)
            print(f"Arquivo {filename} movido para {origem_serv_aplicado_folder} e renomeado para {new_filename}")
            self._log(f"Arquivo {filename} movido para {origem_serv_aplicado_folder} e renomeado para {new_filename}")
        except (PermissionError, FileNotFoundError) as e:
            print(f"Erro ao processar arquivo {filename}: {e}")

    def _process_tempoveiculooficina(self, filename):
        tempo_veiculo_oficina_folder = os.path.join(self.dest_folder, "TempoVeiculoOficina")
        new_filename = self._rename_tempoveiculooficina(filename)
        new_file_path = os.path.join(tempo_veiculo_oficina_folder, new_filename)

        if not os.path.exists(tempo_veiculo_oficina_folder):
            os.makedirs(tempo_veiculo_oficina_folder)

        try:
            shutil.move(os.path.join(self.src_folder, filename), new_file_path)
            print(f"Arquivo {filename} movido para {tempo_veiculo_oficina_folder} e renomeado para {new_filename}")
            self._log(f"Arquivo {filename} movido para {tempo_veiculo_oficina_folder} e renomeado para {new_filename}")
        except (PermissionError, FileNotFoundError) as e:
            print(f"Erro ao processar arquivo {filename}: {e}")
        except Exception as e:
            print(f"Ocorreu um erro ao mover o arquivo {filename}: {e}")

    def _process_os_em_aberto(self, filename):
        new_filename = self._rename_os_em_aberto(filename)
        new_file_path = os.path.join(self.dest_folder, "OSEmAberto", new_filename)

        try:
            shutil.move(os.path.join(self.src_folder, filename), new_file_path)
            print(f"Arquivo {filename} movido para a pasta OSEmAberto e renomeado para {new_filename}")
            self._log(f"Arquivo {filename} movido para a pasta OSEmAberto e renomeado para {new_filename}")
        except (PermissionError, FileNotFoundError) as e:
            print(f"Erro ao processar arquivo {filename}: {e}")
        except Exception as e:
            print(f"Ocorreu um erro ao mover o arquivo {filename}: {e}")

    def _process_garantia(self, filename):
        new_filename = self._rename_garantia(filename)
        new_file_path = os.path.join(self.dest_folder, "Garantia", new_filename)

        try:
            shutil.move(os.path.join(self.src_folder, filename), new_file_path)
            print(f"Arquivo {filename} movido para a pasta Garantia e renomeado para {new_filename}")
            self._log(f"Arquivo {filename} movido para a pasta Garantia e renomeado para {new_filename}")
        except (PermissionError, FileNotFoundError) as e:
            print(f"Erro ao processar arquivo {filename}: {e}")
        except Exception as e:
            print(f"Ocorreu um erro ao mover o arquivo {filename}: {e}")

    def _process_pedido_fornecedor(self, filename):
        new_filename = self._rename_pedido_fornecedor_pack(filename)
        new_file_path = os.path.join(self.dest_folder, "PedidoPorFornecedor", new_filename)

        try:
            shutil.move(os.path.join(self.src_folder, filename), new_file_path)
            print(f"Arquivo {filename} movido para a pasta PedidoPorFornecedor e renomeado para {new_filename}")
            self._log(f"Arquivo {filename} movido para a pasta PedidoPorFornecedor e renomeado para {new_filename}")
        except (PermissionError, FileNotFoundError) as e:
            print(f"Erro ao processar arquivo {filename}: {e}")
        except Exception as e:
            print(f"Ocorreu um erro ao mover o arquivo {filename}: {e}")

    def _process_os_em_aberto_s(self, filename):
        new_filename = self._rename_os_em_aberto_s(filename)
        new_file_path = os.path.join(self.dest_folder, "OSEmAberto_Sintetico", new_filename)

        try:
            shutil.move(os.path.join(self.src_folder, filename), new_file_path)
            print(f"Arquivo {filename} movido para a pasta OSEmAberto_Sintetico e renomeado para {new_filename}")
            self._log(f"Arquivo {filename} movido para a pasta OSEmAberto_Sintetico e renomeado para {new_filename}")
        except (PermissionError, FileNotFoundError) as e:
            print(f"Erro ao processar arquivo {filename}: {e}")
        except Exception as e:
            print(f"Ocorreu um erro ao mover o arquivo {filename}: {e}")

    def _process_checklist(self, filename):
        new_filename = self._rename_checklist(filename)
        new_file_path = os.path.join(self.dest_folder, "Checklist", new_filename)

        try:
            shutil.move(os.path.join(self.src_folder, filename), new_file_path)
            print(f"Arquivo {filename} movido para a pasta Checklist e renomeado para {new_filename}")
            self._log(f"Arquivo {filename} movido para a pasta Checklist e renomeado para {new_filename}")
        except (PermissionError, FileNotFoundError) as e:
            print(f"Erro ao processar arquivo {filename}: {e}")
        except Exception as e:
            print(f"Ocorreu um erro ao mover o arquivo {filename}: {e}")

    def _process_generic(self, filename):
        generic_folder = os.path.join(self.dest_folder, "Genericos")
        new_file_path = os.path.join(generic_folder, filename)

        if not os.path.exists(generic_folder):
            os.makedirs(generic_folder)

        try:
            shutil.move(os.path.join(self.src_folder, filename), new_file_path)
            print(f"Arquivo {filename} movido para {generic_folder}")
            self._log(f"Arquivo {filename} movido para {generic_folder}")
        except (PermissionError, FileNotFoundError) as e:
            print(f"Erro ao processar arquivo {filename}: {e}")
        except Exception as e:
            print(f"Ocorreu um erro ao mover o arquivo {filename}: {e}")

# ------------------------------------- MAIN ------------------------------------- #

if __name__ == "__main__":
    src_folder = "C:\\Users\\Automação\\Downloads"
    dest_folder = "Y:\\CORPORATIVO\\INTELIGENCIA\\BI\\PowerBI - Geral Cotrasa\\Arquivos"
    folder_to_watch = src_folder

    # Criar um manipulador de eventos
    event_handler = MyHandler(src_folder, dest_folder)
    observer = Observer()
    observer.schedule(event_handler, folder_to_watch, recursive=False)
    observer.start()

    stop_file = "stop.txt"

    try:
        while not os.path.exists(stop_file):
            event_handler.process_all_files()  # Processar todos os arquivos a cada 10 segundos
            time.sleep(10)
    except KeyboardInterrupt:
        pass

    observer.stop()
    observer.join()
