
def cutMusic(start, end, path, formats):
    from pydub import AudioSegment

    from pydub.utils import which





    song = AudioSegment.from_file(path, format= formats)
    startTime = start
    endTime = end
    extract = song[startTime:endTime]


