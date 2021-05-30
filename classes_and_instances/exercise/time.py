class Time:

    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        hh = self.hours
        mm = self.minutes
        ss = self.seconds
        return f"{hh:02d}:{mm:02d}:{ss:02d}"

    def next_second(self):
        time = self.hours * 3600 + self.minutes * 60 + self.seconds + 1
        self.hours = time // 3600
        time -= self.hours * 3600
        if self.hours > 23:
            self.hours -= 24
        self.minutes = time // 60
        time -= self.minutes * 60
        self.seconds = time
        return self.get_time()


time = Time(9, 30, 59)
print(time.next_second())
time = Time(10, 59, 59)
print(time.next_second())
time = Time(23, 59, 59)
print(time.next_second())
