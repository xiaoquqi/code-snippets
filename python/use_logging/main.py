#!/usr/bin/env python

import logging

from init_logging import init_logging

# This is the common usage
init_logging(verbose=True, log_file="app.log")
logging.info("Print logs into files and stdout")

# Clean handlers from logging, this only happends in this scripts
init_logging()
logging.info("Print logs into stdout only")

#logging.getLogger().handlers = []
init_logging(verbose=False, log_file="app.log")
logging.info("Print logs into files, not in stdout")
