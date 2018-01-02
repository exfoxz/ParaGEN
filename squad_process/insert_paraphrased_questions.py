import json
import nltk


para_list = []
# load original questions and their ids
with open("squad_train.qtns", encoding="utf8") as fin:
    for line in fin.readlines():
        ls = line.split('\t')
        key = ls[0]
        qtn = ls[1].strip()
        para_list.append([key, qtn, ""])

with open("squad_train.qtns.para", encoding="utf8") as fin:
    cur = 0
    for line in fin.readlines():
        para_list[cur][2] = line.strip()
        cur += 1
print(len(para_list))
para_dic = {}
for p in para_list:
    if p[1]!= p[2]:
        para_dic[p[0]] = (p[1], p[2])
print(len(para_dic))

with open("train-v1.1.json", 'r', encoding='utf8') as load_f:
    load_dict = json.load(load_f)

data = load_dict['data']
i_cnt = 0
for i in data:
    j_cnt = 0
    for j in i['paragraphs']:
        z_cnt = 0
        tmp_j_qas = j['qas'][:]
        for z in tmp_j_qas:
            key = str(i_cnt) + '-' + str(j_cnt) + '-' + str(z_cnt)
            if key in para_dic:
                # assert para_dic[key][0] == " ".join(nltk.word_tokenize(z['question']))
                new_z = z.copy()
                new_z['question'] = para_dic[key][1]
                # new_z['id'] = new_z['id'].reverse()
                j['qas'].append(new_z)
            z_cnt = z_cnt + 1
        j_cnt = j_cnt + 1
    i_cnt = i_cnt + 1
with open("train-v1.1.para_qtns.json", 'w', encoding='utf8') as save_f:
    text = json.dumps(load_dict)
    save_f.write(text)
