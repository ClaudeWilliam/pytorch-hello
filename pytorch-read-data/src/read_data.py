from typing import LiteralString

from torch.utils.data.dataset import Dataset
import torchvision
import torchvision.transforms as transforms
from PIL import Image
import os


class MyDataset(Dataset):



    path: LiteralString | str | bytes

    def __init__(self, root_dir, label_dir, transform=None, target_transform=None):
        self.root_dir = root_dir
        self.label_dir = label_dir
        self.path = os.path.join(self.root_dir, self.label_dir)
        self.img_paths = os.listdir(self.path)


    def __getitem__(self, item):
        img_name = self.img_paths[item]
        item_path = os.path.join(self.root_dir, self.label_dir, img_name)
        img = Image.open(item_path)
        label = self.label_dir
        return img,label

    def __len__(self):
        return len(self.img_paths)
