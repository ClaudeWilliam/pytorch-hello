项目目录
pytorch-read-data
--dataset           gitignore 数据集
--log               gitignore tensorboard event文件
--src               代码文件

requirements.txt    依赖文件
README.md           readme文件
蚂蚁蜜蜂分类数据集下载连接
https://download.pytorch.org/tutorial/hymenoptera_data.zip
下载完成后解压到dataset文件夹

控制台运行读取event的指令 指定log文件夹和端口 这里是相对路径，
pytorch-read-data 以单独项目打开，如果多个项目打开，把项目名路径也加上

tensorboard --logdir=log --port=6005 

踩坑的点 pip install "setuptools<82.0.0" 将setuptools要降级低于 82.0.0
查看pip 安装的版本 pip list