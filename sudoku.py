import pygame
import requests
from pygame import mixer


WIDTH = 550
background_color = (251,247,245)
original_grid_element_color = (52, 31, 151)
buffer = 5

response = requests.get('https://sugoku.herokuapp.com/board?difficulty=easy')
grid = response.json()['board']
grid_original = [[grid[x][y] for y in range(len(grid[0]))] for x in range(len(grid))]

# function to write the user input
def insert(window,position):
    i,j = position[1],position[0]
    myFont = pygame.font.SysFont('Comic Sans MS',36)
    
    while True:
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                return
            if(event.type == pygame.KEYDOWN):
                if(grid_original[i-1][j-1] != 0):
                    return
                if(event.key == 48): #checking with 0
                    grid[i-1][j-1] = event.key - 48
                    pygame.draw.rect(window, background_color, (position[0]*50 + buffer, position[1]*50+ buffer,50 -2*buffer , 50 - 2*buffer))
                    pygame.display.update()
                    return
                if(0 < event.key - 48 <10):  #We are checking for valid input
                    pygame.draw.rect(window, background_color, (position[0]*50 + buffer, position[1]*50+ buffer,50 -2*buffer , 50 - 2*buffer))
                    value = myFont.render(str(event.key-48), True, (255,0,0))
                    window.blit(value, (position[0]*50 +15, position[1]*50))
                    grid[i-1][j-1] = event.key - 48
                    pygame.display.update()
                    return
                return


def main():
    # initializing the pygame
    pygame.init()
    # setting up the window
    window = pygame.display.set_mode((WIDTH,WIDTH))
    pygame.display.set_caption('Sudoku')
    window.fill(background_color)
    myFont = pygame.font.SysFont('Comic Sans MS',36)
    # background music
    mixer.music.load('concentration.mp3')
    mixer.music.play(-1)
    
    
    for i in range(0,10):
        # drawing the grid
        # line function contains staring position x and y cordinates and width of the line
        if(i%3==0):  # to make bold lines as there in sudoku
            pygame.draw.line(window,(0,0,0),(50+50*i,50),(50+50*i,500),4)
            pygame.draw.line(window,(0,0,0),(50,50+50*i),(500,50+50*i),4)
            
        pygame.draw.line(window,(0,0,0),(50+50*i,50),(50+50*i,500),2)
        pygame.draw.line(window,(0,0,0),(50,50+50*i),(500,50+50*i),2)
    pygame.display.update()
    
    # checking if the number is in between 0,9
    for i in range(0, len(grid[0])):
        for j in range(0, len(grid[0])):
            if(0<grid[i][j]<10):
                value = myFont.render(str(grid[i][j]), True, original_grid_element_color)
                window.blit(value, ((j+1)*50 + 15, (i+1)*50 ))
    pygame.display.update()
    
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                pos = pygame.mouse.get_pos()
                insert(window, (pos[0]//50, pos[1]//50))
            if(event.type == pygame.QUIT):
                pygame.quit()
                return
    
main()
                