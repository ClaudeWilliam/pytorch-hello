from PIL import Image
from torch.utils.tensorboard import SummaryWriter
from torchvision import transforms

img_path = '../dataset/train/bees/36900412_92b81831ad.jpg'

#img_path = '..\\dataset\\train\\bees\\16838648_415acd9e3f.jpg.jpg'

pil_img = Image.open(img_path)

image_tensor_trans = transforms.ToTensor()

ten_img = image_tensor_trans(pil_img)

print(ten_img)

writer = SummaryWriter('../log')

writer.add_image('tensor_img',ten_img,0)

writer.close()

#在控制台运行读取event的指令
#tensorboard --logdir=logs-test --port=6005