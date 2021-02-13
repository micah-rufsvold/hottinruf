from pocketsphinx.pocketsphinx import *
from sphinxbase.sphinxbase import *

import os

#Intermediate\\EMN_Ep132.wav


def find_curses(file):
    #get audio file and keywords
    stream = os.path.join(path.dirname(path.realpath(__file__)), file)
    kw_file = os.path.join(path.dirname(path.realpath(__file__)), 'kw_files/curse.kwlist')

    #Configure decoder
    config = Decoder.default_config()
    MODELDIR = "../../tools/pocketsphinx/model"
    DATADIR = "../../tools/pocketsphinx/test/data"
    config.set_string('-hmm', os.path.join(MODELDIR, 'en-us/en-us'))
    config.set_string('-lm', os.path.join(MODELDIR, 'en-us/en-us.lm.bin'))
    config.set_string('-dict', os.path.join(MODELDIR, 'en-us/cmudict-en-us.dict'))
    decoder = Decoder(config)
    decorder.set_kws('kws', kw_file)
    decoder.set_search('kws')

    #not yet sure if these definitions are necessary.
    CHUNK = 1024  # CHUNKS of bytes to read each time from mic
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 16000
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
            decoder.end_utt()
            decoder.start_utt()


    





# Use this website as demo code
# http://blog.justsophie.com/python-speech-to-text-with-pocketsphinx/