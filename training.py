import torch
import torch.nn as nn
import os
from torch.utils.data import DataLoader
from tensorboardX import SummaryWriter
from tqdm import tqdm

from model import GruRnn
from config import hidden_size, n_layers, DEVICE, model_save_path, model_name
from text_dataloader import TextLoader

def run_epoch(decoder, critirion, decoder_optimizer, train_loader, batch_size):
    data_len = len(train_loader)
    epoch_loss = 0
    for i, (inp, target) in tqdm(enumerate(train_loader), total=data_len):
        inp = inp.to(DEVICE)
        target = target.to(DEVICE)
        # print("input size : {}\ntarget size : {}".format(inp.size(), target.size()))
        batch_size = inp.size()[0]
        hidden = decoder.init_hidden(batch_size).cuda()
        decoder_optimizer.zero_grad()
   
        output, hidden = decoder(inp, hidden)
        # print(output.size(), target.size())
        loss = critirion(output, target.view(-1))
        epoch_loss += loss.item()
        loss.backward()
        
        decoder_optimizer.step()

    return epoch_loss/data_len


def train(train_file_path):
    n_epoch = 300
    print_every = 2
    lr = 1e-3
    batch_size = 4096

    obj_text = TextLoader(train_file_path)
    voc_len = obj_text.get_voc_len()
    train_loader = DataLoader(dataset=obj_text,
                            batch_size = batch_size,
                            shuffle = True,
                            num_workers = 8)
    
    if not(os.path.exists(model_save_path)):
        os.makedirs(model_save_path)
    
    decoder = GruRnn(voc_len, hidden_size, voc_len, n_layers).to(DEVICE)
    decoder_optimizer = torch.optim.Adam(decoder.parameters(), lr = lr)
    critirion = nn.CrossEntropyLoss()

    all_losses = []
    loss_avg = 0
    
    decoder.train()
    for an_epoch in (range(1, n_epoch + 1, 1)):
        loss = run_epoch(decoder, critirion, decoder_optimizer, train_loader, batch_size)
        loss_avg += loss


        if an_epoch % print_every == 0:
            loss_avg = loss_avg / print_every
            print("epoch : {} , loss : {}".format(an_epoch, loss_avg))
            loss_avg = 0

            current_model_path = os.path.join(model_save_path, "epoch_{}.pt".format(an_epoch))
            torch.save(decoder.state_dict(), current_model_path)