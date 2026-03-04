from langchain_core.runnables import RunnableConfig
from typing import TypedDict, Literal
from app.chat.chains import chain_memory_chain_marketing, chain_router, chain_memory_chain_technician, chain_memory_chain_accountant, chain_marketing
from app.core.logger import logger
from app.session.manager import manager
from app.chat.prompts import Route

# State of nodes
class State(TypedDict):
    query: str
    response: str
    sector: Route

# Node router
async def node_router(state: State, config=RunnableConfig):
    try:
        session_id = None
        if isinstance(config, dict):
            session_id = config.get("configurable", {}).get("session_id", None)

        if session_id is not None:
            saved_sector = manager.get_session_sector(session_id)
            if saved_sector is not None:
                
                return {"sector": saved_sector}

        sector = await chain_router.ainvoke({"query": state["query"]}, config=config)

        if session_id is not None:
            manager.set_session_sector(session_id, sector)

        return {"sector": sector}
        
    except:
        logger.exception("Failure in node_router")
        raise

# Node technician
async def node_technician(state: State, config: RunnableConfig):
    try:
        return {"response": await chain_memory_chain_technician.ainvoke({"query": state["query"]}, config=config)}
    except:
        logger.exception("Failure in node_technician")  
        raise

# Node accountant
async def node_accountant(state: State, config: RunnableConfig):
    try:
        return {"response": await chain_memory_chain_accountant.ainvoke({"query": state["query"]}, config=config)}
    except:
        logger.exception("Failure in node_accountant")  
        raise

# Node marketing
async def node_marketing(state: State, config: RunnableConfig):
    try:
        return {"response": await chain_memory_chain_marketing.ainvoke({"query": state["query"]}, config=config)}
    except:
        logger.exception("Failure in node_marketing") 
        raise 

# Choose the nodes

async def choose_node(state: State) -> Literal["node_technician", "node_accountant", "node_marketing"]:
    try:
        match state["sector"]["sector"]:
                case "technician":
                    return "node_technician"
                case "accountant":
                    return "node_accountant"
                case "marketing":
                    return "node_marketing"
    except:
        logger.exception("Error during node selection")  
        raise



