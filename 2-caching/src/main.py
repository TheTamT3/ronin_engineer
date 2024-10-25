import logging
from typing import Optional

from cachetools import cached, TTLCache

from storage import AIRPORTS

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s : %(name)s : %(levelname)s : %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S'
                    )
logger = logging.getLogger(__name__)


@cached(cache=TTLCache(maxsize=50, ttl=600))
def get_from_db(code: str, name: str) -> Optional[dict]:
    airports = AIRPORTS["airports"]
    for airport in airports:
        if code == airport["code"] and name == airport["name"]:
            logger.info("Getting data from Database")
            return airport
    return {}


def get_airports(code: str, name: str) -> Optional[dict]:
    result = get_from_db(code, name)
    return result
