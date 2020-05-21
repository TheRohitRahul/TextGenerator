import torch
import os

hidden_size = 300
n_layers = 1

DEVICE = "cpu"
if torch.cuda.is_available():
    DEVICE = "cuda"


print("working on : {}".format(DEVICE))

'''
Change these values for training
'''
model_name = ""
training_file_path = ""

'''
Change these values for inference
'''
num_words_to_generate = 15

'''
Don't touch this
'''

model_save_path = "./models/{}".format(model_name)

if not os.path.exists(model_save_path):
    os.makedirs(model_save_path)