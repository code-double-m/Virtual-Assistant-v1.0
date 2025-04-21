from fuzzywuzzy import fuzz

class TextSimilarityApproximator():
    def __init__(self):
        pass

    def approximate(self, text_1, text_2):
        ratio = fuzz.ratio(text_1, text_2)
        partial_ratio = fuzz.partial_ratio(text_1, text_2)
        token_set_ratio = fuzz.token_set_ratio(text_1, text_2)

        average_score = (ratio + partial_ratio + token_set_ratio) / 3

        return average_score



