class Grader:
    """Compares the user's input with the sample text to check if the user typed the sample text successfully.
    It also points out where, in the text, the user made an error if an error exists."""
    def __init__(self):
        self.error_text = None
        self.relevant_computer_section = None

    def check_text(self, sample_text, user_text):
        sample_text = sample_text.replace('\n', '')
        for index in range(len(sample_text)):
            try:
                if sample_text[index] != user_text[index]:
                    if index < 15:
                        index = 15
                    self.error_text = user_text[index - 15: index + 15]
                    self.relevant_computer_section = sample_text[index - 15: index + 15]
                    return False
            except IndexError:
                index -= 1
                if index < 15:
                    index = 15
                self.error_text = user_text[index - 15: index + 15]
                self.relevant_computer_section = sample_text[index - 15: index + 15]
                return False
        return True
