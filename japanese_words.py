import random
import sys
import romkan
import abc

from abc import ABC


# This isn't the "best" use of these patterns (e.g. I could avoid using the romkan library), but this is just to get practice with the Factory Pattern to refresh my memory.

# Strategy pattern. Probably not the best use of it here but it works.
#class HiraganaStrategy:

#class KatakanaStrategy:

# TODO: find a way to not hardcode this. e.g. some algorithm that appends just 't' to the beginning, except for 'chi' and 'tsu', etc.
ALL_KANA = ['a', 'i', 'u', 'e', 'o', 'ka', 'ki', 'ku', 'ke', 'ko', 'sa', 'shi', 'su', 'se', 'so', 'ta', 'chi', 'tsu', 'te', 'to', 'na', 'ni', 'nu', 'ne', 'no',
        'ha', 'hi', 'fu', 'he', 'ho', 'ma', 'mi', 'mu', 'me', 'mo', 'ra', 'ri', 'ru', 're', 'ro', 'ya', 'yu', 'yo', 'wa', 'wo', 'n']

# Product generated from Factory
class JapaneseWordGenerator:
	# WARNING: This implementation assumes letters are in the same order of the ALL_KANA list and there are exactly that many letters in the list.
	def __init__(self, letters):
		self.letters = letters

	def _get_list_restricted_to_index(self, last_kana):
		kana_index = ALL_KANA.index(last_kana)
		return self.letters[0:kana_index]

	# The main business logic here. It's so simple, it doesn't need to use strategy classes.
	def generate(self, num_letters, last_kana):
		letter_list = self._get_list_restricted_to_index(last_kana)
		final_word = ''
		for i in range(num_letters):
			letter = random.choice(letter_list)
			final_word += letter
		return final_word

# Factory Method class
class JapaneseWordGeneratorFactory(ABC):
	def __init__(self):
		pass

	@abc.abstractmethod
	def build_word_generator(self):
		# This is implemented by individual subclasses.
		return

# If you want practice translating random kana (in Roumaji) to Hiragana or Katakana
class RoumajiFactory(JapaneseWordGeneratorFactory):
	def build_word_generator(self):
                return JapaneseWordGenerator(ALL_KANA)

class HiraganaJapaneseWordGeneratorFactory(JapaneseWordGeneratorFactory):
	def build_word_generator(self):
		return JapaneseWordGenerator([romkan.to_hiragana(kana) for kana in ALL_KANA])

class KatakanaJapaneseWordGeneratorFactory(JapaneseWordGeneratorFactory):
        def build_word_generator(self):
                return JapaneseWordGenerator([romkan.to_katakana(kana) for kana in ALL_KANA])

def main():
	if len(sys.argv) != 5:
		raise ValueError('Usage: japanese_words.py <r/h/k> <up_to (the last kana in Roumaji)> <num_letters_per_word> <num_words>')

	args = sys.argv

	# We don't get to fully utilize the advantages of abstract factory interface types here, as Python uses duck typing.
	# So we will always deal with the concrete class objects, even though they will all also be objects of type JapaneseWordGeneratorFactory.
	factory = None
	if args[1] == 'r':
		factory = RoumajiFactory()
	elif args[1] == 'h':
		factory = HiraganaJapaneseWordGeneratorFactory()
	elif args[1] == 'k':
		factory = KatakanaJapaneseWordGeneratorFactory()
	else:
		raise ValueError

	word_gen = factory.build_word_generator()
	num_words = int(args[4])
	num_letters_per_word = int(args[3])
	up_to = args[2]

	for i in range(num_words):
		word = word_gen.generate(num_letters_per_word, up_to)
		print(word)

if __name__ == "__main__":
	main()
