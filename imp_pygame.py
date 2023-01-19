import pygame
pygame.init()
pygame.mixer.pre_init(frequency=11025, size=-8, channels=1)
pygame.mixer.init()
pygame.mixer.set_num_channels(100)

class sound():
    def __init__(self, wav):
        self.sound = pygame.mixer.Sound(wav) 
        print(f"loaded {wav}")
    def play(self):
        self.sound.play()
