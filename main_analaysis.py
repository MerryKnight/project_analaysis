import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), 'scripts'))

from data_visualization import visualize_data
from forecasting_models import forecast_data
import pandas as pd

def create_directories(directories):
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)

def main():
    # Создание необходимых директорий
    directories = [
        'data/visualizations', 
        'data/forecasts', 
        'data/final_data'
    ]
    create_directories(directories)
    
    # Визуализация данных
    titles = [
        'Динамика ВВП России',
        'Динамика инфляции в России',
        'Динамика процентных ставок в России',
        'Динамика уровня безработицы в России',
        'Динамика потребительских расходов в России',
        'Динамика численности населения в России',
        'Динамика уровня бедности в России'
    ]
    output_files = [
        'data/cleaned_data/cleaned_gdp_data.csv',
        'data/cleaned_data/cleaned_inflation_data.csv',
        'data/cleaned_data/cleaned_interest_rates_data.csv',
        'data/cleaned_data/cleaned_unemployment_data.csv',
        'data/cleaned_data/cleaned_household_consumption_data.csv',
        'data/cleaned_data/cleaned_population_data.csv',
        'data/cleaned_data/cleaned_poverty_data.csv'
    ]
    visualization_files = [
        'data/visualizations/gdp_visualization.png',
        'data/visualizations/inflation_visualization.png',
        'data/visualizations/interest_rates_visualization.png',
        'data/visualizations/unemployment_visualization.png',
        'data/visualizations/household_consumption_visualization.png',
        'data/visualizations/population_visualization.png',
        'data/visualizations/poverty_visualization.png'
    ]
    
    visualize_data(output_files, visualization_files, titles)
    
    # Построение модели и прогнозирование
    forecast_output_files = [
        'data/forecasts/gdp_forecast.csv',
        'data/forecasts/inflation_forecast.csv',
        'data/forecasts/interest_rates_forecast.csv',
        'data/forecasts/unemployment_forecast.csv',
        'data/forecasts/household_consumption_forecast.csv',
        'data/forecasts/population_forecast.csv',
        'data/forecasts/poverty_forecast.csv'
    ]
    
    forecast_plot_files = [
        'data/forecasts/gdp_forecast_regression.png',
        'data/forecasts/inflation_forecast_regression.png',
        'data/forecasts/interest_rates_forecast_regression.png',
        'data/forecasts/unemployment_forecast_regression.png',
        'data/forecasts/household_consumption_forecast_regression.png',
        'data/forecasts/population_forecast_regression.png',
        'data/forecasts/poverty_forecast_regression.png'
    ]
    
    forecast_data(output_files, forecast_output_files, forecast_plot_files)
    
    # Создание файла для Power BI
    final_data = pd.concat([pd.read_csv(file) for file in forecast_output_files])
    final_data.to_csv('data/final_data/final_data_for_powerbi.csv', index=False)
    print("Финальный файл для Power BI успешно создан")

if __name__ == "__main__":
    main()
