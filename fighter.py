import pygame

class Fighter():
    def __init__(self, x, y, flip, data, sprite_sheet, animation_steps):
        self.size = data[0]
        self.image_scale = data[1]
        self.offset = data[2]
        self.flip = flip
        self.animation_list = self.load_images(sprite_sheet, animation_steps)
        self.action = 0 #0:idle, 1:run, 2:attack
        self.frame_index = 0
        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = pygame.Rect((x, y, 80, 180))
        self.vel_y = 0
        self.jump = False
        self.attacking = False
        self.health = 100

    def load_images(self, sprite_sheet, animation_steps):
        #Extract images from sprite sheet
        animation_list = []
        for y, animation in enumerate(animation_steps):
            temp_img_list = []
            for x in range(animation):
                temp_img = sprite_sheet.subsurface(x * self.size, y * self.size, self.size, self.size)
                temp_img_list.append(pygame.transform.scale(temp_img, (self.size * self.image_scale, self.size * self.image_scale)))
            animation_list.append(temp_img_list)
        return animation_list


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
        attack_rect = pygame.Rect(self.rect.centerx - (1.5 * self.rect.width * self.flip), self.rect.y, 1.5 * self.rect.width, self.rect.height)
        if attack_rect.colliderect(target.rect):
            target.health -= 5 
         
          

        # Temp visual of hit box
        pygame.draw.rect(surface, (0, 255, 0), attack_rect)

    def draw(self, surface):
        img = pygame.transform.flip(self.image, self.flip, False)
        pygame.draw.rect(surface, (255, 0, 0), self.rect)
        if not self.flip:  #Not 100% sure how this works but without the else statement the fighter wont stay in rect...
            surface.blit(img, (self.rect.x - (self.offset[0] * self.image_scale), self.rect.y - (self.offset[1] * self.image_scale)))
        else:
            surface.blit(img, (self.rect.x - ((self.size * self.image_scale) - (self.offset[0] * 4.2 * self.image_scale)), self.rect.y - (self.offset[1] * self.image_scale)))
        