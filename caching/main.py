import time
import logging
from typing import Optional

from cachetools import cached, TTLCache

from storage import AIRPORTS

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s : %(name)s : %(levelname)s : %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S'
                    )
logger = logging.getLogger(__name__)


@cached(cache=TTLCache(maxsize=2, ttl=2))
def get_from_db(code: str, name: str) -> Optional[dict]:
    airports = AIRPORTS["airports"]
    for airport in airports:
        if code == airport["code"] and name == airport["name"]:
            logger.info("Getting data from Database")
            return airport
    return None


def get_airport(code: str, name: str) -> Optional[dict]:
    result = get_from_db(code, name)
    return result


if __name__ == '__main__':
    get_airport(code='001', name='vn001')
    get_airport(code='001', name='vn001')
    time.sleep(3)
    print("=====================")
    get_airport(code='001', name='vn001')
    time.sleep(1)
    print("=====================")
    get_airport(code='002', name='vn002')
    get_airport(code='002', name='vn002')
    time.sleep(3)
    print("get 1")
    get_airport(code='001', name='vn001')
