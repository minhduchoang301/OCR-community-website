### Data Preparation Instructions

Apart from the pre-trained MNIST database, download and generate the data from the following
project by instructions: https://textrecognitiondatagenerator.readthedocs.io/en/latest/index.html
Extract training and testing set into /Model - Handwriting/char train data and /Model - Handwriting/char test data

## Training model
"MNIST.h5" is loaded and trained with generated dataset from /Model - Handwriting/char train data
By this time, our model should achieve a testing accuracy of ... while classifying characters

## Text region extraction
We rely on CRAFT - a PyTorch based model of Clova AI Research from https://github.com/clovaai/CRAFT-pytorch to detect text region
Given the coordinates of the text, we make use of OpenCV to extract these character's image to classify by MNIST model.py

## Sample Notebook:

