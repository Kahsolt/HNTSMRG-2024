#!/usr/bin/env python3
# Author: Armit
# Create Time: 2024/06/20 

# 读取并展示 .nii.gz 文件

from argparse import ArgumentParser
from pathlib import Path
from PIL import Image
from typing import Tuple, List

import numpy as np
from numpy import ndarray
import nibabel as nib
from tqdm import tqdm
from moviepy.editor import ImageSequenceClip

BASE_PATH = Path(__file__).parent
DATA_PATH = BASE_PATH / 'data' / 'HNTSMRG24_train'
TMP_PATH = BASE_PATH / 'tmp' ; TMP_PATH.mkdir(exist_ok=True)

def minmax_norm(x:ndarray) -> ndarray:
  x = x.astype(np.float32)
  vmin, vmax = x.min(), x.max()
  return (x - vmin) / (vmax - vmin)

def im_f2u(x:ndarray) -> ndarray:   # img f32 to u8
  assert 0.0 - 1e-8 < x.min() and x.max() <= 1.0 + 1e-8
  return np.round(x * 255).astype(np.uint8)

def im_ch3(x:ndarray) -> ndarray:   # img repeat grey to 3-ch
  if len(x.shape) == 3: return x
  return np.tile(np.expand_dims(x, axis=-1), (1, 1, 3))


def get_preRT_sample(id:int) -> Tuple[ndarray, ndarray]:
  img_fp = DATA_PATH / str(id) / 'preRT' / f'{id}_preRT_T2.nii.gz'
  lbl_fp = DATA_PATH / str(id) / 'preRT' / f'{id}_preRT_mask.nii.gz'
  img = np.asarray(nib.load(img_fp).dataobj, dtype=np.uint16)
  lbl = np.asarray(nib.load(lbl_fp).dataobj, dtype=np.uint8)
  return img, lbl


def vis(args):
  if args.task == 'preRT':
    img, lbl = get_preRT_sample(args.id)
  elif args.task == 'midRT':
    raise NotImplementedError

  print('img.shape:', img.shape)  # [H=512, W=512, L=83]
  print('  min:', img.min())
  print('  max:', img.max())
  print('  avg:', img.mean())
  print('  std:', img.std())
  print('lbl.shape:', lbl.shape)
  print(f'  0: {np.sum(lbl == 0) / lbl.size:.7f} %')
  print(f'  1: {np.sum(lbl == 1) / lbl.size:.7f} %')
  print(f'  2: {np.sum(lbl == 2) / lbl.size:.7f} %')

  frames: List[ndarray] = []
  L = img.shape[-1]
  for l in tqdm(range(L)):
    X = np.rot90(img[:, :, l])
    Y = np.rot90(lbl[:, :, l])

    X = im_ch3(im_f2u(minmax_norm(X)))
    mask = np.expand_dims(Y == 0, axis=-1)  # bg, [H, W, 1]
    Y_ch3 = np.zeros_like(im_ch3(Y))
    Y_ch3[:, :, 0] = Y == 1   # GTVp: tumor -> R channel
    Y_ch3[:, :, 1] = Y == 2   # GTVn: lymph -> G channel
    Y_ch3[:, :, 0] = Y_ch3[:, :, 0] * 192 + 63
    Y_ch3[:, :, 1] = Y_ch3[:, :, 1] * 192 + 63
    Z = X * mask + Y_ch3 * ~mask
    frames.append(np.concatenate([X, Z], axis=1))

  save_fp = TMP_PATH / f'{args.task}_id={args.id}.mp4'
  print(f'>> export video to: {save_fp}')
  clip = ImageSequenceClip(frames, fps=args.fps, with_mask=False)
  clip.write_videofile(str(save_fp), fps=args.fps)


if __name__ == '__main__':
  parser = ArgumentParser()
  parser.add_argument('-T', '--task', default='preRT', choices=['preRT', 'midRT'], help='task')
  parser.add_argument('-i', '--id', required=True, type=int, help='sample id')
  parser.add_argument('--fps', type=int, default=5, help='FPS')
  args = parser.parse_args()

  vis(args)
