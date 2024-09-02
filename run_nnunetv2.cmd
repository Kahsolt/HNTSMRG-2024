@ECHO OFF
PUSHD %~dp0

REM Remember the dataset code:
REM - task1: 241
REM - task2: 242
SET ID=241

REM k-fold, 0~4
SET K=0

REM configuration, choose from [2d, 3d_fullres, 3d_lowres]
SET C=3d_fullres

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
REM Step 0: set up envvar (run every new shell)

SET DATASET_PATH=data/HNTSMRG24_train

SET nnUNet_raw=%CD%\data_nnUNet\nnUNet_raw
SET nnUNet_preprocessed=%CD%\data_nnUNet\nnUNet_preprocessed
SET nnUNet_results=%CD%\data_nnUNet\nnUNet_results


:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
REM Step 1: convert dataset from contest-given to nnUNet-recognizable (run only once)

python -m nnunetv2.dataset_conversion.Dataset%ID%_HNTSMRG24_task1 %DATASET_PATH%


:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
REM Step 2: run preprocess (run only once)

REM nnUNetv2_plan_and_preprocess -d TARGET_DATASET
nnUNetv2_plan_and_preprocess -d %ID% -c %C% --verify_dataset_integrity --verbose

REM The following is only for pretrain-refine learning schema
REM nnUNetv2_extract_fingerprint -d PRETRAINING_DATASET
REM nnUNetv2_move_plans_between_datasets -s PRETRAINING_DATASET -t TARGET_DATASET -sp PRETRAINING_PLANS_IDENTIFIER -tp TARGET_PLANS_IDENTIFIER
REM nnUNetv2_preprocess -d PRETRAINING_DATASET -plans_name TARGET_PLANS_IDENTIFIER


:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
REM Step 3: run training

nnUNetv2_train %ID% %C% %K%
