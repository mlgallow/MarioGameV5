import pygame
import time
import math
import json

from pygame.locals import*
from time import sleep

#Sprite class------------------------------------------------------------------------------
class Sprite():
	def __init__(self):
		"Sprite"
	def isBrick(self):
		return false
	def isCoin(self):
		return false
	def isCoinBlock(self):
		return false
	def isMario(self):
		return false
	def doesCollide(self, object1, object2):
		if self.object1.x + self.object1.w <= self.object2.x: 
			return false;
		if self.object1.x >= self.object2.x + self.object2.w: 
			return false;
		if self.object1.y + self.object1.h <= self.object2.y: 
			return false;        
		if self.object1.y >= self.object2.y + self.object2.h: 
			return false;        
		else:
			return true;
#Mario class-------------------------------------------------------------------------------
class Mario(Sprite):
	def __init__(self, model, x, y, w, h, Type):
		super()
		self.model = model
		self.Type = Type
		self.frame_count = 0
		self.w = w
		self.h = h
		self.x = x
		self.y = y
		self.prev_x = 0
		self.prev_y = 0
		self.coin_counter = 0
		self.vert_vel= 0
		self.marioFrame = 0;

		#loading images
		#self.mario_images = new Image()
		#self.mario_images = []
		#self.mario_images[0] = new Image()
		#self.mario_images[1] = new Image()
		#self.mario_images[2] = new Image()
		#self.mario_images[3] = new Image()
		#self.mario_images[4] = new Image()

		#self.mario_images[0].src = "mario1.png"
		#self.mario_images[1].src = "mario2.png"
		#self.mario_images[2].src = "mario3.png"
		#self.mario_images[3].src = "mario4.png"
		#self.mario_images[4].src = "mario5.png"

	def prev_location(self):
		self.prev_x = self.x
		self.prev_y = self.y

	def isMario(self):
		return true

	def get_out(self,s):
		if self.x + self.w > s.x and self.prev_x + self.w <= s.x:
			#If mario enters from the left
			self.x = s.x - self.w
		elif self.x < s.x + s.w and self.prev_x >= s.x + s.w: 
			#If mario enters form the right
			self.x = s.x + s.w
		elif self.y + self.h > s.y and self.prev_y + self.h <= s.y:
			#If mario enters form the top
            		self.y = s.y - self.h
            		self.vert_vel = 0
            		self.frame_count = 0
		elif (self.y < s.y + s.h and self.prev_y >= s.y + s.h): 
			#If mario enters form the bottom
			self.y = s.y + s.h
			self.vert_vel = 2
			if s.isCoinBlock():
				if (self.coin_counter < 6):
					self.coin_counter += 1

				s.pop_out_coin(this.coin_counter)
	def update(self):
		self.marioFrame = (math.floor(math.abs(self.x / 15)) % 5)
		#locks the scrolling to mario's x position
		self.model.scrollPos = self.x - 200
		#setting mario's velocity to a specific number
		self.vert_vel += 3
		self.y += self.vert_vel
		#stop when mario hits the groung
		if self.y > 330:
			self.y = 330
			self.vert_vel = 0
			self.frame_count = 0
		#checking for collisions with all the bricks and coin blocks
		for i in xrange (0, self.model.sprites.length, 1):
			s = self.model.sprites[i]
			if s.isBrick():
				if s.doesCollide(self, s):
					self.get_out(s)
			if s.isCoinBlock():
				if s.doesCollide(self, s):
					self.get_out(s)
 			self.frame_count+=1
#Coin Block class-----------------------------------------------------------------------
class Coin_Block(Sprite):
	def __init__(self, model, x, y, w, h, Type):
		super()
		self.model = model
		self.Type = Type
		self.coins_remaining = 5
		self.cion_frame_count = 0
		self.x = x
		self.y = y
		self.w = w
		self.h = h

		"""
		#loading images
		self.image = new Image()
		self.Coin_Block_image = []
		self.Empty_Coin_Block_image = []

		self.Coin_Block_image[0] = new Image()
		self.Empty_Coin_Block_image[0] = new Image()

		self.Coin_Block_image[0].src = "Coin_Block.png"
		self.Empty_Coin_Block_image[0].src = "Empty_Coin_Block.png"
		"""
	def update(self):
		"Coin block"
	def isCoin_Block():
		return true
	def isCoin():
		return false
	def pop_out_coin(coin_frame_count):
		if self.coins_remaining > 0:
			self.model.sprites.append(coin(self.x, self.y, 40, 40, self.model, math.floor((math.random() * 16) + 8)))
			self.coins_remaining-=1
#Coin class----------------------------------------------------------------------
class Coin(Sprite):
	def __init__(self, x, y, w, h, model, hv):
		super()
		self.ver_velocity
		self.hori_velocity
		self.hv = hv
		self.model
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.hori_velocity = hv
		"""
		#loading image
		self.Coin_image = new Image();
		self.Coin_image.src = "Coin.png"
		"""
	def update(self):
		self.ver_velocity = 3.14159
		self.y += self.ver_velocity
		self.x += self.hori_velocity
		for i in xrange (0, self.model.sprites.length, 1):
			s = self.model.sprites[i]
	def isCoin():
		return true
#Brick class-------------------------------------------------------------------------
class Brick(Sprite):
	def __init__(self, model, x, y, w, h, Type):
		super()
		self.Type = Type
		self.model = model
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		"""
		#load images
		self.Brick_iamge = new Image()
		self.Brick_image.src = "Brick_1.png"
		"""
	def update(self):
		"Brick"
	def isBrick(self):
		return true
#Model Class------------------------------------------------------------------------		
class Model():
	def __init__(self, mario):
		self.sprites = []
		self.scrollPos = 0
		self.mario = mario

	def mario_prev_locations():
		self.mario.prev_location()
		
	def update(self):
		if self.rect.left < self.dest_x:
			self.rect.left += 1
		if self.rect.left > self.dest_x:
			self.rect.left -= 1
		if self.rect.top < self.dest_y:
			self.rect.top += 1
		if self.rect.top > self.dest_y:
			self.rect.top -= 1

	def set_dest(self, pos):
		self.dest_x = pos[0]
		self.dest_y = pos[1]
#View class------------------------------------------------------------------------
class View():
	def __init__(self, model):
		screen_size = (1000,500)
		self.screen = pygame.display.set_mode(screen_size, 32)
		self.mario_image = pygame.image.load("mario1.png")
		self.background = pygame.image.load("super_mario_backgrounds_edit.png")
		self.screen.blit(self.background, self.model.rect)
		self.model = model
		self.model.rect = self.background.get_rect()

	def update(self):    
		self.screen.fill([0,0,0])
		self.screen.blit(self.background, self.screen)
		pygame.display.flip()
#Controller class-------------------------------------------------------------------------
class Controller():
	def __init__(self, model):
		self.model = model
		self.keep_going = True

	def update(self):
		for event in pygame.event.get():
			if event.type == QUIT:
				self.keep_going = False
			elif event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					self.keep_going = False
			elif event.type == pygame.MOUSEBUTTONUP:
				self.model.set_dest(pygame.mouse.get_pos())
		keys = pygame.key.get_pressed()
		if keys[K_LEFT]:
			self.model.mario.x -= 10
		if keys[K_RIGHT]:
			self.model.mario.x += 10
		if keys[K_SPACE]:
			if self.model.mario.frame_count <= 5:
				self.model.mario.vert_vel = 21

print("Use the arrow keys to move. Press Esc to quit.")
#initiating the game---------------------------------------------------------------------------------
pygame.init()
m = Model()
v = View(m)
c = Controller(m)
while c.keep_going:
	c.update()
	m.update()
	v.update()
	sleep(0.04)
print("Goodbye")
