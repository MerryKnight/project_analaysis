import requests
import pandas as pd

def fetch_data_and_save(indicators, country_code):
    base_url = 'http://api.worldbank.org/v2/country/{}/indicator/{}?format=json'
    
    for indicator_code, file_name in indicators.items():
        response = requests.get(base_url.format(country_code, indicator_code))
        
        if response.status_code == 200:
            data = response.json()[1]
            df = pd.DataFrame(data)
            df = df[['date', 'value']].dropna()  # Оставляем только год и значение, удаляем пропущенные значения
            df.columns = ['year', 'value']
            df.to_csv(file_name, index=False)
            print(f"Данные по индикатору {indicator_code} успешно сохранены в файл {file_name}")
        else:
            print(f"Ошибка при запросе данных для индикатора {indicator_code}: {response.status_code}")
