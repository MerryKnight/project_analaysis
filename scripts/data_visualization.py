import matplotlib.pyplot as plt
import pandas as pd

def visualize_data(input_files, output_files, titles):
    for input_file, output_file, title in zip(input_files, output_files, titles):
        df = pd.read_csv(input_file)
        plt.figure(figsize=(10, 6))
        plt.plot(df['year'], df['value'], marker='o', linestyle='-', color='b')
        plt.title(title)
        plt.xlabel('Год')
        plt.ylabel('Значение')
        plt.grid(True)
        plt.savefig(output_file)
        plt.show()
