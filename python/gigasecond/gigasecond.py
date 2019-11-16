from datetime import datetime
from datetime import timedelta

def add(moment):
    return moment.__add__(timedelta(1000000000 / 86400))
