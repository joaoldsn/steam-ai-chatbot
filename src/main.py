import os
import requests
import re

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# =========================
# CONFIG
# =========================

os.environ["USER_AGENT"] = "GameGPT/2.0"
os.environ["GROQ_API_KEY"] = "SUA API"

headers = {"User-Agent": "Mozilla/5.0"}

llm = ChatGroq(model="llama-3.3-70b-versatile")

historico = []

# =========================
# FILTRAR RESULTADOS RUINS
# =========================

def resultado_valido(nome):

    bloquear = [
        "soundtrack",
        "demo",
        "dlc",
        "pack",
        "bundle",
        "editor",
        "tool"
    ]

    nome = nome.lower()

    for palavra in bloquear:
        if palavra in nome:
            return False

    return True


# =========================
# BUSCAR JOGO NA STEAM
# =========================

def buscar_jogo(nome):

    try:

        busca = f"https://store.steampowered.com/search/?term={nome}"
        html = requests.get(busca, headers=headers).text

        jogos = re.findall(
            r'data-ds-appid="(\d+)".*?<span class="title">(.*?)</span>',
            html,
            re.S
        )

        for appid, titulo in jogos:

            if resultado_valido(titulo):

                api = f"https://store.steampowered.com/api/appdetails?appids={appid}&l=portuguese"
                data = requests.get(api, headers=headers).json()

                info = data[appid]["data"]

                nome = info.get("name", "")
                desc = info.get("short_description", "")

                dev = ", ".join(info.get("developers", []))
                pub = ", ".join(info.get("publishers", []))

                preco = "Grátis"

                if "price_overview" in info:
                    preco = info["price_overview"]["final_formatted"]

                plataformas = info.get("platforms", {})

                plats = []

                if plataformas.get("windows"):
                    plats.append("Windows")

                if plataformas.get("mac"):
                    plats.append("Mac")

                if plataformas.get("linux"):
                    plats.append("Linux")

                requisitos = ""

                if "pc_requirements" in info:
                    requisitos = info["pc_requirements"].get("minimum", "")

                capa = f"https://cdn.cloudflare.steamstatic.com/steam/apps/{appid}/header.jpg"

                return {
                    "appid": appid,
                    "nome": nome,
                    "descricao": desc,
                    "dev": dev,
                    "pub": pub,
                    "preco": preco,
                    "plataformas": ", ".join(plats),
                    "requisitos": requisitos,
                    "capa": capa
                }

        return None

    except:
        return None


# =========================
# NOTA DA STEAM
# =========================

def nota_steam(appid):

    try:

        url = f"https://store.steampowered.com/appreviews/{appid}?json=1"
        data = requests.get(url, headers=headers).json()

        score = data["query_summary"]["review_score_desc"]
        total = data["query_summary"]["total_reviews"]

        return f"{score} ({total} reviews)"

    except:
        return "Sem avaliação"


# =========================
# RECOMENDAR
# =========================

def recomendar(nome):

    try:

        busca = f"https://store.steampowered.com/search/?term={nome}"
        html = requests.get(busca, headers=headers).text

        jogos = re.findall(r'class="title">(.*?)</span>', html)

        recomendados = []

        for j in jogos:

            if resultado_valido(j) and j.lower() != nome.lower():
                recomendados.append(j)

        return recomendados[:5]

    except:
        return []


# =========================
# MENU DO JOGO
# =========================

def mostrar_menu(jogo, nota):

    print("\n🎮 Jogo encontrado!\n")

    print("Nome:", jogo["nome"])
    print("Preço:", jogo["preco"])
    print("Plataformas:", jogo["plataformas"])
    print("Avaliação:", nota)
    print("Capa:", jogo["capa"])

    print("\nAgora pergunte algo sobre o jogo.\n")


# =========================
# PROMPT DA IA
# =========================

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
Você é o GameGPT.

Um especialista em videogames que explica jogos
como um gamer experiente.

Explique gameplay, história, curiosidades
e dê opiniões quando necessário.
"""
    ),
    (
        "user",
        """
Histórico:
{historico}

Dados do jogo:
{contexto}

Pergunta:
{pergunta}
"""
    )
])

chain = prompt | llm | StrOutputParser()

# =========================
# ESTADO DO BOT
# =========================

jogo_atual = None
contexto = None

print("🎮 GameGPT PRO iniciado!\n")

while True:

    pergunta = input("Você: ")

    if pergunta.lower() in ["sair", "exit", "quit"]:
        print("🎮 Até mais gamer!")
        break

    # =========================
    # DETECTAR NOVO JOGO
    # =========================

    novo = None

    if len(pergunta.split()) <= 4 and not pergunta.endswith("?"):
        novo = buscar_jogo(pergunta)

    if novo:

        # limpar memória ao trocar jogo
        historico = []

        jogo_atual = novo["nome"]

        contexto = f"""
Nome: {novo["nome"]}
Descrição: {novo["descricao"]}
Desenvolvedor: {novo["dev"]}
Publicadora: {novo["pub"]}
Preço: {novo["preco"]}
Plataformas: {novo["plataformas"]}
Requisitos: {novo["requisitos"]}
"""

        nota = nota_steam(novo["appid"])

        # MOSTRA APENAS MENU
        mostrar_menu(novo, nota)

        continue

    # =========================
    # SE NÃO TIVER JOGO
    # =========================

    if jogo_atual is None:

        print("Digite o nome de um jogo primeiro.")
        continue

    # =========================
    # CONVERSA NORMAL
    # =========================

    texto_hist = "\n".join(historico)

    resposta = chain.invoke({
        "historico": texto_hist,
        "contexto": contexto,
        "pergunta": pergunta
    })

    print("\n🎮 GameGPT:\n")
    print(resposta)

    print("\n" + "-"*50)

    historico.append("Usuário: " + pergunta)
    historico.append("GameGPT: " + resposta)

    # =========================
    # RECOMENDAÇÕES
    # =========================

    if "recomendar" in pergunta.lower():

        jogos = recomendar(jogo_atual)

        print("\n🎮 Jogos parecidos:\n")

        for j in jogos:
            print("-", j)

        print("\n" + "-"*50)
