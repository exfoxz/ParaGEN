import nltk
import sys
output = ""

original_en = "Wikipedia.de-en.en"
original_de = "Wikipedia.de-en.de"

s1 =  1220000 # 0~1220000 for en-de training
s2 =  1229381 # 1220000~1229381 for en-de validation
s3 =  2449381 # 1229381~2449381 for de-en training
s4 =  2449381 # 1229381~2459662 for de-en validation


def output_file(output_path, output):
    print('start saving', output_path)
    with open(output_path, 'w', encoding="utf-8") as fout:
        fout.write(output)
    print('end saving', output_path)

def preprocess(original_path, lang = "english"):
    output_en_de_train = ""
    output_en_de_val = ""
    output_de_en_train = ""
    output_de_en_val = ""
    with open(original_path, encoding="utf-8") as fin:
        print('load corpus')
        text = fin.read()
        print('start tokenizing')
        tknzed = []
        for line in text.split('\n'):
            line = " ".join(nltk.word_tokenize(line, language=lang))
            tknzed.append(line+'\n')
            if len(tknzed) % 10000 == 0:
                print((len(tknzed)+0.0)/s4*100,'%')
        print('end tokenizing')

        print('start slicing')
        output_en_de_train = "\n".join(tknzed[0:s1])
        output_en_de_val = "\n".join(tknzed[s1:s2])
        output_de_en_train = "\n".join(tknzed[s2:s3])
        output_de_en_val = "\n".join(tknzed[s3:])
        print('end slicing')

    output_file('en_de_train' + original_path[-3:], output_en_de_train)
    output_file('en_de_val' + original_path[-3:], output_en_de_val)
    output_file('de_en_train' + original_path[-3:], output_de_en_train)
    output_file('de_en_val' + original_path[-3:], output_de_en_val)

if sys.argv[1] == 'en':
    print('preprocessing en')
    preprocess(original_en, lang="english")
elif sys.argv[1] == 'de':
    print('preprocessing de')
    preprocess(original_de, lang="german")
