import datetime

def get_peak_trading_hours():
    return ["09:00-11:00", "13:00-15:00", "19:00-21:00"]

def is_peak_hour():
    current_hour = datetime.datetime.utcnow().hour
    return current_hour in [9, 13, 19]