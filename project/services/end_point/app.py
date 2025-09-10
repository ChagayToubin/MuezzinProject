from fastapi import FastAPI
from project.config.settings import Settings
import os
from project.utilities.elastic.elastic import Elastic
from project.utilities.logger.logger_info import Logger

logger=Logger.get_logger()



app = FastAPI()

es =Elastic(Settings.uri_es)
logger.info("The server work")

@app.get("/high_risk")
def hige_risk():
    return es.find_risk("high")

@app.get("/medium_risk")
def medium_risk():
    return es.find_risk("medium")

@app.get("/none_risk")
def medium_risk():
    return es.find_risk("none")
