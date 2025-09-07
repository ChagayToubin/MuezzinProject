import os

class Settings:

    KAFKA_URI   = os.getenv("KAFKA_URI", "localhost")
