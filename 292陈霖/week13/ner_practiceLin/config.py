# -*- coding: utf-8 -*-

"""
配置参数信息
"""

Config = {
    "model_path": "model_output",
    "schema_path": "ner_data/schema.json",
    "train_data_path": "ner_data/train",
    "valid_data_path": "ner_data/test",
    "vocab_path":"chars.txt",
    "max_length": 20,
    "hidden_size": 128,
    "kernel_size": 3,
    "num_layers": 2,
    "epoch": 20,
    "batch_size": 16,
    "tuning_tactics":"lora_tuning",
    "pooling_style":"max",
    "optimizer": "adam",
    "learning_rate": 1e-3,
    "use_crf": True,
    "class_num": 9,
    "bert_path": r"F:\Desktop\work_space\pretrain_models\bert-base-chinese"
}