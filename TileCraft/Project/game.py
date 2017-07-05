# import required modules here -- 'pygame' and 'sys' for now
try:
    import pygame, sys
    from pygame.locals import *
    from constants import SCREEN_SIZE
except ImportError as err:
    print("%s module failed to load" % str(err))
    
class Game:
    def __init__(self):
        # initialise the pygame module
        pygame.init()

        # create a new window drawing surface, width=300, height=300
        self.winsurf = pygame.display.set_mode(SCREEN_SIZE)

        # give the window a caption
        pygame.display.set_caption('TileCraft - A 2D Minecraft clone')

    def run(self):
        ''' Runs the game i.e. game loop, events, game logic etc. '''

        # create a bool to allow us to check if the player is still playing the game and hasn't quit
        isRunning = True

        while isRunning:
            ''' Define the main game loop - for now, we only want it to track user events -- only whether the player wishes to quit, for now. '''
            # handle pygame events - if user closes the game, stop running
            isRunning = self.event_handler()

            # update the display
            self.update()
        
        # close the game
        self.close()

    def event_handler(self):
        ''' Poll for pygame events and behave accordingly.  Return false to stop the event loop and end the game '''
        # get all the user events
        for event in pygame.event.get():
            # if the user wants to quit
            if event.type == QUIT:
                return False
            # handle user input
            elif event.type == KEYDOWN:
                # if the user presses escape, quit the event loop
                if event.key == K_ESCAPE:
                    return False
        return True

    def update(self):
        # update the display every frame
        pygame.display.flip()

    def close(self):
        # end the game and close the window
        pygame.quit()
        sys.exit()

    