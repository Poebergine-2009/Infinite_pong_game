import pygame

class Ball(pygame.sprite.Sprite):

  def __init__(self):
    pygame.sprite.Sprite.__init__(self)

    self.image = pygame.Surface([10,10])
    self.image.fill((255,255,255))

    self.rect = self.image.get_rect()