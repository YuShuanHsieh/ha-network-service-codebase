from abc import ABC, abstractmethod
import json
import logging
from urllib import request
import requests
from typing import List

from app.settings import Settings, get_settings

from app.schema import Record, Report, Result


logger: logging.Logger = logging.getLogger(__name__)
settings: Settings = get_settings()


class Repository(ABC):
    @abstractmethod
    def save(self, record: Record) -> bool:
        raise NotImplementedError()

    @abstractmethod
    def query(self, category: str, date: str) -> List[Record]:
        raise NotImplementedError()

    @abstractmethod
    def report(self, category: str, date: str) -> Report:
        raise NotImplementedError()


URL_SAVE_RECORD: str = f"{settings.STORAGE_URL}/records"


class RestRepository(Repository):

    def save(self, record: Record) -> bool:
        response = requests.post(url=URL_SAVE_RECORD, json=record.dict())
        return Result(**response.json())

    def query(self, category: str, date: str) -> List[Record]:
        response = requests.get(
            url=f"{settings.STORAGE_URL}/records?category={category}&date={date}"
        )
        return response.json()

    def report(self, category: str, date: str) -> Report:
        response = requests.get(
            url=f"{settings.STORAGE_URL}/report?category={category}&date={date}"
        )
        return Report(**response.json())
