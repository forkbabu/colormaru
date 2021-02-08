from deoldify import device
from deoldify.device_id import DeviceId
#choices:  CPU, GPU0...GPU7
device.set(device=DeviceId.GPU0)
 
import torch
 
if not torch.cuda.is_available():
    print('GPU not available.')
 
from os import path
import fastai
from deoldify.visualize import *
from pathlib import Path
torch.backends.cudnn.benchmark=True
import warnings
warnings.filterwarnings("ignore", category=UserWarning, message=".*?Your .*? set is empty.*?")
colorizer = get_video_colorizer()
import fire

def color(vid="/content/cut1.mp4",render_factor=27):
  video_path = colorizer.colorize_from_file_name(vid, render_factor, watermarked=False)
  return videopath

if __name__ == '__main__':
  vpath = fire.Fire(color)
  print(vpath)

