import threading
import play
import time 

time.sleep(1)

t1 = threading.Thread(None,play.play, kwargs={"beat":1})
t2 = threading.Thread(None,play.play, kwargs={"song":"4O5BGB.A.Fs.G.GsGsGs.GGG.FsFsFs.EGEAE.", "beat":1})

t1.start();t2.start()
