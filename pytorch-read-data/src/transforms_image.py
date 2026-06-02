#使用transforms处理图片
from PIL import Image
from torch.utils.tensorboard import SummaryWriter
from torchvision import transforms

image_path = '../dataset/train/bees/39747887_42df2855ee.jpg'
image_path_1 = '../dataset/train/bees/150013791_969d9a968b.jpg'
image_path_2 = '../dataset/train/bees/365759866_b15700c59b.jpg'

pil_image = Image.open(image_path)
pil_image_1 = Image.open(image_path_1)
pil_image_2 = Image.open(image_path_2)


print(pil_image.size)
print(pil_image_1.size)
trans_resize = transforms.Resize((256,256))
trans_tensor = transforms.ToTensor()

#使用resize
image_resize = trans_resize(pil_image)
image_tender = trans_tensor(image_resize)
# 使用compose
trans_com = transforms.Compose([trans_resize,trans_tensor])
tensor_img = trans_com(pil_image_1)

writer = SummaryWriter('../log')
writer.add_image('tensor_img_resize', image_tender, 0)
writer.add_image('tensor_img_resize', tensor_img, 1)
#RandomCrop
trans_rand_crop = transforms.RandomCrop(128)
trans_rand_com = transforms.Compose([trans_rand_crop,trans_tensor])
for i in range(10):
    writer.add_image('tensor_rand_crop', trans_rand_com(pil_image_2), i)

writer.close()



#在控制台运行读取event的指令
#tensorboard --logdir=logs-test --port=6005