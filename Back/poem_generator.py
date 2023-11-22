from lyrics_processor import LyricsProcessor
import random

"""
    This class is in charge of generating our poems and saving them
    to the lyrics.txt file
"""
class PoemGenerator:
    def __init__(self):
        """ Initializer 
            Calls the lyric processor to obtain a word dictionary
            mapping word types, to all words of that type, who 
            themselves map to their frequencies in the lyrics.
            Also obtains sentence structures from lyrics and stores
            in dict mapping sentence structures to their frequencies.
        """
        processor = LyricsProcessor()
        self.words = processor.get_words()
        self.sentence_structs = processor.get_sentence_structs()
    
    def generate_poem(self):
        """ Method to generate and write a poem to the text db
        """
        self.sums = self.get_sums(self.words)
        poem = self.generate_poem_lines(self.words, self.sentence_structs)
        f = open("poems.txt", "a")
        f.write("Name: " + poem[0] + "\n")
        for line in poem:
            f.write(line + '\n')
        f.close()
        return poem

    def generate_poem_lines(self, words, structs, length=10):
        """ Method to generate a list of poem lines
            args:
                words (dict): containing mappings of word types to words
                structs (dict): containing structs to their frequency
                length (int): length of the poem
        """
        # start with picking a random sentence struct
        struct = self.pick_struct(structs)

        # convert struct to list
        order = struct.split(',')
        poem = []
        for i in range(length):
            poem.append(self.generate_line(order, words))
            # pick a new random struct
            struct = self.pick_struct(structs)
            order = struct.split(',')    

        return poem
        
    def generate_line(self, order, words):
        """ Method to generate a line of poetry
            args:
                order (list): the sentence structure to follow
                words (dict): of types of words to all words of that type
        """
        line = ""
        for type in order:
            word_choice = self.words[type]
            word = self.select_random(self.sums[type], word_choice)
            line += word + " "
        return line.strip()
             
        
    def get_sums(self, words):
        """ Returns dictionary containing word type to its sum of words used by Muse
            NOUN: 30, ADV: 10

            args:
                words (dict): of types of words to all words of that type
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
        """ Method to select random word from dictionary in certain range
            args:
                range (int): the ith item within the dictinary to select
                dictionary (dict): the dictionary to select from
        """
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
        """ Method to pick a sentence structure
            args:
                structs (dict): dict of structs mapping to their frequency
        """
        # sum the values up
        sum = 0
        for struct in structs.keys():
             sum += structs[struct]

        # pick a random number in the range of that sum
        return self.select_random(sum, structs)
    
    def rate_poem(self, rating):
        """ Method to add a rating to a poem in the txt file
            args:
                rating (int): the rating to leave
        """
        f = open("poems.txt", "a")
        f.write("User Rating: " + str(rating) + "\n\n")
        f.close()