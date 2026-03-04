import logging
import sys

def setup_logger():
    logging.basicConfig(
        level=logging.INFO,  
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        handlers=[
            logging.StreamHandler(sys.stdout), 
            logging.FileHandler("app.log", encoding="utf-8")  
        ]
    )

setup_logger()
logger = logging.getLogger(__name__)