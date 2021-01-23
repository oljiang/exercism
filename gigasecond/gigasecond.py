import datetime

def add(moment):
    new_moment = moment + datetime.timedelta(seconds=10**9)
    return new_moment
