from torch.utils.tensorboard import SummaryWriter
import numpy as np
from PIL import Image


writer = SummaryWriter("../log")
#在../logs-test 生成event文件
image_path1 = '..\\dataset\\train\\ants\\0013035.jpg'
img_PIL = Image.open(image_path1)
print('img_np_arr.shape',img_PIL)
img_np_arr = np.array(img_PIL)
print('img_np_arr.shape',img_np_arr.shape)
writer.add_image('test',img_np_arr,0,dataformats='HWC',)
image_path2 = '..\\dataset\\train\\ants\\5650366_e22b7e1065.jpg'
img_PIL2 = Image.open(image_path2)
print('img_np_arr.shape',img_PIL2)
img_np_arr2 = np.array(img_PIL2)
print('img_np_arr2.shape',img_np_arr2.shape)
writer.add_image('test',img_np_arr2,1,dataformats='HWC',)


writer.close()
#在控制台运行读取event的指令
#tensorboard --logdir=logs --port=6005
#踩坑的点 pip install "setuptools<82.0.0" 将setuptools要降级低于 82.0.0
#查看pip 安装的版本 pip list