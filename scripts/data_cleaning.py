import pandas as pd

def clean_data(input_files, output_files):
    for input_file, output_file in zip(input_files, output_files):
        df = pd.read_csv(input_file)
        # Пример очистки: удаление строк с пропущенными значениями
        df_cleaned = df.dropna()
        df_cleaned.to_csv(output_file, index=False)
        print(f"Данные из файла {input_file} успешно очищены и сохранены в файл {output_file}")
