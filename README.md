# English_Python_Translator

# Train Embedding Layer:

The python scripts extracted from Pytorch github (https://github.com/pytorch/pytorch) is used as a dataset to train the python keywords to build the embedding layer. As a part of preprocessing, the real new lines and tabs are replaced with \n and \t.

The custom_embeddings file is generated as a result of the Glove embedding training

![alt text](https://github.com/bala1802/English_Python_Translator/blob/main/Images/Embedding_Image01.JPG)


The Custom python embedding is loaded to the target attribute like below,

![alt text](https://github.com/bala1802/English_Python_Translator/blob/main/Images/Load_Custom_Embeddings_Image02.JPG)

#Data Preprocessing:

The real new line and tabs are replaced by \n and \t. Each source will have corresponding python program as a target.

Dataset before cleaning:

![alt text](https://github.com/bala1802/English_Python_Translator/blob/main/Images/Sample_SRC_TRG_Image03.JPG)

Dataset after cleaning:

![alt text](https://github.com/bala1802/English_Python_Translator/blob/main/Images/After_Cleaning_Image04.JPG)
