
import pyaudio
import wave

CHUNK = 1024

# instantiate PyAudio (1)
p = pyaudio.PyAudio()
# open stream (2)

def callback(in_data, frame_count, time_info, status):
    data = wf.readframes(frame_count)
    return (data, pyaudio.paContinue)


wf = wave.open(wav, 'rb')

stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(), 
                rate=wf.getframerate(), 
                output=True,
                stream_callback=callback)

stream.start_stream()

xy

# stop stream (4)
stream.stop_stream()
stream.close()
# close PyAudio (5)
p.terminate()
