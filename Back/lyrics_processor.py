import spacy

"""
    Run these commands before using this class

    python -m venv .env
    source .env/bin/activate
    pip install -U pip setuptools wheel
    pip install -U spacy
"""
class LyricsProcessor:
    def __init__(self):
        # dictionary mapping nouns, verbs, etc to their own list of ints
        # which map to the frequency of a certain word
        # Noun -> Woman: 12, Dog: 10, Car: 3
        # Verb -> run: 3, sit: 1
        self.words = {}
        
        # dictionary of sentence structs and frequency
        # "NOUN,PRON,VERB" : 3
        # TODO: when it comes to picking sentence structs, we can sum
        # the total of sentecne structs, pick a random value and index
        # into that one
        # to adjust for more common or less common we can shift that
        # indexing either to front or back of list since more common
        # are at the front
        self.sentence_structs = {}

        data = []
        with open("lyrics.txt") as lyrics:
            for line in lyrics:
                data.append(line.strip())
        self.process_sentence_structs(data)
        self.process_word_choice(data)

    def get_words(self):
        return self.words
    
    def get_sentence_structs(self):
        return self.sentence_structs

    def process_sentence_structs(self, lyrics):
        nlp = spacy.load("en_core_web_sm")
        for line in lyrics:
            doc = nlp(line)

            sentence_struct = ""
            for token in doc:
                sentence_struct += str(token.pos_) + ","
            sentence_struct = sentence_struct[:-1]
            if sentence_struct in self.sentence_structs.keys():
                self.sentence_structs[sentence_struct] += 1
            else:
                self.sentence_structs[sentence_struct] = 1
        
        # sort dictionary
        self.sentence_structs = sorted(
            self.sentence_structs.items(), key=lambda x:x[1], reverse=True)
        self.sentence_structs = dict(self.sentence_structs)
    
    def process_word_choice(self, lyrics):
        nlp = spacy.load("en_core_web_sm")
        for line in lyrics:
            doc = nlp(line)

            sentence_struct = ""
            for token in doc:
                type = token.pos_
                text = token.text
                # if type there add to it
                if type in self.words.keys():
                    # TODO: might want to insert some capitalization checks here
                    if text in self.words[type].keys():
                        self.words[type][text] += 1
                    else:
                        self.words[type][text] = 1
                # if type not there add it
                else:
                    self.words[type] = {text: 1}
    
        # sort dictionaries
        for gram in self.words.keys():
            sorted_gram = sorted(
                self.words[gram].items(), key=lambda x:x[1], reverse=True)
            self.words[gram] = dict(sorted_gram)