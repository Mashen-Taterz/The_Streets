import pygame, sys, random 

pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()
FPS = 60
background = None
music = None


#Set up game window
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 960
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


#Load font
font = pygame.font.SysFont("freesansbold.ttf", 150)
#Create text surface
text_surface = font.render("The Streets", True, (255, 70, 70))
#Get text surface dimensions
text_width, text_height = text_surface.get_rect().size

#Play button font
button_font = pygame.font.SysFont("freesansbold.ttf", 100)
play_button_text = button_font.render("Play", True, (50, 50, 50))
        
#playbutton rectangle
play_button_rect = play_button_text.get_rect()
play_button_rect.centerx = screen.get_rect().centerx
play_button_rect.centery = screen.get_rect().centery + 100


# Define the character selection rectangles
char1_rect = pygame.Rect((SCREEN_WIDTH // 6, SCREEN_HEIGHT // 3, SCREEN_WIDTH // 6, SCREEN_HEIGHT // 3))
char2_rect = pygame.Rect((SCREEN_WIDTH // 2.35, SCREEN_HEIGHT // 3, SCREEN_WIDTH // 6, SCREEN_HEIGHT // 3))
char3_rect = pygame.Rect((SCREEN_WIDTH - SCREEN_WIDTH // 6 * 2, SCREEN_HEIGHT // 3, SCREEN_WIDTH // 6, SCREEN_HEIGHT // 3))

# Load character images
char1_img = pygame.transform.scale(pygame.image.load("images/characters/biker/biker.jpg"), char1_rect.size)
char2_img = pygame.transform.scale(pygame.image.load("images/characters/cyborg/cyborg.jpg"), char2_rect.size)
char3_img = pygame.transform.scale(pygame.image.load("images/characters/punk/punk.jpg"), char3_rect.size)

# Define stage select rectangles
stage1_rect = pygame.Rect((SCREEN_WIDTH // 6, SCREEN_HEIGHT // 3, SCREEN_WIDTH // 6, SCREEN_HEIGHT // 3))
stage2_rect = pygame.Rect((SCREEN_WIDTH // 2.35, SCREEN_HEIGHT // 3, SCREEN_WIDTH // 6, SCREEN_HEIGHT // 3))
stage3_rect = pygame.Rect((SCREEN_WIDTH - SCREEN_WIDTH // 6 * 2, SCREEN_HEIGHT // 3, SCREEN_WIDTH // 6, SCREEN_HEIGHT // 3))

# Load stage images
stage1_img = pygame.transform.scale(pygame.image.load("images/bg/bg1.png"), char1_rect.size)
stage2_img = pygame.transform.scale(pygame.image.load("images/bg/bg2.png"), char2_rect.size)
stage3_img = pygame.transform.scale(pygame.image.load("images/bg/bg3.png"), char3_rect.size)

#Create class for  game state
class GameState:
    def __init__(self):
        self.current_state = "title"
        self.background = None
        self.music = None

    def play_music(self):
        if self.current_state == "title":
            self.music = pygame.mixer.music.load("audio/music/title_music.ogg")
        elif self.current_state == "character_select":
            self.music = pygame.mixer.music.load("audio/music/c_select_music.ogg")
        elif self.current_state == "stage_select":
            self.music = pygame.mixer.music.load("audio/music/s_select_music.ogg")
        elif self.current_state == "main_game":
            self.music = pygame.mixer.music.load("audio/music/stage_music_0.ogg")
        pygame.mixer.music.play(-1)


    def title_state(self):
        self.current_state = "title"

        #Draw background
        self.background = pygame.transform.scale(pygame.image.load("images/bg/bg_title.png"), (SCREEN_WIDTH, SCREEN_HEIGHT))
        screen.blit(game_state.background, (0, 0))
        
        #Check if music is already playing
        if not pygame.mixer.music.get_busy():
            self.play_music()

        #Draw title background and text
        screen.blit(text_surface, ((SCREEN_WIDTH - text_width) // 2, (SCREEN_HEIGHT - text_height) // 4))

        #Draw play button
        pygame.draw.rect(screen, (255, 50, 50), play_button_rect)
        screen.blit(play_button_text, play_button_rect)

        

    def character_select(self):
        self.current_state = "character_select"

        #Draw background
        self.background = pygame.transform.scale(pygame.image.load("images/bg/bg_cs.png"), (SCREEN_WIDTH, SCREEN_HEIGHT))
        screen.blit(game_state.background, (0, 0))

        #Play music
        if not pygame.mixer.music.get_busy():
            self.play_music()
        
        # Draw character selection images
        screen.blit(char1_img, char1_rect)
        screen.blit(char2_img, char2_rect)
        screen.blit(char3_img, char3_rect)
        pygame.draw.rect(screen, (255, 0, 0), char1_rect, 2)
        pygame.draw.rect(screen, (0, 255, 0), char2_rect, 2)
        pygame.draw.rect(screen, (0, 0, 255), char3_rect, 2)

    def stage_select(self):
        self.current_state = "stage_select"
        #Draw background
        self.background = pygame.transform.scale(pygame.image.load("images/bg/bg_ss.png"), (SCREEN_WIDTH, SCREEN_HEIGHT))
        screen.blit(game_state.background, (0, 0))

        #Play music
        if not pygame.mixer.music.get_busy():
            self.play_music()

        # Draw stage selection images
        screen.blit(stage1_img, stage1_rect)
        screen.blit(stage2_img, stage2_rect)
        screen.blit(stage3_img, stage3_rect)
        pygame.draw.rect(screen, (255, 0, 0), char1_rect, 2)
        pygame.draw.rect(screen, (0, 255, 0), char2_rect, 2)
        pygame.draw.rect(screen, (0, 0, 255), char3_rect, 2)

    def main_game(self):
        self.current_state = "main_game"
        self.background = "images/bg/bg1.png"
        self.music = "audio/music/stage_music_0.ogg" 

        # code to start the main game here

    


game_state = GameState()
#Run main loop
while True:
    if game_state.current_state == "title":
        game_state.title_state()
    elif game_state.current_state == "character_select":
        game_state.character_select()
    elif game_state.current_state == "stage_select":
        game_state.stage_select()
    elif game_state.current_state == "main_game":
        game_state.main_game()
    
    # code to handle user input here
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and game_state.current_state == "title":
        # Check if button is pressed
            if play_button_rect.collidepoint(event.pos):
                # move to character select screen
                game_state.character_select()  # call the method on the instance
                game_state.play_music()
        elif event.type == pygame.MOUSEBUTTONDOWN and game_state.current_state == "character_select":
            # Check if a character is selected
            if char1_rect.collidepoint(event.pos):
                print("Character 1 selected!")
                game_state.stage_select()
                game_state.play_music()
            elif char2_rect.collidepoint(event.pos):
                print("Character 2 selected!")
                game_state.stage_select()
                game_state.play_music()
            elif char3_rect.collidepoint(event.pos):
                print("Character 3 selected!")
                game_state.stage_select()
                game_state.play_music()

    
    #Update the frames
    pygame.display.update()
    clock.tick(FPS)
