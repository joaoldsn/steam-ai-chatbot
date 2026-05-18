from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from chatbot.persona import SYSTEM_PROMPT
from config.settings import llm

prompt = ChatPromptTemplate.from_messages([
    ("system", SYSTEM_PROMPT),
    ("user", """
Histórico:
{historico}

Dados do jogo:
{contexto}

Pergunta:
{pergunta}
""")
])

chain = prompt | llm | StrOutputParser()
