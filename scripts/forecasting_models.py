import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def forecast_data(input_files, output_files, plot_files):
    for input_file, output_file, plot_file in zip(input_files, output_files, plot_files):
        df = pd.read_csv(input_file)
        X = np.array(df['year']).reshape(-1, 1)
        y = np.array(df['value']).reshape(-1, 1)
        
        model = LinearRegression()
        model.fit(X, y)
        
        future_years = np.array(range(df['year'].max() + 1, df['year'].max() + 11)).reshape(-1, 1)
        predictions = model.predict(future_years)
        
        future_df = pd.DataFrame({'Date': future_years.flatten(), 'Forecasted Value': predictions.flatten()})
        future_df.to_csv(output_file, index=False)
        
        plt.figure(figsize=(10, 6))
        plt.plot(df['year'], df['value'], label='Historical Data')
        plt.plot(future_df['Date'], future_df['Forecasted Value'], label='Forecast', linestyle='--')
        plt.title(f'Forecast for {input_file.split("/")[-1].replace("cleaned_", "").replace("_data.csv", "")}')
        plt.xlabel('Year')
        plt.ylabel('Value')
        plt.legend()
        plt.grid(True)
        plt.savefig(plot_file)
        plt.show()
        plt.close()
        
        print(f"Forecast and plot saved for {input_file}")

