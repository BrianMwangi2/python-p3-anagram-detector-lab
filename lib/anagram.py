# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word
        self.sorted_word = sorted(word)

    def match(self, possible_anagrams):
        return [anagram for anagram in possible_anagrams if sorted(anagram) == self.sorted_word and anagram.lower()!= self.word.lower()]


listen = Anagram("listen")
print(listen.match(['enlists', 'google', 'inlets', 'banana']))  # => ['inlets']