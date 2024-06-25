from .geral_estoque import run_codeestoque
from .vendas_lucro_comissoes import run_codevendaslucrocomissoes
from .nao_movimentados import run_codeitensnaomov
from .pedido_fornecedor import run_codepedidofornecedor
from .os_em_aberto_s import run_codeosemabertosint
from .os_aberta_num_periodo_s import run_codeosabertanumperiodosint
from .os_fechada_num_periodo_s import run_codeosfechadanumperiodosint
from ..Library.library import *

app = Flask(__name__)
scheduler = BackgroundScheduler()

resultado = None

@app.route("/")
def interface():
    return render_template(
        "interface.html",
        resultado=resultado
    )

@app.route("/geralestoque", methods=["POST"])
def run_geralestoque():
    global resultado
    resultado = run_codeestoque()
    return jsonify({"message": "Executado com Sucesso!"})

@app.route("/vendaslucrocomissoes", methods=["POST"])
def run_vendaslucrocomissoes():
    global resultado
    resultado = run_codevendaslucrocomissoes()
    return jsonify({"message": "Executado com Sucesso!"})

@app.route("/itensnaomov", methods=["POST"])
def run_itensnaomov():
    global resultado
    resultado = run_codeitensnaomov()
    return jsonify({"message": "Executado com Sucesso!"})

@app.route("/pedidofornecedor", methods=["POST"])
def run_pedidofornecedor():
    global resultado
    resultado = run_codepedidofornecedor()
    return jsonify({"message": "Executado com Sucesso!"})

@app.route("/osemabertosint", methods=["POST"])
def run_osemabertosint():
    global resultado
    resultado = run_codeosemabertosint()
    return jsonify({"message": "Executado com Sucesso!"})

@app.route("/osabertanumperiodosint", methods=["POST"])
def run_osabertanumperiodosint():
    global resultado
    resultado = run_codeosabertanumperiodosint()
    return jsonify({"message": "Executado com Sucesso!"})

@app.route("/osfechadanumperiodosint", methods=["POST"])
def run_osfechadanumperiodosint():
    global resultado
    resultado = run_codeosfechadanumperiodosint()
    return jsonify({"message": "Executado com Sucesso!"})

def my_cron_job():
    routes = [
        "/geralestoque",
        "/vendaslucrocomissoes",
        "/itensnaomov",
        "/osemabertosint",
        "/osabertanumperiodosint",
        "/osfechadanumperiodosint",
        "/pedidofornecedor"

    ]
    
    for route in routes:
        with app.test_client() as c:
            c.post(route)

scheduler.add_job(
    func=my_cron_job,
    trigger=CronTrigger(hour=5, minute=30, day_of_week='mon-fri'),
    id='scheduled_job',
    name='Execução de todas as abas ás 5:30',
    replace_existing=True
)

# Inicia o agendador
scheduler.start()

if __name__ == "__main__":
    serve(app, host='172.16.54.11', port=80)