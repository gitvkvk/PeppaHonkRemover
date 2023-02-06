import os
import math
from pydub import AudioSegment
import audioread

dataset_path = r"C:\Users\kvk19\Projects\PeppaHonkRemover\SampleCopy"
#json_path = r"C:\Users\kvk19\Projects\PeppaHonkRemover\ProcessedSamples.json"
#EXTRACTED_LENGTH = 0.027
EXTRACTED_LENGTH = 0.08


for i, (roots, dirs, files) in enumerate(os.walk(dataset_path)):
        if roots is not dataset_path:
            for file in files:
                print ("file = %s" % file)
                file_path = os.path.join(roots, file)
                print(file_path)
                sample_duration = audioread.audio_open(file_path)
                print(sample_duration.duration)
                num_divisions = sample_duration.duration / EXTRACTED_LENGTH
                num_divisions = math.floor(num_divisions)
                print(num_divisions)
                sound = AudioSegment.from_wav(file_path)
                print(type(sound))

                for i in range(num_divisions):
                    print(i)
                    #note i starts at 0
                    start_slice = 1000 * EXTRACTED_LENGTH * i
                    finish_slice = start_slice + 1000 * EXTRACTED_LENGTH

                    wavs = sound[start_slice:finish_slice]
                    #wavs = sound[:]
                    print(len(wavs))
                    wavs.export('{}pt{}'.format(i, file), format = "wav")

                    # if i > 6:
                    #     break

 