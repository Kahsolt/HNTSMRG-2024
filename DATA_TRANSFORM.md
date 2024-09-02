# nnUNet data transform

### raw

- `imagesTr/2_0000.nii.gz`: ndarray
  - shape=(512, 512, 83), dtype=float32, vrng=[0.0, 407.0+)
- `labelsTr/2.nii.gz`: ndarray
  - shape=(512, 512, 83), dtype=uint8, vset={0, 1, 2}


### preprocess

⚪ gt

应当与 `raw-labelsTr` 一致

⚪ 2d

- `2.npz`: Dict[str, ndarray]
  - data: shape=(1, 83, 510, 511), dtype=float32, vrng=(-0.6502874, 0.20535244)
    - i.e.: `2.npy`
  - seg: shape=(1, 83, 510, 511), dtype=int8, vrng={0, 1, 2, -1}
    - i.e.: `2_seg.npy`
- `2.pkl`: Dict[str, Any]
  - nibabel_stuff
    - original_affine: shape=(4, 4), transform matrix
    - reoriented_affine: shape=(4, 4), transform matrix
  - spacing: `[2.0, 0.5, 0.5]`
  - shape_before_cropping: `(83, 512, 512)`
  - bbox_used_for_cropping: `[[0, 83], [0, 510], [0, 511]]`
  - shape_after_cropping_and_before_resampling: `(83, 510, 511)`
  - class_locations: Dic[int, ndarray[int64]]
    - 1: shape=(3526, 4), should eqv. to `torch.where(seg == 1)`
    - 2: shape=(9264, 4)

⚪ 3d_fullres

- `2.npz`: Dict[str, ndarray]
  - data: shape=(1, 138, 510, 511), dtype=float32, vrng=(-0.6502874, 0.20535244)
  - seg: shape=(1, 138, 510, 511), dtype=int8, vrng={0, 1, 2, -1}
- `2.pkl`: Dict[str, Any]
  - The same as in 2d... wtf!!

⚪ 3d_lowres

- `2.npz`: Dict[str, ndarray]
  - data: shape=(1, 103, 309, 309), dtype=float32, vrng=(-0.6502874, 0.20535244)
  - seg: shape=(1, 103, 309, 309), dtype=int8, vrng={0, 1, 2, -1}
- `2.pkl`: Dict[str, Any]
  - The same as in 2d... wtf!!
