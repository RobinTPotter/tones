import time
import pygame
import os

DIR = "wavs"

pygame.init()
pygame.mixer.pre_init(frequency=11025, size=-8, channels=1)
pygame.mixer.init()
pygame.mixer.set_num_channels(100)

wavs = [w for w in os.listdir(DIR) if w.endswith("wav")]

print(f"files found {wavs}")

order = "C D EF G A B"
order = list(order)
neworder = []
for o in order:
    if o==" ": o = lasto+"s"
    neworder.append(o)
    lasto = o

order = neworder

wavs.sort(key=lambda val: 1 if "s" in val else 0)
wavs.sort(key=lambda val: order.index(val[0]))
wavs.sort(key=lambda val: int(val[-5:-4]))

print(f"loading {len(wavs)} sounds to dict wav")

wav = {}
for w in wavs:
    t = pygame.mixer.Sound(DIR+"/"+w) 
    print(f"loaded {w}")
    t.play()
    #time.sleep(2)
    wav[w[:-4]] = t
