from pydub import AudioSegment

startTime = (30) * 1000
endTime = (1*60) * 1000

from pydub.utils import which





song = AudioSegment.from_file("/home/dizziolica/Music/gens.mp3", format="mp3")
startTime = 80
endTime = 120
extract = song[startTime:endTime]


