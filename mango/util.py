"""
Utilities of the application,
this will contain diferent functions.
"""


def process(function):
    """
    Starts a thread with the function provided.
    """
    from threading import Thread

    def wrapper(*args):
        Thread(target = function, args=args).start()
    return wrapper
