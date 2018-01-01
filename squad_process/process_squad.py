# get vocab from squad dataset
import json
import nltk

def process_squad(load_f, output_path, output_path_input):
    load_dict = json.load(load_f)
    data = load_dict['data']
    fout = open(output_path, 'w', encoding='utf8')
    fout_input = open(output_path_input, 'w', encoding='utf8')
    i_cnt = 0
    for i in data:
        j_cnt = 0
        for j in i['paragraphs']:
            z_cnt = 0
            for z in j['qas']:
                sent = " ".join(nltk.word_tokenize(z['question']))
                fout_input.write(sent + '\n')
                fout.write(str(i_cnt) + '-' + str(j_cnt) + '\t' + sent + '\n')
                z_cnt = z_cnt + 1
            j_cnt = j_cnt + 1
        i_cnt = i_cnt + 1
    fout.close()
    load_f_train.close()

load_f_train = open("train-v1.1.json", 'r', encoding='utf8')
process_squad(load_f_train, output_path="squad_train.qtns", output_path_input = "squad_train.qtns.input")
