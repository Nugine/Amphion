import glob
import random
import os
import shutil

# 数据集的根目录
dataset_dir = 'VCTK/vctk-16k'
# 测试集音频的目标目录
test_set_dir = 'VCTK/test_data'

# 确保测试集目录存在
if not os.path.exists(test_set_dir):
    os.makedirs(test_set_dir)

# 获取所有wav文件的路径
wav_files = glob.glob(os.path.join(dataset_dir, '**/*.wav'), recursive=True)
# print(len(wav_files))

# 随机选择100个音频文件
selected_files = random.sample(wav_files, 300)

# 将选中的文件复制到测试集目录
for file_path in selected_files:
    # 构建目标文件路径
    dest_path = os.path.join(test_set_dir, os.path.basename(file_path))
    # 复制文件
    shutil.copy(file_path, dest_path)

print("Done!")
