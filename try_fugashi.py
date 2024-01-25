import fugashi


tagger = fugashi.Tagger()
text = open("episode1.txt", "r").read()
lemma_dict = {}
for word in tagger(text):
    lemma = word.feature.lemma

    if lemma in lemma_dict:
        lemma_dict[lemma] = lemma_dict[lemma] + 1
    else:
        lemma_dict[lemma] = 1
    # print(word.surface, word.feature.lemma, sep="\t")

# Use any translator you like, in this example GoogleTranslator

lemma_list = [(str(entry[0]) + '|' + str(entry[1])) for entry in sorted(lemma_dict.items(), key=lambda item: item[1], reverse=True)]
output = '\n'.join(lemma_list)
print(output)
open("output.txt", "w").write(output)