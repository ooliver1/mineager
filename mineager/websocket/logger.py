# SPDX-License-Identifier: MIT

from logging import Formatter, LoggerAdapter, getLogger, INFO
from logging.handlers import TimedRotatingFileHandler

__all__ = ("default_logger",)


class UUIDAdapter(LoggerAdapter):
    def process(self, msg, kwargs):
        try:
            websocket = kwargs["extra"]["websocket"]
        except KeyError:
            return msg, kwargs

        xff = websocket.request_headers.get("CF-Connecting-IP")
        uuid = getattr(websocket, "uuid", "unknown".ljust(22))
        return f"{uuid} {xff}: {msg}", kwargs


raw_default_logger = getLogger("mineager.websocket")
raw_default_logger.setLevel(INFO)
h = TimedRotatingFileHandler("./logs/mg/io.log", when="midnight")
h.setFormatter(
    Formatter(
        "%(levelname)-7s %(asctime)s %(filename)12s:%(funcName)-28s: %(message)s",
        datefmt="%H:%M:%S %d/%m/%Y",
    )
)
h.namer = lambda name: name.replace(".log", "") + ".log"
raw_default_logger.addHandler(h)
default_logger = UUIDAdapter(raw_default_logger)
