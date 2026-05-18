historico = []

def adicionar_memoria(usuario, resposta):

    historico.append(
        f"Usuário: {usuario}"
    )

    historico.append(
        f"GameGPT: {resposta}"
    )


def limpar_memoria():
    historico.clear()


def obter_historico():
    return "\n".join(historico)
