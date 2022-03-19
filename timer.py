import time


class Timer:
    """Acts as a timer that tracks how quickly the user completed the typing test."""
    def __init__(self):
        self.start_time = None
        self.finish_time = None

    def set_start_time(self):
        self.start_time = time.time()

    def set_finish_time(self):
        self.finish_time = time.time()

    def get_total_time(self):
        total_time = self.finish_time - self.start_time
        return total_time
