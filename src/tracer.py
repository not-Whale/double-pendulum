class Tracer:
    def __init__(self):
        self.trace_x = []
        self.trace_y = []
        self.history_length = 500

    def add_coord(self, x, y):
        if len(self.trace_x) >= self.history_length:
            self.trace_x.clear()
            self.trace_y.clear()
        self.trace_x.append(x)
        self.trace_y.append(y)

    def set_history_length(self, history_length):
        self.history_length = history_length

    def get_trace(self):
        return [self.trace_x, self.trace_y]
