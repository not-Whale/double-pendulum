from point import Point


class Tracer:
    def __init__(self):
        self.trace = []
        self.history_length = 500

    def add_coord(self, x, y):
        if len(self.trace) >= self.history_length:
            self.trace.clear()
        self.trace.append(Point(x, y))

    def set_history_length(self, history_length):
        self.history_length = history_length

    def get_trace(self):
        return self.trace
