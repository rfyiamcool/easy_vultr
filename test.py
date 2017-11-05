#!/usr/bin/env python

import sys
import logging
from os import environ

from vultr import Vultr

SUB_ID = 11458384
API_KEY = ''
if not API_KEY:
    API_KEY = environ.get('VULTR_KEY')

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s [%(funcName)s():%(lineno)d] %(message)s'
)
logging.getLogger("requests").setLevel(logging.WARNING)


def stop():
    vultr = Vultr(API_KEY)
    vultr.server.halt(SUB_ID)


def start():
    vultr = Vultr(API_KEY)
    vultr.server.start(SUB_ID)


def destroy():
    vultr = Vultr(API_KEY)
    vultr.server.destroy(SUB_ID)


if __name__ == "__main__":
    if sys.argv[1] == "start":
        start()
    elif sys.argv[1] == "stop":
        stop()
    elif sys.argv[1] == "destroy":
        destroy()
