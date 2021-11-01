#!/usr/bin/env python

import logging

from retry import retry

MAX_TRIES = 5
INTERVAL = 1

logging.basicConfig()

#
# Retry 5 times, retry interval all all 1 second
#

@retry(tries=MAX_TRIES, delay=INTERVAL)
def make_trouble():
    raise Exception

try:
    logging.info("Retry 5 times, and interval is 1 second")
    make_trouble()
except Exception:
    logging.warning("Retry end, handle exception here.")

#
# Retry 5 times, retry interval 1/2/4/6/8 seconds
#

@retry(tries=MAX_TRIES, delay=INTERVAL, backoff=2)
def make_trouble_backoff():
    raise Exception

try:
    logging.info("Retry 10 times with backoff=2")
    make_trouble_backoff()
except Exception:
    logging.warning("Retry end, handle exception here.")

#
# Retry 5 times, retry interval 1/2/3/3 seconds
#

@retry(tries=MAX_TRIES, delay=INTERVAL, backoff=2, max_delay=3)
def make_trouble_backoff_with_max_delay():
    raise Exception

try:
    logging.info("Retry 10 times with backoff=2 and max_delay=3")
    make_trouble_backoff_with_max_delay()
except Exception:
    logging.warning("Retry end, handle exception here.")

#
# Retry 5 times, retry interval 1/2/5/7 seconds
#

@retry(tries=MAX_TRIES, delay=INTERVAL, jitter=2)
def make_trouble_jitter():
    raise Exception

try:
    logging.info("Retry 10 times with jitter=2")
    make_trouble_jitter()
except Exception:
    logging.warning("Retry end, handle exception here.")
