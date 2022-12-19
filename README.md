# Tones

Tone generation commands in sox and more

# Requirements

pygame (python), sox

# Detailed instructions

- Edit and run gen.sh - uses the notes.txt file to generate sox commands
- review and run resulting run.sh script - uses sox commands to generate tone files
- python shell: import play; play.play() - plays the default demo tune in the play function

play module imports load which read the wav files and divines the correct order of the files based on the scale

# Fun

```
import threading
t1 = threading.Thread(None,play.play)
t2 = threading.Thread(None,play.play, args=["O4BGB.A.Fs.G.GsGsGs.GGG.FsFsFs.EGEAE."])
t1.start();t2.start()
```

_note_: possible limit of pygame, or raspi zero, new sounds not overriding current sounds play on pygame channel, so while fun, this example may not actually work properly, could try ```pygame.mixer.set_num_channels(36)```

