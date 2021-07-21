'''
Space Shooter Game demo for Linux
Coded by Stuart Anderson
Art by Claire Anderson
Copyright 2019
'''

#requires pygame
import pygame
import random


class Bullet:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.img = pygame.image.load('img/misc/bullet.png')


class Rocket:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.img = pygame.image.load('img/ship/rocket.png')


class Explosion:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.img = pygame.image.load('img/misc/explosion.png')


class Flash:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.img = pygame.image.load('img/misc/flash.png')


class Monster:
	def __init__(self, x, y, num):
		self.x = x
		self.y = y
		self.dead_monster = False
		self.dead_count = 0
		self.num = num
		if self.num <= 50:
			self.img = pygame.image.load('img/monster/usaginingyo.png')
		else:
			self.img = pygame.image.load('img/monster/monster.png')


pygame.init()
display_width = 800
display_height = 600
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
car_width = 73
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('My kids game 1')
clock = pygame.time.Clock()


def blit(img, x, y):
	gameDisplay.blit(img, (x, y))


def game_loop():
	x = (display_width * 0.45)
	y = (display_height * 0.8)
	player = [Rocket(x, y)]
	enemy = [Monster(display_width * 0.45, 100, 1)]
	x_change = 0
	y_change = 0
	bullets = []
	gameExit = False
	go_right = True
	go_left = False
	while not gameExit:
		if len(enemy) == 0:
			enemy.append(Monster(display_width * 0.45, 100, random.randint(0, 100)))
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameExit = True
			for i in player:
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_LEFT:
						x_change = -5
					if event.key == pygame.K_RIGHT:
						x_change = 5
					if event.key == pygame.K_UP:
						y_change = -5
					if event.key == pygame.K_DOWN:
						y_change = 5
					if event.key == pygame.K_SPACE:
						bullets.append(Bullet(i.x, i.y - 20))
				if event.type == pygame.KEYUP:
					if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
						x_change = 0
					if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
						y_change = 0
		gameDisplay.fill(black)
		for i in player:
			i.x += x_change
			i.y += y_change
			blit(i.img, i.x, i.y)
		for i in enemy:
			if not i.dead_monster:
				if i.x <= 0:
					go_right = True
					go_left = False
				if i.x >= 720:
					go_right = False
					go_left = True
				if go_right:
					i.x += 5
				if go_left:
					i.x += -5
			if i.dead_monster:
				if i.dead_count <= 20:
					blit(Explosion(i.x, i.y).img, i.x, i.y)
					i.dead_count += 1
				else:
					enemy.remove(i)
			else:
				blit(i.img, i.x, i.y)
		for i in bullets:
			if i.y <= 0:
				bullets.remove(i)
			else:
				if len(enemy) == 0:
					i.y -= 10
					blit(i.img, i.x, i.y)
				else:
					for e in enemy:
						if e.y <= i.y <= e.y+70 and e.x <= i.x <= e.x+80:
							bullets.remove(i)
							e.dead_monster = True
						else:
							i.y -= 10
							blit(i.img, i.x, i.y)
		pygame.display.update()
		clock.tick(60)


game_loop()
pygame.quit()
quit()
