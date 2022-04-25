import os
from detectron2.data.datasets import register_coco_instances

# Script to include datasets in detectron2

nico_netscratch = "/netscratch/lesmes/Datasets"
LIVECell_folder = os.path.join(nico_netscratch, 'LIVECell')
EVICAN_folder = os.path.join(nico_netscratch, 'EVICAN')
Cellpose_folder = os.path.join(nico_netscratch, 'Cellpose')
LE_folder = os.path.join(nico_netscratch, 'LIVECell_EVICAN')
LC_folder = os.path.join(nico_netscratch, 'LIVECell_Cellpose')
LEC_folder = os.path.join(nico_netscratch, 'LIVECell_EVICAN_Cellpose')

datasets_dict = {
    'LIVECell_nico_train': (
        os.path.join(LIVECell_folder, 'annotations/livecell_coco_train.json'),
        os.path.join(LIVECell_folder, 'images/train_val')),
    'LIVECell_nico_test': (
        os.path.join(LIVECell_folder, 'annotations/livecell_coco_test.json'),
        os.path.join(LIVECell_folder, 'images/test')),
    'LIVECell_nico_val': (
        os.path.join(LIVECell_folder, 'annotations/livecell_coco_val.json'),
        os.path.join(LIVECell_folder, 'images/train_val')),
    'EVICAN_train': (
        os.path.join(EVICAN_folder, 'annotations/evican_coco_train.json'),
        os.path.join(EVICAN_folder, 'images/train')),
    'EVICAN_test_easy': (
        os.path.join(EVICAN_folder, 'annotations/nabeel_annotations/evican_coco_test_easy.json'),
        os.path.join(EVICAN_folder, 'images/test')),
    'EVICAN_test_medium': (
        os.path.join(EVICAN_folder, 'annotations/nabeel_annotations/evican_coco_test_medium.json'),
        os.path.join(EVICAN_folder, 'images/test')),
    'EVICAN_test_difficult': (
        os.path.join(EVICAN_folder, 'annotations/nabeel_annotations/evican_coco_val.json'),
        os.path.join(EVICAN_folder, 'images/test')),
    'EVICAN_val': (
        os.path.join(EVICAN_folder, 'annotations/nabeel_annotations/evican_coco_val.json'),
        os.path.join(EVICAN_folder, 'images/val')),
    'Cellpose_train': (
        os.path.join(Cellpose_folder, 'annotations/cellpose_coco_train.json'),
        os.path.join(Cellpose_folder, 'images/train')),
    'Cellpose_test': (
        os.path.join(Cellpose_folder, 'annotations/cellpose_coco_test.json'),
        os.path.join(Cellpose_folder, 'images/test')),
    'LIVECell_EVICAN_train': (
        os.path.join(LE_folder, 'annotations/livecell_evican_coco_train.json'),
        os.path.join(LE_folder, 'images/train_val')),
    'LIVECell_EVICAN_val': (
        os.path.join(LE_folder, 'annotations/livecell_evican_coco_val.json'),
        os.path.join(LE_folder, 'images/train_val')),
    'LIVECell_Cellpose_train': (
        os.path.join(LC_folder, 'annotations/livecell_cellpose_coco_train.json'),
        os.path.join(LC_folder, 'images/train_val')),
    'LIVECell_Cellpose_val': (
        os.path.join(LIVECell_folder, 'annotations/livecell_coco_val.json'),
        os.path.join(LIVECell_folder, 'images/train_val')),
    'LIVECell_EVICAN_Cellpose_train': (
        os.path.join(LEC_folder, 'annotations/livecell_evican_cellpose_coco_train.json'),
        os.path.join(LEC_folder, 'images/train_val')),
    'LIVECell_EVICAN_Cellpose_val': (
        os.path.join(LE_folder, 'annotations/livecell_evican_coco_val.json'),
        os.path.join(LEC_folder, 'images/train_val')),
    'LIVECell_EVICAN_Cellpose_Lchannel_train': (
        os.path.join(LEC_folder, 'annotations/livecell_evican_cellpose_coco_train.json'),
        os.path.join(LEC_folder, 'preprocessing/channel_analysis/L_LAB/train_val')),
    'LIVECell_EVICAN_Cellpose_Lchannel_val': (
        os.path.join(LE_folder, 'annotations/livecell_evican_coco_val.json'),
        os.path.join(LEC_folder, 'preprocessing/channel_analysis/L_LAB/train_val')),
    'LIVECell_EVICAN_Cellpose_histmatch_train': (
        os.path.join(LE_folder, 'annotations/livecell_evican_cellpose_coco_train.json'),
        os.path.join(LEC_folder, 'preprocessing/histogram_matching/train_val')),
    'LIVECell_EVICAN_Cellpose_histmatch_val': (
        os.path.join(LE_folder, 'annotations/livecell_evican_coco_val.json'),
        os.path.join(LEC_folder, 'preprocessing/histogram_matching/train_val')),
    'LIVECell_histmatch_test': (
        os.path.join(LIVECell_folder, 'annotations/livecell_coco_test.json'),
        os.path.join(LIVECell_folder, 'preprocessing/histogram_matching/test')),
    'EVICAN_histmatch_test_easy': (
        os.path.join(EVICAN_folder, 'annotations/nabeel_annotations/evican_coco_test_easy.json'),
        os.path.join(EVICAN_folder, 'preprocessing/histogram_matching/test')),
    'Cellpose_histmatch_test': (
        os.path.join(Cellpose_folder, 'annotations/cellpose_coco_test.json'),
        os.path.join(Cellpose_folder, 'preprocessing/histogram_matching/test')),
    'LIVECell_shannon_train': (
        os.path.join(LIVECell_folder, 'annotations/livecell_coco_train.json'),
        os.path.join(LIVECell_folder, 'preprocessing/Shannon_entropy/train_val')),
    'LIVECell_shannon_val': (
        os.path.join(LIVECell_folder, 'annotations/livecell_coco_val.json'),
        os.path.join(LIVECell_folder, 'preprocessing/Shannon_entropy/train_val')),
    'LIVECell_shannon_test': (
        os.path.join(LIVECell_folder, 'annotations/livecell_coco_test.json'),
        os.path.join(LIVECell_folder, 'preprocessing/Shannon_entropy/test')),
    'LIVECell_shannon_blur_test': (
        os.path.join(LIVECell_folder, 'annotations/livecell_coco_test.json'),
        os.path.join(LIVECell_folder, 'preprocessing/Shannon_entropy_blur/test')),
    # '': (
    #     os.path.join(),
    #     os.path.join()),
}



#if __name__ == "__main__":
#    for key, value in datasets_dict.items():
#        register_coco_instances(key, {}, value[0], value[1])
#    print('hola')
