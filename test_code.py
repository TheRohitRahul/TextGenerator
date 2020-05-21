import torch
import torch.nn as nn
import os
import pickle

from model import GruRnn
from config import DEVICE, n_layers, hidden_size, model_save_path, model_name, num_words_generate

def preprocess_words(list_words, word_to_num):
    for a_word in list_words:
        if a_word not in word_to_num.keys():
            print(a_word, "not present in vocab")
            exit()
    inputs = torch.tensor([[word_to_num[w] for w in list_words]], dtype=torch.long)

    return inputs    

def post_process_words(first_two_words, list_num_of_words, num_to_word):
    created_string = " ".join(first_two_words)
    for a_num in list_num_of_words:
        created_string = created_string + " " + num_to_word[a_num]

    return created_string

def run_model(inputs, voc_len, model_path):
    outputs = []
    decoder = GruRnn(voc_len, hidden_size, voc_len, n_layers).to(DEVICE)
    decoder.load_state_dict(torch.load(model_path))

    decoder.eval()
    hidden = decoder.init_hidden(1).cuda()
    for i in range(num_words_generate):
        output, hidden = decoder(inputs.cuda(), hidden)
        
        argmax = torch.argmax(output)
        outputs.append(argmax.item())
        inputs = torch.tensor([[inputs[0][1], inputs[0][2], inputs[0][3], inputs[0][4], argmax.item()]], dtype=torch.long)
    return outputs

def test_with_input(first_two_words, word_to_num, num_to_word, voc_len, model_path):
    inputs = preprocess_words(first_two_words, word_to_num)
    outputs = run_model(inputs, voc_len, model_path)
    processed_output  = post_process_words(first_two_words, outputs, num_to_word)
    print("\n-----------------------------\n")
    print(processed_output)
    print("\n-----------------------------\n")
if __name__ == "__main__":
    
    
    load_dict = {}
    with open(os.path.join(model_save_path, "preprocess_dict_word_num_rel_{}.pkl".format(model_name)), "rb") as f:
        load_dict = pickle.load(f)

    model_save_path = os.path.join(model_save_path, "epoch_30.pt")

    word_to_num = load_dict["word_to_num"]
    num_to_word = load_dict["num_to_word"]
    voc_len = load_dict["voc_len"]
    print(word_to_num.keys())
    first_two_words = input("Enter first 5 words : ")
    first_two_words = first_two_words.lower().split(" ")
    test_with_input(first_two_words, word_to_num, num_to_word, voc_len, model_save_path)
    print(voc_len)