from __future__ import annotations 
import argparse
import contextlib
import enum
import os.path
import re
import sys
import time 

import urllib.error
import urllib.parse
import urllib.request

from typing import Generator

FILE = os.path.dirname(os.path.abspath(__file__))



