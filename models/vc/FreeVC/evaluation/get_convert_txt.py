import glob
import random
import os

# 数据集和测试集目录
dataset_dir = r'VCTK\vctk-16k'
selected_sources_dir = r'VCTK\test_data'
# output_dir = '/path/to/output/directory/'

# 获取speaker list
speaker_dirs = glob.glob(os.path.join(dataset_dir, 'p*'))
# print(speaker_dirs)

# 随机选择12个speaker
selected_speakers = random.sample(speaker_dirs, 12)
# print(selected_speakers)

# 读取所有选定的音频A文件
source_audios = glob.glob(os.path.join(selected_sources_dir, '*.wav'))

# 创建convert.txt文件
with open(r'VCTK\convert.txt', 'w') as file:
    for source_audio in source_audios:
        # 从每个选定讲话者中随机选择一个音频作为音频B
        speaker_audio_b = random.choice([glob.glob(os.path.join(speaker, '*.wav')) for speaker in selected_speakers])
        # 构建输出音频C的名称
        output_audio_c = os.path.basename(source_audio).replace('.wav', '_sync')
        # 写入文件
        file.write(f"{output_audio_c}|{os.path.join('data', source_audio)}|{os.path.join('data', random.choice(speaker_audio_b))}\n")

print("convert.txt 文件已生成")
