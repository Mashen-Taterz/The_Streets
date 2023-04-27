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
        
        #Create character selection images and rectangles
        char1_img = pygame.image.load("images/characters/biker/biker.jpg")
        char1_rect = char1_img.get_rect(center = (SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2))
        char2_img = pygame.image.load("images/characters/punk/punk.jpg")
        char2_rect = char2_img.get_rect(center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        char3_img = pygame.image.load("images/characters/cyborg/cyborg.jpg")
        char3_rect = char3_img.get_rect(center = (SCREEN_WIDTH // 4 * 3, SCREEN_HEIGHT // 2))

        # Run character select loop ##Move this to main loop???
        while self.current_state == "character_select":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Check if a character is selected
                    if char1_rect.collidepoint(event.pos):
                        print("Character 1 selected!")
                        self.current_state = "stage_select"
                    elif char2_rect.collidepoint(event.pos):
                        print("Character 2 selected!")
                        self.current_state = "stage_select"
                    elif char3_rect.collidepoint(event.pos):
                        print("Character 3 selected!")
                        self.current_state = "stage_select"
                        
            # Draw background and character selection images
            screen.blit(self.background, (0, 0))
            screen.blit(char1_img, char1_rect)
            screen.blit(char2_img, char2_rect)
            screen.blit(char3_img, char3_rect)

    def stage_select(self):
        self.current_state = "stage_select"
        self.background = "images/bg/bg4.png"
        self.music = "audio/music/s_select_music.ogg"
        
        # code to display stage select screen here

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
        ##Maybe move this elif to title state method or add on the character select loop here

    #Update the frames
    pygame.display.update()
    clock.tick(FPS)
