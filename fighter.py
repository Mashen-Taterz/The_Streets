import pygame

class Fighter():
    def __init__(self, x, y):
        self.health = 100
        self.rect = pygame.Rect((x, y, 80, 180))
        self.vel_y = 0
        self.flip = False
        self.jump = False
        self.attacking = False

    def move(self, screen_width, screen_height, surface, target):
        SPEED = 10
        GRAVITY = 2
        dx = 0
        dy = 0

        # Get keypresses
        key = pygame.key.get_pressed()

        # Movement
        if key[pygame.K_a]: #Move left
            dx = -SPEED
        if key[pygame.K_d]: #Move right
            dx = SPEED
        if key[pygame.K_w] and self.jump == False: #Jump
            self.vel_y = -30
            self.jump = True

        # Fight moves
        if self.attacking == False:
            if key[pygame.K_SPACE]:
                self.attack(surface, target)
            if key[pygame.K_s]:
                pass #Block

        # Apply gravity
        self.vel_y += GRAVITY
        dy += self.vel_y

        # Keep players on screen
        if self.rect.left + dx < 0:
            dx = -self.rect.left + 1
        if self.rect.right + dx > screen_width:
            dx = screen_width - self.rect.right - 1
        if self.rect.bottom + dy > screen_height - 60:
            self.vel_y = 0
            self.jump = False
            dy = screen_height - 60 - self.rect.bottom

        #Make sure players face eachother
        if target.rect.centerx > self.rect.centerx:
            self.flip = False
        else:
            self.flip = True

        # Update player position
        self.rect.x += dx
        self.rect.y += dy

    def attack(self, surface, target):
        self.attacking = True
        attack_rect = pygame.Rect(self.rect.centerx - (1.5 * self.rect.width * self.flip), self.rect.y, 1.5 * self.rect.width, self.rect.height / 2)
        if attack_rect.colliderect(target.rect):
            target.health -= 5 
         
          

        # Temp visual of hit box
        pygame.draw.rect(surface, (0, 255, 0), attack_rect)

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), self.rect)
