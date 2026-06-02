from typing import Any

import torch
from torch import nn


class test_model(nn.Module):

    def __init__(self) -> None:
        super().__init__()

    def forward(self, x):
        out = x + 1
        return out

test_model = test_model()
input = torch.tensor((1,3,32,32))
output = test_model(input)
print(output)