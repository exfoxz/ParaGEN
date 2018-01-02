### Quora Question Pair Dataset  

#### preprocessing: 

> python preprocess.py -train_src para_data/quora/train.q1 -train_tgt para_data/quora/train.q2  -valid_src para_data/quora/val.q1 -valid_tgt para_data/quora/val.q2 -save_data data/para_quora -dynamic_dict -share_vocab

#### training:

> python train.py -data data/para_quora -save_model models/quora-model -copy_attn -global_attention mlp -word_vec_size 128 -rnn_size 256 -layers 1 -encoder_type brnn -epochs 16 -seed 777 -batch_size 256 -max_grad_norm 2 -share_embeddings -gpuid 1


#### paraphrasing:

> python translate.py -model models/quora-model_acc_xxx_ppl_yyy_e2.pt -src para_data/quora/test.q1 -output para_gen.txt  -beam_size 10 -replace_unk -verbose


### WikiAnswers Dataset
#### preprocessing:


> python preprocess.py -train_src para_data/wikianswers/train.q1 -train_tgt para_data/wikianswers/train.q2  -valid_src para_data/wikianswers/val.q1 -valid_tgt para_data/wikianswers/val.q2 -save_data data/para_wikianswers -dynamic_dict -share_vocab


#### training:


> python train.py -data data/para_wikianswers -save_model models/wikianswers-model -copy_attn -global_attention mlp -word_vec_size 128 -rnn_size 256 -layers 1 -encoder_type brnn -epochs 16 -seed 777 -batch_size 32 -max_grad_norm 2 -share_embeddings -gpuid 1


#### paraphrasing:
 
> python translate.py -model models/wikianswers-model_acc_xxx_ppl_yyy_e2.pt -src para_data/quora/test.q1 -output para_gen.txt  -beam_size 10 -replace_unk -verbose
 


### Paraphrasing the SQuAD training dataset

#### split
```
split -l 15000 squad_process/squad_train.qtns.input -d -a 1 squad_process/squad_train.qtns.input.split_ 

python translate.py -model models/quora-model_acc_66.37_ppl_5.94_e14.pt -src squad_process/squad_train.qtns.input.split_0 -output squad_process/squad_train.qtns.para.split_0  -beam_size 10 -replace_unk -share_vocab -verbose -batch_size 1 -gpu 0
python translate.py -model models/quora-model_acc_66.37_ppl_5.94_e14.pt -src squad_process/squad_train.qtns.input.split_1 -output squad_process/squad_train.qtns.para.split_1  -beam_size 10 -replace_unk -share_vocab -verbose -batch_size 1 -gpu 1
python translate.py -model models/quora-model_acc_66.37_ppl_5.94_e14.pt -src squad_process/squad_train.qtns.input.split_2 -output squad_process/squad_train.qtns.para.split_2  -beam_size 10 -replace_unk -share_vocab -verbose -batch_size 1 -gpu 2
python translate.py -model models/quora-model_acc_66.37_ppl_5.94_e14.pt -src squad_process/squad_train.qtns.input.split_3 -output squad_process/squad_train.qtns.para.split_3  -beam_size 10 -replace_unk -share_vocab -verbose -batch_size 1 -gpu 3
python translate.py -model models/quora-model_acc_66.37_ppl_5.94_e14.pt -src squad_process/squad_train.qtns.input.split_4 -output squad_process/squad_train.qtns.para.split_4  -beam_size 10 -replace_unk -share_vocab -verbose -batch_size 1 -gpu 4
python translate.py -model models/quora-model_acc_66.37_ppl_5.94_e14.pt -src squad_process/squad_train.qtns.input.split_5 -output squad_process/squad_train.qtns.para.split_5  -beam_size 10 -replace_unk -share_vocab -verbose -batch_size 1 -gpu 5

cat  squad_process/squad_train.qtns.para.split_0 squad_process/squad_train.qtns.para.split_1 squad_process/squad_train.qtns.para.split_2 squad_process/squad_train.qtns.para.split_3 squad_process/squad_train.qtns.para.split_4 squad_process/squad_train.qtns.para.split_5 > squad_process/squad_train.qtns.para
```

### Paraphrase via Bidirectional Translation 

#### Preprocessing Wikipedia Parallel Corpora
 
> wget http://opus.nlpl.eu/download.php?f=Wikipedia/de-en.txt.zip

This parallel corpora has 2,459,662 sentence pairs. 
We used fist half (1,229,381) for en-de and last half for de-en, each with 1,229,381 -> 1,220,000 for training, 9,381 for validation.
