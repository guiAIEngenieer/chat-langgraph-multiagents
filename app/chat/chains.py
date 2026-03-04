from langchain_core.output_parsers import StrOutputParser
from app.chat.prompts import prompt_accountant , prompt_marketing , prompt_router, prompt_technician , Route
from app.chat.models import chat_gemini, chat_gemini_choice
from app.session.manager import manager
from langchain_core.runnables.history import RunnableWithMessageHistory

# Chain router
chain_router = prompt_router | chat_gemini_choice.with_structured_output(Route)

# Chains prompts
chain_technician = prompt_technician | chat_gemini | StrOutputParser()

chain_accountant = prompt_accountant | chat_gemini | StrOutputParser()

chain_marketing = prompt_marketing | chat_gemini | StrOutputParser()

# Chains with memory

chain_memory_chain_technician = RunnableWithMessageHistory(
    runnable= chain_technician,
    get_session_history=manager.session_history,
    input_messages_key= "query",
    history_messages_key="history"
)

chain_memory_chain_accountant = RunnableWithMessageHistory(
    runnable= chain_accountant,
    get_session_history=manager.session_history,
    input_messages_key= "query",
    history_messages_key="history"
)

chain_memory_chain_marketing = RunnableWithMessageHistory(
    runnable= chain_marketing,
    get_session_history=manager.session_history,
    input_messages_key= "query",
    history_messages_key="history"
)
