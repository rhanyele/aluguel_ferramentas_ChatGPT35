# Aluguel de Ferramentas - Sistema de Reservas
Este é um sistema web desenvolvido em Flask para gerenciar o aluguel de ferramentas entre usuários. Ele permite que os usuários cadastrem ferramentas, façam reservas e realizem pagamentos. Este projeto foi totalmente construído utilizando o ChatGPT 3.5.

## Objetivo
Este projeto foi concebido com o propósito de explorar as capacidades de uma Inteligência Artificial, especificamente o modelo LLM (Language Learning Model), na criação de um sistema web funcional. O intuito era utilizar a IA como assistente no desenvolvimento, fornecendo orientações, sugestões e até mesmo o código necessário para a construção do sistema.

## Prompts
1- Atue como um product manager, você deve descrever um projeto para ser enviada para o time de desenvolvimento, o projeto é de locação de ferramentas
2- Atue como um programador experiente que vai receber as funcionalidades de um projeto e escolha a linguagem e o banco de dados

## Funcionalidades
Cadastro e gerenciamento de usuários
Cadastro e gerenciamento de ferramentas
Reserva de ferramentas
Pagamento de reservas
Autenticação de usuários

## Pré-requisitos
Python 3.x
Flask
PostgreSQL

## Começando
Para utilizar o projeto, é necessário clonar o repositório do GitHub em um diretório de sua preferência:

```shell
cd "diretorio"
git clone https://github.com/rhanyele/aluguel_ferramentas_ChatGPT35
```

## Dependências
Para instalar as dependências do projeto, execute o seguinte comando:

```shell
pip install -r requirements.txt
```

## Configuração do Banco de Dados
É necessário criar um arquivo .env na raiz do projeto com os parâmetros de configuração do banco de dados:

```shell
DB_HOST='url_database'
DB_PORT='5432'
DB_NAME='database'
DB_USER='usuario'
DB_PASS='password'
```
Certifique-se de substituir os valores 'url_database', 'database', 'usuario' e 'password' pelos detalhes de conexão do seu banco de dados PostgreSQL.

## Executando a Aplicação
Após configurar o banco de dados e instalar as dependências, você pode executar a aplicação Flask com o seguinte comando:

```shell
python app.py
```
Isso iniciará o servidor Flask, e você poderá acessar o sistema através do navegador web no endereço http://localhost:5000/.

## Contribuindo
Se você deseja contribuir com o projeto, sinta-se à vontade para abrir uma issue ou enviar um pull request no repositório do GitHub.

## Licença
Este projeto é distribuído sob a licença MIT. Consulte o arquivo LICENSE para obter mais detalhes.