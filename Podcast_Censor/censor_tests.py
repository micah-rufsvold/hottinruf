import unittest
import os
from os import listdir, path
from pathlib import Path


class TestCensor(unittest.TestCase):

    def test_get_inputs(self, dir = Path('Podcast_Censor\Test_Files\Test_Input'), f = 'audio_test.mp3'):
        from convert_to_wav import get_inputs
        inputs = get_inputs(dir)
        self.assertTrue(f in inputs)
    
    def test_mp3_to_wav(self, f = "audio_test.mp3"):
        from convert_to_wav import mp3_to_wav
        dest_dir = Path('Podcast_Censor/Test_Files/Test_Intermediate')
        in_file = Path('Podcast_Censor/Test_Files/Test_Input/') / f
        mp3_to_wav(in_file, dest_dir)
        f = dest_dir / (in_file.stem + '.wav')
        self.assertTrue(os.path.isfile(f))
        if os.path.exists(f):
            os.remove(f)

    def test_convert_files_to_wav(self):
        from convert_to_wav import convert_files_to_wav
        in_dir = 'Podcast_Censor\\Test_Files\\Test_Input'
        out_dir = 'Podcast_Censor\\Test_Files\\Test_Intermediate'
        convert_files_to_wav(in_dir,out_dir)
    
        inputs = [f[0:-4] + '.wav' for f in listdir(in_dir) if path.isfile(path.join(in_dir,f))]
        out = [f for f in listdir(out_dir) if path.isfile(path.join(out_dir,f))]
        self.assertEqual(inputs, out)
        for f in out:
            if os.path.exists(f):
                os.remove(f)



if __name__ == "__main__":
    unittest.main()