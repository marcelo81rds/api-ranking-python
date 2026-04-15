from fastapi import FastAPI
from models import JogadorCreate
from service import salvar_pontuacao
from repository import listar_top10

app = FastAPI(title="API Ranking Jogo")

# endpoint para salvar pontuação


@app.post("/pontuacao")
def salvar(jogador: JogadorCreate):
    return salvar_pontuacao(jogador.nome, jogador.pontuacao)


# endpoint para ver ranking
@app.get("/ranking")
def ranking():
    dados = listar_top10()

    return [
        {"id": j[0], "nome": j[1], "pontuacao": j[2]}
        for j in dados
    ]


@app.get("/")
def home():
    return {"mensagem": "API online 🚀"}
