from mmseg.registry import DATASETS
from .basesegdataset import BaseSegDataset

@DATASETS.register_module()
class FlawDataset(BaseSegDataset):
    METAINFO = dict(
        classes = ('normal','abnormal'),
        palette = [[120, 120, 120], [6, 230, 230]]
    )
    def __init__(self,
                 img_suffix = '.jpg',seg_map_suffix = '_mask.png',
                 reduce_zero_label=False,
                 **kwargs):
        super().__init__(
            img_suffix=img_suffix, seg_map_suffix=seg_map_suffix,reduce_zero_label=reduce_zero_label, **kwargs)
