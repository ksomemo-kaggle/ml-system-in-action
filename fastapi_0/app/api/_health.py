from typing import Dict
import logging

logger = logging.getLogger(__name__)


def health() -> Dict[str, str]:
    return {'health': 'ok'}


def health_sync() -> Dict[str, str]:
    return health()


async def health_async() -> Dict[str, str]:
    return health()