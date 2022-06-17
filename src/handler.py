import joblib
import os
import pandas as pd
from flask import Flask, request, Response
from healthinsurance.HealthInsurance import HealthInsurance

path = ''
model = joblib.load(path + 'models/xgb_model.joblib')

# Inicializando API
app = Flask(__name__)

@app.route('/healthinsurance/predict', methods=['POST'])
def healthinsurance_predict():
    test_json = request.get_json()
    if test_json: # Há dados
        if isinstance(test_json, dict): # Exemplo único
            test_raw = pd.DataFrame(test_json, columns=test_json[0])
        else: #Multiplos exemplos
            test_raw = pd.DataFrame(test_json, columns=test_json[0].keys())
        
        # Instanciando a classe HealthInsurance
        pipeline = HealthInsurance()
        
        # Data Cleaning
        df1 = pipeline.data_cleaning(test_raw)
        
        # Data Preparation
        df2 = pipeline.data_preparation(df1)
        
        # Predição
        df_response = pipeline.get_prediction(model, test_raw, df2)
        
        return df_response
    
    else:
        return Response('{}', status=200, mimetype='application/json')
    
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)