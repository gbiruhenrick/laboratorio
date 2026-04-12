# Laboratório Docker - Nginx Base

Este repositório registra meus primeiros passos com **Docker** e **Nginx**. 
Foi o ponto de partida para entender a containerização antes de avançar para projetos mais complexos, como o **GasControl**.

## 🛠️ Tecnologias
* **Docker**: Criação e gestão do container.
* **Nginx**: Servidor web para entrega da página.
* **Linux (Ubuntu)**: Ambiente de desenvolvimento.

## 📁 Estrutura do Projeto
Os arquivos principais de configuração do servidor e a página inicial estão organizados na pasta `/docker-nginx`.

## 🚀 Como rodar o projeto
1. Acesse a pasta do projeto:
   `cd docker-nginx`
2. Faça o build da imagem:
   `docker build -t servidor-nginx-lab .`
3. Inicie o container na porta 8080:
   `docker run -d -p 8080:80 servidor-nginx-lab`
4. Acesse no navegador: `localhost:8080`
5. 
<img width="651" height="342" alt="image" src="https://github.com/user-attachments/assets/1df66a6a-7f14-4d61-9c31-125b0deffe27" />
