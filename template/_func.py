import random
import string
import datetime

def random_string(length: int = 10) -> str:
    """Generate a random string of fixed length"""
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

def random_number(length: int = 5) -> str:
    """Generate a random number of fixed length"""
    return ''.join(random.choice(string.digits) for _ in range(length))

def get_time(time: str) -> str:
    """Get the current time or date based on the input"""
    time_formats = {
        'second': '%S',
        'minute': '%M',
        'hour': '%H',
        'date': '%d',
        'month': '%m',
        'year': '%Y',
        'day': '%A'
    }
    if time in time_formats:
        return datetime.datetime.now().strftime(time_formats[time])
    else:
        return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')