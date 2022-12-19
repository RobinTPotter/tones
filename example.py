import pygame
import threading
import play

t1 = threading.Thread(None,play.play, kwargs={"beat":0.3})
t2 = threading.Thread(None,play.play, kwargs={"song":"O5BGB.A.Fs.G.GsGsGs.GGG.FsFsFs.EGEAE.", "beat":0.3})

t1.start();t2.start()
