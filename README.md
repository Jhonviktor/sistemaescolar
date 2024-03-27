<h1>Sistema Escolar</h1>

### Bem-vindos ao meu desafio, Sistema CRUD Escolar, onde aqui pude elaborar um banco de dados utilizando o MySQL e a linguagem de programação utilizada foi Python. Onde eu pude escrever scripts para me conectar com o banco de dados e criar um FASTAPI que permitiu criar uma interação diretamente pela API.


### Primeiramente eu gostaria de realçar alguns pontos que fizeram parte da minha curva de aprendizagem na elaboração deste projeto:
+ 1 - O primeiro contato que tive com o Docker, onde pude subir a imagem de SQLSERVER e utiliza-lo a partir dali.
+ 2 - Aprimoramento do meu conhecimento em banco de dados, onde puder aprender a criação de Tabelas e adicionar, atualizar e apagar os VALUES, no caso as informações.
+ 3 - A utilização de uma API, conhecida como FASTAPI, onde permitiu de forma simples, "criar" o rascunho de uma interface interativa.
+ 4 - A utilização da ferramenta OpenSource: DBeaver, onde pude agilizar o processo de registro das tabelas: curso e professor (ambas exigidas no desafio).

### Criação de tabelas.

Para realizar com precisão a construção do banco, eu criei as tabelas por ordem:
+ 1. Primeiramente criei a tabela curso, onde eu optei por criar 5 cursos, pois a primeira tabela Aluno exigia uma chave estrangeira.
+ 2. Logo em seguida criei a tabela Professor, onde cadastrei 5 professores.
+ 3. Então criei a tabela aluno com as informações exigidas.


## Inicialização Rápida

### 1. Clone repositório:
+ git clone https://github.com/Jhonviktor/sistemaescolar.git
+ cd sistemaescolar

### 2. Inicie o Ambiente Docker:
+ docker-compose up -d

### 3. Comando utilizado para iniciar o servidor do FASTAPI usando o Uvicorn:
+ uvicorn main:app --host localhost --port 100
#### Observação: para evitar algum conflito com a porta 8000, optei por subir na porta 100.

### 4. Acessar a API:
+ http://localhost:100/docs
+ Utilizando o diretorio docs para mostrar a tela de documentação da API, mas onde as mesmas estão selecionadas.


# Considerações finais.
+ Eu tive bastante dificuldade na utilização do Docker e a principal é de como enviar o meu banco de dados para testes.
+ Tive também dificuldade em como definir essa FASTAPI para listar os alunos cadastrados.
+ Os pontos fortes desse desafio foi que pude aprender a manipular diretamente o banco de dados utilizando a ferramenta DBeaver, pude também aprender a subir contoiners do terminal e no aplicado Desktop do Docker.
+ Pude aprimorar mais a minha busca autoditada.
+ Gostaria de ter a oportunidade de explicar tudo o que eu fiz e tentei fazer dar certo.

