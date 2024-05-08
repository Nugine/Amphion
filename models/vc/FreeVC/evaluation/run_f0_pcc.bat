@echo off
echo Running f0_PCC.py with different parameters...

:: 使用不同的参数调用文件
python F0_PCC.py --tgt_path "result\freevc-12k-G" --output_path "result\freevc-12k-G\eval"
python F0_PCC.py --tgt_path "result\freevc-12k-sG" --output_path "result\freevc-12k-sG\eval"
python F0_PCC.py --tgt_path "result\freevc-12k-noSR-G" --output_path "result\freevc-12k-noSR-G\eval"

echo All processes completed.