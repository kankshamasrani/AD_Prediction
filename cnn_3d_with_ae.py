import torch
from autoencoder import AutoEncoder 
import torch.nn as nn

class CNN(nn.Module):
    def __init__(self, num_classes=2):
        super(CNN, self).__init__()
        self.conv1 = nn.Conv3d(1, 410, kernel_size=7, stride=1, padding=3)
        self.relu1 = nn.ReLU(inplace=True)
        self.pool1 = nn.MaxPool3d(kernel_size=7,stride=7)
        # self.conv2 = nn.Conv3d(410, 200, kernel_size=3, stride=1, padding=1)
        # self.relu2 = nn.ReLU(inplace=True)
        # self.pool2 = nn.MaxPool3d(kernel_size=3, stride=3)
        # self.fc1 = nn.Linear(5*5*5*200, 800)
        self.fc1 = nn.Linear(15*15*15*410, 800)
        self.fc2 = nn.Linear(800, num_classes)
        self.softmax = nn.LogSoftmax()

    def forward(self, out):
        out = self.pool1(self.relu1(self.conv1(out)))
        # out = self.pool2(self.relu2(self.conv2(out)))
        # out = out.view(-1,5*5*5*200)
        out = out.view(-1, 15*15*15*410)
        out = self.fc1(out)
        out = self.fc2(out)
        out = self.softmax(out)
        return out
