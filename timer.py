from time import time, sleep

class Timer:

    def __init__(self):
        self.start_time = 0
        self.stop_time = 0
        self.time = 0
        self.timeout = 0

    def set_timer(self, t):
        self.timeout = t

    def start(self):
        self.start_time = time()

    def stop(self):
        self.stop_time = time()

class Clock:

    def __init__(self):
        self.start_time = time()
        self.delta = float()
        self.target_fps = 60
        self.fps = 0
        self.timer = Timer()
        self.wall_time = time()
        self.elapsed = self.get_elapsed()
        
        self.set_fps(self.target_fps)

    def set_fps(self, fps):
        self.target_fps = 1 / fps

    def get_fps(self):
        return self.fps

    def wall_time(self):
        self.wall_time = time()
        return self.wall_time

    def get_elapsed(self):
        return time() - self.start_time
    
    def tick(self):
        while (self.wall_time + self.target_fps) > time():
            sleep(0.0000000000001)
        self.fps = 1 / (time() - self.wall_time)
        self.wall_time = time()
        self.elapsed = self.get_elapsed()
