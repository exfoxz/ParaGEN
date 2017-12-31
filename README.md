
preprocessing:

```
python preprocess.py -train_src para_data/quora/train.q1 -train_tgt para_data/quora/train.q2  -valid_src para_data/quora/val.q1 -valid_tgt para_data/quora/val.q2 -save_data data/para_quora -dynamic_dict -share_vocab
```

training:

```
python train.py -data data/para_quora -save_model quora-model -copy_attn -global_attention mlp -word_vec_size 128 -rnn_size 256 -layers 1 -encoder_type brnn -epochs 16 -seed 777 -batch_size 32 -max_grad_norm 2 -share_embeddings -gpuid 1
```

paraphrasing:


