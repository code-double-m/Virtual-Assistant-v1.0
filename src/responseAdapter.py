import os
from textSimilarityApproximator import TextSimilarityApproximator


class ResponseAdapter():
    def __init__(self):
        self.TSA = TextSimilarityApproximator()
        self.conversations = {}




    def loadCorpus(self, directory):
        raw_corpus = []
        corpus = []
        files = os.listdir(directory)
        for file in files:
            with open(directory + file, "r") as file_content:
                raw_corpus += file_content.readlines()
        for line in raw_corpus:
            corpus.append(line.rstrip('\r\n'))

        for index in range(len(corpus)):

            line = corpus[index]
            
            if line.startswith("*"):
                self.conversations[line[1:]] = corpus[index + 1][1:]


    
    def generateResponse(self, text):

        scores = []

        for query in self.conversations:
            scores.append((self.TSA.approximate(text, query), query))



        if max(scores)[0] > 75:
            
            response = self.conversations[max(scores)[1]]
            return response
        else:
            return "POOR_CONFIDENCE"
            



