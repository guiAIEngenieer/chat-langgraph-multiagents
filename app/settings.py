from dotenv import load_dotenv
from app.core.logger import logger
import os

load_dotenv(".env")

GEMINI_API_KEY = os.getenv("GEMINI-API-KEY")

if not GEMINI_API_KEY:
    logger.error("GEMINI_API_KEY not configured")
    raise

logger.info("GEMINI_API_KEY configured")