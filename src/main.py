from src.google_sheets import read_sheet, write_classification


def main():
    spreadsheet_id = 'seu-id-da-planilha'
    range_name = 'Sheet1!A2:B'  # Ajuste conforme a localização dos dados

    # Leitura das notícias da planilha
    noticias = read_sheet(spreadsheet_id, range_name)

    # Aqui você pode adicionar a lógica de IA para classificar as notícias
    classificacoes = [["Classificação Exemplo"]] * len(noticias)  # Exemplo de classificação genérica

    # Escrevendo a classificação de volta na planilha
    write_classification(spreadsheet_id, 'Sheet1!C2:C', classificacoes)


if __name__ == '__main__':
    main()