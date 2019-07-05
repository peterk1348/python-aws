#!/usr/bin/env python
import os
from lib import vendor
vendor.add(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'ext'))

# logging
import logging
LOGGER = logging.getLogger()
LOGGER.setLevel(logging.DEBUG)
