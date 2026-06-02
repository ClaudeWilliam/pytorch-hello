from torch.utils.tensorboard import SummaryWriter


writer = SummaryWriter("../log")
#在../logs-test 生成event文件
for i in range(100):
    writer.add_scalar("y=x",i, i)

for i in range(100):
    writer.add_scalar("y=2x",i, 2*i)
writer.close()

#在控制台运行读取event的指令
#tensorboard --logdir=log --port=6005
#踩坑的点 pip install "setuptools<82.0.0" 将setuptools要降级低于 82.0.0
#查看pip 安装的版本 pip list
