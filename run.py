#!/usr/bin/python3

# Classic Console Engine by digits version 1.03.2020.2

from display import *
from event import Event, Keys
from timer import Timer, Clock

class Engine:

    def __init__(self):
        self.running = True
        self.paused = False
        self.is_typing = False
        self.display = Display(32, 32)
        self.palette = Palette()
        self.clock = Clock()
        self.clock.set_fps(10)
        self.sprites = []
        self.action_limit = 10
        self.action_queue = []
        self.debug_text = ""
        self.title = "Press 'Esc' to quit."
        
    def perform_action(self):
        K = Keys()
        # Add Keypress to Action Queue
        self.event()
        actn = self.action_queue[0]

        ### Add Key Events Here ###
        if actn == "i":
            self.display.get_console_info()
        if actn == "r":
            self.clock = Clock()
        if actn == "x":
            if self.paused == False:
                self.paused = True
            elif self.paused == True:
                self.paused = False

        if actn == K.ESC:
            self.running = False
        
        # Clears Action Queue
        if len(self.action_queue) > self.action_limit:
            self.action_queue.pop(0)

    def event(self):
        # Get Key Press
        if self.is_typing == False:
            sel = Event.keypress()
        if self.is_typing == True:
            self.is_typing = False
            sel = input(": ")

        self.action_queue.append(sel)

    def draw_sprites(self):
        if len(self.sprites) > 0:
            for s in self.sprites:
                self.display.draw_sprite(s)

    def start(self):
        self.run()

    def update(self):
        self.debug_text = 'FPS({:.1f}) Elapsed({:.10f}) Actions({})'.format(#''Title({})Display({}, {}) FPS({:.1f}) Elapsed({:.1f}) Actions({})'.format(
                #self.title,
                #self.display.width,
                #self.display.height,
                self.clock.fps,
                self.clock.elapsed,
                self.action_queue)
        self.clock.tick()
        #self.display.refresh()
        
        #size = self.display.get_console_size()
        #self.display.set_console_size(size.x, size.y)
        
        # Draw Here
        #self.draw_sprites
        # Game Frame
        #self.display.render()

    def run(self):
        while self.running:
            if self.paused == False:
                self.update()
                print(self.debug_text)
            self.perform_action()

E = Engine()
E.start()
