# -*- coding: UTF-8 -*-

# Filename : 01-string.py
# author by : Emiya

import logging

# Phase 1:  基本用法
logging.basicConfig(level=logging.DEBUG,
                    filename='my.log',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)

msg = "调试用信息?!"
logger.info(msg)
