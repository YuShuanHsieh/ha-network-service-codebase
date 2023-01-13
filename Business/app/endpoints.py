import logging
from typing import List

from fastapi import FastAPI
from app.schema import Orders, Record, Report, Result
from app.repository import Repository, RestRepository

from app.settings import Settings, get_settings


logger: logging.Logger = logging.getLogger(__name__)

settings: Settings = get_settings()

app: FastAPI = FastAPI()

URL_MATERIAL: str = f'{settings.INVENTORY_URL}/material'

repository: Repository = RestRepository()


@app.post("/order")
def order(orders: Orders) -> Result:
    logger.info(orders)
    return Result.ok()


@app.post("/report")
def report(category: str, date: str) -> Report:
    return repository.report(category=category, date=date)


@app.post("/record")
def record(category: str, date: str) -> List[Record]:
    return repository.report(category=category, date=date)
