import pickle
import torch
import os

from sentence_parser import read_sentences, word_tokenizer
from word_converter import make_word_num_relation_file
from ngram_construction import construct_trigrams, construct_pentagram
from config import model_save_path, model_name

class TextLoader(object):
    def __init__(self, train_file_path):
        all_sentences = read_sentences(train_file_path)
        all_tokenized_sentences = word_tokenizer(all_sentences)
        
        self.word_to_num, self.num_to_word, self.voc_len = make_word_num_relation_file(all_tokenized_sentences)
        

        dict_to_save = {"word_to_num" : self.word_to_num, "num_to_word" : self.num_to_word, "voc_len" : self.voc_len}

        '''
        Saving it for inference
        '''
        with open(os.path.join(model_save_path, "preprocess_dict_word_num_rel_{}.pkl".format(model_name)), "wb") as f:
            pickle.dump(dict_to_save, f)

        
        self.all_trigrams = construct_pentagram(all_tokenized_sentences)

    def get_voc_len(self):
        return self.voc_len

    def __len__(self):
        return len(self.all_trigrams)

    def __getitem__(self, index):
        inp, tar = self.all_trigrams[index]
        tensor_inp = torch.tensor([self.word_to_num[w] for w in inp], dtype=torch.long)
        target = torch.tensor([self.word_to_num[tar]], dtype=torch.long)
        return tensor_inp, target

