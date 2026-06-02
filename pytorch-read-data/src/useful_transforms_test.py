from PIL import Image
from torch.utils.tensorboard import SummaryWriter
from torchvision import transforms

img_path = '../dataset/train/bees/39672681_1302d204d1.jpg'


pil_img = Image.open(img_path)

image_tensor_trans = transforms.ToTensor()

ten_img = image_tensor_trans(pil_img)

print(ten_img)
#初始化writer
writer = SummaryWriter('../log')
#讲没有归一化的写入
writer.add_image('useful_tensor_img',ten_img,0)
print(ten_img[0][0][0])
trans_norm =  transforms.Normalize([0.1,0.1,0.1],[0.1,0.2,0.5])
img_norm = trans_norm(ten_img)
print(img_norm[0][0][0])
writer.add_image('useful_tensor_img_norm', img_norm, 0)

writer.close()

#在控制台运行读取event的指令
#tensorboard --logdir=logs-test --port=6005