import requests
from common.utils import logger

def get_quote():
    url = "https://dummyjson.com/quotes/random"

    response = requests.get(url)
    data = response.json()

    logger.debug(data)

