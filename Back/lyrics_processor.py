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

        # IMPORTANT: Thinking of using a maxheap here to access maxes easier
        # We will want to construct the list first
        # and then heapify it after to save time

        # dictionary mapping nouns, verbs, etc to their own list of ints
        # which map to the frequency of a certain word
        # Noun -> 12: Woman, 10: Dog, 3: Car
        # Verb -> 3: run, 1: sit
        self.words = {}
        # list of sentence structures
        # 12: ['ADV', 'PRON', 'VERB']
        self.sentence_structs = []

    def process_lyrics(self, lyrics):
        nlp = spacy.load("en_core_web_sm")

        for line in lyrics:
            doc = nlp(line)

            sentence_struct = []
            for token in doc:
                print("text: ", token.text)
                print("pos: ", token.pos_)
                sentence_struct.append(token.pos_)

            self.sentence_structs.append()
            print(sentence_struct)
            return

def main():
    data = []
    with open("lyrics.txt") as lyrics:
        for line in lyrics:
            data.append(line.strip())
    scraper = LyricsProcessor()
    scraper.process_lyrics(data)

if __name__ == '__main__':
	main()