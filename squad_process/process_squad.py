# get vocab from squad dataset
import json
import nltk

vocab = set()
def process_squad(load_f, output_path):
    global vocab
    load_dict = json.load(load_f)
    data = load_dict['data']
    fout = open(output_path, 'w', encoding='utf8')
    i_cnt = 0
    for i in data:
        j_cnt = 0
        for j in i['paragraphs']:
            vocab = vocab.union(set(nltk.word_tokenize(j['context'])))
            z_cnt = 0
            for z in j['qas']:
                # vocab = vocab.union(set(nltk.word_tokenize(z['question'])))
                if "input" in output_path:
                    fout.write(z['question'] + '\n')
                else:
                    fout.write(str(i_cnt) + '-' + str(j_cnt) + '\t' + z['question'] + '\n')
                z_cnt = z_cnt + 1
            j_cnt = j_cnt + 1
        i_cnt = i_cnt + 1
    fout.close()

load_f_train = open("train-v1.1.json", 'r', encoding='utf8')
# load_f_dev = open("dev-v1.1.json", 'r', encoding='utf8')

# process_squad(load_f_train, output_path="squad_train.qtns")
process_squad(load_f_train, output_path="squad_train.qtns.input")

# process_squad(load_f_dev, output_path="../tmp/para_data/squad_dev.qtns")

# def output(data, path):
#     with open(path, 'w', encoding='utf8') as f:
#         for d in data:
#             f.write(d+'\n')
# # output(vocab, '../tmp/para_data/vocab')