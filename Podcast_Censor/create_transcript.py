from pocketsphinx.pocketsphinx import *
from sphinxbase.sphinxbase import *
from pathlib import Path
import os
import pyaudio

#Intermediate\\EMN_Ep132.wav
def create_decoder():
    config = Decoder.default_config()
    home_dir = Path.home()
    MODELDIR = home_dir / "Anaconda3/Lib/site-packages/pocketsphinx/model"
    DATADIR = "../../tools/pocketsphinx/test/data"
    kw_file = str(Path(os.path.dirname(os.path.realpath(__file__))) / 'kw_files/curses.list')
    config.set_string('-hmm', str(MODELDIR / 'en-us'))
    config.set_string('-lm', str(MODELDIR / 'en-us.lm.bin'))
    config.set_string('-dict', str(MODELDIR / 'cmudict-en-us.dict'))
    #config.set_string('-kws', str(kw_file))
    decoder = Decoder(config)
    decoder.set_kws('keywords', kw_file)
    decoder.set_search('keywords')
    return decoder
    
def find_curses(file):
    #get audio file and keywords
    decoder = create_decoder()
    stream = open(Path(os.path.dirname(os.path.realpath(__file__))) / file, 'rb')
    

    #not yet sure if these definitions are necessary.
    CHUNK = 1024  # CHUNKS of bytes to read each time from mic
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 16000
    word_catch = []
    decoder.start_utt()
    while True:
        buf = stream.read(1024)
        if buf:
            decoder.process_raw(buf, False, False)
        else:
            break
        if decoder.hyp() != None:
            print ([(seg.word, seg.prob, seg.start_frame, seg.end_frame) for seg in decoder.seg()])
            print ("Detected curse, restarting search")
            [word_catch.append([seg.word, seg.start_frame]) for seg in decoder.seg()]
            decoder.end_utt()
            decoder.start_utt()
    print(word_catch)


file = "Intermediate/EMN_Ep132.wav"

find_curses(file)

# Use this website as demo code
#http://blog.justsophie.com/python-speech-to-text-with-pocketsphinx/
