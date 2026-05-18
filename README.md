# GameGPT — Chatbot Especialista em Jogos da Steam

---

# 📖 Contexto do Projeto

O GameGPT é um chatbot inteligente desenvolvido em Python com a ferramenta do Google Colab com foco em Inteligência Artificial aplicada ao universo gamer. O sistema utiliza integração com a Steam para buscar informações reais sobre jogos e utiliza o modelo de IA Llama 3.3 70B através da biblioteca LangChain Groq para responder perguntas dos usuários de forma contextualizada.

O chatbot é capaz de explicar aspectos como gameplay, história, curiosidades, avaliações, requisitos mínimos e características técnicas dos jogos, sendo um especialista em videogames.

Além disso, o projeto utiliza memória simples da conversa para manter o contexto durante o diálogo, proporcionando uma melhor experiência para o usuário.

---

# 🎯 Objetivo

O objetivo do sistema é desenvolver um chatbot conversacional especializado em jogos da Steam utilizando conceitos de Inteligência Artificial, Engenharia de Prompt, Programação em Python e Manipulação de dados.

O projeto também busca aplicar boas práticas de arquitetura de software, modularização e documentação técnica.

---

# ⚙️ Visão Geral do Sistema

O usuário inicia a conversa digitando o nome de um jogo da Steam, em seguida, o sistema busca informações reais da Steam, extrai os dados do jogo organizando essas informações como contexto e envia para o modelo de IA, gerando respostar contextualizadas através do bot.

O chatbot mantém memória simples da conversa para tornar as respostas mais coerentes durante o diálogo.

Caso o usuário informe outro jogo, o sistema limpa o histórico anterior e carrega um novo contexto, reiniciando a conversa baseada no novo jogo que foi solicitado.

---

# 🧩 Tecnologias Utilizadas

## Linguagem
- Python (Colab)

## Inteligência Artificial
- LangChain
- langchain_groq
- Llama 3.3 70B Versatile

## APIs e Dados
- Steam Store API
- Requests

## Versionamento
- Git
- GitHub

---

# 🏗️ Arquitetura da Solução

## Funcionamento da aplicação

```txt
Usuário
   ↓
Entrada do nome do jogo
   ↓
Busca de informações na Steam
   ↓
Extração e tratamento dos dados
   ↓
Construção do contexto do jogo
   ↓
Envio para LangChain + Groq
   ↓
Modelo Llama 3.3 70B
   ↓
Resposta contextualizada da IA
```

---

# ▶️ Instruções de Uso

## 1. Clone o repositório

```bash
git clone URL_DO_REPOSITORIO
```

---

## 2. Entre na pasta do projeto

```bash
cd gamegpt-ai-chatbot
```

---

## 3. Instale as dependências

```bash
pip install -r requirements.txt
```

---

## 4. Configure a API da Groq

Crie um arquivo `.env` na raiz do projeto:

```env
GROQ_API_KEY=sua-chave-aqui
```

---

## 5. Execute o projeto

```bash
python src/main.py
```

---

## 6. Utilização

Digite o nome de um jogo para iniciar:

```txt
Elden Ring
```

Depois disso, faça perguntas como:

```txt
Como é a gameplay?
```

```txt
Esse jogo possui boa história?
```

```txt
Quais jogos parecidos você recomenda?
```

Para encerrar o chatbot:

```txt
sair
```

---

# 🚧 Desafios Superados

## Gerenciamento de Contexto

Um dos principais desafios do projeto foi manter o contexto da conversa sem misturar informações entre jogos diferentes. Foi necessário implementar códigos para armazenar histórico, limpar a memória ao trocar de jogo e preservar a continuidade da conversa.

## Extração de Dados da Steam

Outro desafio importante foi a coleta de dados reais da Steam. Tive que implementar a capacidade do sistema para filtrar conteúdos irrelevantes como DLCs, demos e bundles.

## Engenharia de Prompt

Para construir a Persona do GameGPT, foram utilizados prompts para definir o comportamento da IA para evitar respostas genéricas e criar comportamento especializado em videogames.

## Modularização do Projeto

O sistema inicialmente foi desenvolvido em apenas um único arquivo e posteriormente modularizado para melhoras a organização, facilitar manutenção e transmitir maturidade técnica.

---

# 🤝 Contribuição

Contribuições são bem-vindas! Caso queira colaborar, sinta-se à vontade!
