# Microcalc-Detect
Convolutional network model trained for detection of microcalcifications using patch classification approach

The files must be concatenated by e.g. the macos/linux command

cat model.* > PRETRAINED_RESNET101_ADAM_LR5e-06_WD0.001_BS8.tar

After the files model.aa .. model.ag are merged into one file PRETRAINED_RESNET101_ADAM_LR5e-06_WD0.001_BS8.tar, the provided script example1.py demonstrates a classification of two patches. 

This is a Suppementary material of a paper submitted for publication. Here we provide the abstract of the paper:


Breast cancer is the most common type of cancer among women. Integrating machine
learning models with mammography holds the potential to transform breast cancer screening and
diagnostics by making them more accurate, efficient, and accessible, ultimately leading to better
patient outcomes. This study addresses the classification of mammography patches into two cate-
gories: those with suspicious clusters of microcalcifications and those without. Using high-resolution
patches (674 x 674 pixels) was crucial to preserve the detail necessary for detecting microcalcifica-
tions. Data were sourced from the CBIS-DDSM and OMI-DB databases, each presenting unique 
challenges in preprocessing. The study highlighted the importance of manual evaluation to ensure 
the accuracy of patches, particularly when generating patches without suspicious clusters. For model 
training, the ResNet101 convolutional architecture was employed, leveraging transfer learning with 
pre-trained weights on ImageNet to achieve faster convergence and better performance. Various hy- 
perparameters, including learning rate and weight decay, were optimized. The best model achieved 
a validation accuracy of 98.2% (F1 score - 0.955, MCC - 0.944, specificity - 99.1%, and sensitivity - 
94.6%), demonstrating strong capability in identifying important radiological features and handling 
visually challenging microcalcifications. The model has been made publicaly available. Despite 
some incorrect predictions, the model reliably located clusters, suggesting practical utility in clinical 
settings where high-resolution imaging is essential.



