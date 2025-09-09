
import logging
from elasticsearch import Elasticsearch
from datetime import datetime



class Logger:
    _logger = None

    @classmethod
    def get_logger(cls, name="your_logger_name", es_host="your_es_host_name"
                   ,index="your_index_logs_name", level=logging.DEBUG):
        if cls._logger:

            return cls._logger
        logger = logging.getLogger(name)
        logger.setLevel(level)
        if not logger.handlers:
            es = Elasticsearch(es_host)

        class ESHandler(logging.Handler):
            def emit(self, record):
                try:
                    es.index(index=index, document={
                        "timestamp": datetime.utcnow().isoformat(),
                        "level": record.levelname,
                        "logger": record.name,
                        "message": record.getMessage()

                    })
                except Exception as e:
                    print(f"ES log failed: {e}")
                    logger.addHandler(ESHandler())
                    logger.addHandler(logging.StreamHandler())
                    cls._logger = logger
                    return logger


logger = Logger.get_logger(name="process", es_host="http://localhost:9200", index="muezzin_logs")
# print(logger)
# logger.info("dsds")
# import logging

# Get a logger named after the current module
logger = logging.getLogger("chagay")

# Set the logging level (optional, but good practice)
logger.setLevel(logging.INFO)

# Log messages using the logger
logger.info("This is an informational message.")
logger.warning("This is a warning message.")