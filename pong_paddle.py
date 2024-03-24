import pygame

class Paddle(pygame.sprite.Sprite):

  def __init__(self):
    pygame.sprite.Sprite.__init__(self)

    self.image = pygame.Surface([10,100])
    self.image.fill((255,255,255))

    self.rect = self.image.get_rect()