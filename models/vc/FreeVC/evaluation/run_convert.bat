@echo off
echo Running convert.py with different parameters...

:: 调用convert.py，使用不同的--ptfile参数
python convert.py --hpfile "configs\freevc.json" --ptfile "checkpoints\ckpts\freevc-G_120000.ckpt" --outdir "result\freevc-12k-G"
python convert.py --hpfile "configs\freevc-s.json" --ptfile "checkpoints\ckpts\freevc_s-G_120000.ckpt" --outdir "result\freevc-12k-sG"
python convert.py --hpfile "configs\freevc-nosr.json" --ptfile "checkpoints\ckpts\freevc_nosr-G_120000.ckpt" --outdir "result\freevc-12k-noSR-G"

echo All processes completed.