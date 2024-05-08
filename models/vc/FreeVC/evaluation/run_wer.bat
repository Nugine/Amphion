@echo off
echo Running wer.py with different parameters...

:: 使用不同的参数调用文件
python wer.py --res_wavdir "result\freevc-12k-G" --outdir "result\freevc-12k-G\eval"
python wer.py --res_wavdir "result\freevc-12k-sG" --outdir "result\freevc-12k-sG\eval"
python wer.py --res_wavdir "result\freevc-12k-noSR-G" --outdir "result\freevc-12k-noSR-G\eval"

echo All processes completed.