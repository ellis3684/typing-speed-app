from sample_texts import list_of_texts
from random import choice


class Sampler:
    """Gets a random sample text (and its word count) from a list of sample texts."""
    def __init__(self):
        self.texts = []
        for text in list_of_texts:
            text_dict = {'text': text, 'length': len(text.split())}
            self.texts.append(text_dict)
        self.text = None
        self.length = None

    def set_random_text(self):
        random_text_and_length = choice(self.texts)
        self.text = random_text_and_length['text']
        self.length = random_text_and_length['length']

    def get_random_text(self):
        self.set_random_text()
        return self.text

    def get_random_text_length(self):
        return self.length
