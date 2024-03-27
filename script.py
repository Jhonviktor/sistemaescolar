import mysql.connector

# Conectar ao banco de dados
conn = mysql.connector.connect(
    host="localhost",
    port=3307,
    user="root",
    password="root",
    database="escola"
)
cursor = conn.cursor()

# Exemplo de função para inserir um aluno no banco de dados
def inserir_aluno(nome, data_nascimento, logradouro, numero, bairro, cidade, estado, cep, id_curso):
    sql = "INSERT INTO ALUNO (NOME, DATA_NASCIMENTO, LOGRADOURO, NUMERO, BAIRRO, CIDADE, ESTADO, CEP, ID_CURSO) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (nome, data_nascimento, logradouro, numero, bairro, cidade, estado, cep, id_curso)
    cursor.execute(sql, val)
    conn.commit()
    print("Aluno inserido com sucesso.")

# Exemplo de função para buscar todos os alunos no banco de dados
def buscar_alunos():
    cursor.execute("SELECT * FROM ALUNO")
    alunos = cursor.fetchall()
    for aluno in alunos:
        print(aluno)
    return alunos
# Outras operações CRUD (atualizar, deletar) podem ser implementadas de maneira semelhante

# Exemplo de uso
# inserir_aluno("Kamilah", "2000-09-05", "Rua b", "520", "Centro", "Sao Luis", "SP", "12345678", 1)
# buscar_alunos()

# Função para atualizar dados do aluno
def atualizar_aluno(id_aluno, nome, data_nascimento, logradouro, numero, bairro, cidade, estado, cep, id_curso):
    sql = "UPDATE ALUNO SET NOME = %s, DATA_NASCIMENTO = %s, LOGRADOURO = %s, NUMERO = %s, BAIRRO = %s, CIDADE = %s, ESTADO = %s, CEP = %s, ID_CURSO = %s WHERE ID_ALUNO = %s"
    val = (nome, data_nascimento, logradouro, numero, bairro, cidade, estado, cep, id_curso, id_aluno)
    cursor.execute(sql, val)
    conn.commit()
    print("Dados do aluno atualizados com sucesso.")

# Exemplo de uso
# atualizar_aluno(1, "Novo Nome", "2000-01-01", "Nova Rua", "456", "Novo Bairro", "Nova Cidade", "SP", "87654321", 2)

# Função para apagar um aluno
def apagar_aluno(id_aluno):
    sql = "DELETE FROM ALUNO WHERE ID_ALUNO = %s"
    val = (id_aluno,)
    cursor.execute(sql, val)
    conn.commit()
    print("Aluno apagado com sucesso.")

# Exemplo de uso
# apagar_aluno(6)  # Isso apagaria o aluno com ID_ALUNO igual a 1
