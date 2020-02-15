#!/usr/bin/python3

# Classic Console Engine by digits version 1.0.2019.12

import random

from display import *
from event import *
from timer import *

class Engine:

    def __init__(self):
        self.running = True
        self.paused = False
        self.is_typing = False
        self.display = Display(12, 12)
        self.palette = Palette()
        self.clock = Clock()
        self.clock.set_fps(60)
        self.sprites = []
        self.action_limit = 0
        self.action_queue = []
        self.debug_text = ""
        self.title = "Press 'Esc' to quit."
        
    def perform_action(self):
        K = Keys()
        # Add Keypress to Action Queue
        self.event()
        actn = self.action_queue[0]

        ### Add Key Events Here ###
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
            sel = Event.keypress()#get_key(f=str)
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
        self.debug_text = '"{}"\nDisplay({}, {}) FPS({})'.format(self.title, self.display.width, self.display.height, self.clock.fps)
        self.clock.tick()
        self.display.new_display()
        
        # Draw Here
        self.draw_sprites

        # Game Frame
        self.display.render()

    def run(self):
        while self.running:
            if self.paused == False:
                self.update()
                print(self.debug_text)
            self.perform_action()

E = Engine()
E.start()
