import os
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from dotenv import load_dotenv

# Carregar variáveis de ambiente do .env
load_dotenv()

# Carregar chave da API
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

# Autenticação com o Google Sheets
def authenticate_google_sheets():
    credentials = Credentials.from_service_account_info(
        GOOGLE_API_KEY,
        scopes=["https://www.googleapis.com/auth/spreadsheets"]
    )
    service = build('sheets', 'v4', credentials=credentials)
    return service

# Função para ler os dados da planilha
def read_sheet(spreadsheet_id, range_name):
    service = authenticate_google_sheets()
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=spreadsheet_id, range=range_name).execute()
    values = result.get('values', [])
    return values

# Função para escrever a classificação na planilha
def write_classification(spreadsheet_id, range_name, classification_data):
    service = authenticate_google_sheets()
    body = {
        'values': classification_data
    }
    service.spreadsheets().values().update(
        spreadsheetId=spreadsheet_id,
        range=range_name,
        valueInputOption="RAW",
        body=body
    ).execute()
