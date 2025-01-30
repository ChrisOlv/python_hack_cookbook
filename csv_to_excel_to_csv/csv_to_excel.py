import pandas as pd

def csv_to_excel(csv_file_path, excel_file_path, encoding='utf-8'):
    df = pd.read_csv(csv_file_path, delimiter=",", encoding=encoding)
    # Écrire les données dans un fichier Excel
    df.to_excel(excel_file_path, index=False)

if __name__ == "__main__":
    # Chemin du fichier CSV d'entrée
    input_csv = 'COUCOU.csv'

    # Chemin du fichier Excel de sortie
    output_excel = 'coucou.xlsx'

    # Conversion du fichier CSV en fichier Excel
    csv_to_excel(input_csv, output_excel)
    print(f'CSV file {input_csv} has been converted to Excel file {output_excel}.')