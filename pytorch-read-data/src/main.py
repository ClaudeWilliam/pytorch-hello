# 这是一个示例 Python 脚本。
from torch.utils.data import Dataset

from src import read_data
from src.read_data import MyDataset
import os

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。


# 按装订区域中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print('PyCharm')
    root_dir = 'dataset\\train'
    bee_label_dir = 'bees'
    ant_label_dir = 'ants'
    print("当前工作目录:", os.getcwd())
    parent_dir = os.path.dirname(os.getcwd())
    root_dir = os.path.join(parent_dir, root_dir)
    print("转换绝对路径:", root_dir)
    bee_dataset = MyDataset(root_dir, bee_label_dir)
    ant_dataset = MyDataset(root_dir, ant_label_dir)

    print(bee_dataset.__len__())
    print(ant_dataset.__len__())
    add_data_set = bee_dataset + ant_dataset
    print(add_data_set.__len__())
