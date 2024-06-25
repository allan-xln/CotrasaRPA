from .service_pack import run_codeservicepack
from .debitos_internos import run_codedebitosinternos
from .aproveitamento_temp_mec import run_codetempomec
from .garantia import run_codegarantia
from .ranking_clientes import run_coderankingclientes
from .os_aberta_num_periodo import run_codeosabertanumperiodo
from .os_em_aberto import run_codeosemaberto
from .os_fechada_num_periodo import run_codeosfechadanumperiodo
from .orcamento import run_codeorcamento
from .checklist import run_codechecklist
from .tempo_permanencia import run_codetempopermanencia
from .origem_serv_aplicados import run_codeorigemservaplicados
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

@app.route("/tempomec", methods=["POST"])
def run_tempomec():
    global resultado
    resultado = run_codetempomec()
    return jsonify({"message": "Executado com Sucesso!"})

@app.route("/servicepack", methods=["POST"])
def run_servicepack():
    global resultado
    resultado = run_codeservicepack()
    return jsonify({"message": "Executado com Sucesso!"})

@app.route("/debitosinternos", methods=["POST"])
def run_debitosinternos():
    global resultado
    resultado = run_codedebitosinternos()
    return jsonify({"message": "Executado com Sucesso!"})

@app.route("/garantia", methods=["POST"])
def run_garantia():
    global resultado
    resultado = run_codegarantia()
    return jsonify({"message": "Executado com Sucesso!"})

@app.route("/rankingclientes", methods=["POST"])
def run_rankingclientes():
    global resultado
    resultado = run_coderankingclientes()
    return jsonify({"message": "Executado com Sucesso!"})

@app.route("/osemaberto", methods=["POST"])
def run_osemaberto():
    global resultado
    resultado = run_codeosemaberto()
    return jsonify({"message": "Executado com Sucesso!"})

@app.route("/osabertanumperiodo", methods=["POST"])
def run_osabertanumperiodo():
    global resultado
    resultado = run_codeosabertanumperiodo()
    return jsonify({"message": "Executado com Sucesso!"})

@app.route("/osfechadanumperiodo", methods=["POST"])
def run_osfechadanumperiodo():
    global resultado
    resultado = run_codeosfechadanumperiodo()
    return jsonify({"message": "Executado com Sucesso!"})

@app.route("/orcamentos", methods=["POST"])
def run_orcamentos():
    global resultado
    resultado = run_codeorcamento()
    return jsonify({"message": "Executado com Sucesso!"})

@app.route("/checklist", methods=["POST"])
def run_checklist():
    global resultado
    resultado = run_codechecklist()
    return jsonify({"message": "Executado com Sucesso!"})

@app.route("/tempopermanencia", methods=["POST"])
def run_tempopermanencia():
    global resultado
    resultado = run_codetempopermanencia()
    return jsonify({"message": "Executado com Sucesso!"})

@app.route("/origemservaplicados", methods=["POST"])
def run_origemservaplicados():
    global resultado
    resultado = run_codeorigemservaplicados()
    return jsonify({"message": "Executado com Sucesso!"})

def my_cron_job():
    routes = [
        "/tempomec",
        "/servicepack",
        "/debitosinternos",
        "/garantia",
        "/rankingclientes",
        "/osemaberto",
        "/osabertanumperiodo",
        "/osfechadanumperiodo",
        "/orcamentos",
        "/checklist",
        "/tempopermanencia",
        "/origemservaplicados"
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
    serve(app, host='172.16.54.12', port=80)
