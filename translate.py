from deep_translator import GoogleTranslator
translator = GoogleTranslator(source='ja', target='en')

lines = open("output.txt", "r").readlines()
wordlist = list()
for line in lines[:100]:
    split = line.split("|")
    lemma = split[0]
    count = split[1]
    english = translator.translate(lemma)
    together = f'{lemma}|{english}|{count}'
    wordlist += [together]
# print(wordlist)

open('with_english.txt', 'w').write(''.join(wordlist))