from datetime import datetime
from repository import buscar_por_nome, inserir, atualizar


def salvar_pontuacao(nome, pontuacao):

    jogador = buscar_por_nome(nome)
    agora = datetime.now()

    if jogador:
        id_jogador, pontuacao_antiga = jogador

        if pontuacao > pontuacao_antiga:
            atualizar(id_jogador, agora.date(), agora.time(), pontuacao)
            return {"mensagem": "Novo recorde!", "id": id_jogador}

        return {"mensagem": "Pontuação não superou recorde", "id": id_jogador}

    else:
        novo_id = inserir(nome, agora.date(), agora.time(), pontuacao)
        return {"mensagem": "Jogador criado", "id": novo_id}
