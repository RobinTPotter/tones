import time
import pygame
import os

print(pygame.init())
pygame.mixer.pre_init(frequency=11025, size=-8, channels=1)
print(pygame.mixer.init())

wavs = [w for w in os.listdir(".") if w.endswith("wav")]

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
    t = pygame.mixer.Sound(w) 
    print(f"loaded {w}")
    t.play()
    #time.sleep(2)
    wav[w[:-4]] = t
