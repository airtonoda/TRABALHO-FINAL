from flask import Flask, request, jsonify
import pandas as pd
import joblib

# Inicialize o Flask
app = Flask(__name__)

# Carregar os modelos e o scaler
model_bayesian = joblib.load('modelo_final_bayesian.pkl')
model_linear = joblib.load('modelo_regressao_linear.pkl')
scaler = joblib.load('scaler.pkl')

@app.route('/', methods=['GET'])
def home():
    return {"message": "Bem-vindo à API do Trabalho Final!"}

@app.route('/predict', methods=['POST'])
def predict():
    # Receber os dados do cliente
    data = request.get_json()

    # Converter para DataFrame
    df = pd.DataFrame([data])

    # Escalar os dados
    df_scaled = scaler.transform(df)

    # Fazer previsões com ambos os modelos
    predicted_bayesian = model_bayesian.predict(df_scaled)[0]
    predicted_linear = model_linear.predict(df_scaled)[0]

    # Retornar a previsão
    return jsonify({
        "predicted_price_bayesian": f"R$ {predicted_bayesian:.2f}",
        "predicted_price_linear": f"R$ {predicted_linear:.2f}"
    })

if __name__ == '__main__':
    app.run(debug=True)