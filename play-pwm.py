import re 
import time
from machine import Pin, PWM
from random import random


#with open("notes.txt","r") as f:
#    data = f.readlines()
#
#data = [[d.split()[0].split("/")[0].replace("#","s"), int(float(d.split()[1])) ] for d in data]


class PWMPLayer():
    def __init__(self, pin_num=0, freq_offset=0, freq_mult=1.0, transpose=0, freq_random_mult=0, duty_mult=1.0, duty_offset=0):
        self.pwm = PWM(Pin(pin_num, Pin.OUT))
        self.freq_offset = freq_offset
        self.freq_mult = freq_mult
        self.transpose = transpose
        self.freq_random_mult = freq_random_mult
    def duty_u16(self, duty):
        self.pwm.duty_u16(int(duty * self.duty_mult + self.duty_offset))
    def freq(self, freq):
        self.pwm.freq(int(
            (freq * 2**(1/12) * self.transpose ) * self.freq_mult
            + self.freq_offset
            + random()*self.freq_random_mult
        ))

pattern = re.compile("(\d\d|\d|V\d\d|V\d|O\d|[A-Ga-g]s|[A-Ga-g]|\.)", "g")
freqs = [['C4', 261], ['Cs4', 277], ['D4', 293], ['Ds4', 311], ['E4', 329], ['F4', 349], ['Fs4', 369], ['G4', 392],
     ['Gs4', 415], ['A4', 440], ['As4', 466], ['B4', 493], ['C5', 523], ['Cs5', 554], ['D5', 587], ['Ds5', 622],
     ['E5', 659], ['F5', 698], ['Fs5', 739], ['G5', 783], ['Gs5', 830], ['A5', 880], ['As5', 932], ['B5', 987],
     ['C6', 1044], ['Cs6', 1108], ['D6', 1174], ['Ds6', 1244], ['E6', 1318], ['F6', 1396], ['Fs6', 1479], ['G6', 1567],
     ['Gs6', 1661], ['A6', 1760], ['As6', 1864], ['B6', 1975], ['C7', 2093], ['Cs7', 2217], ['D7', 2349]]

#_notes = {f[0]: {"freq":f[1], "id": f[2]} for f in [xx[0]+[xx[1]] for xx in list(zip(freqs,range(len(freqs))))]}
notes = {f[0]:f[1] for f in freqs}


def play(pwms, song="V994O6GEG.Fs.V30Ds.E.V99DDD.V22CsCsCs.CCC.V99O5BeceB", beat=1, length=4, vol = 99):
    # case sensistive song string
    # V0-99 volume
    # O1-N octave
    # . rest
    # s - sharp
    # n / N note and note + octave
    # 1-TT time divisor
    # beat = length in seconds of beat (default 1 second)
    # length = current time divisor (default 4)
    # vol = volume (related to duty cycle) (default 99)
    if isinstance(pwms, PWMPLayer): pwms = [pwms]
    octave = 3
    while len(song)>0:
        match = pattern.search(song) # no re.split in micropython
        n = match.group(1)
        song = song[match.end():]
        print(f"n {n}")
        if n[0]=="O":
            octave = int(n[1])
            continue
        if n[0]=="V":
            vol = int(n[1])
            continue
        if n.isdigit(): #no isnumeric in micropython
            length=int(n)
            continue
        small = n[0].islower()
        sharp = 1 if len(n)==2 and n[1]=="s" else 0
        note = n[0].upper() + ("s" if sharp else "")
        #print(f"note {note}")
        if note!=".":
            ding = f"{note}{octave + (1 if small else 0)}"
            print(f"ding {ding}")
            for pwm in pwms:
                pwm.duty_u16(int(32000.0 * vol / 100))
                pwm.freq(notes[ding])
        
        time.sleep(beat/length)
        
        if note!=".":
            for pwm in pwms:
                pwm.duty_u16(0)


play()
