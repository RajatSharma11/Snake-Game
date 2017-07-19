# Snake Game! by Rajat Sharma

# Packages needed 
import pygame       # useful for graphics, sounds, vector calculation etc
import sys          # useful for exit function
import random       # for placing food of snake at random position
import time         # for sleeping a few seconds after game over and before quitting the game for showing game overview such as score

check_errors = pygame.init()  # initialising pygame, it will return a tuple for eg. (6, 0)
if(check_errors[1] > 0):
  print("(!) Had {0} initialising errors, exiting....".format(check_errors[0]))
  sys.exit(-1)
else:
  print("(+) PyGame Successfully Initialised!")
  
# Play Surface
playSurface = pygame.display.set_mode((720, 460)) # display.set_mode requires a tuple (width, height)
pygame.display.set_caption("Snake Game!")
  
# Colors 
# Color take three arguments r,g,b
red   = pygame.Color(255, 0, 0)     # For Game Over
green = pygame.Color(0, 255, 0)     # For Snake
black = pygame.Color(0, 0, 0)       # For Score
white = pygame.Color(255, 255, 255) # For Background
brown = pygame.Color(165, 42, 42)   # For food

# FPS (frame per second)  Controller
fpsController = pygame.time.Clock()

# Variables
snakePos = [100,50]           # position of Snake at the beginning of the game
snakeBody = [[100,50], [90,50], [80,50]]

foodPos = [random.randrange(1, 72) * 10, random.randrange(1, 46) * 10] # position of food
foodSpwan = True

direction = "RIGHT"
changeTo = direction

score = 0

# Game Over function
def gameOver():
  # using system font, Two argument required font name, font size
  font = pygame.font.SysFont("monaco", 72)
  GoSurf = font.render("Game Over!", True, red)
  Gorect = GoSurf.get_rect()
  Gorect.midtop = (360, 15)             # positioning the rectangle
  playSurface.blit(GoSurf,Gorect)       # for placing the Gosurf on playerSurface
  showScore(0)
  pygame.display.flip()
  time.sleep(2)
  pygame.quit()         # pygame exit
  sys.exit()            # console exit
  
# Show Score function
def showScore(choice = 1):
  score_font = pygame.font.SysFont("monaco", 30)
  scoreSurface = score_font.render("Score : {0}".format(score), True, black)
  scoreRect = scoreSurface.get_rect()
  if choice == 1:
    scoreRect.midtop = (80, 10)
  else:
    scoreRect.midtop = (360, 120)
  playSurface.blit(scoreSurface,scoreRect)

# Main Logic of the game
while True:                                 # Infinite loop for looping game frames
    for event in pygame.event.get():        # lopping through the event availbale in pygame
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == ord("d"):
                #   w
                # a s d
                changeTo = "RIGHT"
            if event.key == pygame.K_LEFT or event.key == ord("a"):
                #   w
                # a s d
                changeTo = "LEFT"
            if event.key == pygame.K_UP or event.key == ord("w"):
                #   w
                # a s d
                changeTo = "UP"
            if event.key == pygame.K_DOWN or event.key == ord("s"):
                #   w
                # a s d
                changeTo = "DOWN"
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT)) # creating an event for Quitting on pressing Escape Key

    # Validation of direction
    # if snake is moving to right then it cannot be moved to left instantly. it can move either up or down similarily for other directions
    if changeTo == "RIGHT" and not direction == "LEFT":
        direction = "RIGHT"
    if changeTo == "LEFT" and not direction == "RIGHT":
        direction = "LEFT"
    if changeTo == "UP" and not direction == "DOWN":
        direction = "UP"
    if changeTo == "DOWN" and not direction == "UP":
        direction = "DOWN"
        
    # Updating the snake position [x, y]
        
    if direction == "RIGHT":
      snakePos[0] += 10       # increasing x coordinate
    if direction == "LEFT":
      snakePos[0] -= 10       # decreasing x coordinate
    if direction == "UP":
      snakePos[1] -= 10       # decreasing y coordinate
    if direction == "DOWN":
      snakePos[1] += 10       # increasing y coordinate
      
    # updating snake body
    snakeBody.insert(0,list(snakePos))
    if snakePos[0] == foodPos[0] and snakePos[1] == foodPos[1]:
      score += 1
      foodSpwan = False
    else:
      snakeBody.pop()
    
    if foodSpwan == False:
      foodPos = [random.randrange(1, 72) * 10, random.randrange(1, 46) * 10] # position of food
    foodSpwan = True
    
    playSurface.fill(white)       # will fill the display with white colour
    
    for pos in snakeBody:
      pygame.draw.rect(playSurface, green, pygame.Rect(pos[0], pos[1], 10, 10))
      
    pygame.draw.rect(playSurface, brown, pygame.Rect(foodPos[0], foodPos[1], 10, 10))
    
    # Bounds
    if snakePos[0] > 710 or snakePos[0] < 0:
      gameOver()
    if snakePos[1] > 450 or snakePos[1] < 0:
      gameOver()
      
    for block in snakeBody[1:]:
      if snakePos[0] == block[0] and snakePos[1] == block[1]:       # if head of snake collides with any of its body part
        gameOver()
      
    showScore()
    pygame.display.flip()         # important, otherwise the screen will not be updated
    fpsController.tick(22)        # for controlling frame per second speed
