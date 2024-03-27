# defining our logger to maintain logs in our code
import logging

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)

handler = logging.FileHandler('logs/logs.log')

formatter = logging.Formatter(' %(asctime)s - %(lineno)d - %(name)s - %(levelname)s - %(message)s ')

handler.setFormatter(formatter)
logger.addHandler(handler)