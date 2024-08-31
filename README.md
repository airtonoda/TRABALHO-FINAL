API de Previsão de Preços das Ações PETR4
Esta API foi desenvolvida como parte de um projeto de pós-graduação para prever o preço de fechamento das ações da Petrobras (PETR4) usando modelos de regressão linear e Bayesian Ridge.

Funcionalidades
Previsão de preços baseada em dados fornecidos manualmente.
(Não implentado ainda) Previsão automática de preços utilizando dados da Yahoo Finance.

Requisitos
Python 3.12 ou superior
pip para gerenciar pacotes Python

Instalação
Clonar o Repositório

git clone https://github.com/airtonoda/TRABALHO-FINAL.git
cd TRABALHO-FINAL/API_ProjetoFinal

Criar e Ativar o Ambiente Virtual (Opcional)

Criar o ambiente virtual:
python -m venv venv

Ativar o ambiente virtual:

Windows:
.\venv\Scripts\activate
Linux/Mac:
source venv/bin/activate

Instalar Dependências

pip install -r requirements.txt

Uso da API

Iniciar o Servidor
Para iniciar o servidor Flask, execute:
python app.py

O servidor estará disponível em http://127.0.0.1:5000.

Endpoints Disponíveis
1. Rota de Bem-Vindo
Método: GET
Endpoint: /
Descrição: Verifica se a API está ativa.
Resposta: Uma mensagem de boas-vindas.

2. Previsão Manual
Método: POST
Endpoint: /predict
Descrição: Recebe dados de entrada do usuário e retorna a previsão do preço de fechamento.
Exemplo de Requisição:

{
  "Abertura": 39.22,
  "Máxima": 39.65,
  "Mínima": 38.88,
  "Vol.": 84437200,
  "Media_Movel_7d": 39.00,
  "Media_Movel_30d": 38.50,
  "Var_Dia_Anterior": 0.01
}
Exemplo de Resposta:

{
  "predicted_price_bayesian": "R$ 2.91",
  "predicted_price_linear": "R$ 2.91"
}

3. (Opcional) Previsão Automática
Método: POST
Endpoint: /predict-auto
Descrição: Faz a previsão automática utilizando dados do Yahoo Finance.
Resposta: A previsão dos preços de fechamento utilizando ambos os modelos.

Estrutura do Projeto
app.py: Código principal da API.
requirements.txt: Dependências necessárias para rodar a API.
venv/: Ambiente virtual Python.

Contribuições
Pull requests são bem-vindos. Para mudanças significativas, por favor, abra uma issue para discutir o que você gostaria de modificar.

