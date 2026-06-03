import torch
import torchvision
from torch import nn

from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter

dataset = torchvision.datasets.CIFAR10(root='../dataset', train=False, download=True,
                                       transform=torchvision.transforms.ToTensor())
dataloader = DataLoader(dataset, batch_size=128, num_workers=0)


class Net(nn.Module):
    # net类的构造函数
    def __init__(self):
        # 调用父类初始化
        super().__init__()
        # 指定一个卷积层 输入3通道  输出6通道  卷积核是3*3 步长是1 填充是0
        self.conv1 = nn.Conv2d(3, 6, 3, stride=1, padding=0)

    # 前向函数
    def forward(self, x):
        x = self.conv1(x)
        return x


net = Net()
# 打印net
print(net)

writer = SummaryWriter("../log")
step = 0
for data in dataloader:
    # 从dataset 获取数据
    img, label = data
    print(img.shape)
    # 写入数据，未卷积的数据
    writer.add_images("input", img, step)
    # 卷积后的数据
    output = net(img)
    print(output.shape)
    # 插入卷据后的数据
    output = torch.reshape(output, (-1, 3, 30, 30))
    print(output.shape)
    writer.add_images("output", output, step)
    step =step + 1
    print(step)

writer.close()
#tensorboard --logdir=log --port=6005
