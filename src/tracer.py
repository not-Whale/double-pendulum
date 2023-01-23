from point import Point


class Tracer:
    def __init__(self):
        self.trace = []
        self.history_length = 100

    def add_coord(self, x, y):
        if len(self.trace) >= self.history_length:
            self.trace = self.trace[1:]
        self.trace.append(Point(x, y))

    def get_trace(self):
        return self.trace
