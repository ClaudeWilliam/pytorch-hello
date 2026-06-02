import torchvision
from torch.utils.tensorboard import SummaryWriter
from torchvision import transforms

trans_com = transforms.Compose([transforms.ToTensor()])

train_set = torchvision.datasets.CIFAR10(root='../dataset', train=True, download=True, transform=trans_com)
train_set_test = torchvision.datasets.CIFAR10(root='../dataset', train=False, download=True, transform=trans_com)
print(len(train_set_test))
print(type(train_set_test))
print(train_set_test.classes)
print(train_set_test[0])
img, label = train_set_test[0]
print(img)
print(label)
print(train_set_test.classes[label])

write = SummaryWriter("../log")
for i in range(10):
    img, label = train_set_test[i]
    write.add_image(tag='trian_set_test', img_tensor=img, global_step=i)
write.close()
#在控制台运行读取event的指令
#tensorboard --logdir=log --port=6005