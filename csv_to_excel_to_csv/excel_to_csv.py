import pandas as pd

def excel_to_csv(excel_file_path, sheet_name, csv_file_path):
    "Ouvre le excel avec pandas et l'exporte en csv"
    df = pd.read_excel(excel_file_path, sheet_name=sheet_name)
    df.to_csv(csv_file_path, index=False, encoding='utf-8')

# Variables :

excel_file_path = 'input.xlsx'
sheet_name = 'Feuil1'
csv_file_path = 'output.csv'

excel_to_csv(excel_file_path, sheet_name, csv_file_path)