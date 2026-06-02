from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter
from torchvision import datasets, transforms

dataset_test = datasets.CIFAR10(root="../dataset", train=False, transform=transforms.ToTensor(), download=True)

test_loader = DataLoader(dataset=dataset_test, batch_size=64, shuffle=True, num_workers=0, drop_last=False)

writer = SummaryWriter("../log")
step = 0
for data in test_loader:
    imgs, labels = data
    writer.add_images("data_loader_test_64", imgs, step)
    # print(imgs.shape, labels)
    # print(step)
    step = step + 1
    print(step)

writer.close()
#tensorboard --logdir=log --port=6005
