from src.modules.logging_config import setup_logger
from loguru import logger
import time

# Настройка логирования
log = setup_logger()


@logger.catch
def main():
    log.info("===START===")
    print("Helo world")


if __name__ == "__main__":
    main()
