import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), 'scripts'))

from data_extraction import fetch_data_and_save
from data_cleaning import clean_data
import pandas as pd

def create_directories(directories):
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)

def main():
    # Создание необходимых директорий
    directories = [
        'data/raw_data', 
        'data/cleaned_data', 
    ]
    create_directories(directories)
    
    # Извлечение данных
    indicators = {
        'NY.GDP.MKTP.CD': 'data/raw_data/gdp_data.csv',
        'FP.CPI.TOTL': 'data/raw_data/inflation_data.csv',
        'FR.INR.RINR': 'data/raw_data/interest_rates_data.csv',
        'SL.UEM.TOTL.ZS': 'data/raw_data/unemployment_data.csv',
        'NE.CON.PRVT.CD': 'data/raw_data/household_consumption_data.csv',
        'SP.POP.TOTL': 'data/raw_data/population_data.csv',
        'SI.POV.DDAY': 'data/raw_data/poverty_data.csv'
    }
    
    fetch_data_and_save(indicators, 'ru')
    
    # Очистка данных
    input_files = [
        'data/raw_data/gdp_data.csv',
        'data/raw_data/inflation_data.csv',
        'data/raw_data/interest_rates_data.csv',
        'data/raw_data/unemployment_data.csv',
        'data/raw_data/household_consumption_data.csv',
        'data/raw_data/population_data.csv',
        'data/raw_data/poverty_data.csv'
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
    
    clean_data(input_files, output_files)

if __name__ == "__main__":
    main()
