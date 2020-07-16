### Data Preparation Instructions
Apart from the pre-trained EMNIST[0] ByMerge and ByClass database, we also test data on the IAM Dataset[1]

## Libraries and framework
Tensorflow 1.13.1/n
OpenCV/n
Numpy/n
Pandas/n
craft-text-detection/n
dhsegment/n

## Training model
By this time, our model should achieve a testing accuracy of 91% from nicely captured image (plain background with minimal noise). Planning to add RNN for auto0correction

## Preprocessing
We divided our preprocess into several steps of extracting baseline, lines, words, characters\n
For baseline extraction: we employ dhsegment[2] pretrained models: https://dhsegment.readthedocs.io/en/latest/start/demo.html\n
To extract lines, we make use of https://github.com/CrazyCrud/simple-text-line-extraction [4]\n
We rely on CRAFT - a PyTorch based model of Clova AI Research from https://github.com/clovaai/CRAFT-pytorch to detect words and character text region [3]\n
Each character will be converted to MNIST-like input to be classified

## Sample Notebook: Coming soon

## Reference:
[0] Cohen, G., Afshar, S., Tapson, J., & van Schaik, A. (2017). EMNIST: an extension of MNIST to handwritten letters. Retrieved from http://arxiv.org/abs/1702.05373\n
[1] U. Marti and H. Bunke. The IAM-database: An English Sentence Database for Off-line Handwriting Recognition. Int. Journal on Document Analysis and Recognition, Volume 5, pages 39 - 46, 2002.\n
[2] Sofia Ares Oliveira, Benoit Seguin, and Frederic Kaplan. Dhsegment: a generic deep-learning approach for document segmentation. In Frontiers in Handwriting Recognition (ICFHR), 2018 16th International Conference on, 7–12. IEEE, 2018.\n
[2] Tobias Grüning, Roger Labahn, Markus Diem, Florian Kleber, and Stefan Fiel. Read-bad: a new dataset and evaluation scheme for baseline detection in archival documents. In 2018 13th IAPR International Workshop on Document Analysis Systems (DAS), 351–356. IEEE, 2018.\n
[2] Foteini Simistira, Mathias Seuret, Nicole Eichenberger, Angelika Garz, Marcus Liwicki, and Rolf Ingold. Diva-hisdb: a precisely annotated large dataset of challenging medieval manuscripts. In Frontiers in Handwriting Recognition (ICFHR), 2016 15th International Conference on, 471–476. IEEE, 2016\n
[2] Chris Tensmeyer, Brian Davis, Curtis Wigington, Iain Lee, and Bill Barrett. Pagenet: page boundary extraction in historical handwritten documents. In Proceedings of the 4th International Workshop on Historical Document Imaging and Processing, 59–64. ACM, 2017.\n
[3]Youngmin Baek, Bado Lee, Dongyoon Han, Sangdoo Yun, Hwalsuk Lee: Character Region Awareness for Text Detection\n


