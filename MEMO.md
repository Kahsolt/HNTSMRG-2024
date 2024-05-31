### Overview

- 任务: 头/颈肿瘤图像分割
- 数据: MRI 医学图像 (CC BY-NC 4.0)
  - NIfTI 格式 (.nii.gz)
  - 训练集 ~150 人, 测试集 ~50 人
  - 图像裁剪区域位置为: 锁骨以上, 鼻中隔以下
  - 放疗前 (1-3 weeks prior-RT) 和 放疗中 (2-4 weeks intra-RT) 成组给出
  - 可能会有 fat-suppressed 和 non-fat-suppressed 两个版本
- 标注: 3~4人打标, 由 [STAPLE](https://pubmed.ncbi.nlm.nih.gov/36761036/) 算法得出GT
  - background: 0
  - GTVp: 1 (primary gross tumor volumes)，每张图里最多只有一个 (连通域?) 
  - GTVn: 2 (metastatic lymph nodes)，每张图里可能有多个
- 建模 (历史经验)
  - nnUNet, nnUNetV2, nnUNet_SE; UniSeg; DynUNet; MultiTalent
  - data_aug; pacth_size
  - masked loss
- 评估： $ \mathrm{DSC}_\mathrm{agg} = \frac{2 \sum_i |A_i \cap B_i|}{\sum_i |A_i| + |B_i|} $
  - 对 GTVp 和 GTVn 分别求，再平均
- 提交
  - 将应用构建为一个 docker 镜像
  - 6 ~ 12 页小论文
- 医学术语缩略
  - HNC: head and neck cancer, 头/颈肿瘤
  - RT: radiation therapy, 放疗
  - CT-guided: 借助X光断层扫描
  - MRI-guided: 借助核磁共振成像


### Challenge Task

⚠ 不可使用外源数据，提交次数有限

⚪ Task 1: Pre-RT Segmentation

> 类似于 [2022 HECKTOR](https://hecktor.grand-challenge.org/Overview/) 和 [2023 SegRap](https://segrap2023.grand-challenge.org/)

⚠ 训练此任务时也可以使用 mid-RT data 作为辅助建模，但注意测试时只有 pre-RT data 作为输入！！

- input
  - pre-RT image
  - mid-RT image & segment (train only)
- output
  - pre-RT segment

⚪ Task 2: Mid-RT Segmentation

> mimic a real-world scenario for adaptive RT

- input
  - unseen/original pre-RT image & segment
  - deformed/registered pre-RT image & segment
  - mid-RT image
- output
  - mid-RT segment


### Timeline

- 注册: 5.1 - 11.15
- 训练数据集发布: 6.15
- 测试数据集(Docker)发布: 8.15
- 算法提交: 8.15 - 9.15
- 论文摘要提交: 9.15
- 发榜: 9.20
- 论文初稿提交: 9.20
- Live event: 10.10 之后 (MICCAI)
- 论文终稿提交(发布在LNCS): 11.1
