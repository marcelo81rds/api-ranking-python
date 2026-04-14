from pydantic import BaseModel


class JogadorCreate(BaseModel):
    nome: str
    pontuacao: int


class JogadorResponse(BaseModel):
    id: int
    nome: str
    pontuacao: int
