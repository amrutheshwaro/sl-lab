from operator import attrgetter

class Sentence:
    def __init__(self):
        self.sentence = input("Enter a sentence to be reversed word by word.\n")
        self.vowel_list = ['a', 'e', 'i', 'o', 'u']
        self.v_count = self.vowel_count()
        self.r_sentence = self.reverse_sentence()
    def vowel_count(self):
        return sum(x in self.vowel_list for x in self.sentence.lower())
    def reverse_sentence(self):
        return ' '.join(reversed(self.sentence.strip().split(' ')))

sentences = []

for i in range(3):
    sentences.append(Sentence())

sentences.sort(key=attrgetter("v_count"), reverse=True)
for i in range(3):
    print(sentences[i].r_sentence)