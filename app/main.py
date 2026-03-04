from app.langgraph.graphs import app
from app.utils.validations import validate_prompt
from app.core.logger import logger
from app.config.constants import SESSION_ID
import asyncio

async def main():

    while True:
        try:
            question = input("prompt: ").strip()

            if question.lower() == "sair":
                break

            error = validate_prompt(question)
        
            if error:
                logger.error(error)
                continue

            response = await app.ainvoke(
                {"query": question},
                {"configurable": {"session_id": SESSION_ID}}
            )

            logger.info(response["response"])
        
        except:
            logger.exception("Error during application execution")
            raise

if __name__ == "__main__":
    asyncio.run(main())
