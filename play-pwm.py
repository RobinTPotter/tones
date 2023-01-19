import re 
import time
from machine import Pin, PWM

#with open("notes.txt","r") as f:
#    data = f.readlines()
#
#data = [[d.split()[0].split("/")[0].replace("#","s"), int(float(d.split()[1])) ] for d in data]

freqs = [['C4', 261], ['Cs4', 277], ['D4', 293], ['Ds4', 311], ['E4', 329], ['F4', 349], ['Fs4', 369], ['G4', 392], ['Gs4', 415], ['A4', 440], ['As4', 466], ['B4', 493], ['C5', 523], ['Cs5', 554], ['D5', 587], ['Ds5', 622], ['E5', 659], ['F5', 698], ['Fs5', 739], ['G5', 783], ['Gs5', 830], ['A5', 880], ['As5', 932], ['B5', 987], ['C6', 1046], ['Cs6', 1108], ['D6', 1174], ['Ds6', 1244], ['E6', 1318], ['F6', 1396], ['Fs6', 1479], ['G6', 1567], ['Gs6', 1661], ['A6', 1760], ['As6', 1864], ['B6', 1975], ['C7', 2093], ['Cs7', 2217], ['D7', 2349]]

notes = {f[0]:f[1] for f in freqs}

pwm = PWM(Pin(0, Pin.OUT))

def play(song="4O6GEG.Fs.Ds.E.DDD.CsCsCs.CCC.O5BeceB", beat=1, length=4, vol = 50):
    song = re.split("(\d{1,2}|V\d{1,2}|O\d|[A-Ga-g]s|[A-Ga-g])",song)
    song = [s for s in song if s is not ""]
    octave = 3
    for n in song:
        print(f"n {n}")
        if n[0]=="O":
            octave = int(n[1])
            continue
        if n[0]=="V":
            vol = int(n[1])
            continue
        if n.isnumeric():
            length=int(n)
            continue
        small = n[0].islower()
        sharp = 1 if len(n)==2 and n[1]=="s" else 0
        note = n[0].upper() + ("s" if sharp else "")
        #print(f"note {note}")
        if note!=".":
            ding = f"{note}{octave + (1 if small else 0)}"
            print(f"ding {ding}")
            pwm.freq(notes[ding])
			      pwm.duty_u16(int(32000.0 * vol / 100))
        
        time.sleep(beat/length)
        
        if note!=".":
			      pwm.duty_u16(0)


