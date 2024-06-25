var loader = document.getElementById('loader');
var activeRequests = 0; // Contador de requisições ativas

function startLoader() {
    loader.style.display = 'block'; // Exibe o loader
}

function stopLoader() {
    loader.style.display = 'none'; // Oculta o loader
}

function submitFormWithLoader(event) {
    event.preventDefault(); // Impede o envio do formulário padrão
    var form = event.target;

    startLoader(); // Inicia o loader
    activeRequests++; // Incrementa o contador de requisições ativas

    // Função para tratar a resposta de uma requisição
    function handleResponse(xhr, form) {
        if (xhr.readyState === XMLHttpRequest.DONE) {
            if (xhr.status === 200) {
                var response = JSON.parse(xhr.responseText);
                console.log(response.message); // Exibe a mensagem de conclusão no console
                // Exibe a mensagem de conclusão abaixo do formulário
                var resultado = form.querySelector('.resultado');
                resultado.textContent = response.message;
                resultado.style.color = 'green'; // Estiliza a cor do texto para verde
            } else {
                console.error('Erro ao executar o código de estoque');
            }

            activeRequests--; // Decrementa o contador de requisições ativas

            if (activeRequests === 0) {
                stopLoader(); // Para o loader quando todas as requisições forem concluídas
            }
        }
    }

    var xhr = new XMLHttpRequest();
    xhr.open(form.method, form.action, true);
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xhr.onreadystatechange = function () {
        handleResponse(xhr, form);
    };
    xhr.send(new FormData(form));
}

var forms = document.getElementsByClassName('aligned-form');
for (var i = 0; i < forms.length; i++) {
    forms[i].addEventListener('submit', submitFormWithLoader);
}

function runAllTabs() {
    console.log('Iniciando execução de todas as abas...');
    startLoader(); // Inicia o loader
    activeRequests++; // Incrementa o contador de requisições ativas

    // Lista de URLs para cada rota
    var routes = [
        '/servicepack',
        '/debitosinternos',
        '/garantia',
        '/osemaberto',
        '/osabertanumperiodo',
        '/osfechadanumperiodo',
        '/rankingclientes',
        '/checklist',
        '/orcamento',
        '/aproveitamento_temp_mec',
        '/tempopermanencia'
    ];

    // Função recursiva para executar as abas em sequência
    function runTab(index) {
        if (index < routes.length) {
            console.log('Executando rota:', routes[index]);
            fetch(routes[index], { method: 'POST' })
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Erro na solicitação: ' + response.status);
                    }
                    return response.json();
                })
                .then(data => {
                    console.log('Resposta da rota', routes[index], ':', data.message);
                    setTimeout(function () {
                        runTab(index + 1); // Chama a próxima aba após 5 segundos
                    }, 5000);
                })
                .catch(error => {
                    console.error('Erro ao executar a aba:', error);
                })
                .finally(() => {
                    activeRequests--; // Decrementa o contador de requisições ativas
                    if (index === routes.length - 1 && activeRequests === 0) {
                        stopLoader(); // Para o loader quando todas as requisições forem concluídas
                        showSuccessMessage(); // Exibe a mensagem de sucesso após rodar todas as páginas
                        console.log('Todas as abas executadas.');
                    }
                });
        }
    }

    // Inicia a execução das abas
    runTab(0);
}