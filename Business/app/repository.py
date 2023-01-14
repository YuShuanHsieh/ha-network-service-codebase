from __future__ import annotations

import logging
from abc import ABC
from abc import abstractmethod

import requests
from app.schema import Record
from app.schema import Report
from app.schema import Result
from app.settings import get_settings
from app.settings import Settings


logger: logging.Logger = logging.getLogger(__name__)

settings: Settings = get_settings()


class Repository(ABC):
    @abstractmethod
    def save(self, record: Record) -> bool:
        raise NotImplementedError()

    @abstractmethod
    def query(self, category: str, date: str) -> list[Record]:
        raise NotImplementedError()

    @abstractmethod
    def report(self, category: str, date: str) -> Report:
        raise NotImplementedError()


URL_SAVE_RECORD: str = f'{settings.STORAGE_URL}/records'


class RestRepository(Repository):

    def save(self, record: Record) -> bool:
        response = requests.post(url=URL_SAVE_RECORD, json=record.dict())
        return Result(**response.json())

    def query(self, category: str, date: str) -> list[Record]:
        url = f'{settings.STORAGE_URL}/records?category={category}&date={date}'
        response = requests.get(url=url)
        return response.json()

    def report(self, category: str, date: str) -> Report:
        url = f'{settings.STORAGE_URL}/report?category={category}&date={date}'
        response = requests.get(url=url)
        return Report(**response.json())
