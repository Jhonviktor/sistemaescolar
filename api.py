from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from script import inserir_aluno, buscar_alunos, atualizar_aluno, apagar_aluno

app = FastAPI()

class Aluno(BaseModel):
    nome: str
    data_nascimento: str
    logradouro: str
    numero: str
    bairro: str
    cidade: str
    estado: str
    cep: str
    id_curso: int

# Operações CRUD

# Criar (inserir) um novo aluno
@app.post("/alunos/")
def cadastrar_aluno(aluno: Aluno):
    try:
        inserir_aluno(aluno.nome, aluno.data_nascimento, aluno.logradouro, aluno.numero, aluno.bairro, aluno.cidade, aluno.estado, aluno.cep, aluno.id_curso)
        return {"message": "Aluno cadastrado com sucesso"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Ler (listar) todos os alunos
@app.get("/alunos/", response_model=List[Aluno])
def listar_alunos():
    try:
        alunos = buscar_alunos()
        return alunos
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Atualizar os dados de um aluno
@app.put("/alunos/{aluno_id}/")
def atualizar_dados_aluno(aluno_id: int, aluno: Aluno):
    try:
        atualizar_aluno(aluno_id, aluno.nome, aluno.data_nascimento, aluno.logradouro, aluno.numero, aluno.bairro, aluno.cidade, aluno.estado, aluno.cep, aluno.id_curso)
        return {"message": "Dados do aluno atualizados com sucesso"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Deletar um aluno
@app.delete("/alunos/{aluno_id}/")
def deletar_aluno(aluno_id: int):
    try:
        apagar_aluno(aluno_id)
        return {"message": "Aluno deletado com sucesso"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
