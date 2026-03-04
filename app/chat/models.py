from langchain_google_genai import ChatGoogleGenerativeAI
from app.core.logger import logger
from app.config.constants import MODEL_CHAT , TEMPERATURE_DEFAULT, TEMPERATURE_MIN
from app.settings import GEMINI_API_KEY

try:
    chat_gemini = ChatGoogleGenerativeAI(
        model= MODEL_CHAT,
        temperature= TEMPERATURE_DEFAULT,
        api_key= GEMINI_API_KEY
    )
    logger.info("Chat configured")
except:
    logger.exception("Error while trying to configure the chat_gemini.")
    raise

try:
    chat_gemini_choice = ChatGoogleGenerativeAI(
        model= MODEL_CHAT,
        temperature= TEMPERATURE_MIN,
        api_key= GEMINI_API_KEY
    )
    logger.info("Chat configured")
except:
    logger.exception("Error while trying to configure the chat_gemini_choice.")
    raise