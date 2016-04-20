import pygame
#antialiasing
from pygame import gfxdraw
import random

class Beat(pygame.sprite.Sprite):
    #RGB numbers for white
    WHITE = (255, 255, 255)
    def __init__(self, x, y, color, ordinal):
        super(Beat, self).__init__()
        self.clock = 0
        self.radius = 50
        self.rOuter = self.radius * 5
        self.rRing = self.rOuter
        self.ringWidth = 3
        self.dRadius = self.rOuter // 60
        self.outline = 4
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x - self.rOuter, self.y - self.rOuter,
                                2 * self.rOuter, 2 * self.rOuter)
        self.image = pygame.Surface((2 * self.rOuter, 2 * self.rOuter),
                                    pygame.SRCALPHA)
        self.image = self.image.convert_alpha()
        self.ord = ordinal
        self.fontSize = 50
        self.color = color
        self.draw()

    def update(self):
        self.clock += 1
        if (self.rRing > self.radius):
            self.rRing -= self.dRadius
        #Fills in white, with the fourth number being the alpha (transparent).
        self.image.fill((255,255,255,0))
        self.draw()

    def draw(self):
        pygame.draw.circle(self.image, Beat.WHITE, (self.rOuter, self.rOuter),
            self.rRing, self.ringWidth)
        radius = 2 * self.radius
        outline = 2 * self.outline
        surface = pygame.Surface((2 * radius, 2 * radius),
                                    pygame.SRCALPHA)
        surface = surface.convert_alpha()
        pygame.draw.circle(surface, Beat.WHITE, (radius, radius),
                        radius)
        pygame.draw.circle(surface, self.color, (radius, radius),
                        radius-outline)
        (width, height) = (2 * self.radius, 2 * self.radius)
        surface = pygame.transform.smoothscale(surface, (width, height))
        startPoint = self.rOuter - self.radius
        self.image.blit(surface, (startPoint,startPoint))
        self.drawText()

    def drawText(self):
        font = pygame.font.Font(None, self.fontSize)
        text = font.render(str(self.ord), 1, Beat.WHITE)
        pos = text.get_rect()
        pos.centerx = self.image.get_rect().centerx
        pos.centery = self.image.get_rect().centery
        self.image.blit(text, pos)

#Used for collision detection.
class MousePointer(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(MousePointer, self).__init__()
        self.radius = 1
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x - self.radius, self.y - self.radius,
                                2 * self.radius, 2 * self.radius)