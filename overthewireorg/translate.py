# Preprocess an input text:
#  - delete punctuation symbols (commas, periods, exclamation and question marks ,.!?),
#  - convert all symbols to lowercase.
# Then print your text.

string = input()
print(string.lower().translate({44: None, 46: None, 33: None, 63: None}))

# 'translate' changes characters according of theit ASCII code in dictionary, ({44: 46}) for example.
