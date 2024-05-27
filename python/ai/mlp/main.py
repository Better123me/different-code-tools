import pandas as pd
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
from sklearn.model_selection import train_test_split

import matplotlib.pyplot as plt

class MLP(nn.Module):
    def __init__(self, input_size, hidden_size1, hidden_size2, output_size):
        super(MLP, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size1)
        self.activate1 = nn.SiLU()
        self.fc2 = nn.Linear(hidden_size1, hidden_size2)
        self.activate2 = nn.SiLU()
        self.fc3 = nn.Linear(hidden_size2, output_size)

    def forward(self, x):
        x = self.activate1(self.fc1(x))
        x = self.activate2(self.fc2(x))
        x = self.fc3(x)
        return x

class CustomDataset(Dataset):
    def __init__(self, data, targets):
        self.data = data
        self.targets = targets

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return torch.tensor(self.data[idx], dtype=torch.float), torch.tensor(self.targets[idx], dtype=torch.float)


def train_model(model, criterion, optimizer, scheduler, train_loader, num_epochs, patience=5, min_delta=1):
    model.train()
    prev_loss = best_loss = float('inf')
    losses = []
    for epoch in range(num_epochs):
        running_loss = 0.0
        for inputs, targets in train_loader:
            optimizer.zero_grad()
            outputs = model(inputs)
            loss = criterion(outputs.squeeze(), targets)
            loss.backward()
            optimizer.step()
            running_loss += loss.item()
        print(f"Epoch [{epoch + 1}/{num_epochs}], Loss: {running_loss / len(train_loader)}")

        if abs(running_loss - prev_loss) < min_delta:
            no_improvement_count += 1
        else:
            no_improvement_count = 0
        if no_improvement_count >= patience:
            print(f"No significant improvement in loss. Terminating training.")
            break
        prev_loss = running_loss
        losses.append(running_loss)
        scheduler.step(running_loss)
        current_loss = running_loss / len(train_loader)

        if scheduler.is_better(current_loss, best_loss):
            print("Reducing learning rate.")
            best_loss = current_loss

