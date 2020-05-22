import torch
import os

hidden_size = 300
n_layers = 1

'''
If it is taking way too much GPU then you would want to decrease this
'''
batch_size = 4096
n_epoch = 300

DEVICE = "cpu"
if torch.cuda.is_available():
    DEVICE = "cuda"


print("working on : {}".format(DEVICE))

'''
Change these values for training
'''
# you can put anything in model_name it is used to create folders only
model_name = ""
# txt file path which contains text for training
training_file_path = ""

'''
Change these values for inference
'''
#name of the model saved under the directory ./models/<model_name>/<test_model_name>
test_model_name = ""
num_words_to_generate = 15

'''
Don't touch this
'''

model_save_path = "./models/{}".format(model_name)

if not os.path.exists(model_save_path):
    os.makedirs(model_save_path)