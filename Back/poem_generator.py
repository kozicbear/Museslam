# class that will call lyric processor to construct db
# use its methods to generate a poem
from lyrics_processor import LyricsProcessor
import random

class PoemGenerator:
    def __init__(self):
        processor = LyricsProcessor()
        self.words = processor.get_words()
        self.sentence_structs = processor.get_sentence_structs()
        print(self.words)
        print(self.sentence_structs)

        self.generate_poem(self.words, self.sentence_structs)

    def generate_poem(self, words, structs):
        # start with picking a random sentence struct
        struct = self.pick_struct(structs)

        print("struct: ", struct)
        # and put random words in there

    def pick_struct(self, structs):
        # sum the values up
        sum = 0
        for struct in structs.keys():
             sum += structs[struct]

        # pick a random number in the range of that sum
        index = random.randint(0, sum)

        # iterate through keys
        for struct in structs.keys():
            if index == 0:
                return struct
            index -= structs[struct]
            if index < 0:
                 return struct

def main():
	PoemGenerator()

if __name__ == '__main__':
	main()