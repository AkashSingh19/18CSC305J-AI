from nltk.tokenize import word_tokenize
quote = """If you wish to make an apple pie from scratch, you must first invent the
universe."""
words_in_quote = word_tokenize(quote)
import nltk
nltk.pos_tag(words_in_quote)