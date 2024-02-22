import numpy as np

from mmseg.apis import init_model,inference_model
import mmcv,cv2
import matplotlib.pyplot as plt
# 将模型加载到内存中
model = init_model(config='configs/deeplabv3plus/deeplabv3plus_r50-d8_1xb8-40k_flaw-400x400.py',checkpoint='work_dirs/deeplabv3plus_r50-d8_1xb8-40k_flaw-400x400/iter_8000.pth',device="cuda:0")

# 推理
result = inference_model(model = model,img='./data/flaw/img_dir/val/20220513_00008.jpg')
out = 'demo/outputs/flaw.png'
print(result.keys())
pred_mask = result.pred_sem_seg.data[0].cpu().numpy()
print(np.unique(pred_mask))
plt.figure(figsize=(5,5))
plt.imshow(pred_mask)
plt.savefig(out)
plt.show()
plt.close()

