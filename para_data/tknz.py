import nltk
import sys
output = ""

print('processing', sys.argv[1])
with open(sys.argv[1], encoding="utf-8") as fin:
    text = fin.read()
    for line in text.split("\n"):
        output += " ".join(nltk.word_tokenize(line)) + '\n'
with open(sys.argv[1], 'w', encoding="utf-8") as fout:
    fout.write(output)
