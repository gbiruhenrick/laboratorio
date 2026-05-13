Aqui vai, pode copiar e colar direto:
markdown# Gmail Cleaner

Script Python que deleta todos os emails sem estrela da sua conta Gmail.

## Como funciona

Conecta na Gmail API via OAuth2, busca todos os emails sem estrela e deleta em lote. Na primeira execução abre o navegador para autenticação — depois disso o token fica salvo localmente.

## Requisitos

- Python 3.8+
- Conta Google com Gmail API ativada no Google Cloud Console

## Configurando as credenciais

1. Acesse [console.cloud.google.com](https://console.cloud.google.com)
2. Crie um projeto e ative a **Gmail API**
3. Vá em **Credentials → Create Credentials → OAuth client ID**
4. Tipo: **Desktop app**
5. Baixe o JSON e renomeie para `credentials.json`
6. Coloque o arquivo na mesma pasta do script

## Instalação

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

## Uso

```bash
python3 cleaner.py
```

O script mostra quantos emails foram encontrados e pede confirmação antes de deletar.

## Atenção

Os emails deletados ficam na lixeira por 30 dias antes de sumirem de vez.
