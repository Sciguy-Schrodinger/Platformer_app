import pygame
import tkinter
from tkinter import *
from PIL import Image, ImageTk
import sys
import os
from subprocess import Popen
import random
import time
import math
from pygame import mixer
from executable import resource_path

sys.path.append("/home/sciguy/Phils_Documents/Education/University/Computer_Science_and_Programming/Personal_Programming_Projects/Executable_apps/Python")

pygame.mixer.init()
 
game_music = pygame.mixer.music.load(resource_path("Game_music.mp3"))
coin_sound = pygame.mixer.Sound(resource_path("coin.mp3"))
win_sound = pygame.mixer.Sound(resource_path("win.mp3"))
unlock_door_sound = pygame.mixer.Sound(resource_path("unlock_door.mp3"))
death_sound = pygame.mixer.Sound(resource_path("death.mp3"))

global width
global height
width = 1500
height = 1500
Move = 1

global x_char 
global y_char 
global enemy_x
global enemy_y

global level
level = 1
global coins_got

coins_got = 0

global Quit
global main_menu_running
global play
global dead
global win
global facing_right
global player_facing_right

global enemies

enemies = []
enemy_frames_R = []
enemy_frames_L = []

enemy1 = pygame.image.load(resource_path("Enemy1.png"))
enemy1 = pygame.transform.scale(enemy1,(75,75))

enemy_frames_R.append(enemy1)

enemy1 = pygame.transform.flip(enemy1,True,False)

enemy_frames_L.append(enemy1)

enemy2 = pygame.image.load(resource_path("Enemy2.png"))
enemy2 = pygame.transform.scale(enemy2,(75,75))

enemy_frames_R.append(enemy2)

enemy2 = pygame.transform.flip(enemy2,True,False)

enemy_frames_L.append(enemy2)

enemy2 = pygame.image.load(resource_path("Enemy2.png"))
enemy2 = pygame.transform.scale(enemy2,(75,75))

enemy_frames_R.append(enemy2)

enemy2 = pygame.transform.flip(enemy2,True,False)

enemy_frames_L.append(enemy2)

player1 = pygame.image.load(resource_path("Character1.png"))
player1 = pygame.transform.scale(player1,(75,75))

player2 = pygame.image.load(resource_path("Character2.png"))
player2 = pygame.transform.scale(player2,(75,75))

player_frames_R = []
player_frames_L = []

player_frames_R.append(player1)

player1 = pygame.transform.flip(player1,True,False)

player_frames_L.append(player1)

player2 = pygame.transform.scale(player2,(75,75))

player_frames_R.append(player2)

player2 = pygame.transform.flip(player2,True,False)

player_frames_L.append(player2)

enemy_x = 0.5*width
enemy_y = 0.4*height
facing_right = True
dead = False
Quit = False
main_menu_running = True
play = False
Win = False
Next_Level = False
start = True

# air = 0, platform = 1, coin = 2, enemy = 3 (player and exit coded dymaniclly)

Level_1_map = [[0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,2,0],
               [1,1,0,0,0,0,0,0,0,0], 
               [0,0,0,0,2,0,0,0,0,0],
               [0,0,0,0,1,1,1,2,0,0],
               [0,0,0,0,0,0,0,0,0,0],
               [2,0,0,0,0,0,0,0,3,0],
               [0,0,0,0,2,0,0,1,1,0],
               [0,4,0,0,0,0,0,0,0,0],
               [1,1,0,0,0,0,0,0,0,0]]

Level_2_map = [[2,0,0,0,0,0,0,0,2,0],
               [0,0,0,0,0,0,0,0,0,0],
               [0,1,0,1,0,1,0,1,0,1],
               [0,0,0,0,3,0,0,2,0,0],
               [1,0,1,0,1,0,1,0,1,0],
               [2,0,0,0,0,3,0,0,0,0],
               [0,1,0,1,2,1,0,1,0,1],
               [0,0,0,0,0,0,0,0,0,0],
               [0,0,1,0,1,0,1,0,1,0],
               [1,1,0,0,0,0,0,0,0,0]]

Level_3_map = [[0,2,0,0,0,0,0,0,0,0],
               [0,0,1,0,0,0,0,0,0,0],
               [0,0,0,0,3,0,1,0,0,0],
               [0,0,2,0,1,1,1,0,0,0],
               [0,0,0,0,0,0,0,1,0,0],
               [2,0,0,0,2,0,0,3,0,0],
               [0,0,0,0,1,0,0,1,1,0],
               [0,0,0,0,0,0,0,0,0,0],
               [3,0,0,0,0,1,0,0,0,2],
               [1,1,0,0,0,0,0,0,0,0]]

def info():
    global INFO, canvas, info_text
    
    INFO = "Welcome to the playformer game. Collect all the (5) coins on each level, to open\nthe door to the next level, while scaling the heights and avoiding enemies.\nCan you escape the danger?\n\nControls: Key arrows to move!\n\nTo restart -> click restart, then start game."
    
    info_text = canvas.create_text(0.55*width,0.4*height,text=INFO,fill="black",font=("Ariel",20))
    
def restart_program():
    main_menu.destroy()
    Popen(['python3', 'platformer.py'])
    
def end_state(Type):
    global coins_got, level, canvas
    
    if Type == "dead":
        coins_got = 0
        level = 1
        death = Text(main_menu,height = 2, width = 15)
        DEATH = "You died! Play again?"
        death_text = canvas.create_text(0.499*width,0.4*height,text=DEATH,fill="black",font=("Ariel",20))
        
    elif Type == "win":
        coins_got = 0
        level = 1
        win = Text(main_menu,height = 2, width = 20)
        WIN = "Congratulations, you won! Play again?"
        win_text = canvas.create_text(0.499*width,0.4*height,text=WIN,fill="black",font=("Ariel",20))
        
def QUIT():
    global Quit, main_menu_running, main_menu
    
    Quit = True
    main_menu_running = False
    main_menu.destroy()

def start_game(level,Level_map,position_player):
    global play, main_menu_running, Level_1_map, Level_2_map, Level_3_map, coins_got
    coins_got = 0
    play = True
    main_menu_running = False
    main_menu.destroy()
    setup()
    level_generator(level,Level_map,position_player)
    collisions(Level_map)
    Game_loop()

def wave():
    global Move, speed, letters, title_line
    bounds = [100,170]
    for letter in letters:
        canvas.move(letter,0,Move)
    canvas.move(title_line,0,Move)

    coords = canvas.coords(letters[0])
    
    if coords[1] <= bounds[0] or coords[1] >= bounds[1]:
        Move *= -1

    main_menu.after(10,wave)
    
def Main_Menu(dead,Win):
    global main_menu, main_menu_running, level, state, canvas, title, title_line, letters, Move

    pygame.mixer.init()
    pygame.mixer.music.load(resource_path("Main_menu_music.mp3"))
    pygame.mixer.music.play(-1)
    
    main_menu = tkinter.Tk()
    main_menu_running = True
    main_menu.geometry("1500x1500")
    main_menu.title("Platformer")
    main_menu.wm_attributes('-alpha',0.5)
    main_menu.wait_visibility(main_menu)
    background = Image.open(resource_path("Main_menu.png"))
    background = background.resize((1500,1500))
    background = ImageTk.PhotoImage(background)
    canvas = Canvas(main_menu, width = 1500, height = 1500)
    canvas.pack(fill = "both", expand = True)
    canvas.create_image(0,0,image = background, anchor = "nw")
    TITLE = "Platformer"
    colors = ["red","blue","green","yellow","orange"]
    T_x = width/2
    T_y = height/15
    letter_spacing = 75
    text_width = len(TITLE)*letter_spacing
    current_x = T_x - text_width/2
    letters = []
    for i, letter in enumerate(TITLE):
        color = colors[i%len(colors)]
        letter_object = canvas.create_text(current_x,T_y,text=letter,fill=color,font=("Ariel",75))
        letters.append(letter_object)
        current_x += letter_spacing
    x1 = width/5
    y1 = height/10
    x2 = 3*width/4
    y2 = height/10
    title_line  = canvas.create_line(x1, y1, x2, y2, fill="black", width=5)

    quit_button = Button(canvas,text="Quit",command=QUIT)
    quit_button.place(x=1410701*width/3000000,y=4*height/15)
    quit_button.config(bg="red")
    restart_button = Button(canvas,text="Resart!",command=restart_program)
    restart_button.place(x=462667*width/1000000,y=7*height/30)
    restart_button.config(bg="blue")
    play_button = Button(canvas,text="Start Game!",command=lambda: start_game(1, Level_1_map, (0, 0)))
    play_button.place(x=452657*width/1000000,y=height/5)
    play_button.config(bg="green")
    info_button = Button(canvas,text="Info",command=info)
    info_button.place(x=47*width/100,y=349*height/2100)
    info_button.config(bg="yellow")
    
    if dead:
        pygame.mixer.Sound.play(death_sound)
        end_state("dead")

    if Win:
        pygame.mixer.Sound.play(win_sound)
        end_state("win")

    Move = 1
    main_menu.after(10,wave)
    main_menu.mainloop()

def setup():
    global screen, width, height, player, gravity, Level_1_map, Level_2_map, Level_3_map, x_char, y_char, enemy_x, enemy_y, enemy_speed, level, background_level_1, background_level_2, background_level_3, enemy

    pygame.init()
    screen = pygame.display.set_mode((width,height))

    pygame.display.set_caption("Platformer")
    pygame.init()
    font = pygame.font.Font(pygame.font.get_default_font(),30)

    background_level_1 = pygame.image.load(resource_path("Level_1.png"))
    background_level_1 = pygame.transform.scale(background_level_1,(width,height))
    background_level_2 = pygame.image.load(resource_path("Level_2.png"))
    background_level_2 = pygame.transform.scale(background_level_2,(width,height))
    background_level_3 = pygame.image.load(resource_path("Level_3.png"))
    background_level_3 = pygame.transform.scale(background_level_3,(width,height))

    tile = pygame.image.load(resource_path("Platform.png"))
    tile = pygame.transform.scale(tile,(250,15))

    Exit_image = pygame.image.load(resource_path("exit.png"))
    Exit_image = pygame.transform.scale(Exit_image,(75,75))

    enemy1 = pygame.image.load(resource_path("Enemy1.png"))
    enemy1 = pygame.transform.scale(enemy1,(75,75))

    enemy_frames_R.append(enemy1)

    enemy1 = pygame.transform.flip(enemy1,True,False)

    enemy_frames_L.append(enemy1)

    enemy2 = pygame.image.load(resource_path("Enemy2.png"))
    enemy2 = pygame.transform.scale(enemy2,(75,75))

    enemy_frames_R.append(enemy2)

    enemy2 = pygame.transform.flip(enemy2,True,False)

    enemy_frames_L.append(enemy2)
    
    gravity = 3
    coins_got = 0

    x_char = 0
    y_char = 0

    enemy_speed = 5
    switch = False
    coin_generate = True
    in_air = False

    coin = pygame.image.load(resource_path("coin.png"))
    coin = pygame.transform.scale(coin,(15,15))
    
    Level_text = font.render("Level: "+str(level),False,(0,0,0))

    tile_rects = []
    coin_rects = []
    enemy_rects = []
    exit_rect = []

    EXIT = False

    tile_width = 100
    
def level_generator(level,Level_map,position_player):
    global x_char, y_char, background_level_1, background_level_2, background_level_3, enemy_x, enemy_y
    
    coin = pygame.image.load(resource_path("coin.png"))
    coin = pygame.transform.scale(coin,(50,50))
    tile = pygame.image.load(resource_path("Platform.png"))
    tile = pygame.transform.scale(tile,(250,15))

    player1 = pygame.image.load(resource_path("Character1.png"))
    player1 = pygame.transform.scale(player1,(75,75))

    player2 = pygame.image.load(resource_path("Character2.png"))
    player2 = pygame.transform.scale(player2,(75,75))

    x_char, y_char = position_player
        
    font = pygame.font.Font(pygame.font.get_default_font(),30)
    tile_width = 100
    
    if level == 1:
        screen.blit(background_level_1,(0,0))
        Level_text = font.render("Level: "+str(level),False,(0,0,0))
        screen.blit(Level_text,(0,0))
        
    if level == 2:
        screen.blit(background_level_2,(0,0))
        Level_text = font.render("Level: "+str(level),False,(0,0,0))
        screen.blit(Level_text,(0,0))
        
    if level == 3:
        screen.blit(background_level_3,(0,0))
        Level_text = font.render("Level: "+str(level),False,(0,0,0))
        screen.blit(Level_text,(0,0))
        
    for x in range(len(Level_map)):
        for y in range(len(Level_map[x])):
            value = Level_map[x][y]
            position = (y*tile_width, x*tile_width)
            if value == 1:
                screen.blit(tile,position)
            elif value == 2:
                screen.blit(coin,position)
            elif value == 3:
                enemy_rect = pygame.Rect(y * tile_width + 75, x * tile_width, 75, 75)
                enemies.append(enemy_rect)
                
def collisions(level_map):
    global EXIT, Next_Level, coins_got, x_char, y_char, coins_got, Coin_text, Exit, Exit_image, enemy_x, enemy_y, enemy_speed, switch, level, play, main_menu_running, running, state, dead, Win, enemy_rect, play_door_sound

    player_rect = pygame.Rect(x_char, y_char, 75, 75)
    exit_rect = pygame.Rect(0,12*height/125,75,75)
    
    Next_Level = False
    transition = False
    tile_width = 100
    player_rect = pygame.Rect(x_char,y_char,75,75)
    Exit_image = pygame.image.load(resource_path("exit.png"))
    Exit_image = pygame.transform.scale(Exit_image,(75,75))
    
    font = pygame.font.Font(pygame.font.get_default_font(),30)
    Level_text = font.render("Level: "+str(level),False,(0,0,0))
    Coin_text = font.render("Coins: "+str(coins_got),False,(0,0,0))

    screen.blit(Coin_text,(0.9*width,0))
    
    for x in range(len(level_map)):
        for y in range(len(level_map[x])):
            value = level_map[x][y]
            if value == 1:
                tile_rect = pygame.Rect(y*tile_width, x*tile_width,250,15)
                if pygame.Rect.colliderect(player_rect,tile_rect):
                    y_char = x*tile_width - 75
                    
            if value == 2:
                coin_rect = pygame.Rect(y*tile_width, x*tile_width,50,50)
                if pygame.Rect.colliderect(player_rect,coin_rect):
                    pygame.mixer.Sound.play(coin_sound)
                    coins_got += 1
                    coin_rect = pygame.Rect(-y*tile_width, -x*tile_width,15,15)
                    level_map[x][y] = 0
                    if (level == 1 and coins_got == 5) or (level == 2 and coins_got == 5) or (level == 3 and coins_got == 5):
                        EXIT = True
                        play_door_sound = True
                        
            if value == 3:
                enemy_rect = pygame.Rect(y*tile_width+75, x*tile_width,75,75)

    if y_char >= 0.6*height:
        pygame.quit()
        play = False
        main_menu_running = True
        dead = True
        win = False
        Main_Menu(dead,win)
        
    if coins_got == 5 and EXIT:
        if play_door_sound:
            pygame.mixer.Sound.play(unlock_door_sound)
            play_door_sound = False
        if level == 1:
            screen.blit(Exit_image,(0,12*height/125))
            exit_rect = pygame.Rect(0,12*height/125,75,75)
        elif level == 2:
            screen.blit(Exit_image,(0,0.55*height))
            exit_rect = pygame.Rect(0,0.55*height,75,75)
        elif level == 3:
            screen.blit(Exit_image,(0,11*height/20))
            exit_rect = pygame.Rect(0,11*height/20,75,75)
        if level == 3 and pygame.Rect.colliderect(player_rect,exit_rect):
            pygame.quit()
            play = False
            main_menu_running = True
            dead = False
            Win = True
            Main_Menu(dead, Win)         
            
        if pygame.Rect.colliderect(player_rect,exit_rect) and level != 3:
            Next_Level = True
            level += 1
            coins_got = 0
            Coin_text = font.render("Coins: " + str(coins_got), False, (0, 0, 0))
            screen.blit(Coin_text,(0.9*width,0))
            Exit = False
            
def Game_loop():
    global running, x_char, y_char, level, enemy1, enemy2, enemy_x, enemy_y, player_rect, enemy_rect1, enemy_rect2, enemy_rect3, facing_right
    
    running = True
    player_facing_right = False
    t = 0
    
    font = pygame.font.Font(pygame.font.get_default_font(),30)
    clock = pygame.time.Clock()

    while running:
        screen.fill((255, 255, 255))  

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and x_char > 0:
            x_char -= 10
            player_facing_right = False
            
        if keys[pygame.K_RIGHT] and x_char < width:
            x_char += 10
            player_facing_right = True
            
        if keys[pygame.K_UP] and y_char > 0:
            y_char -= 10
            
        y_char += gravity
            
        current_map = Level_1_map if level == 1 else Level_2_map if level == 2 else Level_3_map
        level_generator(level, current_map, (x_char, y_char))
        collisions(current_map)
        
        if level == 1:
            if facing_right and enemy_x <= 0.65*width:
                enemy_speed = 2
                enemy_x += enemy_speed

            elif facing_right and enemy_x > 0.65*width:
                enemy_speed = -2
                enemy_x += enemy_speed
                facing_right = False
                
            if not facing_right and enemy_x >= 0.45*width:
                enemy_speed = -2
                enemy_x += enemy_speed
                
            elif not facing_right and enemy_x <= 0.45*width:
                enemy_speed = -2
                enemy_x += enemy_speed
                facing_right = True
                
            enemy_rect1 = pygame.Rect(enemy_x,enemy_y,75,75)

            index_enemyR = int((t*0.5)%len(enemy_frames_R))
            index_enemyL = int((t*0.5)%len(enemy_frames_L))

            if not facing_right:
                screen.blit(enemy_frames_R[index_enemyR],(enemy_x,enemy_y))
            elif facing_right:
                screen.blit(enemy_frames_L[index_enemyL],(enemy_x,enemy_y))
            
            player_rect = pygame.Rect(x_char, y_char, 75, 75)

            indexplayer_R = int((t*0.5)%len(player_frames_R))
            indexplayer_L = int((t*0.5)%len(player_frames_L))

            t += 1
            
            if not player_facing_right:
                screen.blit(player_frames_R[indexplayer_R],(x_char,y_char))
            elif player_facing_right:
                screen.blit(player_frames_L[indexplayer_L],(x_char,y_char))
            
            if pygame.Rect.colliderect(player_rect,enemy_rect1) or y_char >= 0.6*height:
                pygame.quit()
                play = False
                main_menu_running = True
                dead = True
                Win = False
                Main_Menu(dead, Win)

        if level == 2:
            if facing_right and enemy_x <= 0.85*width:
                enemy_speed = 4
                enemy_x += enemy_speed

            elif facing_right and enemy_x > 0.85*width:
                enemy_speed = -4
                enemy_x += enemy_speed
                facing_right = False
                
            if not facing_right and enemy_x >= 0.25*width:
                enemy_speed = -4
                enemy_x += enemy_speed
                
            elif not facing_right and enemy_x <= 0.25*width:
                enemy_speed = -4
                enemy_x += enemy_speed
                facing_right = True

            enemy_rect1 = pygame.Rect(enemy_x,0.54*enemy_y,75,75)
            enemy_rect2 = pygame.Rect(enemy_x,enemy_y,75,75)

            index_enemyR = int((t*0.5)%len(enemy_frames_R))
            index_enemyL = int((t*0.5)%len(enemy_frames_L))

            if not facing_right:
                screen.blit(enemy_frames_R[index_enemyR],(enemy_x,0.54*enemy_y))
                screen.blit(enemy_frames_R[index_enemyR],(enemy_x,enemy_y))
            elif facing_right:
                screen.blit(enemy_frames_L[index_enemyL],(enemy_x,0.54*enemy_y))
                screen.blit(enemy_frames_L[index_enemyL],(enemy_x,enemy_y))

            t += 1
        
            player_rect = pygame.Rect(x_char, y_char, 75, 75)

            indexplayer_R = int((t*0.5)%len(player_frames_R))
            indexplayer_L = int((t*0.5)%len(player_frames_L))

            if not player_facing_right:
                screen.blit(player_frames_R[indexplayer_R],(x_char,y_char))
            elif player_facing_right:
                screen.blit(player_frames_L[indexplayer_L],(x_char,y_char))

                
            if pygame.Rect.colliderect(player_rect,enemy_rect1) or pygame.Rect.colliderect(player_rect,enemy_rect2) or y_char >= 0.6*height:
                pygame.quit()
                play = False
                main_menu_running = True
                dead = True
                Win = False
                Main_Menu(dead, Win)       
            
        if level == 3:
            if facing_right and enemy_x <= 0.85*width:
                enemy_speed = 6
                enemy_x += enemy_speed

            elif facing_right and enemy_x > 0.85*width:
                enemy_speed = -6
                enemy_x += enemy_speed
                facing_right = False
                
            if not facing_right and enemy_x >= 0.25*width:
                enemy_speed = -6
                enemy_x += enemy_speed
                
            elif not facing_right and enemy_x <= 0.25*width:
                enemy_speed = -6
                enemy_x += enemy_speed
                facing_right = True
                
            enemy_rect1 = pygame.Rect(0.6*enemy_x,0.54*enemy_y,75,75)
            enemy_rect2 = pygame.Rect(0.1*enemy_x,1.4*enemy_y,75,75)
            enemy_rect3 = pygame.Rect(enemy_x,0.9*enemy_y,75,75)
            
            index_enemy_R = int((t*0.5)%len(enemy_frames_R))
            index_enemy_L = int((t*0.5)%len(enemy_frames_L))

            if not facing_right:
                screen.blit(enemy_frames_R[index_enemy_R],(0.6*enemy_x,0.54*enemy_y))
                screen.blit(enemy_frames_R[index_enemy_R],(0.1*enemy_x,1.4*enemy_y))
                screen.blit(enemy_frames_R[index_enemy_R],(enemy_x,0.9*enemy_y))
                
            elif facing_right:
                screen.blit(enemy_frames_L[index_enemy_L],(0.6*enemy_x,0.54*enemy_y))

                screen.blit(enemy_frames_L[index_enemy_L],(0.1*enemy_x,1.4*enemy_y))
                screen.blit(enemy_frames_L[index_enemy_L],(enemy_x,0.9*enemy_y))
                
            t += 1

            player_rect = pygame.Rect(x_char, y_char, 75, 75)

            indexplayer_R = int((t*0.5)%len(player_frames_R))
            indexplayer_L = int((t*0.5)%len(player_frames_L))

            if not player_facing_right:
                screen.blit(player_frames_R[indexplayer_R],(x_char,y_char))
            elif player_facing_right:
                screen.blit(player_frames_L[indexplayer_L],(x_char,y_char))
        
            if pygame.Rect.colliderect(player_rect,enemy_rect1) or pygame.Rect.colliderect(player_rect,enemy_rect2) or pygame.Rect.colliderect(player_rect,enemy_rect3) or y_char >= 0.6*height:
                pygame.quit()
                play = False
                main_menu_running = True
                dead = True
                Win = False
                Main_Menu(dead, Win)       
        
        Level_text = font.render(f"Level: {level}", True, (0, 0, 0))
        Coin_text = font.render(f"Coins: {coins_got}", True, (0, 0, 0))

        pygame.display.update()
        clock.tick(60)

Main_Menu(dead, Win)
