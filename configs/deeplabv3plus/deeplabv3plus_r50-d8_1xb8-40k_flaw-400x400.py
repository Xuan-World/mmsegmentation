_base_ = [
    '../_base_/models/deeplabv3plus_r50-d8.py',
    '../_base_/datasets/flaw_400x400.py', '../_base_/default_runtime.py',
    '../_base_/schedules/schedule_40k.py'
]
crop_size = (400,400)
data_preprocessor = dict(size=crop_size)
model = dict(
    data_preprocessor = data_preprocessor,
    decode_head = dict( num_classes = 2),
    auxiliary_head = dict(num_classes = 2)
)