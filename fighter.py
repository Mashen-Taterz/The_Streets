import pygame

class Fighter():
    def __init__(self, x, y):
        self.rect = pygame.Rect((x, y, 80, 180))

    def move(self, screen_width):
        SPEED = 10
        dx = 0
        dy = 0

        #get keypresses
        key = pygame.key.get_pressed()

        #Movement
        if key[pygame.K_a]:
            dx = -SPEED
        if key[pygame.K_d]:
            dx = SPEED
        if key[pygame.K_s]:
            pass #Block
        if key[pygame.K_w]:
            pass #Jump

        #Keep players on screen
        if self.rect.left + dx < 0:
            dx = -self.rect.left + 1

        if self.rect.right + dx > screen_width:
            dx = screen_width - self.rect.right - 1

        #Update player position
        self.rect.x += dx
        self.rect.y += dy

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), self.rect)
