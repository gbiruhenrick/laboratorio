import os
import time
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# ============================================================
# CONFIGURACAO
# Baixe o credentials.json no Google Cloud Console:
# console.cloud.google.com > APIs & Services > Credentials
# OAuth 2.0 Client ID > Desktop App > Fazer download do JSON
# ============================================================
CREDENTIALS_FILE = 'credentials.json'  # caminho para o seu arquivo de credenciais
TOKEN_FILE = 'token.json'              # gerado automaticamente na primeira execucao
SCOPES = ['https://mail.google.com/']
# ============================================================

def autenticar():
    creds = None
    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        with open(TOKEN_FILE, 'w') as token:
            token.write(creds.to_json())
    return creds

def buscar_sem_estrela(service):
    ids = []
    page_token = None
    while True:
        params = {'userId': 'me', 'q': '-is:starred', 'maxResults': 500}
        if page_token:
            params['pageToken'] = page_token
        response = service.users().messages().list(**params).execute()
        mensagens = response.get('messages', [])
        ids.extend([m['id'] for m in mensagens])
        print(f'  Encontrados ate agora: {len(ids)} emails...')
        page_token = response.get('nextPageToken')
        if not page_token:
            break
    return ids

def deletar_em_lote(service, ids):
    total = len(ids)
    deletados = 0
    for i in range(0, total, 1000):
        bloco = ids[i:i + 1000]
        service.users().messages().batchDelete(userId='me', body={'ids': bloco}).execute()
        deletados += len(bloco)
        print(f'  Deletados: {deletados}/{total}')
        time.sleep(0.5)

def main():
    print('Autenticando...')
    creds = autenticar()
    service = build('gmail', 'v1', credentials=creds)
    print('Buscando emails sem estrela...')
    ids = buscar_sem_estrela(service)
    if not ids:
        print('Nenhum email sem estrela encontrado.')
        return
    print(f'Total encontrado: {len(ids)} emails.')
    confirmacao = input('Confirmar delecao? (s/n): ').strip().lower()
    if confirmacao == 's':
        print('Deletando...')
        deletar_em_lote(service, ids)
        print('Concluido!')
    else:
        print('Cancelado.')

if __name__ == '__main__':
    main()
