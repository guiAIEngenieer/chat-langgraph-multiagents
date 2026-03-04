from langchain_core.prompts import ChatPromptTemplate
from typing import Literal, TypedDict

# Route for the router
class Route(TypedDict):
    sector: Literal["technician","accountant","marketing"]

# Router prompt
prompt_router = ChatPromptTemplate(
    [
        ("system", "Responda apenas com 'technician', 'accountant', ou 'marketing'."),
        ("human", "{query}")
    ]
)

# Core prompts
prompt_technician = ChatPromptTemplate(
    [
        ("system", "Você é um especialista em suportes tecnicos , Se aprensente como Sra. Gambiarra"),
        ("placeholder", "{history}"),
        ("human", "{query}")
    ]
)

prompt_accountant = ChatPromptTemplate(
    [
        ("system", "Você é um especialista em contabilidade , Se aprensente como Sr. Dinheiro"),
        ("placeholder", "{history}"),
        ("human", "{query}")
    ]
)

prompt_marketing = ChatPromptTemplate(
    [
        ("system", "Você é um especialista em marketing , Se aprensente como Sr. Marqueteiro"),
        ("placeholder", "{history}"),
        ("human", "{query}")
    ]
)

