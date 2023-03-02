import os
import numpy as np


def save_dict_by_numpy(filename, dict_vale):
    if not (os.path.exists(os.path.dirname(filename))):
        os.mkdir(os.path.dirname(filename))
    np.save(filename, dict_vale)


my_dict = {"name": "小明", "age": 12}
output_filename = "save_dir/my_dict.npy"

# 保存
save_dict_by_numpy(output_filename, my_dict)

# 加载
my_dict2 = np.load(output_filename, allow_pickle=True).item()

print(my_dict, my_dict2)
