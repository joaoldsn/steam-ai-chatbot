# 🎮 GameGPT — AI Steam Games Assistant

GameGPT é um chatbot inteligente especializado em jogos da Steam, desenvolvido com Python, LangChain e Groq API.  

O sistema utiliza Inteligência Artificial para responder perguntas sobre jogos, explicando gameplay, história, curiosidades, avaliações, requisitos e características técnicas de forma amigável e contextualizada.

---

# 🚀 Objetivo do Projeto

O objetivo deste projeto é explorar aplicações práticas de IA conversacional utilizando:
- Engenharia de Prompt;
- Integração com APIs;
- Manipulação de dados;
- Arquitetura modular;
- Memória contextual;
- Automação de fluxos conversacionais.

Além disso, o projeto busca simular uma aplicação real de assistente inteligente especializado em videogames.

---

# 🧠 Contexto do Projeto

O crescimento de aplicações baseadas em IA abriu espaço para assistentes especializados em nichos específicos.

O GameGPT foi desenvolvido como um chatbot focado no universo gamer, utilizando dados reais da Steam para enriquecer as respostas da IA e proporcionar conversas contextualizadas sobre:
- gameplay;
- história;
- desenvolvedores;
- avaliações;
- requisitos mínimos;
- curiosidades;
- recomendações de jogos.

O projeto também explora conceitos modernos de:
- engenharia de prompts;
- gerenciamento de contexto;
- memória conversacional;
- modularização de sistemas inteligentes.

---

# ⚙️ Visão Geral da Solução

O usuário informa o nome de um jogo da Steam.

O sistema:
1. Busca informações na Steam;
2. Extrai os dados do jogo;
3. Organiza as informações como contexto;
4. Envia o contexto para o modelo de IA;
5. Gera respostas inteligentes e contextualizadas.

O chatbot mantém memória simples da conversa para permitir interações mais naturais.

Quando o usuário escolhe outro jogo:
- o contexto anterior é limpo;
- um novo contexto é carregado.

---

# 🏗️ Arquitetura da Solução

```txt
Usuário
   ↓
Loop Conversacional
   ↓
Busca de jogo na Steam
   ↓
Extração de informações
   ↓
Construção do contexto
   ↓
LangChain + Groq API
   ↓
Modelo Llama 3.3 70B
   ↓
Resposta contextualizada
```

---

# 📂 Estrutura do Projeto

```txt
gamegpt-ai-chatbot/
├── src/
│   ├── chatbot/
│   │   ├── chain.py
│   │   ├── memory.py
│   │   └── persona.py
│   │
│   ├── steam/
│   │   ├── steam_api.py
│   │   ├── reviews.py
│   │   └── recommendations.py
│   │
│   ├── ui/
│   │   └── menu.py
│   │
│   ├── config/
│   │   └── settings.py
│   │
│   ├── utils/
│   │   └── filters.py
│   │
│   └── main.py
│
├── docs/
├── tests/
├── assets/
├── README.md
├── requirements.txt
├── .env.example
└── LICENSE
```

---

# 🔥 Funcionalidades

- Busca automática de jogos na Steam
- Extração de informações reais da plataforma
- Chatbot especializado em videogames
- Memória contextual simples
- Recomendações de jogos
- Persona personalizada (GameGPT)
- Respostas contextualizadas com IA
- Avaliações da Steam integradas
- Consulta de requisitos mínimos
- Conversa contínua via terminal

---

# 🧩 Tecnologias Utilizadas

## Linguagem
- Python

## Inteligência Artificial
- LangChain
- langchain_groq
- Llama 3.3 70B Versatile

## APIs e Dados
- Steam Store API
- Requests
- Regex

## Versionamento
- Git
- GitHub

---

# 🎮 Como Funciona

## Fluxo do chatbot

1. O usuário digita o nome de um jogo;
2. O sistema busca os dados na Steam;
3. O GameGPT cria um contexto inteligente;
4. O usuário pode fazer perguntas sobre o jogo;
5. O chatbot responde utilizando IA + contexto da Steam.

---

# 🔑 Configuração da API Groq

Crie um arquivo `.env` na raiz do projeto:

```env
GROQ_API_KEY=sua-chave-aqui
```

---

## Instale a dependência

```bash
pip install python-dotenv
```

---

## Carregue a variável ambiente no projeto

```python
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
```

---

## Configuração do modelo

```python
from langchain_groq import ChatGroq

llm = ChatGroq(
    model="llama-3.3-70b-versatile"
)
```

---

## ⚠️ Importante

Nunca publique sua chave da API no GitHub.

Adicione `.env` no arquivo `.gitignore`:

```txt
.env
```
---

# 💬 Exemplos de Perguntas

```txt
Como é o gameplay desse jogo?
```

```txt
Esse jogo possui boa história?
```

```txt
Vale a pena jogar?
```

```txt
Quais jogos parecidos você recomenda?
```

---

# 🧠 Engenharia de Prompt

O GameGPT foi projetado utilizando técnicas de Engenharia de Prompt para:
- manter consistência;
- melhorar contextualização;
- gerar respostas naturais;
- evitar respostas genéricas;
- simular um especialista gamer.

A persona do chatbot foi construída para atuar como:
- especialista em videogames;
- consultor gamer;
- guia para descoberta de jogos.

---

# 🧠 Memória Conversacional

O sistema mantém um histórico simples da conversa para:
- preservar contexto;
- melhorar continuidade;
- tornar o diálogo mais natural.

Ao trocar de jogo:
- o histórico é reiniciado;
- um novo contexto é carregado.

---

# ⭐ Sistema de Recomendações

O chatbot consegue recomendar jogos similares utilizando:
- resultados relacionados da Steam;
- filtragem de conteúdos irrelevantes;
- similaridade contextual.

---

# 📦 Instalação

## Clone o repositório

```bash
git clone URL_DO_REPOSITORIO
```

---

## Entre na pasta

```bash
cd gamegpt-ai-chatbot
```

---

## Instale as dependências

```bash
pip install -r requirements.txt
```

---

# ▶️ Executando o Projeto

```bash
python src/main.py
```

---

# 🖥️ Exemplo de Uso

```txt
🎮 GameGPT PRO iniciado!

Você: Elden Ring

🎮 Jogo encontrado!

Nome: Elden Ring
Preço: R$ 229,90
Avaliação: Extremamente positivas

Você: Como é o combate?
```

---

# 🚧 Desafios Técnicos Superados

## Gerenciamento de Contexto
Um dos principais desafios foi manter o contexto da conversa sem misturar informações entre jogos diferentes.

---

## Extração de Dados da Steam
A coleta de informações exigiu:
- parsing de páginas;
- tratamento de dados inconsistentes;
- filtragem de resultados irrelevantes.

---

## Engenharia de Prompt
Foi necessário estruturar prompts capazes de:
- manter personalidade;
- evitar respostas genéricas;
- contextualizar informações corretamente.

---

## Memória Conversacional
Outro desafio importante foi criar uma memória simples, porém eficiente, para manter continuidade no diálogo.

---

# 📈 Melhorias Futuras

- Interface Web
- Integração com Discord
- Integração com WhatsApp
- Banco vetorial
- Memória persistente
- Sistema de favoritos
- Histórico de conversas
- RAG (Retrieval-Augmented Generation)
- Dashboard administrativo

---

# ⚡ GitHub Actions

O projeto pode utilizar GitHub Actions para:
- automação de testes;
- validação de código;
- integração contínua;
- deploy automatizado.

---

# 📚 Aprendizados do Projeto

Este projeto permitiu aprofundar conhecimentos em:
- IA aplicada;
- LangChain;
- Engenharia de Prompt;
- APIs;
- Arquitetura de Software;
- Modularização;
- Context Engineering;
- Manipulação de dados;
- Fluxos conversacionais.

---

# 🤝 Contribuição

Contribuições são bem-vindas.

Caso queira colaborar:
1. Faça um fork do projeto;
2. Crie uma branch;
3. Faça suas alterações;
4. Envie um Pull Request.

---

# 📄 Licença

Este projeto está sob a licença MIT.

---

# 👨‍💻 Autor

João Leite

🎓 Estudante de Análise e Desenvolvimento de Sistemas  
💻 Focado em IA, Engenharia de Prompt e Desenvolvimento de Software
