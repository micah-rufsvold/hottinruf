from os import path, listdir
from pydub import AudioSegment

#get mp3 files from input
def get_inputs(dir):
    audio_files = [f for f in listdir(dir) if path.isfile(path.join(dir,f))]
    return audio_files

def mp3_to_wav(file, dest_dir):
    sound = AudioSegment.from_mp3(file)
    sound = sound.set_frame_rate(16000)
    sound = sound.set_channels(1)
    f = file.split('\\')
    name = f[-1][0:-4] + '.wav'
    dst = path.join(dest_dir,name)
    sound.export(dst, format="wav")


def convert_files_to_wav(input_dir = "Podcast_Censor\\Input", int_dir = "Podcast_Censor\\Intermediate"):
    fs = get_inputs(input_dir)
    
    for f in fs:
        mp3_to_wav(input_dir+"\\"+f, int_dir)
