from datetime import datetime, timedelta, timezone
from time import sleep


def get_isoformat(zone: timezone = timezone(timedelta(hours=+8))) -> str:
    return datetime.now(zone).isoformat(timespec="milliseconds")
