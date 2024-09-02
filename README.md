# HNTSMRG-2024

    Contest solution for "Head and Neck Tumor Segmentation for MR-Guided Applications"

----

⚠ 弃赛了，本仓库请勿使用！

Contest page: [https://hntsmrg24.grand-challenge.org/](https://hntsmrg24.grand-challenge.org/)  


### Quickstart

⚪ install

- `conda create -n HNTS python==3.11 && conda activare HNTS`
- install PyTorch follow [official guide](https://pytorch.org/get-started/) according to your hardware settings
- `git clone https://github.com/Kahsolt/HNTSMRG-2024 --recursive`
- `pip install -r requirements.txt`
- `cd repo\nnUNet && pip install -e .`

⚪ run

- download & extract dataset `HNTSMRG24_train.zip` under folder `data/`
- see command examples in `run_nnunetv2.cmd`


#### refenrence

- data (13.9G): [https://zenodo.org/records/11199559](https://zenodo.org/records/11199559)
- repo
  - nnUNet: [https://github.com/MIC-DKFZ/nnUNet](https://github.com/MIC-DKFZ/nnUNet)
  - MedNeXt: [https://github.com/MIC-DKFZ/MedNeXt](https://github.com/MIC-DKFZ/MedNeXt)
- contests
  - SegRap (2023): https://segrap2023.grand-challenge.org/segrap2023/
  - HaN-Seg (2023): https://han-seg2023.grand-challenge.org/ 
  - HECKTOR (2022): https://hecktor.grand-challenge.org/

----
by Armit
2024/05/31
