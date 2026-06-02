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
安装pytorch
mac
pip install torch==2.9.0 torchvision==0.24.0 torchaudio==2.9.0
如果你使用cuda加速，那么根据你显卡支持cuda版本决定
windows  cuda126
pip install torch==2.9.0 torchvision==0.24.0 torchaudio==2.9.0 --index-url https://download.pytorch.org/whl/cu126
安装tensorboard
pip install tensorboard

tensorboard --logdir=log --port=6005 

踩坑的点 pip install "setuptools<82.0.0" 将setuptools要降级低于 82.0.0
查看pip 安装的版本 pip list
