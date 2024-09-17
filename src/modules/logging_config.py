import os
import sys
from loguru import logger


def setup_logger(log_file_name='app.log', rotation_size='50 MB', level='INFO', retention_days='7 days', compression='zip'):
    """
    Настройка логгера для записи сообщений в файл.

    Параметры
    ----------
    `log_file_name` : str, optional
        Имя файла для логирования, по умолчанию '`app.log`'
    `rotation_size` : str, optional
        Размер файла, при котором произойдет ротация, по умолчанию '`50 MB`'
    `level` : str, optional
        Минимальный уровень логирования (например, '`DEBUG`', '`INFO`', '`WARNING`', '`ERROR`', '`CRITICAL`'), по умолчанию '`INFO`'
    `retention_days` : str, optional
        Количество дней, в течение которых будут храниться архивы, по умолчанию '`7 days`'
    `compression` : str, optional
        Формат сжатия архивов (например, '`zip`'), по умолчанию '`zip`'

    Возвращает
    -------
    `logger`
        Настроенный объект логгера
    """
    # Создаем путь к папке log в корневой директории проекта
    log_dir = 'logs'
    os.makedirs(log_dir, exist_ok=True)
    log_file_path = os.path.join(log_dir, log_file_name)

    log_format = "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan> : <cyan>{line}</cyan> - <level>{message}</level>"

    logger.remove()
    logger.add(
        log_file_path,
        rotation=rotation_size,
        retention=retention_days,
        compression=compression,
        format=log_format,
        level=level
    )

    logger.add(sys.stderr, format=log_format, level="ERROR")

    return logger

# Устанавливаем логгер при импорте модуля
logger = setup_logger()

if __name__ == '__main__':
    logger.info("This is an information message.")
