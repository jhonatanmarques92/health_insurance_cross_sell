import pandas as pd
import numpy as np
import joblib

class HealthInsurance:
    def __init__(self):
        self.home_path = ''
        self.fe_policy_sales_channel = joblib.load(self.home_path + 'features/fe_policy_sales_channel.joblib')
        self.mms_age = joblib.load(self.home_path + 'features/mms_age.joblib')
        self.mms_vintage = joblib.load(self.home_path + 'features/mms_vintage.joblib')
        self.ss_annual_premium = joblib.load(self.home_path + 'features/ss_annual_premium.joblib')
        self.target_encode_gender = joblib.load(self.home_path + 'features/target_encode_gender.joblib')
        self.target_encode_region_code = joblib.load(self.home_path + 'features/target_encode_region_code.joblib')
        
    def data_cleaning(self, data):
        # Renomear as colunas
        new_columns = []
        for e in data.columns:
            new_columns.append(e.lower())

        data.columns = new_columns
        
        return data
    
    def data_preparation(self, data):
        # Normalização
        data['annual_premium'] = self.ss_annual_premium.transform(data[['annual_premium']])
        
        # Rescaling
        data['vintage'] = self.mms_age.transform(data[['vintage']])
        data['vintage'] = self.mms_vintage.transform(data[['vintage']])
        
        # Encoding
        data['vehicle_damage'] = data['vehicle_damage'].apply(lambda x: 0 if x == 'No' else 1)
        data = pd.get_dummies( data, prefix='vehicle_age', columns=['vehicle_age'] )
        data.loc[:, 'gender'] = data['gender'].map(self.target_encode_gender)
        data.loc[:, 'region_code'] = data['region_code'].map(self.target_encode_region_code)
        data.loc[:, 'policy_sales_channel'] = data['policy_sales_channel'].map(self.fe_policy_sales_channel)
        
        # Seleção das colunas
        cols_selected = ['vintage', 'annual_premium', 'age', 'region_code', 'vehicle_damage', 'policy_sales_channel', 'previously_insured']
        
        return data[cols_selected]
    
    def get_prediction(self, model, original_data, test_data):
        # Predição do modelo
        pred = model.predict_proba(test_data)

        # Colocar os dados da predição nos dados originais
        original_data['score'] = pred[:,1]
        
        return original_data.to_json(orient='records', date_format='iso')