# competition_orange
orange pest recognition competition


### 1. Data process
##### 1.1 数据的预处理：生成COCO格式
+ 使用pyscripts/generate_list.py生成train_list.txt文件
+ 使用pyscripts/draw_bbox.py查看框的形式
+ 使用pyscripts/draw_figure.py生成一些figure
+ 先用pyscripts/change_bbox_format.py把train_list.txt变成annos.txt
+ 然后用pyscripts/tococo.py得到instances_train2017.json等coco格式的文件

##### 1.2 COCO数据集的格式如下
├── categories
│   ├── 'id'
│   ├── 'name'
│   └── 'supercategory': 'mark'
├── images
│   ├── 'file_name'
│   ├── 'id'
│   ├── 'width'
│   └── 'height'
├── annotations
│   ├── 'area'
│   ├── 'bbox'
│   ├── 'category_id'
│   ├── 'id'
│   ├── 'image_id'
│   ├── 'iscrowd'
│   └── 'segmentation'


### 2. Environment
##### 2.1 使用mmdetection时的环境配置
+ python 3.6.9
+ torch: 1.8.1+cu111
+ cuda: 11.3
+ mmcv-full: 1.3.9 pip3 install mmcv-full -f https://download.openmmlab.com/mmcv/dist/cu111/torch1.8.0/index.html
+ pip3 install openmim==0.1.2
+ mim install mmdet
export LC_ALL=C.UTF-8
export LANG=C.UTF-8
+ git clone https://github.com/open-mmlab/mmdetection.git
+ cd mmdetection
##### Install build requirements and then install mmdetection.
pip3 install -r requirements/build.txt
pip3 install "git+https://github.com/cocodataset/cocoapi.git#subdirectory=PythonAPI"
pip3 install -v -e .  # or "python setup.py develop"
##### 打开python验证是否安装成功
from mmdet.apis import init_detector, inference_detector, show_result


### 3. Train阶段
##### 3.1 使用mask-rcnn
###### 单卡训练
+ python3 tools/train.py configs/orange/mask_rcnn_r50_caffe_fpn_mstrain-poly_1x_orange.py

##### 3.2 使用Deformable DETR
###### 单卡训练
+ python3 tools/train.py configs/orange/deformable_detr_twostage_refine_r50_16x2_50e_orange.py
###### 多卡训练
+ tools/dist_train.sh configs/orange/deformable_detr_twostage_refine_r50_16x2_50e_orange.py 4
##### 测试
/usr/bin/python3 tools/test.py configs/orange/deformable_detr_twostage_refine_r50_16x2_50e_orange.py work_dirs/deformable_detr_twostage_refine_r50_16x2_50e_orange/latest.pth  --eval bbox --show --show-dir result_file


### 4.训练日志：
###### 20210713_145521 
+ tools/dist_train.sh configs/orange/deformable_detr_twostage_refine_r50_16x2_50e_orange.py 4
+ optimizer = dict(lr=0.00002)
+ lr_config = dict(policy='step', step=[40])
+ 测试结果发现预测框都好大，应该是学习率设置太小了，模型参数没能收敛好。重新训练时调整学习率

##### 20210713_174233
+ tools/dist_train.sh configs/orange/deformable_detr_twostage_refine_r50_16x2_50e_orange.py 4
+ optimizer = dict(lr=0.0002)
+ lr_config = dict(policy='step', step=[25，40])

##### 202107

