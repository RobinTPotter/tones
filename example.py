
import threading
import play
import pygame
pygame.mixer.set_num_channels(100)

t1 = threading.Thread(None,play.play, kwargs={"beat":0.2})
t2 = threading.Thread(None,play.play, kwargs={"song":"O5BGB.A.Fs.G.GsGsGs.GGG.FsFsFs.EGEAE.", "beat":0.2})

t1.start();t2.start()
