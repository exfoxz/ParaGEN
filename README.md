
### Quora Dataset
preprocessing:

```
python preprocess.py -train_src para_data/quora/train.q1 -train_tgt para_data/quora/train.q2  -valid_src para_data/quora/val.q1 -valid_tgt para_data/quora/val.q2 -save_data data/para_quora -dynamic_dict -share_vocab
```

training:

```
python train.py -data data/para_quora -save_model models/quora-model -copy_attn -global_attention mlp -word_vec_size 128 -rnn_size 256 -layers 1 -encoder_type brnn -epochs 16 -seed 777 -batch_size 32 -max_grad_norm 2 -share_embeddings -gpuid 1
```

paraphrasing:

```
python translate.py -model models/quora-model_acc_xxx_ppl_yyy_e2.pt -src para_data/quora/test.q1 -output para_gen.txt  -beam_size 10 -replace_unk -verbose
```

### WikiAnswers Dataset
preprocessing:

```
python preprocess.py -train_src para_data/wikianswers/train.q1 -train_tgt para_data/wikianswers/train.q2  -valid_src para_data/wikianswers/val.q1 -valid_tgt para_data/wikianswers/val.q2 -save_data data/para_wikianswers -dynamic_dict -share_vocab
```

training:

```
python train.py -data data/para_wikianswers -save_model models/wikianswers-model -copy_attn -global_attention mlp -word_vec_size 128 -rnn_size 256 -layers 1 -encoder_type brnn -epochs 16 -seed 777 -batch_size 32 -max_grad_norm 2 -share_embeddings -gpuid 1
```

paraphrasing:

```
python translate.py -model models/wikianswers-model_acc_xxx_ppl_yyy_e2.pt -src para_data/quora/test.q1 -output para_gen.txt  -beam_size 10 -replace_unk -verbose
```
