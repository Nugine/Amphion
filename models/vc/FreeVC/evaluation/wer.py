from transformers import Wav2Vec2Processor, HubertForCTC
import os
import argparse
import torch
import librosa
from tqdm import tqdm
from glob import glob
from jiwer import wer, cer


# Get text from the audio using facebook Hubert model
def get_text(wav_dir, txt_dir):
    print(f"Starting to get text from audios in {wav_dir}...")
    # load model and processor
    model = HubertForCTC.from_pretrained("facebook/hubert-large-ls960-ft").cuda()
    processor = Wav2Vec2Processor.from_pretrained("facebook/hubert-large-ls960-ft")

    # get transcriptions
    wavs = glob(f"{wav_dir}/*.wav")
    wavs.sort()
    text_dict = {}

    with open(txt_dir, "w") as f:
        for path in tqdm(wavs):
            wav = [librosa.load(path, sr=16000)[0]]
            input_values = processor(
                wav, sampling_rate=16000, return_tensors="pt"
            ).input_values.cuda()
            logits = model(input_values).logits
            predicted_ids = torch.argmax(logits, dim=-1)
            text = processor.batch_decode(predicted_ids)[0]
            f.write(f"{path}|{text}\n")
            title = os.path.basename(path)[:-4]
            text_dict[title] = text

    return text_dict


def cal_wer_ner(gt_dict, trans_dict):
    # calc
    gts, trans = [], []
    for key in trans_dict.keys():
        text = trans_dict[key]
        trans.append(text)
        # gttext = gt_dict[key.split("-")[0]]
        gttext = gt_dict[key[:8]]
        gts.append(gttext)

    wer_score = wer(gts, trans)
    cer_score = cer(gts, trans)
    with open(f"{args.outdir}/wer.txt", "w") as f:
        f.write(f"wer: {wer_score}\n")
        f.write(f"cer: {cer_score}\n")
    print(f"WER of {args.res_wavdir} is:", wer_score)
    print(f"CER of {args.res_wavdir} is:", cer_score)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--res_wavdir",
        type=str,
        default=r"data\VCTK\test_output",
        help="path to the converted audio",
    )
    parser.add_argument(
        "--src_wavdir",
        type=str,
        default=r"data\VCTK\test_data",
        help="path to the source audio",
    )
    parser.add_argument(
        "--outdir", type=str, default="result", help="path to output dir"
    )
    # parser.add_argument("--use_cuda", default=True, action="store_true")
    args = parser.parse_args()

    os.makedirs(args.outdir, exist_ok=True)
    gt_dict = get_text(args.src_wavdir, os.path.join(args.outdir, "gt.txt"))
    trans_dict = get_text(args.res_wavdir, os.path.join(args.outdir, "res_text.txt"))

    cal_wer_ner(gt_dict, trans_dict)
