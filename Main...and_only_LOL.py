#import all the libraries i will use
import pygame, random

#initialize pygame
pygame.init()

#set all the variable
game_crashed = False
game_loop = False 
enemy_on_screen = False
tree_on_screen = False
up = True
clock = pygame.time.Clock()
pressed = pygame.key.get_pressed()
tree_green = (82 ,107, 45)
grass_green = (120, 240, 0)
blue = (0, 191, 255)
red = (255, 0, 0)
brown = (160, 95, 45)
tree_brown = (113, 75, 71)
yellow = (255, 255, 51)
black = (0, 0, 0)
white = (255, 255, 255)
gray = (210, 210, 210)
height = 500
width = 800
tree_pos_x = width - 30
tree_pos_y = 300
unit = 10
dark_blue = (45, 100, 125)
unitofmountain = 1
x0 = 0
x1 = x0 + 900
x2 = x1 + 900
random_x0 = random.randint(300, 700)
random_x1 = random.randint(300, 700)
random_x2 = random.randint(300, 700)
random_y0 = random.randint(320, 400)
random_y1 = random.randint(320, 400)
random_y2 = random.randint(320, 400)
funnyNumber0 = random.randint(390, 450)
funnyNumber1 = random.randint(390, 450)
funnyNumber2 = random.randint(390, 450)
cloud_white = (230, 230, 230)
cloud_x = 1200 + random.randint(0, 500)
cloud_y = 230
cloud_unit = 1
playtxt_x = 143
playtxt_y = 300
playtxt_width = 185
playtxt_height = 100
quittxt_x = playtxt_x + playtxt_x + playtxt_width
quittxt_y = playtxt_y
quittxt_width = playtxt_width
quittxt_height = playtxt_height
ground_width = 800
ground_height = 80
ground_pos_y = height - ground_height
ground_pos_x = 0
player_width = 40
player_height = 40
player_pos_y = height - player_height - ground_height
player_pos_x = player_width
asthetic_pos_x = 0
asthetic_pos_y = 100
movement = -5
enemy_height = player_height
enemy_width = player_width 
falling_speed = 7
jumping_speed = 17
bouncing_speed = 10
bounce_var = 0
Score = 0
BBText = "Bouncing Boxes"
on_ground = height - player_height - ground_height

pygame.display.set_caption("Bouncing Boxes")
screen = pygame.display.set_mode((width, height))

#Get the text box of play and quit
Main_font = pygame.font.Font("freesansbold.ttf", 67)
Play_text = Main_font.render("Play", True, (black), (gray))
PlayTextBox = Play_text.get_rect()
PlayTextBox = (playtxt_x + 25, playtxt_y + 10)
Quit_text = Main_font.render("Quit", True, (black), (gray))
QuitTextBox = Quit_text.get_rect()
QuitTextBox = (quittxt_x + 25, quittxt_y + 10)

#main loop with menu AND game loop
while game_crashed == False:
    
    #Writes the title and draws the play and quit "buttons"
    screen.fill(blue)
    pygame.draw.polygon(screen, dark_blue, [(400, 440), (670, 360), (790, 440)])
    pygame.draw.circle(screen, yellow, (20, 40), 70)
    tree_pos_x = 740
    pygame.draw.polygon(screen, tree_brown, [(tree_pos_x, tree_pos_y), (tree_pos_x + (unit * 4), tree_pos_y), (tree_pos_x + (unit * 4), tree_pos_y + (unit * 8)), (tree_pos_x + (unit * 4.2), tree_pos_y + (unit * 12)), (tree_pos_x - (unit * .3), tree_pos_y + (unit * 12))])
    pygame.draw.ellipse(screen, tree_green, [(tree_pos_x - (unit * 6), tree_pos_y - (unit * 16)), (unit * 16, unit  * 20)])
    pygame.draw.rect(screen, (brown),(ground_pos_x, ground_pos_y, ground_width, ground_height))
    pygame.draw.rect(screen, (grass_green),(ground_pos_x, ground_pos_y, ground_width, ground_height - 68))
    pygame.draw.rect(screen, (gray), (playtxt_x, playtxt_y, playtxt_width, playtxt_height))
    pygame.draw.rect(screen, (black), (playtxt_x, playtxt_y, playtxt_width, playtxt_height), 4)
    screen.blit(Play_text, PlayTextBox)
    pygame.draw.rect(screen, (gray), (quittxt_x, quittxt_y, quittxt_width, quittxt_height))
    pygame.draw.rect(screen, (black), (quittxt_x, quittxt_y, quittxt_width, quittxt_height), 4)
    screen.blit(Quit_text, QuitTextBox)
    BB_font = pygame.font.Font("freesansbold.ttf", 75)
    BB_text = BB_font.render(BBText, True, (black), (blue))
    BBTextBox = BB_text.get_rect()
    BBTextBox = (100, 80)
    screen.blit(BB_text, BBTextBox)
    
    asthetic_pos_y =  asthetic_pos_y + movement
    if up == True:
        movement = movement + .1
    
    if asthetic_pos_y >= height - player_height - ground_height - 1:
        movement = -5
        
    if asthetic_pos_x >= width - 1:
        pass
    else:
        asthetic_pos_x = asthetic_pos_x + 2.7
        
    pygame.draw.rect(screen, (red), (asthetic_pos_x, asthetic_pos_y, player_width, player_height))
    pygame.draw.rect(screen, (black), (asthetic_pos_x, asthetic_pos_y, player_width, player_height), 2)
    
    #Get the coordinates of the mouse and check if its clicking on play or quit
    for event in pygame.event.get():
        epic = pygame.mouse.get_pos()     
    if epic[1] > playtxt_y and epic[1] < playtxt_y + playtxt_height:
        if epic[0] > playtxt_x and epic[0] < playtxt_x + playtxt_width:
            epicbutton = pygame.mouse.get_pressed()
            if epicbutton[0] == 1:
                game_loop = True
                Score = 0
        elif epic[0] > quittxt_x and epic[0] < quittxt_x + quittxt_width:
            epicbutton = pygame.mouse.get_pressed()
            if epicbutton[0] == 1:
                pygame.quit()
                quit()
    
    pygame.display.flip()
    clock.tick(60)
    
    #loop that loops while you aren't in the menu
    while game_loop == True:
        
        #fill the screen blue
        screen.fill(blue)
    
        #if you press the X button, quit the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and player_pos_y >= on_ground:
                player_pos_y = player_pos_y - jumping_speed
                falling_speed = 0
                bounce_var = 100
    
        #if the player is not on the ground, fall and fall faster
        if player_pos_y < on_ground:
            player_pos_y = player_pos_y - (jumping_speed - falling_speed)
            falling_speed = falling_speed + 0.7
    
        #if the bounce is reset and the player is on the ground, bouce and bounce slower
        if 100 >= bounce_var > 0 and player_pos_y >= on_ground:
            player_pos_y = player_pos_y - bouncing_speed
            bounce_var = bounce_var - 101
            falling_speed = 7
    
        #if the player is in the ground, put him on the ground
        if player_pos_y > on_ground:
            player_pos_y = on_ground
        
        #If there is an enemy on the screen move it across the screen
        if enemy_on_screen == True:
            enemy_speed = Score // 20 + random.randint(6, 10)
            enemy_pos_x = enemy_pos_x - 5 - (Score / 2)
        elif enemy_on_screen == False:
            enemy_spawn = 800 + random.randint(30, 400)
            enemy_pos_x = enemy_spawn
            enemy_on_screen = True
        
        #when the enemy has left the screen, turn off enemy on screen and add a point to the score
        if enemy_pos_x <= -enemy_width:
            enemy_on_screen = False
            Score = Score + 1
            if Score >= 20:
                BBText = "     You Won!"
                enemy_pos_x = 881
                game_loop = False
                break
        
        #When the player collides with the enemy
        if (player_pos_y >= on_ground - player_height + 1 and enemy_pos_x < player_pos_x + enemy_width - 1 and enemy_pos_x > player_pos_x - enemy_width + 1):
            BBText = "     You Died!"
            enemy_pos_x = 881
            game_loop = False
            break
        
        #tree
        if tree_on_screen == False:
            tree_on_screen = True
            tree_pos_x = 1000 + random.randint(1, 200)
        elif tree_on_screen == True:
            tree_pos_x = tree_pos_x - 0.75
            if tree_pos_x <= - 150:
                tree_on_screen = False
                
        if cloud_x < -200:
            cloud_x = 1200 + random.randint(0, 700)
        else:
            cloud_x = cloud_x - 1
            
        #draw the player and the ground, update the display
        if game_loop == True:
            font = pygame.font.Font("freesansbold.ttf", 32)
            Score_string = str(Score)
            Actual_Score = "Score = " + Score_string
            text = font.render(Actual_Score, True, black, blue)
            textRect = text.get_rect()
            textRect.center = (600, 100)
            pygame.draw.circle(screen, yellow, (20, 40), 70)
            x0 = x0 - 0.5
            x1 = x1 - 0.5
            x2 = x2 - 0.5
            if x0 < -999:
                x0 = x2 + 900
                random_x0 = random.randint(70, 800)
                random_y0 = random.randint(250, 350)
                funnyNumber0 = random.randint(280, 390)

            elif x1 < -999:
                x1 = x0 + 900
                random_x1 = random.randint(70, 800)
                random_y1 = random.randint(250, 350)
                funnyNumber1 = random.randint(280, 390)

            elif x2 < -999:
                x2 = x1 + 900
                random_x2 = random.randint(70, 800)
                random_y2 = random.randint(250, 350)
                funnyNumber2 = random.randint(280, 390)
                
            pygame.draw.polygon(screen, dark_blue, [(x0, unitofmountain * funnyNumber0), (x0,  height), (x0 + unitofmountain * 950,  height), (x0 + unitofmountain * 950, unitofmountain * funnyNumber1), (x0 + unitofmountain * random_x0,  unitofmountain * random_y0)])
            pygame.draw.polygon(screen, dark_blue, [(x1, unitofmountain * funnyNumber1), (x1,  height), (x1 + unitofmountain * 950,  height), (x1 + unitofmountain * 950, unitofmountain * funnyNumber2), (x1 + unitofmountain * random_x1,  unitofmountain * random_y1)])
            pygame.draw.polygon(screen, dark_blue, [(x2, unitofmountain * funnyNumber2), (x2,  height), (x2 + unitofmountain * 950,  height), (x2 + unitofmountain * 950, unitofmountain * funnyNumber0), (x2 + unitofmountain * random_x2,  unitofmountain * random_y2)])

            screen.blit(text, textRect)
            pygame.draw.circle(screen, cloud_white, (cloud_x, cloud_y), cloud_unit * 50)
            pygame.draw.circle(screen, cloud_white, (cloud_x + cloud_unit * 50, cloud_y + cloud_unit * 10), cloud_unit * 40)
            pygame.draw.circle(screen, cloud_white, (cloud_x + cloud_unit * 95, cloud_y + cloud_unit * 7), cloud_unit * 30)
            pygame.draw.circle(screen, cloud_white, (cloud_x - cloud_unit * 45, cloud_y + cloud_unit * 7), cloud_unit * 30)
            pygame.draw.circle(screen, cloud_white, (cloud_x + cloud_unit * 120, cloud_y + cloud_unit * 12), cloud_unit * 20)
            pygame.draw.polygon(screen, tree_brown, [(tree_pos_x, tree_pos_y), (tree_pos_x + (unit * 4), tree_pos_y), (tree_pos_x + (unit * 4), tree_pos_y + (unit * 8)), (tree_pos_x + (unit * 4.2), tree_pos_y + (unit * 12)), (tree_pos_x - (unit * .3), tree_pos_y + (unit * 12))])
            pygame.draw.ellipse(screen, tree_green, [(tree_pos_x - (unit * 6), tree_pos_y - (unit * 16)), (unit * 16, unit  * 20)])
            pygame.draw.rect(screen, (brown),(ground_pos_x, ground_pos_y, ground_width, ground_height))
            pygame.draw.rect(screen, (grass_green),(ground_pos_x, ground_pos_y, ground_width, ground_height - 68))
            pygame.draw.rect(screen, (red), (player_pos_x, player_pos_y, player_width, player_height))
            pygame.draw.rect(screen, (yellow),(enemy_pos_x, on_ground, enemy_width, enemy_height))

            pygame.display.flip()
            clock.tick(60)
        
#quit pygame if the game crashes
pygame.quit()
quit()


