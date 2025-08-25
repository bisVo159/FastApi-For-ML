import logging
from fastapi import FastAPI

app = FastAPI()

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] (line %(lineno)d) - %(name)s - %(levelname)s - %(message)s",
    datefmt="%m-%d-%Y %H:%M:%S"
)

logger = logging.getLogger("logging-demo")


@app.get('/debug')
def debug_route():
    logging.info('Debug endpoint hit.')
    logging.info('Another one right here!')
    return {'message': 'Check logs!'}