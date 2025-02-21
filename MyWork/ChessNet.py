#CHESS NN MODEL
import torch.nn as nn

class ChessNet(nn.Module):
  def __init__(self):
    super().__init__()
    self.conv1 = nn.Conv2d(12, 64, kernel_size=3, padding=1)
    self.conv2 = nn.Conv2d(64, 64, kernel_size=3, padding=1)
    self.conv3 = nn.Conv2d(64, 128, kernel_size=3, padding=1)

    self.fc1 = nn.Linear(128 * 8 * 8, 512)
    self.fc2 = nn.Linear(512, 1965) # 1965 possible moves

  def forward(self, x):
    x = F.relu(self.conv1(x))
    x = F.relu(self.conv2(x))
    x = F.relu(self.conv3(x))

    x = x.view(-1, 128 * 8 * 8)
    x = F.relu(self.fc1(x))
    x = self.fc2(x)
    
    return x