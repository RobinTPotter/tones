import time
import re
import load 

def play(song="O6GEG.Fs.Ds.E.DDD.CsCsCs.CCC.O5BeceB", beat=0.5):
    song = re.split("(O\d|[A-Ga-g]s|[A-Ga-g])",song)
    song = [s for s in song if s is not ""]
    octave = 3
    for n in song:
        print(f"n {n}")
        if n[0]=="O":
            octave = int(n[1])
            continue
        small = n[0].islower()
        sharp = 1 if len(n)==2 and n[1]=="s" else 0
        note = n[0].upper() + ("s" if sharp else "")
        #print(f"note {note}")
        if note!=".":
            ding = f"{note}{octave + (1 if small else 0)}"
            #print(f"ding {ding}")
            load.wav[ding].play()
        time.sleep(beat)


