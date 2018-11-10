import tdl

#actual size of the window
#Special Numbers
SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50
LIMIT_FPS = 20 #20 frames-per-second maximum
playerx = SCREEN_WIDTH//2
playery = SCREEN_HEIGHT//2

#player movement 
def handle_keys():
    global playerx, playery
    
    #turn base mode
    user_input = tdl.event.key_wait()
    
    #realtime
# =============================================================================
#     keypress = False
#     for event in tdl.event.get():
#         if event.type == 'KEYDOWN':
#            user_input = event
#            keypress = True
#     if not keypress:
#         return
#     
# =============================================================================
    #extra functions
    if user_input.key == 'ENTER' and user_input.alt:
        #Alt+Enter: toggle fullscreen
        tdl.set_fullscreen(not tdl.get_fullscreen()) 
    elif user_input.key == 'ESCAPE':
        return True  #exit game
 
    #movement keys
    if user_input.key == 'UP':
        playery -= 1 
    elif user_input.key == 'DOWN':
        playery += 1 
    elif user_input.key == 'LEFT':
        playerx -= 1
    elif user_input.key == 'RIGHT':
        playerx += 1
        

#############################################
# Initialization & Main Loop                #
#############################################
     
#displays screen until it is manually closed by the player and is the main loop
               
tdl.set_font('arial10x10.png', greyscale=True, altLayout=True)
console = tdl.init(SCREEN_WIDTH, SCREEN_HEIGHT, title="Roguelike", fullscreen=False)
##tdl.setFPS(LIMIT_FPS)

while not tdl.event.is_window_closed():
    
    console.draw_char(1, 1, '@', bg=None, fg=(255,255,255))
    
    tdl.flush()
    
    console.draw_char(playerx, playery, ' ', bg=None)
    
    exit_game = handle_keys()
    if exit_game:
        break
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    