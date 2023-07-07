import requests
import pandas as pd
import time
import schedule
import logging

logging.basicConfig(filename='error.log', level=logging.ERROR)

def eventos_CETRIO():
    start_time = time.time()
    print("\n Inicializando requisições!")

    url = "https://api.dados.rio/v2/adm_cor_comando/ocorrencias_abertas/"
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        logging.error(f"Erro na requisição: {e}")
        return

    data = response.json()

    events = [(item["id"], item["inicio"], item["status"], item["titulo"]) for item in data.get("eventos", [])]
    id_list = [item['id'] for item in data.get('eventos', [])]

    df_events = pd.DataFrame(events, columns=["id", "datetime", "status_ocorrencia", "tipo_ocorrencia"])

    orgaos = {}
    print(' \n --- Buscando pelos órgãos responsáveis pelos eventos em aberto!')
    for id in id_list:
        url = f"https://api.dados.rio/v2/adm_cor_comando/ocorrencias_orgaos_responsaveis/?eventoId={id}"

        try:
            response = requests.get(url)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            logging.error(f"Erro na requisição: {e}")
            continue

        data = response.json()
        atividades = data.get("atividades", [])

        for atividade in atividades:
            orgao = atividade.get("orgao")

            if id in orgaos:
                orgaos[id].append(orgao)
            else:
                orgaos[id] = [orgao]

    orgaos_filtrados = {k: "CET-RIO" for k, v in orgaos.items() if "CET-RIO" in v}
    df_orgaos = pd.DataFrame(list(orgaos_filtrados.items()), columns=['id', 'orgao'])

    df_final = df_events.merge(df_orgaos, on='id', how='left')
    df_final['datetime'] = pd.to_datetime(df_final['datetime'])
    contagem = df_final['status_ocorrencia'].value_counts()
    df_final["quantidade_ocorrencia"] = df_final["status_ocorrencia"].map(contagem)

    try:
        df = pd.read_csv('eventos_rio.csv', encoding='latin1')
    except FileNotFoundError:
        df = pd.DataFrame()

    if len(df) == len(df_final):
        print("\n   - Sem novos eventos para adicionar! \n")
    else:
        df_csv = pd.concat([df, df_final], ignore_index=True).drop_duplicates(subset=['id'], keep='last')
        df_csv = df_csv.dropna()

        print(f"   -  Adicionado {len(df_csv) - len(df_final)} eventos ao arquivo eventos_rio.csv \n")
        df_csv.to_csv('eventos_rio.csv', index=False, encoding='latin1')
        

        print("\n   - Dados salvos com sucesso!")

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"   - Tempo decorrido: {execution_time} segundos")


def agendar_tarefa():
    eventos_CETRIO()
    time.sleep(2)
    
    print('\n- Aguardando 20 minutos.')
    schedule.every(20).minutes.do(eventos_CETRIO)

    while True:
        try:
            schedule.run_pending()
            time.sleep(1)
        except KeyboardInterrupt:
            break
        except Exception as e:
            logging.error(f"Erro durante a execução: {e}")

agendar_tarefa()