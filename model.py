import torch
import torch.nn as nn
from torch.autograd import Variable


class GruRnn(nn.Module):
    def __init__(self, input_size, hidden_size, output_size, n_layers = 1):
        super(GruRnn, self).__init__()
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        self.n_layers = n_layers

        self.encoder = nn.Embedding(input_size, hidden_size)
        self.gru = nn.GRU(hidden_size, hidden_size, n_layers, batch_first = True, bidirectional = False)
        self.decoder = nn.Linear(hidden_size, output_size)

    def forward(self, inp, hidden):
        x = self.encoder(inp)
        # print(x.size())
        output, hidden = self.gru(x, hidden)
        # print(output.size(), hidden.size())
        output = self.decoder(output[:, -1])
        return output, hidden

    def init_hidden(self, batch_size):
        return Variable(torch.zeros(self.n_layers, batch_size, self.hidden_size))