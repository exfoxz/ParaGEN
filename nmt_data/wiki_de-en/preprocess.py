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
    with open(output_path, 'w', encoding="utf-8") as fout:
        fout.write(output)

def preprocess(original_path):
    output_en_de_train = ""
    output_en_de_val = ""
    output_de_en_train = ""
    output_de_en_val = ""
    count = 0
    with open(original_path, encoding="utf-8") as fin:
        text = fin.read()
        for line in text.split("\n"):
            tknzed_line =  " ".join(nltk.word_tokenize(line)) + '\n'
            count += 1
            if count <= s1:
                output_en_de_train += tknzed_line
            elif count <= s2:
                output_en_de_val += tknzed_line
            elif count <= s3:
                output_de_en_train += tknzed_line
            else:
                output_de_en_val += tknzed_line
            if count % 10000 == 0:
                print(count)
    output_file('en_de_train' + original_path[-3:], output_en_de_train)
    output_file('en_de_val' + original_path[-3:], output_en_de_val)
    output_file('de_en_train' + original_path[-3:], output_de_en_train)
    output_file('de_en_val' + original_path[-3:], output_de_en_val)

if sys.argv[1] == 'en':
    print('preprocessing en')
    preprocess(original_en)
elif sys.argv[1] == 'de':
    print('preprocessing de')
    preprocess(original_de)