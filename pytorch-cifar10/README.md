项目目录
pytorch-cifar10
--dataset           gitignore 数据集
--log               gitignore tensorboard event文件
--src               代码文件

requirements.txt    依赖文件
README.md           readme文件
cifar-10数据集下载地址
https://www.cs.toronto.edu/~kriz/cifar.html
选择python版本下载 下载完成后解压到dataset文件夹

控制台运行读取event的指令 指定log文件夹和端口 这里是相对路径，
pytorch-cifar10 以单独项目打开，如果多个项目打开，把项目名路径也加上

tensorboard --logdir=log --port=6005 