from mmengine import Config
config = Config.fromfile("configs/deeplabv3plus/deeplabv3plus_r50-d8_1xb8-40k_flaw-400x400.py")
print(config.pretty_text)