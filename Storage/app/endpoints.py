from collections import defaultdict

import logging
from typing import Dict, List

from app.schema import Record
from app.schema import Report
from app.schema import Result
from app.settings import get_settings
from app.settings import Settings
from fastapi import FastAPI


logger: logging.Logger = logging.getLogger(__name__)

settings: Settings = get_settings()

app: FastAPI = FastAPI()

CACHE: Dict[str, Dict[str, List[Record]]
            ] = defaultdict(lambda: defaultdict(list))


@app.post('/records')
def save(record: Record) -> Result:
    category_dict = CACHE[record.category]
    records = category_dict[record.timestamp[0:10]]  # datetime to date
    records.append(record)
    return Result.ok()


@app.get('/records')
def query(category: str, date: str) -> List[Record]:
    if category_dict := CACHE.get(category):
        return category_dict.get(date)
    return []


@app.get('/report')
def report(category: str, date: str) -> Report:
    data_list = query(category=category, date=date)
    report: Report = Report(category=category, date=date)
    report.count = len(data_list)
    report.a = sum(r.a for r in data_list)
    report.b = sum(r.b for r in data_list)
    report.c = sum(r.c for r in data_list)
    report.d = sum(r.d for r in data_list)
    return report


@app.post("/clean")
def clean() -> Result:
    CACHE.clear()
    return Result.ok()
