from pygame import *
from settings import *


class Menu():
	def __init__(self):
		self.option_surfaces = []
		self.callbacks = []
		self.option_index = 0

	def append_option(self, option, callback):
		self.option_surfaces.append(Arial.render(option, True, (255, 255, 255)))
		self.callbacks.append(callback)

	def switch(self, direction):
		self.option_index = max(0, min(self.option_index + direction, len(self.option_surfaces) - 1))

	def select(self):
		self.callbacks[self.option_index]()

	def draw(self, surf, x, y , option_y):
		for i, option in enumerate(self.option_surfaces):
			option_rect = option.get_rect()
			option_rect.topleft = (x, y + i * option_y)
			if i == self.option_index:
				draw.rect(surf, (0, 100, 0), option_rect)
			surf.blit(option, option_rect)
			