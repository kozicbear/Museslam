# class that will call lyric processor to construct db
# use its methods to generate a poem
from lyrics_processor import LyricsProcessor
import random

"""
    Run these commands before using this class

    python -m venv .env
    source .env/bin/activate
    pip install -U pip setuptools wheel
    pip install -U spacy
"""
class PoemGenerator:
    def __init__(self):
        # TODO: will want to name our poems as well
        processor = LyricsProcessor()
        self.words = processor.get_words()
        self.sentence_structs = processor.get_sentence_structs()
        # print(self.words)
        # print(self.sentence_structs)

        # Call helper method to help with generation
        self.sums = self.get_sums(self.words)

        self.poem = self.generate_poem(self.words, self.sentence_structs)

        # f = open("poems.txt", "a")
        # f.write("POEM: \n")
        # f.write(self.poem + '\n')
        # f.close()

    def generate_poem(self, words, structs, length=10):
        # start with picking a random sentence struct
        struct = self.pick_struct(structs)

        # convert struct to list
        order = struct.split(',')
        
        poem = []
        for i in range(length):
            poem.append(self.generate_line(order, words))
            # pick a new random struct
            # TODO: still looks like it picks the same struct for the entire poem
            struct = self.pick_struct(structs)

        return poem
        
        
    def generate_line(self, order, words):
        line = ""
        for type in order:
            word_choice = self.words[type]
            word = self.select_random(self.sums[type], word_choice)
            line += word + " "
        return line.strip()
             
        
    def get_sums(self, words):
        """
            Returns dictionary containing word type to its sum of words used by Muse
            NOUN: 30, ADV: 10
        """
        sums = {}
        for type in words:
            sum = 0
            word_choice = self.words[type]
            for word in word_choice:
                sum += word_choice[word]
            sums[type] = sum
        return sums

    def select_random(self, range, dictionary):
        # pick a random number in the range of that sum
        index = random.randint(0, range)

        # iterate through keys
        for key in dictionary.keys():
            if index == 0:
                return key
            index -= dictionary[key]
            if index <= 0:
                 return key

    def pick_struct(self, structs):
        # sum the values up
        sum = 0
        for struct in structs.keys():
             sum += structs[struct]

        # pick a random number in the range of that sum
        return self.select_random(sum, structs)
    
    def get_poem(self):
        return self.poem