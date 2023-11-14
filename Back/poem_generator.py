# class that will call lyric processor to construct db
# use its methods to generate a poem
from lyrics_processor import LyricsProcessor

class PoemGenerator:
    def __init__(self):
        processor = LyricsProcessor()
        self.words = processor.get_words()
        self.sentence_structs = processor.get_sentence_structs()
        print(self.words)
        print(self.sentence_structs)
    
def main():
	PoemGenerator()

if __name__ == '__main__':
	main()