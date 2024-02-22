import os
import shutil

img_train = "/home/wanghaoxuan/workspace/datasets/flaw_mmseg/img_dir/train"
if os.path.exists(img_train):
    shutil.rmtree(img_train)
os.makedirs(img_train,exist_ok=True)

anno_train = "/home/wanghaoxuan/workspace/datasets/flaw_mmseg/ann_dir/train"
if os.path.exists(anno_train):
    shutil.rmtree(anno_train)
os.makedirs(anno_train,exist_ok=True)

img_val = "/home/wanghaoxuan/workspace/datasets/flaw_mmseg/img_dir/val"
if os.path.exists(img_val):
    shutil.rmtree(img_val)
os.makedirs(img_val,exist_ok=True)

anno_val = "/home/wanghaoxuan/workspace/datasets/flaw_mmseg/ann_dir/val"
if os.path.exists(anno_val):
    shutil.rmtree(anno_val)
os.makedirs(anno_val,exist_ok=True)


for jpg in os.listdir("/home/wanghaoxuan/workspace/datasets/flaw_data/train/mask_png"):
    jpg = os.path.splitext(jpg)[0][:-5]+".jpg"
    src_path = os.path.join("/home/wanghaoxuan/workspace/datasets/flaw_data/train/sample",jpg)
    tgt_path = os.path.join(img_train,jpg)
    if not os.path.exists(tgt_path):
        shutil.copy(src_path,tgt_path)

for jpg in os.listdir("/home/wanghaoxuan/workspace/datasets/flaw_data/val/mask_png"):
    jpg = os.path.splitext(jpg)[0][:-5]+".jpg"
    src_path = os.path.join("/home/wanghaoxuan/workspace/datasets/flaw_data/val/sample",jpg)
    tgt_path = os.path.join(img_val,jpg)
    if not os.path.exists(tgt_path):
        shutil.copy(src_path,tgt_path)


for png in os.listdir("/home/wanghaoxuan/workspace/datasets/flaw_data/train/mask_png"):
    src_path = os.path.join("/home/wanghaoxuan/workspace/datasets/flaw_data/train/mask_png",png)
    tgt_path = os.path.join(anno_train,png)
    if not os.path.exists(tgt_path):
        shutil.copy(src_path,tgt_path)

for png in os.listdir("/home/wanghaoxuan/workspace/datasets/flaw_data/val/mask_png"):
    src_path = os.path.join("/home/wanghaoxuan/workspace/datasets/flaw_data/val/mask_png",png)
    tgt_path = os.path.join(anno_val,png)
    if not os.path.exists(tgt_path):
        shutil.copy(src_path,tgt_path)