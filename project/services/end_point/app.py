from fastapi import FastAPI
from project.config.settings import Settings
import os
from project.utilities.elastic.elastic import Elastic
#
# def get_uri(host=Settings.uri_es[1],port=Settings[0]):
#     if host and port:
#         return f"http://{host}:{port}"
#     else:
#         return "http://localhost:9200"


app = FastAPI()

es =Elastic(Settings.uri_es)




@app.get("/high_risk")
def hige_risk():
    return es.find_risk("high")


@app.get("/medium_risk")
def medium_risk():
    return es.find_risk("medium")



@app.get("/none_risk")
def medium_risk():
    return es.find_risk("none")
